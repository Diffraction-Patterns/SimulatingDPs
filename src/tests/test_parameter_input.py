from unittest import mock
from unittest import TestCase
from processing.parameter_handler import prompt_input

class TestInput(TestCase):
    @mock.patch('processing.parameter_handler.input', create=True)
    def test_exit(self, mocked_input):
        mocked_input.side_effect = ['3.287', 'Exit']
        actual = prompt_input()
        self.assertIsNone(actual)