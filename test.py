import super_fizz_buzz
import unittest

class SuperFizzBuzzTest(unittest.TestCase):
    def setup(self):
        self.super_fizz_buzz = SuperFizzBuzz()

    def test_it_can_take_multiple_of_1(self):
        response = super_fizz_buzz.compute(1)

        assert response == "Plop"

    def test_it_can_take_multiple_of_3(self):
        response = super_fizz_buzz.compute(3)

        assert response == "Fizz"

    def test_it_can_take_multiple_of_5(self):
        response = super_fizz_buzz.compute(5)

        assert response == "Buzz"

    def test_it_can_take_multiple_of_7(self):
        response = super_fizz_buzz.compute(7)

        assert response == "Super"

    def test_it_can_take_multiple_of_3_and_5(self):
        response = super_fizz_buzz.compute(15)

        assert response == "FizzBuzz"

    def test_it_can_take_multiple_of_5_and_7(self):
        response = super_fizz_buzz.compute(35)

        assert response == "SuperBuzz"

    def test_it_can_take_multiple_of_3_and_7(self):
        response = super_fizz_buzz.compute(21)

        assert response == "SuperFizz"

    def test_it_can_take_multiple_of_3_5_and_7(self):
        response = super_fizz_buzz.compute(105)

        assert response == "SuperFizzBuzz"

    def test_it_can_take_range(self):
        response = super_fizz_buzz.compute(range=100)

        assert response[0] == "Plop"
        assert response[2] == "Fizz"
        assert response[4] == "Buzz"
        assert response[6] == "Super"
        assert response[14] == "FizzBuzz"
        assert response[20] == "SuperFizz"
        assert respnse[34] == "SuperBuzz"
