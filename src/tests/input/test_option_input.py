from unittest import mock
from unittest import TestCase
from processing.prompt_option import prompt_options

@mock.patch('processing.prompt_option.input', create=True)
class TestOptionInput(TestCase):
  def test_lattice_option(self, mocked_input):
      mocked_input.side_effect = [
          '3',
          '1',
          'b',
          ]
      actual1, actual2 = prompt_options()
      print(actual1)
      expected1, expected2 = 1, 'b'
      self.assertEqual(actual1, expected1)
      self.assertEqual(actual2, expected2)

  def test_zone_axis_option(self, mocked_input):
      mocked_input.side_effect = [
          '3',
          '2',
          '6',
          'u',
          'd'
          ]
      actual1, actual2 = prompt_options()
      print(actual1)
      expected1, expected2 = 2, 'd'
      self.assertEqual(actual1, expected1)
      self.assertEqual(actual2, expected2)