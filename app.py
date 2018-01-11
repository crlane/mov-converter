import os

from ffmpy import FFmpeg

from flask import (
    Flask,
    request,
    redirect,
    send_from_directory,
    url_for,
)

app = Flask(__name__)
UPLOAD_DIR = '/tmp/video_conversion'

app.config['STATIC_FOLDER'] = 'static'
app.config['UPLOAD_DIR'] = UPLOAD_DIR


def _new_filename(filename):
    name, ext = os.path.splitext(filename)
    return f'{name}.mp4'


def _convert_to_mov(original, new):
    app.logger.info('Converting %s -> %s', original, new)
    ff = FFmpeg(
        inputs={original: None},
        outputs={new: None}
    )
    ff.run()
    app.logger.info('Conversion successful: %s', new)
    return new


@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return url_for('static', filename='favicon.ico')


@app.route('/convert', methods=['GET', 'POST'])
def convert_video():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            app.logger.error('No file submitted')
            return redirect(request.url)

        file_to_convert = request.files['file']
        original = file_to_convert.filename
        app.logger.info('File received: %s', original)
        original_path = os.path.join(app.config['UPLOAD_DIR'], original)
        new_path = os.path.join(app.config['UPLOAD_DIR'], _new_filename(original))
        if file_to_convert:
            file_to_convert.save(original_path)
            new_file = _convert_to_mov(original_path, new_path)
            app.logger.info('Will return file: %s', os.path.basename(new_file))
            return send_from_directory(app.config['UPLOAD_DIR'], os.path.basename(new_file), as_attachment=True)

    return '''
    <!doctype html>
    <title>Upload MOV File to Convert</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
    <p><input type=file name=file>
    <input type=submit value=Upload>
    </form>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', 5000))
