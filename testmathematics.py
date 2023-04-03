import unittest
from mathematics import Mathematics

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.math = Mathematics()
    def test_add(self):
        result = self.math.sumTwoNumbers(10,5)
        self.assertEqual(result, 15)
    def test_multiply(self):
        result = self.math.multiplyTwoNumbers(10,5)
        self.assertEqual(result, 50)

if __name__ == '__main__':
    unittest.main()
