from temp import Temperature
import unittest

class test_temp(unittest.TestCase):
    def test1(self):
        with self.assertRaises(ValueError):
            Temperature() #Success
    def test2(self):
        with self.assertRaises(ValueError):
            Temperature(kelvin=20) #Fail
    def test3(self):
        with self.assertRaises(ValueError):
            Temperature(-1) #Success
    def test4(self):
        with self.assertRaises(ValueError):
            Temperature(20,40) #Success

if __name__=="__main__":
    unittest.main()   