#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

print(os.path.dirname(__file__))
print(os.path.dirname(os.path.dirname(__file__)))
print(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

sys.path
sys.meta_path

print(__name__.__str__())

