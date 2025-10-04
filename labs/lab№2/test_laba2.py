from func_laba2 import funSum
import unittest


# Тесты
class TestMath(unittest.TestCase):
    def test_rigth_0el(self):
        self.assertEqual(funSum([], 5), 'Массив отсутсвует, пуст или слишком мал')

    def test_rigth_1el(self):
        self.assertEqual(funSum([1], 5), 'Массив отсутсвует, пуст или слишком мал')

    def test_rigth_2el(self):
        self.assertEqual(funSum([2, 3], 5), [0, 1])

    def test_rigth_4el(self):
        self.assertEqual(funSum([2, 3, 7, 1], 5), [0, 1])

    def test_rigth_notSum(self):
        self.assertEqual(funSum([1, 3, 5, 2], 13), 'Отсутсвует комбинация элементов подходящих условию')
    
    def test_rigth_notInt(self):
        self.assertEqual(funSum([2, 3], ''), "Target нераспознан")

    def test_rigth_notList(self):
        self.assertEqual(funSum('', 5), 'Массив отсутсвует, пуст или слишком мал')
    
    def test_rigth_bigInt(self):
        self.assertEqual(funSum([1,10000,5780002, 678129, 544000, 6754356, 1434782739428], 544001), [0,4])

    def test_rigth_0list(self):
        self.assertEqual(funSum([0,0,0,0,0,0,0,8], 8), [0,7])



# Запуск тестов
unittest.main(argv=[''], verbosity=2, exit=False)