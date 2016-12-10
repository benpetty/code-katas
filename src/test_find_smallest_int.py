"""Test find_smallest_int function."""


import sys

test.assert_equals(findSmallestInt([78,56,232,12,11,43]), 11)
test.assert_equals(findSmallestInt([78,56,-2,12,8,-33]), -33)
test.assert_equals(findSmallestInt([0, -1-sys.maxint,sys.maxint]), -1-sys.maxint)