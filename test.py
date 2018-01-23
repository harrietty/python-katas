import os
import unittest
from datetime import datetime

os.environ['ENV'] = 'TEST'

from katas.string_char_frequency import string_char_frequency
from katas.title_case import title_case
from katas.compare_arrays import comp
from katas.persistence import persistence
from katas.button_presses import button_presses
from katas.find_unique import find_unique
from katas.find_uniq_string import find_uniq_string
from katas.string_incrementer import string_inc
from katas.range_parser import range_parser
from katas.kebabize import kebabize
from katas.html_css_parse import parser
from katas.only_duplicates import only_duplicates
from katas.traverse_diagonally import diagonally
from katas.replace_chars import replace_chars
from katas.sort_nested_lists import sort_nested
from katas.reverse_parens import reverse_parens
from katas.product_of_parts import product_of_parts
from katas.esolang1 import parse_esolang
from katas.read_files import read_files
from katas.scramble_letters import scramble
from katas.cantor_diagonals import cantor
from katas.backwards_primes import backwards_primes
from katas.valid_mongo_id import Mongo

# ---------------- Scraping Katas ------------------------
from katas.scraping.get_leaderboard import get_leaderboard
from katas.scraping.scrape_top_users import scrape_top_users
from katas.scraping.get_honor import get_honor
from katas.scraping.get_member_since import get_member_since

class String_char_frequency(unittest.TestCase):
  def test_basic_functionality(self):
    self.assertEqual(string_char_frequency('foobbcc'), True)
    self.assertEqual(string_char_frequency('abcde'), True)
    self.assertEqual(string_char_frequency('aaaa'), True)
    self.assertEqual(string_char_frequency('abba'), False)
    self.assertEqual(string_char_frequency('foobbccffff'), False)
    self.assertEqual(string_char_frequency('aabbb'), True)
    self.assertEqual(string_char_frequency('nnnbnn'), True)
    self.assertFalse(string_char_frequency('gggghhhhii'))
    self.assertTrue(string_char_frequency('abcabcabcggga'))

