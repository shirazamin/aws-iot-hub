# -*- coding: utf-8 -*-

from .context import hub

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(hub.hmm())


if __name__ == '__main__':
    unittest.main()
