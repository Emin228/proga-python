from main_laba3 import gen_bin_tree
import unittest


# Тесты
class TestMath(unittest.TestCase):
    def test_root_0(self):
        self.assertEqual(gen_bin_tree(2, 0), {'left': {'left': {'left': None, 'right': None, 'value': -2},
          'right': {'left': None, 'right': None, 'value': 0},
          'value': -1},
 'right': {'left': {'left': None, 'right': None, 'value': 0},
           'right': {'left': None, 'right': None, 'value': 2},
           'value': 1},
 'value': 0})
        
    def test_root_minus(self):
        self.assertEqual(gen_bin_tree(3, -13), {'left': {'left': {'left': {'left': None, 'right': None, 'value': -16},
                   'right': {'left': None, 'right': None, 'value': -14},
                   'value': -15},
          'right': {'left': {'left': None, 'right': None, 'value': -14},
                    'right': {'left': None, 'right': None, 'value': -12},
                    'value': -13},
          'value': -14},
 'right': {'left': {'left': {'left': None, 'right': None, 'value': -14},
                    'right': {'left': None, 'right': None, 'value': -12},
                    'value': -13},
           'right': {'left': {'left': None, 'right': None, 'value': -12},
                     'right': {'left': None, 'right': None, 'value': -10},
                     'value': -11},
           'value': -12},
 'value': -13})
        
    def test_str(self):
        self.assertEqual(gen_bin_tree('3', '13'), {'left': {'left': {'left': {'left': None, 'right': None, 'value': 10},
                   'right': {'left': None, 'right': None, 'value': 12},
                   'value': 11},
          'right': {'left': {'left': None, 'right': None, 'value': 12},
                    'right': {'left': None, 'right': None, 'value': 14},
                    'value': 13},
          'value': 12},
 'right': {'left': {'left': {'left': None, 'right': None, 'value': 12},
                    'right': {'left': None, 'right': None, 'value': 14},
                    'value': 13},
           'right': {'left': {'left': None, 'right': None, 'value': 14},
                     'right': {'left': None, 'right': None, 'value': 16},   
                     'value': 15},
           'value': 14},
 'value': 13})

    


# Запуск тестов

unittest.main()