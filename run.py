# -*- coding: utf-8 -*-
import os
from flask import render_template, request
from filesystem import Folder, File
from action import Find
from app import create_app

app = create_app()

@app.route('/')
@app.route('/files/<path:path>')
def index(path=''):
    path_join = os.path.join(app.config['FILES_ROOT'], path)
    if os.path.isdir(path_join):
        # If the mouse click the folder
        folder = Folder(app.config['FILES_ROOT'], path)
        folder.read()
        return render_template(
            'folder.html',
            folder=folder,
            cdn_root=app.config['CDN_ROOT'],
            request=request
        )

    else:
        # If the mouse click the file
        my_file = File(app.config['FILES_ROOT'], path)
        folder = Folder(app.config['FILES_ROOT'], my_file.get_path())
        return render_template('file_view.html', file=my_file, folder=folder)

@app.route('/search', methods=['GET', 'POST'])
def search():
    pattern = request.form['pattern']
    find = Find(app.config['FILES_ROOT'])
    result = find.find(pattern)
    return render_template(
        'search.html',
        result=result,
        pattern=pattern
    )

# @app.route('/new_directory', methods=["POST"])
# @app.route('/<path:path>/new_directory', methods=["POST"])
# def create_directory(path = "/"):
    # dirname = request.form["new_directory_name"]
    # directory_root = request.form["directory_root"]
    # full_path = os.path.join(directory_root, dirname)
    # try:
        # os.mkdir(full_path)
    # except error:
        # pass
    # return redirect('/files/' + directory_root)

@app.route('/fast/<path:pix>')
def fast(pix):
    img_src = app.config['CDN_ROOT'] + str(pix)
    return render_template(
        'touch_layout.html',
        img_src=img_src
        )

@app.route('/warning')
def warning():
    return render_template('warning.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
