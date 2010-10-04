"""Unit tests for utils."""

import unittest
import os

import utils


class TestMKDIR(unittest.TestCase) :
    """Unit tests for mkdir_p."""
    
    def test_works(self) :
        utils.mkdir_p('tmp/tmp2')
        self.assertTrue(os.path.exists ('tmp/tmp2'))
        # This should not raise an error.
        utils.mkdir_p('tmp/tmp2')


    def tearDown(self) :
        os.rmdir('tmp/tmp2')
        os.rmdir('tmp')

if __name__ == '__main__' :
    unittest.main()

