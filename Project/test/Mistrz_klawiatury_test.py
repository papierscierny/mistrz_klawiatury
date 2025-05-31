#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from Mistrz_Klawiatury import *

class GetUniqueLettersTest(unittest.TestCase):
    def test_less_than_3_unique_letters(self):
        self.assertSetEqual(set(), get_unique_letters('ah'))

    def test_at_least_3_unique_letters(self):
        self.assertSetEqual({'k', 'a', 'y'}, get_unique_letters('kayak'))

