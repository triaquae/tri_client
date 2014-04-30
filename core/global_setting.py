#!/usr/bin/env python

import os,sys

cur_dir = os.path.split(os.path.abspath(__file__))[0].split('/')[:-1]

base_dir = '/'.join(cur_dir)

sys.path.append(base_dir)
