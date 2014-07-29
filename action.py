# -*- coding: utf-8 -*-

import os
from utils import encoding_detect, join_to_string
from app import create_app

app = create_app()

class Action(object):
    """docstring for Action"""
    def __init__(self, node):
        self.node = node


class View(Action):
    """docstring for View"""
    def apply(self):
        self_path = os.path.join(self.node.root, self.node.path)
        encode = encoding_detect(self_path)
        try:
            text = open(self_path, encoding=encode).read()
        except UnicodeDecodeError:
            return None
        return { 'text' : text }


class Search(Action):
    def apply(self, folder_to_search_into, mask):
        founds = []
        for root, dirs, files in os.walk(folder_to_search_into, topdown=False):
            for name in files:
                if mask in name:
                    founds.append(os.path.join(root, name))
        return founds


class Find(Action):
    def find(self, pattern):
        result = []
        node_root = app.config['CDN_ROOT']
        for root, dirs, files in os.walk(app.config['FILES_ROOT']):
            for name in files:
                if pattern in name:
                    _file_path = os.path.join(root).split(app.config['FILES_ROOT'])[1]
                    file_path = _file_path[1:]
                    result.append([name, file_path, node_root])
        return result
