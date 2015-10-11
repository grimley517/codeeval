#! /usr/bin/env pyhthon 3.4
import unittest
import hexconv as h
import subprocess
import shutil

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def test1(self):
        hexstrings = '0 1 2 3 4 5 6 7 8 9 a b c d e f'.split()
        print ('hexstrings = {0}'.format(hexstrings))
        for string in hexstrings:
            self.assertEqual(h.dec(string),hexstrings.index(string))


if __name__== "__main__":
    subprocess.call (["pep8", "hexconv.py"])
    unittest.main(verbosity=3, exit = False)
    shutil.copyfile("hexconv.py", "hexconv.py3")
