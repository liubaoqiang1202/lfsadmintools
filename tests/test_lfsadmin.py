#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

# Hack around absolute paths
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(current_dir + "/../")
sys.path.insert(0, parent_dir)

import unittest
from lfsadmin.lfsadmin import build_select_info


class BuildSelectInfoTestCase(unittest.TestCase):
    def test_null(self):
        action_list = []
        info = build_select_info(action_list)
        self.assertEqual(info, '')

    def test_one_select(self):
        action_list = [('ttt', None)]
        info = build_select_info(action_list)
        self.assertEquals(info, '(1) ttt\n')

    def test_two_selects(self):
        action_list = [('ttt', None), ('sss', None)]
        info = build_select_info(action_list)
        self.assertEquals(info, '(1) ttt\n(2) sss\n')

    def test_sub_select(self):
        action_list = [('ttt', None), ('sss', None)]
        action_list2 = [('aaa', None)]
        info = build_select_info(action_list, action_list2)
        self.assertEquals(info, '(1) ttt\n(2) sss\n(3) back\n')


if __name__ == '__main__':
    unittest.main()
