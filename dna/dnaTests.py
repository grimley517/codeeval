#! /usr/bin/env pyhthon3.4
import unittest
import dna as d
import subprocess
import shutil

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def test1(self):
        self.assertTrue(d.matchLetter ("G", "G"))
        self.assertFalse(d.matchLetter ("G", "A"))

    def test2(self):
        self.assertEqual(d.score("G","G"),3)

    def test3(self):
        self.assertEqual(d.score("GAAAAAAT",  "GAAT"),1)

    def test4(self):
        self.assertEqual(d.score("GCATGCT","GATTACA"),(0-3))

    def test5(self):
        self.assertEqual(d.score("",""),0)

    def test6(self):
        self.assertEqual(d.score("G","GA"),(0-5))

if __name__== "__main__":
    subprocess.call (["pep8", "dna.py"])
    unittest.main(verbosity=3, exit = False)
    shutil.copyfile("dna.py", "dna.py3")
