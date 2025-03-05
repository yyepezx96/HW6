import unittest
from app import my_var  # Assuming 'my_var' is the variable you're testing

class TestApp(unittest.TestCase):
    def test_environment_variable(self):
        self.assertEqual(my_var, 'example_value')

if __name__ == "__main__":
    unittest.main()

