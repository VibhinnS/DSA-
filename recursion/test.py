import unittest

from practise import subsequence

class SubsequenceTestCase(unittest.TestCase):
    def test_subsequence(self):
        self.assertEqual(subsequence("abc", ""), ['', 'c', 'b', 'bc', 'a', 'ac', 'ab', 'abc'])
        self.assertEqual(subsequence("hello", ""), ['', 'o', 'l', 'lo', 'l', 'll', 'h', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll', 'he', 'ho', 'hl', 'hlo', 'hl', 'hll'])
