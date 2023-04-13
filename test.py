import pytest
from calculator import Calculator

class TestClas:
    def setup(self):
        self.calculator = Calculator

    def test_adding_success(self):
        assert self.calculator.adding(self,1,2) == 3

    def test_multiply(self):
        assert self.calculator.multiply(self,3,6) == 18

    def test_division(self):
        assert self.calculator.division(self,36,6) == 6

    def test_subtraction(self):
        assert self.calculator.subtraction(self, 7, 5) == 2

    def test_zero_division(self):
       with pytest.raises(ZeroDivisionError):
           self.calculator.division(self,1,0)

    def teardown(self):
        print('Выполняеться метод Teardown')