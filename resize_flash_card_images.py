# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 07:47:29 2018

@author: Michael Brown
"""

from PIL import Image
import os, sys
cwd = os.getcwd()
path = cwd + '\\flash_card_images\\'
dirs = os.listdir( path )
final_size = 400;

def resize_aspect_fit():
    for item in dirs:
         if item == '.DS_Store':
             continue
         if os.path.isfile(path+item):
             im = Image.open(path+item)
             f, e = os.path.splitext(path+item)
             size = im.size
             ratio = float(final_size) / max(size)
             new_image_size = tuple([int(x*ratio) for x in size])
             im = im.resize(new_image_size, Image.ANTIALIAS)
             new_im = Image.new("RGB", (final_size, final_size))
             new_im.paste(im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
             if ('resized' in f):
                    continue
             else:
                 new_im.save(f + 'resized.jpg', 'png', quality=100)
resize_aspect_fit()