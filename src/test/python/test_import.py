import unittest

import hamcrest
from hamcrest import assert_that


class TestImport(unittest.TestCase):
    def setUp(self):
        pass

    def test_it(self):
        import py_elastic_int_testing
        assert_that(py_elastic_int_testing, hamcrest.not_none())
