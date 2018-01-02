import unittest

from katas.string_char_frequency import string_char_frequency
from katas.title_case import title_case
from katas.compare_arrays import comp
from katas.persistence import persistence
from katas.button_presses import button_presses
from katas.find_unique import find_unique
from katas.find_uniq_string import find_uniq_string
from katas.string_incrementer import string_inc

class KataTests(unittest.TestCase):
  def test_string_char_frequency(self):
    self.assertEqual(string_char_frequency('foobbcc'), True)
    self.assertEqual(string_char_frequency('abcde'), True)
    self.assertEqual(string_char_frequency('aaaa'), True)
    self.assertEqual(string_char_frequency('abba'), False)
    self.assertEqual(string_char_frequency('foobbccffff'), False)
    self.assertEqual(string_char_frequency('aabbb'), True)
    self.assertEqual(string_char_frequency('nnnbnn'), True)
    self.assertFalse(string_char_frequency('gggghhhhii'))
    self.assertTrue(string_char_frequency('abcabcabcggga'))
  
  def test_title_case(self):
    self.assertEqual(title_case(''), '')
    self.assertEqual(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')
    self.assertEqual(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows')
    self.assertEqual(title_case('the quick brown fox'), 'The Quick Brown Fox')

  def test_comp_arrays(self):
    self.assertTrue(comp([], []))
    self.assertFalse(comp([1], []))
    self.assertTrue(comp([3], [9]))
    self.assertTrue(comp([3, 4], [9, 16]))
    self.assertTrue(comp([3, 4, 5], [9, 16, 25]))
    self.assertFalse(comp([3, 4, 5], [9, 18, 25]))
    self.assertTrue(comp([2, 4], [16, 4]))
    self.assertFalse(comp([2, 4, 6], [36, 3, 16]))
  
  def test_persistence(self):
    self.assertEqual(persistence(4), 0)
    self.assertEqual(persistence(9), 0)
    self.assertEqual(persistence(33), 1)
    self.assertEqual(persistence(999), 4)
    self.assertEqual(persistence(39), 3)
    self.assertEqual(persistence(25), 2)
  
  def test_button_presses(self):
    self.assertEqual(button_presses('a'), 1)
    self.assertEqual(button_presses('b'), 2)
    self.assertEqual(button_presses('9'), 5)
    self.assertEqual(button_presses('r'), 3)
    self.assertEqual(button_presses('G'), 1)
    self.assertEqual(button_presses('AH'), 3)
    self.assertEqual(button_presses('LOL'), 9)
    self.assertEqual(button_presses('HOW R U'), 13)
    self.assertEqual(button_presses('WHERE DO U WANT 2 MEET L8R'), 47)
    self.assertEqual(button_presses('#'), 1)
    self.assertEqual(button_presses('1a'), 2)
  
  def test_find_unique(self):
    self.assertEqual(find_unique([1, 2, 2, 2]), 1)
    self.assertEqual(find_unique([2, 2, 7, 2]), 7)
  
  def test_find_uniq_string(self):
    self.assertEqual(find_uniq_string([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]), 'BbBb')
    self.assertEqual(find_uniq_string(['aaa', 'aaa', 'bbb']), 'bbb')
    self.assertEqual(find_uniq_string([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]), 'foo')
    self.assertEqual(find_uniq_string([ '    ', 'a', '  ' ]), 'a')
    self.assertEqual(find_uniq_string(['foo ffooo', 'bat', 'fofoF', 'fO', 'oooooFFFF']), 'bat')
    self.assertEqual(find_uniq_string(['Tom Marvolo Riddle', 'I am Lord Voldemort', 'Harry Potter']), 'Harry Potter')
  
  def test_str_incrementer(self):
    self.assertEqual(string_inc('foo'), 'foo1')
    self.assertEqual(string_inc('foo1'), 'foo2')
    self.assertEqual(string_inc('hello555'), 'hello556')
    self.assertEqual(string_inc('foobar001'), 'foobar002')
    self.assertEqual(string_inc('foobar101'), 'foobar102')
    self.assertEqual(string_inc('foobar00'), 'foobar01')
    self.assertEqual(string_inc('foobar099'), 'foobar100')
    self.assertEqual(string_inc('foobar99'), 'foobar100')
    self.assertEqual(string_inc('{CuV1hj31QRNW\'<C5881DqzgnTQi379237P_063:2yv*702<67900000009'), '{CuV1hj31QRNW\'<C5881DqzgnTQi379237P_063:2yv*702<67900000010')
    self.assertEqual(string_inc('0002862736139'), '0002862736140')
    self.assertEqual(string_inc('Huu,iuCF014672221000000000829'), 'Huu,iuCF014672221000000000830')
    self.assertEqual(string_inc('009'), '010')