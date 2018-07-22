#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def chinese_contain_check(check_str):
    for character in check_str:
        if '\u4e00' <= character <= '\u9fff':
            return True
        return False
    
    