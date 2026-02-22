from unittest import mock
from unittest import TestCase
from processing.parameter_handler import prompt_zone_axis_direction
from models.zone_axis import ZoneAxis

@mock.patch('processing.parameter_handler.input', create=True)
class TestCrystalInput(TestCase):
    def test_exit(self, mocked_input):
        mocked_input.side_effect = ['1', 'Exit']
        actual = prompt_zone_axis_direction()
        self.assertIsNone(actual)

    