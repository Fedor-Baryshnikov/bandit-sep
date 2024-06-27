import unittest
from unittest.mock import patch
from bandit.core import extension_loader

class TestGetTestId(unittest.TestCase):

    def setUp(self):
        self.manager = extension_loader.Manager()
        self.load_formatters("bandit.formatters")
        self.load_plugins("bandit.plugins")
        self.load_blacklists("bandit.blacklists")

    def test_get_test_id(self):
        self.manager.plugins_by_name = {"cow": 1}
        self.manager.blacklist_by_name = {"chicken": 1}
        self.assertEqual(1, self.manager.get_test_id("cow"))