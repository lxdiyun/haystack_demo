# -*- coding: utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from mmseg import seg_txt


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


def mmseg_test():
    string = "最主要 的更  动是：张无忌最后没有选定自己的配偶。自己的自己"
    print(seg_txt(string))
    output = ""
    for i in seg_txt(string):
        output += i + " "
    print(output)
