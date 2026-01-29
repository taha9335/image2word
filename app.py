from flask import Flask, request, send_file, render_template_string, redirect, url_for
import os
import tempfile
from ocr_utils import process_image_to_docx

app = Flask(__name__, static_folder='static', static_url_path='/static')

INDEX_HTML = '''
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Image → Word (MVP)</title>
    <link rel="stylesheet" href="/static/style.css" />
  </head>
  <body>
    <div class="container">
      <h1>Image → Word Converter (MVP)</h1>
      <form id="uploadForm" action="/convert" method="post" enctype="multipart/form-data">
        <label>Select JPG/PNG:</label>
        <input type="file" name="image" accept="image/*" required />
        <button type="submit">Convert</button>
      </form>
      <div class="note">Output: .docx with basic formatting preserved (bold/italic/alignment).</div>
    </div>
  </body>
</html>
'''


@app.route('/')
def index():
    return render_template_string(INDEX_HTML)


@app.route('/convert', methods=['POST'])
def convert():
    if 'image' not in request.files:
        return redirect(url_for('index'))

    f = request.files['image']
    if f.filename == '':
        return redirect(url_for('index'))

    tmp_dir = tempfile.mkdtemp()
    input_path = os.path.join(tmp_dir, f.filename)
    f.save(input_path)

    output_path = os.path.join(tmp_dir, 'converted.docx')
    try:
        process_image_to_docx(input_path, output_path)
    except Exception as e:
        return f'Error during processing: {e}', 500

    return send_file(output_path, as_attachment=True, download_name='converted.docx')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
