#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

# Hack around absolute paths
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(current_dir + "/../")
sys.path.insert(0, parent_dir)

import unittest
import mock
import commands
from lfsadmin.other import diagnose


class DiagnoseTestCase(unittest.TestCase):
    def test_ok(self):
        commands.getstatusoutput = mock.Mock(return_value=(0, 'OK'))
        ret = diagnose()
        self.assertEqual(True, ret)

    def test_error_msg(self):
        commands.getstatusoutput = mock.Mock(return_value=(0, 'XXXXXXXX'))
        ret = diagnose()
        self.assertEqual(False, ret)

    def test_error_ret(self):
        commands.getstatusoutput = mock.Mock(return_value=(-1, 'OK'))
        ret = diagnose()
        self.assertEqual(False, ret)


if __name__ == '__main__':
    unittest.main()
