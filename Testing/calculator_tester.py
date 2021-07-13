import unittest
import setuptools
from Calculator import *


list_of_numbers=[(1,4),(-1,4),(1,-4),(2.5,3.5),(-2.5,3.5),(2.5,-3.5),
                 (-2.5,-3.5),(2,2.2),(-2,2.2),(2,-2.2),(-2,-2.2),
                 (2,-2)]

list_of_invalid_format=[("hello","world"),("hello",2),(2,"hello"),
                        ("hello",2.2),(2.2,"hello")]

list_of_zero_values=[(0,5),(5,0),(0,0),(5.1,0),(0,5.1)]


class TestTheCalculator(unittest.TestCase):

    def test_addition(self):
        for p1,p2 in list_of_numbers:
            with self.subTest():
                self.assertEqual(Calculator.add(self,p1,p2),p1+p2)
        for p1,p2 in list_of_invalid_format:
            with self.subTest():
                self.assertRaises(TypeError,Calculator.add,self,p1,p2,True)



    def test_subtraction(self):
        for p1,p2 in list_of_numbers:
            with self.subTest():
                self.assertEqual(Calculator.subtract(self,p1,p2),p1-p2)
        for p1,p2 in list_of_invalid_format:
            with self.subTest():
                self.assertRaises(TypeError,Calculator.subtract,self,p1,p2,True)




    def test_multiplication(self):
        for p1,p2 in list_of_numbers:
            with self.subTest():
                self.assertEqual(Calculator.multiply(self,p1,p2),p1*p2)
        for p1,p2 in list_of_invalid_format:
            with self.subTest():
                self.assertRaises(TypeError,Calculator.multiply,self,p1,p2,True)
        for p1,p2 in list_of_zero_values:
            with self.subTest():
                self.assertEqual(Calculator.multiply(self,p1,p2),0)




    def test_division(self):
        for p1,p2 in list_of_numbers:
            with self.subTest():
                self.assertEqual(Calculator.divide(self,p1,p2),p1/p2)
        for p1,p2 in list_of_invalid_format:
            with self.subTest():
                self.assertRaises(TypeError,Calculator.divide,self,p1,p2,True)
        for p1,p2 in list_of_zero_values:
            with self.subTest():
                if p2 == 0:
                    self.assertRaises(TypeError,Calculator.multiply,self,p1,p2,True)


