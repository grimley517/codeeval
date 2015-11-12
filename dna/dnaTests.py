#! /usr/bin/env python3
import unittest
import dna as d
import subprocess
import shutil
import time

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

    def test7(self):
        self.assertEqual(d.clean("G "), "G")
        self.assertEqual(d.clean("g "), "G")
        self.assertEqual(d.clean("G A"), "GA")
        self.assertEqual(d.clean("GOA "), "GA")

    def test8(self):
        string1 = "TAGATCTCGTCTTACTACACGGCGCTCCATATCTGTGAACACATTCCGAATTTGGTCCCTGAACCCCTGGCGAGTAGTAATATATAGTTCCGAATGCTCATAGAAAAAGTAGTGACAAGATTTGTCAATTAGCGTTCCGGCGCCCCGAACAGTTGTAACAAGGCAACCGAATGATGCTATTCACTT | TAGATCTCGTCTTTGGATCGCAATCTGTGACCACATTCAGATAGAGAAATCGGATACGGGGGTAAGTGATAAAATATAGCACCGAAGGCTCAGATTAAAAGTACTGGCAAGATTTATCAATTAGCGTTCCGGTTTATCAGGGGTTGTGTTATCCGACAGACCAAAGTTGGTAACACAGAATTTCACTT"
        string2 = "CAATAAAGCTAGCCAGGCAGTACCACGCGCCAGGCCGACGAACATCTGGACGCGCCTTATTCTTGGCTGGCTCAGTGTGATATCTCGAACTACGAACACGGTCATTGAAATATTGCCCAGACTGTAAGTCCGGACCCGGTGGCTCCGTCGGGTGACGCTCGCTTGTACTCGTGCGTGGTAATAAGTTTTGGGGGACTCACGAAGCGTCCGCC | CAAACGGCGGTCCCTAAAGCGTGGCAGTCAGTAATTCGCGTCCGACCCCTAACTTACGGCGTATAGCGGGCCTCCTGCCTCGGCAGTGTGTTATCTCGAACTTCTAACACATCAGCGAGACTCACGCTCGCAGTACCTTTAGCTATGGCATCCCTCGGCTCCGTCGTGTTATGCTCGGGTGCAGCGCCGCC"
        string3 = "ACGTAATTGTCATGTTGTCGGGCATAAGCTTCCTGTGAGCTCACGGCATTTCCTCATCGTCTTTGAAGAGTGCTCTCAGTTAACATGGGGTTGGTCCCTTGCCTGCAACCGCGTAGTTAAACAGGTGGAATAAAGATGCGCAAATATGGTTCCCCTCGGCTGCTCGGCTGGCCCTTGCTACCCGCTGATGGGTCGCATGGTAACGC | ACGTAATCGTCAAGCATTTAATGCGCCTGTGAGCTCACCAAGATTATGTCATCGTCTGTGTACTCTCAGTTGGGATGTACTATCGGCGAACGTTCCTGCCAGGCCTTTGTCCAAGAAATTACCTAAAATGTTCAACATGGGCTTGGTCCCTAGACTGCAACCTCGTAGTTAAACAGGCGGAATATATGGCAATCTACCAGTGCTCGACTGGTAAGGA"
        strings = [string1, string2, string3]
        answers = []
        expanswers = [1,1,1]

        for string in strings:
            parts = string.split("|")
            partA = d.clean(parts[0])
            partB = d.clean(parts[1])
            if len(partA)>len(partB):
                partA, partB = partB, partA
            for i in range(len(partA)):
                pA = partA[:i]
                pB = partB[:i]
                start = time.time()
                answer = d.score(pA, pB)
                duration = time.time()-start
                print("{0} | {1} | {2} | {3}| {4}".format(i,duration, answer, pA, pB,))
                


if __name__== "__main__":
    #subprocess.call (["pep8", "dna.py"])
    unittest.main(verbosity=3, exit = False)
    shutil.copyfile("dna.py", "dna.py3")
