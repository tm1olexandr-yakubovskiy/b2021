import time
import unittest
from main import*

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Час виконання функції {func.__name__}: {execution_time} секунд")
        return result
    return wrapper

class My_Test(unittest.TestCase):

    @measure_time
    def test_додавання(self):
        result = adder(10, 5)
        self.assertEqual(result, 15)

    @measure_time
    def test_віднімання(self):
        result = adder(10, 5)
        self.assertEqual(result, 15)

    @measure_time
    def test_множення(self):
        result = adder(10, 5)
        self.assertEqual(result, 15)

    @measure_time
    def test_ділення(self):
        result = adder(10, 5)
        self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()