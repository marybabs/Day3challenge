import unittest

from sort import sort_list, find_number

class TestSortingList(unittest.TestCase):
    
    def test_sort(self):
        my_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,"hey","you","hello","c","u","ltr"]
        result= sort_list(my_list)
        self.assertEqual(result, {'Even': [2, 4, 6, 8, 10, 12, 14], 'Odd': [1, 3, 5, 7, 9, 11, 13, 15], 'Char': ['c', 'hello', 'hey', 'ltr', 'u','you'], 'Other': []})


    def find_number(self):
        my_number = [1,2,4,5,7,9]

        result = find_number(my_number)
        self.assertEqual(result,[3,6,8])

