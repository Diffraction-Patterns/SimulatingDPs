from unittest import mock
from unittest import TestCase
from processing.prompt_zone_axis import prompt_zone_axis_direction
from models.zone_axis import ZoneAxis

@mock.patch('processing.prompt_zone_axis.input', create=True)
class TestCrystalInput(TestCase):
    def test_exit(self, mocked_input):
        mocked_input.side_effect = ['1', 'Exit']
        actual = prompt_zone_axis_direction()
        self.assertIsNone(actual)

    def test_valid_input(self, mocked_input):
        mocked_input.side_effect = ['110']
        actual = prompt_zone_axis_direction()
        expected = ZoneAxis(1, 1, 0)
        self.assertEqual(actual, expected)

    def test_invalid_input(self, mocked_input):
        mocked_input.side_effect = [
            '-12', # invalid
            '1.852', # invalid
            '1111', # invalid 
            'bad gam', # invalid 
            '123', # valid
            ]
        actual = prompt_zone_axis_direction()
        expected = ZoneAxis(1, 2, 3)
        self.assertEqual(actual, expected)
    
    def test_space_input(self, mocked_input):
        mocked_input.side_effect = ['1 2 3']
        actual = prompt_zone_axis_direction()
        expected = ZoneAxis(1, 2, 3)
        self.assertEqual(actual, expected)

    def test_space_input(self, mocked_input):
        mocked_input.side_effect = ['1, 2, 3']
        actual = prompt_zone_axis_direction()
        expected = ZoneAxis(1, 2, 3)
        self.assertEqual(actual, expected)

    def test_negative_input(self, mocked_input):
        mocked_input.side_effect = ['1-23', '1,-2,3']
        actual = prompt_zone_axis_direction()
        expected = ZoneAxis(1, -2, 3)
        self.assertEqual(actual, expected)