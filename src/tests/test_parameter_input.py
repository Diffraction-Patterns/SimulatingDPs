from unittest import mock
from unittest import TestCase
from processing.parameter_handler import prompt_input
from models.crystal_parameters import CrystalParameters

@mock.patch('processing.parameter_handler.input', create=True)
class TestInput(TestCase):
    def test_exit(self, mocked_input):
        mocked_input.side_effect = ['3.287', 'Exit']
        actual = prompt_input()
        self.assertIsNone(actual)

    def test_valid_input(self, mocked_input):
        mocked_input.side_effect = [
            '3.852', # a 
            '3.852', # b
            '3.723', # c
            '90.0', # alpha
            '90.0', # beta
            '90.0', # gamma
            'n'
            ]
        actual = prompt_input()
        expected = CrystalParameters(3.852, 3.852, 3.723, 90.0, 90.0, 90.0)
        self.assertEqual(actual, expected)

    def test_invalid_input(self, mocked_input):
        mocked_input.side_effect = [
            '3.852', # a 
            '3.852', # b
            'bad input', # invalid c
            '3.723', # valid c
            '90.0', # alpha
            '90.0', # beta
            'bad gam', # invalid gamma
            '90.0', # valid gamma
            'bad recip', # invalid reciprocal space 
            'y' # valid reciprocal space
            ]
        actual = prompt_input()
        expected = CrystalParameters(3.852, 3.852, 3.723, 90.0, 90.0, 90.0, True)
        self.assertEqual(actual, expected)