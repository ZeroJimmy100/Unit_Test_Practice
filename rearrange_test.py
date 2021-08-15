#!/usr/bin/env python3 

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    # This produce an error because the method is not doing what
    # it is suppose to output, therefore it created an edge case
    # meaning the input has produce an unexpected results and are found 
    # at the extreme ends of the ranges of input we imagine our programs
    # will typically work with
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()