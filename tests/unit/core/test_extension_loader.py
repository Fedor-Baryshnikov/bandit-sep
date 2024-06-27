import unittest
from unittest.mock import patch
from bandit.core import extension_loader

class TestGetTestId(unittest.TestCase):

    def setUp(self):
        self.manager = extension_loader.Manager()
        self.manager.load_plugins("bandit.plugins")
        # self.assertTrue(False, f'plugins: {self.manager.plugins_by_name}')

    def test_get_test_id(self):
        self.manager.load_blacklists("bandit.blacklists")
        self.manager.load_formatters("bandit.formatters")
        self.manager.load_plugins("bandit.plugins")
        # self.assertTrue(False, f'test id is: {self.manager.get_test_id("B001")}')
        self.manager.get_test_id("B001")
    
    def test_get_test_id2(self):
        self.manager.load_blacklists("bandit.blacklists")
        self.manager.load_formatters("bandit.formatters")
        self.manager.load_plugins("bandit.plugins")
        # self.assertTrue(False, f'test id is: {self.manager.get_test_id("any_other_function_with_shell_equals_true")}')
        self.manager.get_test_id("any_other_function_with_shell_equals_true")
