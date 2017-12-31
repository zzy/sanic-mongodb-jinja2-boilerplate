#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def chinese_contain_check(check_str):
    for character in check_str.decode('utf-8'):
        if u'\u4e00' <= character <= u'\u9fff':
            return True
        return False
    
    