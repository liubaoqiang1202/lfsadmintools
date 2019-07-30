# -*- coding: utf-8 -*-

import os
import datetime


def setting():
    print 'setting...'


def before_check():
    now = str(datetime.datetime.now())
    cmd = 'source /LFS_check/venv/bin/activate;robot -d "/home/beforeCheck' + now + '" src/lfs_before_install.robot'
    os.system(cmd)
    return True


def after_check():
    now = str(datetime.datetime.now())
    cmd = 'source /LFS_check/venv/bin/activate;robot -d "/home/afterCheck' + now + '" src/lfs_after_install.robot'
    os.system(cmd)
    return True



