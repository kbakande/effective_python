import unittest
import calc

# create the test class
class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2,3), 5)
        self.assertEqual(calc.add(2,3), 5.5)

if __name__ ==  "__main__":
    unittest.main()

