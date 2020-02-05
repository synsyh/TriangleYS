# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3, 4, 5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5, 3, 4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(3, 5, 4), 'Right', '3, 5, 4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1, 1, 1 should be equilateral')

    def testIsocelesTrianglesA(self):
        self.assertEqual(classifyTriangle(2, 2, 1), 'Isoceles', '2, 2, 1 should be Isoceles')

    def testIsocelesTrianglesB(self):
        self.assertEqual(classifyTriangle(2, 1, 2), 'Isoceles', '2, 1, 2 should be Isoceles')

    def testIsocelesTrianglesC(self):
        self.assertEqual(classifyTriangle(1, 2, 2), 'Isoceles', '1, 2, 2 should be Isoceles')

    def testBoundaryTrianglesA(self):
        self.assertEqual(classifyTriangle(201, 199, 199), 'InvalidInput', '201, 199, 199 should be an invalid triangle')

    def testBoundaryTrianglesB(self):
        self.assertEqual(classifyTriangle(199, 201, 199), 'InvalidInput', '199, 201, 199 should be an invalid triangle')

    def testBoundaryTrianglesC(self):
        self.assertEqual(classifyTriangle(199, 199, 201), 'InvalidInput', '199, 199, 201 should be an invalid triangle')

    def testBoundaryTrianglesD(self):
        self.assertEqual(classifyTriangle(199, 198, 197), 'Scalene', '199, 198, 197 should be an Scalene triangle')

    def testNegativeInputTrianglesA(self):
        self.assertEqual(classifyTriangle(-1, 1, 1), 'InvalidInput', '-1, 1, 1 should be an invalid triangle')

    def testNegativeInputTrianglesB(self):
        self.assertEqual(classifyTriangle(1, -1, 1), 'InvalidInput', '1, -1, 1 should be an invalid triangle')

    def testNegativeInputTrianglesC(self):
        self.assertEqual(classifyTriangle(1, 1, 0), 'InvalidInput', '1, 1, 0 should be an invalid triangle')

    def testInvalidInputTrianglesA(self):
        self.assertEqual(classifyTriangle(1.1, 1, 1), 'InvalidInput', '1.1, 1, 1 should be an invalid triangle')

    def testInvalidInputTrianglesB(self):
        self.assertEqual(classifyTriangle(1, 2.0, 1), 'InvalidInput', '1, 2.0, 1 should be an invalid triangle')

    def testNotATriangleTrianglesA(self):
        self.assertEqual(classifyTriangle(2, 1, 1), 'NotATriangle', '2, 1, 1 should be an invalid triangle')

    def testNotATriangleTrianglesB(self):
        self.assertEqual(classifyTriangle(1, 2, 1), 'NotATriangle', '1, 2, 1 should be an invalid triangle')

    def testNotATriangleTrianglesC(self):
        self.assertEqual(classifyTriangle(1, 1, 2), 'NotATriangle', '1, 1, 2 should be an invalid triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
