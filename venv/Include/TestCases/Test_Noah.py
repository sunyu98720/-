#coding=gbk
import unittest
from Public.TestStepExecute import TestStepExecute


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fun = TestStepExecute()
        cls.fun.step_execute('noah_test_login')

    def test_noah_login(self):
        self.fun.step_execute('noah_test_new_lexicon')



if __name__ == '__main__':
    unittest.main()
