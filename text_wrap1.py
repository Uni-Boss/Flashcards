# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 07:27:14 2018

@author: Michael Brown
"""
global new_lines
def my_text_wrap1(text):
    all_strings = [50, 100, 150]
    new_lines = []
    for num in all_strings:
        while(text[num] != " "):
            num += 1
        new_lines.append(num)
    return new_lines























