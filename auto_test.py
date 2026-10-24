import unittest
from function import task

class TestRashala(unittest.TestCase):

    def test_1(self):
        result = task(1, 2, 3, 4, 5)
        self.assertAlmostEqual(result, -0.763932, places=5)  
    
    def test_2(self):
        result = task(7, 8, '9', '10', 11)
        self.assertAlmostEqual(result, -11.683375, places=5)

    def test_3(self):
        result = task(12, "ertyui", 14, 15, 16)
        self.assertEqual(result, "Datatype is invalid")
    
    def test_4(self):
        result = task(18, 19, 20, 20, 21)
        self.assertEqual(result, "Divizion by zero")

if __name__ == '__main__':
    unittest.main() 