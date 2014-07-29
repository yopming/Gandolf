# -*- coding: utf-8 -*-
import os
import time
import platform
import sys
from genericpath import isfile
from os.path import join, basename, splitext, isdir, dirname
from action import View
from app import create_app
from utils import human_size

app = create_app()


class Node(object):
    def __init__(self, root, path):
        splitetPath = path.split("/")
        self.path = os.path.sep.join(splitetPath)
        self.root = root
        self._basename = basename(self.path)
        self._abspath = os.path.abspath(path)

    def __unicode__(self):
        return self.name

    def get_actions(self):
        return self.avaliable_actions

    def apply_action(self, action_class):
        action = action_class(self)
        return action.apply()

class File(Node):
    avaliable_actions = [View, ]
    def __unicode__(self):
        return self.name

    @property
    def extension(self):
        return splitext(self._basename)[1]

    @property
    def trim_ext(self):
        return self.extension.split('.')[1]

    @property
    def purename(self):
        return splitext(self._basename)[0]

    @property
    def name(self):
        return self._basename

    @property
    def rela_path(self):
        if platform.system() == "Windows":
            return self.path.replace('\\', '/')
        else:
            return self.path

    # @property
    # def size(self):
        # if platform.system() == 'Windows':
            # return os.path.getsize(self._abspath)
            # # upath = self._abspath.replace(r'\\', r'\')
            # # return os.path.getsize(r'D:\Applications\Gandolf\utils.py')
            # # return os.path.getsize(upath)
        # else:
            # return os.path.getsize(self._abspath)
    
    # @property
    # def mtime(self):
        # return self._abspath
        # return time.asctime(time.localtime(os.stat('D:\\Applications\\Gandolf\\utils.py').st_mtime))
    
    @property
    def ancestry_directory(self):
        pdir = os.path.split(self._abspath)[0]
        dirs = pdir.split('\\') # windows, use '/' for *nix
        enable_qrcode_flag = 0
        for dir in dirs:
            if dir.endswith('Q'):
                enable_qrcode_flag = enable_qrcode_flag + 1
        if enable_qrcode_flag > 0:
            return True
        else:
            return False

    def get_path(self):
        return dirname(self.path)


class Folder(Node):
    
    def __init__(self, root, path):
        super(Folder, self).__init__(root, path)
        self.files = []
        self.folders = []

    @property
    def name(self):
        return basename(self.path)
   
    @property
    def depict(self):
        depict_path = os.path.join(app.config['FILES_ROOT'], self.path, 'readme.txt')
        if os.path.exists(depict_path):
            depict_file = File(app.config['FILES_ROOT'], os.path.join(self.path, 'readme.txt'))
            return depict_file.apply_action(View)['text']
        else:
            return None

    def chunks(self):
        chunk_path = ''
        for chunk in self.path.split(os.sep):
            chunk_path = join(chunk_path, chunk)
            yield {'chunk': chunk, 'path': chunk_path}

    def read(self):
        for node in os.listdir(join(self.root, self.path)):
            full_path = join(self.path, node)
            if isdir(join(self.root, full_path)):
                self.folders.append(Folder(self.root, full_path))
            if isfile(join(self.root, full_path)):
                self.files.append(File(self.root, full_path))
