from mock import patch
from django.test import TestCase
from django.utils.six import StringIO
from dbbackup.management.commands._base import BaseDbBackupCommand


class BaseDbBackupCommandLogTest(TestCase):
    def setUp(self):
        self.command = BaseDbBackupCommand()
        self.command.stdout = StringIO()

    def test_less_level(self):
        self.command.verbosity = 1
        self.command.log("foo", 2)
        self.command.stdout.seek(0)
        self.assertFalse(self.command.stdout.read())

    def test_more_level(self):
        self.command.verbosity = 1
        self.command.log("foo", 0)
        self.command.stdout.seek(0)
        self.assertEqual('foo', self.command.stdout.read())

    def test_quiet(self):
        self.command.quiet = True
        self.command.verbosity = 1
        self.command.log("foo", 0)
        self.command.stdout.seek(0)
        self.assertFalse(self.command.stdout.read())


class BaseDbBackupCommandAskYesOrNo(TestCase):
    def setUp(self):
        self.command = BaseDbBackupCommand()
        self.command.stdout = StringIO()

    @patch('dbbackup.management.commands._base.input', return_value='y')
    def test_yes(self, *args):
        self.assertTrue(self.command.ask_yes_or_no(''))

    @patch('dbbackup.management.commands._base.input', return_value='Y')
    def test_Y(self, *args):
        self.assertTrue(self.command.ask_yes_or_no(''))

    @patch('dbbackup.management.commands._base.input', return_value='n')
    def test_no(self, *args):
        self.assertFalse(self.command.ask_yes_or_no(''))

    @patch('dbbackup.management.commands._base.input', return_value='')
    def test_empty_input(self, *args):
        self.assertTrue(self.command.ask_yes_or_no(''))

    @patch('dbbackup.management.commands._base.input', return_value='')
    def test_empty_input_default_false(self, *args):
        self.assertFalse(self.command.ask_yes_or_no('', default=False))

    def test_noinput(self):
        self.assertTrue(self.command.ask_yes_or_no('', noinput=True))

    def test_noinput_default_false(self):
        self.assertFalse(self.command.ask_yes_or_no('', noinput=True, default=False))
