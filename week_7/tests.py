import unittest
from reverse_list_in_place import reverse_list_in_place

class MyAppUnitTestCase(unittest.TestCase):

    def test_list_reverse_odd(self):

        fruits = ['apple', 'berry', 'cherry']
        reverse_list_in_place(fruits)

        self.assertEqual(fruits, ['cherry', 'berry', 'apple'])

    def test_list_reverse_even(self):

        fruits = ['apple', 'berry', 'cherry', 'durian']
        reverse_list_in_place(fruits)

        self.assertEqual(fruits, ['durian', 'cherry', 'berry', 'apple'])


if __name__ == "__main__":
    unittest.main()