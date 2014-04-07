# -*- coding:utf-8 -*-

import charade
import markdown

def encoding_detect(file_path):
    """ get file's encoding """
    file_buf = open(file_path, 'rb').read()
    result = charade.detect(file_buf)
    return result['encoding']

def decode_markdown(text):
    """ convert markdown content to html """
    return markdown.markdown(text)

def human_size(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.00:
            return "%3.1f %s" %(num, x)
        num /= 1024.00
    return num

def join_to_string(diction):
    string = ''
    for x in diction:
        xx = x + '/'
        string += xx
    return string
