# -*- coding: utf-8 -*-
import random
import unittest
import xmlrunner


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = list(range(10))

    @unittest.skip("demonstrating skipping")
    def test_skipped(self):
        self.fail("Algo pasó, este Test fue Omitido")

    def test_choice(self):
        so = ['GNU/Linux','Windows','OSX',]
        value = 'GNU/Linux'
        self.assertTrue(value in so)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

    def test_upper(self):
        self.assertEqual('Daniel'.upper(), 'Omar')

if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)

