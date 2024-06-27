import unittest
from unittest.mock import patch
from bandit.core import extension_loader

class TestGetTestId(unittest.TestCase):

    def setUp(self):
        self.manager = extension_loader.Manager()
        self.manager.load_plugins("bandit.plugins")
        
    def test_get_test_id(self):
        self.manager.load_blacklists("bandit.blacklists")
        self.manager.load_formatters("bandit.formatters")
        self.manager.load_plugins("bandit.plugins")
        self.assertIs(self.manager.get_test_id("B001"), None, f'failed, test id is: {self.manager.get_test_id("B001")}')
        

    def test_get_test_id2(self):
        self.manager.load_blacklists("bandit.blacklists")
        self.manager.load_formatters("bandit.formatters")
        self.manager.load_plugins("bandit.plugins")
        self.assertIs(self.manager.get_test_id("any_other_function_with_shell_equals_true"), "B604", f'test id is: {self.manager.get_test_id("any_other_function_with_shell_equals_true")}')
        
