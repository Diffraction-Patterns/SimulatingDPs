from unittest import mock
from unittest import TestCase
from processing.prompt_abc import prompt_abc

@mock.patch('processing.prompt_abc.input', create=True)
class TestABCInput(TestCase):
  def test_abc_input(self, mocked_input):
      mocked_input.side_effect = [
          'a',
          '3',
          '-4',
          '1.11'
          ]
      actual1, actual2, actual3 = prompt_abc()
      expected1, expected2, expected3 = 3, -4, 1.11
      self.assertEqual(actual1, expected1)
      self.assertEqual(actual2, expected2)
      self.assertEqual(actual3, expected3)