class Title_case(unittest.TestCase):
  def test_basic_functionality(self):
    self.assertEqual(title_case(''), '')
    self.assertEqual(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')
    self.assertEqual(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows')
    self.assertEqual(title_case('the quick brown fox'), 'The Quick Brown Fox')

class Compare_arrays(unittest.TestCase):
  def test_basic_functionality(self):
    self.assertTrue(comp([], []))
    self.assertFalse(comp([1], []))
    self.assertTrue(comp([3], [9]))
    self.assertTrue(comp([3, 4], [9, 16]))
    self.assertTrue(comp([3, 4, 5], [9, 16, 25]))
    self.assertFalse(comp([3, 4, 5], [9, 18, 25]))
    self.assertTrue(comp([2, 4], [16, 4]))
    self.assertFalse(comp([2, 4, 6], [36, 3, 16]))
  
class Persistence(unittest.TestCase):
  def test_basic_functionality(self):
    self.assertEqual(persistence(4), 0)
    self.assertEqual(persistence(9), 0)
    self.assertEqual(persistence(33), 1)
    self.assertEqual(persistence(999), 4)
    self.assertEqual(persistence(39), 3)
    self.assertEqual(persistence(25), 2)
  
class Button_Presses(unittest.TestCase):
  def test_presses_for_single_chars(self):
    self.assertEqual(button_presses('a'), 1)
    self.assertEqual(button_presses('b'), 2)
    self.assertEqual(button_presses('9'), 5)
    self.assertEqual(button_presses('r'), 3)
    self.assertEqual(button_presses('G'), 1)
  def test_presses_for_multiple_chars(self):
    self.assertEqual(button_presses('AH'), 3)
    self.assertEqual(button_presses('LOL'), 9)
    self.assertEqual(button_presses('HOW R U'), 13)
    self.assertEqual(button_presses('WHERE DO U WANT 2 MEET L8R'), 47)
  def test_special_chars(self):
    self.assertEqual(button_presses('#'), 1)
    self.assertEqual(button_presses('1a'), 2)

class Find_Unique(unittest.TestCase):
  def test_basic_functionality(self):
    self.assertEqual(find_unique([1, 2, 2, 2]), 1)
    self.assertEqual(find_unique([2, 2, 7, 2]), 7)

class Find_Unique_String(unittest.TestCase):
  def test_basic_functionality(self):
    self.assertEqual(find_uniq_string([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]), 'BbBb')
    self.assertEqual(find_uniq_string(['aaa', 'aaa', 'bbb']), 'bbb')
    self.assertEqual(find_uniq_string([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]), 'foo')
    self.assertEqual(find_uniq_string([ '    ', 'a', '  ' ]), 'a')
    self.assertEqual(find_uniq_string(['foo ffooo', 'bat', 'fofoF', 'fO', 'oooooFFFF']), 'bat')
    self.assertEqual(find_uniq_string(['Tom Marvolo Riddle', 'I am Lord Voldemort', 'Harry Potter']), 'Harry Potter')

class String_Increment(unittest.TestCase):
  def test_basic_functionality(self):
    self.assertEqual(string_inc('foo'), 'foo1')
    self.assertEqual(string_inc('foo1'), 'foo2')
    self.assertEqual(string_inc('hello555'), 'hello556')
    self.assertEqual(string_inc('foobar001'), 'foobar002')
    self.assertEqual(string_inc('foobar101'), 'foobar102')
    self.assertEqual(string_inc('foobar00'), 'foobar01')
    self.assertEqual(string_inc('foobar099'), 'foobar100')
    self.assertEqual(string_inc('foobar99'), 'foobar100')
  def test_random_combos(self):
    self.assertEqual(string_inc('{CuV1hj31QRNW\'<C5881DqzgnTQi379237P_063:2yv*702<67900000009'), '{CuV1hj31QRNW\'<C5881DqzgnTQi379237P_063:2yv*702<67900000010')
    self.assertEqual(string_inc('0002862736139'), '0002862736140')
    self.assertEqual(string_inc('Huu,iuCF014672221000000000829'), 'Huu,iuCF014672221000000000830')
    self.assertEqual(string_inc('009'), '010')
  
class Range_Parser(unittest.TestCase):
  def test_creates_simple_ranges(self):
    self.assertEqual(range_parser('1-5'), [1, 2, 3, 4, 5])
    self.assertEqual(range_parser('1-10,14'), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14])
    self.assertEqual(range_parser('1'), [1])
  def test_can_provide_step(self):
    self.assertEqual(range_parser('1-5,9,10-20:2'), [1,2,3,4,5,9,10,12,14,16,18,20])
    self.assertEqual(range_parser('1-5, 9, 10-20:2'), [1,2,3,4,5,9,10,12,14,16,18,20])

class Kebebize(unittest.TestCase):
  def test_basic_functionality(self):
    self.assertEqual(kebabize('SOS'), 's-o-s')
    self.assertEqual(kebabize('camelsHaveThreeHumps'), 'camels-have-three-humps')
    self.assertEqual(kebabize('CamelsHaveHumps'), 'camels-have-humps')
  def test_ignores_nums(self):
    self.assertEqual(kebabize('camelsHave3Humps'), 'camels-have-humps')
    self.assertEqual(kebabize('SE60nP9EoexdibRtTYQ16rX1JG'), 's-en-p-eoexdib-rt-t-y-qr-x-j-g')
    self.assertEqual(kebabize('2Rs8slUDMYq22Ltutb'), 'rssl-u-d-m-yq-ltutb')

class Html_Css_Parser(unittest.TestCase):
  def test_basic_functionality(self):
    self.assertEqual(parser('LimeGreen'), {'r': 50,  'g': 205, 'b': 50 })
    self.assertEqual(parser('#80FFA0'), {'r': 128, 'g': 255, 'b': 160})
    self.assertEqual(parser('#3b7'), {'r': 51,  'g': 187, 'b': 119})

class Only_Duplicates(unittest.TestCase):
  def test_basic_functionality(self):
    self.assertEqual(only_duplicates('sass'), 'sss')
    self.assertEqual(only_duplicates('hello'), 'll')
    self.assertEqual(only_duplicates('12314256aaeff'), '1212aaff')

class Traverse_Diagonally(unittest.TestCase):
  def test_traverses_3x3(self):
    self.assertEqual(diagonally([
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ]), [9,6,8,3,5,7,2,4,1])
    self.assertEqual(diagonally([
      [5,3,4],
      [1,6,7],
      [9,7,5]
    ]), [5,7,7,4,6,9,3,1,5])
  def test_traverses_4x4(self):
    self.assertEqual(diagonally([
      [4,5,6,7],
      [1,2,3,4],
      [9,9,9,9],
      [4,3,2,4]
    ]), [4,9,2,4,9,3,7,3,9,4,6,2,9,5,1,4])

class Replace_Chars(unittest.TestCase):
  def test_basic_functionality(self):
    self.assertEqual(replace_chars(''), '')
    self.assertEqual(replace_chars('b'), 'e')
    self.assertEqual(replace_chars('z'), 'a')
    self.assertEqual(replace_chars('e'), 'd')
    self.assertEqual(replace_chars('a'), 'z')
  def test_replaces_chars_in_whole_words(self):
    self.assertEqual(replace_chars('abcdtuvwxyz'), 'zeeeutaaaaa')
    self.assertEqual(replace_chars('codewars'), 'enedazuu')

class Sort_Nested_Lists(unittest.TestCase):
  def test_basic_functionality(self):
    A=[[[3, 2, 1]]]
    expected=[[[1, 2, 3]]]
    self.assertEqual(sort_nested(A),expected)
    A = [[[2, 1], [4, 3]], [[6, 5], [8, 7]]]
    expected = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    self.assertEqual(sort_nested(A), expected)
    A=[[[29, 32], [82, 61], [75, 91]], [[69, 99], [74, 23], [70, 97]]]
    expected=[[[23, 29], [32, 61], [69, 70]], [[74, 75], [82, 91], [97, 99]]]
    self.assertEqual(sort_nested(A), expected)

class Reverse_Parens(unittest.TestCase):
  def test_basic_functionality(self):
    self.assertEqual(reverse_parens(''), -1)
    self.assertEqual(reverse_parens('()))'), 1)
    self.assertEqual(reverse_parens('(((()((())()'), 2)
    self.assertEqual(reverse_parens('())()))))()()('), 4)
    self.assertEqual(reverse_parens('(((())'), 1)
    self.assertEqual(reverse_parens('())((('), 3)
    self.assertEqual(reverse_parens(')))))((((('), 6)
    self.assertEqual(reverse_parens('((('), -1)

class Product_Of_Parts(unittest.TestCase):
  def test_basic_functionality(self):
    self.assertEqual(product_of_parts(1234), 144)
    self.assertEqual(product_of_parts(4321), 252)

class Esolang(unittest.TestCase):
  def test_basic_functionality(self):
    input = '+'*50 + '.'
    self.assertEqual(parse_esolang(input), '2')
    input = '+'*97 + '.'
    self.assertEqual(parse_esolang(input), 'a')
    input = '+'*78 + '.'
    self.assertEqual(parse_esolang(input), 'N')
  def test_longer_instructions(self):
    input = '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++.+++++++..+++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++.+++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.'
    self.assertEqual(parse_esolang(input), 'Hello, World!')
    input = f'{"+"*50}.hfjs9342+++.'
    self.assertEqual(parse_esolang(input), '25')

class Get_Leaderboard(unittest.TestCase):
  def test_basic_functionality(self):
    self.assertEqual(len(get_leaderboard()), 500)
    self.assertTrue(get_leaderboard()[0] > 128828)
    self.assertTrue(get_leaderboard()[1] > 124363)

class Scrape_Top_Users(unittest.TestCase):
  def test_basic_functionality(self):
    self.assertEqual(len(scrape_top_users().position), 500)
    self.assertEqual(scrape_top_users().position[1].name, 'g964')
    self.assertEqual(scrape_top_users().position[1].clan, 'None')
    self.assertTrue(scrape_top_users().position[1].honor >= 128840)

class Get_User_Honor(unittest.TestCase):
  def test_basic_functionality(self):
    self.assertTrue(get_honor('harrietty') > 1000)
    self.assertTrue(get_honor('chrishill') > 2000)

class Get_Member_Since(unittest.TestCase):
  def test_basic_functionality(self):
    self.assertEqual(get_member_since('harrietty'), 'Feb 2016')
    self.assertEqual(get_member_since('chrishill'), 'Nov 2013')
    self.assertEqual(get_member_since('e.milia'), 'Feb 2017')

class Read_Files(unittest.TestCase):
  def test_basic_functionality(self):
    self.assertEqual(read_files(os.getcwd() + '/data/read_files_test'), {
      'a.txt': 'Hello world\n',
      'b.txt': 'Hungry Heart',
      'c.txt': 'Little ghost'
    })

class Scramble_Letters(unittest.TestCase):
  def test_scrambles_single_word(self):
    self.assertEqual(scramble('g'), 'g')
    self.assertEqual(scramble('professionals'), 'paefilnoorsss')
    self.assertEqual(scramble('marzipan'), 'maaiprzn')
    self.assertEqual(scramble('world'), 'wlord')
  def test_multiple_words(self):
    self.assertEqual(scramble('hello world'), 'hello wlord')
    self.assertEqual(scramble('bathroom tiles'), 'bahoortm teils')
  def test_ignore_special_chars(self):
    self.assertEqual(scramble('wor-ld'), 'wlo-rd')
    self.assertEqual(scramble('-world'), '-wlord')
    self.assertEqual(scramble('world-'), 'wlord-')

class Cantor_Diagonals(unittest.TestCase):
  def test_basic_functionality(self):
    self.assertEqual(cantor([[0,0],[1,1]]), [1, 0])
    self.assertEqual(cantor([[0,0,1],[1,1,0],[1,1,1]]), [1, 0, 0])
    self.assertEqual(cantor([[1,1,1],[1,0,0],[1,0,0]]), [0,1,1])

class Backwards_Primes(unittest.TestCase):
  def test_basic_functionality(self):
    self.assertEqual(backwards_primes(2, 15), [13])
    self.assertEqual(backwards_primes(2, 100), [13, 17, 31, 37, 71, 73, 79, 97])
    self.assertEqual(backwards_primes(1095000, 1095403), [1095047, 1095209, 1095319, 1095403])

class Valid_Mongo_ID(unittest.TestCase):
  def test_basic_functionality(self):
    self.assertEqual(Mongo.is_valid(111111111111111111111111), False)
    self.assertEqual(Mongo.is_valid('507f1f77bcf86cd799439011'), True)
    self.assertEqual(Mongo.is_valid('507f1f77bcf86cz799439011'), False)
    self.assertEqual(Mongo.is_valid('507f1f77bcf86cD799439011'), False)
    self.assertEqual(Mongo.get_timestamp(111111111111111111111111), False)
    self.assertEqual(Mongo.get_timestamp('507f1f77bcf86cz799439011'), False)
    self.assertEqual(Mongo.get_timestamp('507f1f77bcf86cd799439016'), datetime(2012, 10, 17, 22, 13, 27))
