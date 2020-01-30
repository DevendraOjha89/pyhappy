import unittest

class Employee:
    pass

class Mytest(unittest.TestCase):

    @classmethod
    def setupclass(cls):
        print("This test will run only once before all test in this testcase is pass")

    def setup(self):
        print("This method will run before every test")

    def test_something(self):
        self.assertTrue(self.employee is not None)

    def test_something2(self):
        self.assertTrue(false)

    def test_something3(self):
        self.assertTrue(true)

    def tearDown(self):
        print("This method will run after every test")

    @classmethod
    def tearDownClass(cls):
        print("This method will run only only once after all tst have executed")


if __name__ == '__main__':
    unittest.main()