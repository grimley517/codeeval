#! usr/bin/env python3

import unittest
import decode
import shutil
import os
from subprocess import call


class testSequences(unittest.TestCase):

    def setUp(self):
        pass

    def test1(self):
        ''' from Task description, 2 ways of decoding 12

        asserts that there are 2 ways of decoding 12'''

        tinput = 12
        expOutput = 2
        self.assertEqual(decode.main(tinput), expOutput)

    def test2(self):
        '''from task description, 3 ways of decoding 123

        asserts that there are three ways of decoding 123'''

        tinput = 123
        expOutput = 3
        self.assertEqual(decode.main(tinput), expOutput)


    def test3(self):
        '''edge case - 1111 should have 5 ways of solving

        asserts that there are 5 ways of decoding 1111
        1) aaaa
        2) kk
        3) kaa
        4) aka
        5) aak
        '''

        tinput = 1111
        expOutput = 5
        self.assertEqual(decode.main(tinput), expOutput)

if __name__ == "__main__":

    direct = os.getcwd()
    print(direct)
    src = os.path.join(direct, 'decode.py')
    dst = os.path.join(direct, 'decode.py3')
    shutil.copyfile(src, dst)
    style = call(['pep8', 'decode.py'])
    unittest.main(verbosity=3)
