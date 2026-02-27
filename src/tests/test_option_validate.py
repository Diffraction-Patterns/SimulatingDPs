from unittest import TestCase
import processing.prompt_option as po

class TestOptions(TestCase):
  def test_validate_parent(self):
    bad_op1 = '11'
    bad_op2 = 'a'
    bad_op3 = '5'
    op = '1'
    self.assertFalse(po.validate_p_option(bad_op1, 2))
    self.assertFalse(po.validate_p_option(bad_op2, 2))
    self.assertFalse(po.validate_p_option(bad_op3, 2))
    self.assertTrue(po.validate_p_option(op, 2))

  def test_validate_child(self):
    bad_op1 = '1'
    bad_op2 = 'aa'
    op = 'a'
    self.assertFalse(po.validate_c_option(bad_op1))
    self.assertFalse(po.validate_c_option(bad_op2))
    self.assertTrue(po.validate_c_option(op))