import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2 ,3) == 6

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 6, 3) == 2

    def test_multiply_subtraction_correctly(self):
        assert self.calc.subtraction(self, 3 ,2) == 1

    def test_multiply_adding_correctly(self):
        assert self.calc.adding(self, 2 ,3) == 5
