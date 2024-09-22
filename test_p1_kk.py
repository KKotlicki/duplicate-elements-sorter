import unittest
from p1_kk import get_ordered_duplicates


class TestGetOrderedDuplicates(unittest.TestCase):

    def test_basic_duplicates(self):
        lst = ["b", "a", "c", "c", "e", "a", "c", "d", "c", "d"]
        expected = ['a', 'c', 'd']
        print(f"\nTesting with input: {lst}")
        print(f"Expected output: {expected}")
        self.assertEqual(get_ordered_duplicates(lst), expected)

    def test_no_duplicates(self):
        lst = ["a", "b", "c", "d", "e"]
        expected = []
        print(f"\nTesting with input: {lst}")
        print(f"Expected output: {expected}")
        self.assertEqual(get_ordered_duplicates(lst), expected)

    def test_all_duplicates(self):
        lst = ["a", "a", "b", "b", "c", "c"]
        expected = ['a', 'b', 'c']
        print(f"\nTesting with input: {lst}")
        print(f"Expected output: {expected}")
        self.assertEqual(get_ordered_duplicates(lst), expected)

    def test_empty_list(self):
        lst = []
        expected = []
        print(f"\nTesting with input: {lst}")
        print(f"Expected output: {expected}")
        self.assertEqual(get_ordered_duplicates(lst), expected)

    def test_single_element(self):
        lst = ["a"]
        expected = []
        print(f"\nTesting with input: {lst}")
        print(f"Expected output: {expected}")
        self.assertEqual(get_ordered_duplicates(lst), expected)

    def test_unhashable_elements(self):
        lst = [1, 2, 3, [4, 5], 1]
        print(f"\nTesting with input: {lst}")
        print(f"Expected output: TypeError")
        with self.assertRaises(TypeError):
            get_ordered_duplicates(lst)

    def test_large_input(self):
        lst = ["a"] * 1000 + ["b"] * 1000 + ["c"] * 500
        expected = ['a', 'b', 'c']
        print(f"\nTesting with large input")
        print(f"Expected output: {expected}")
        self.assertEqual(get_ordered_duplicates(lst), expected)

    def test_mixed_types(self):
        lst = [1, "a", 1, "b", "a", "c"]
        expected = [1, "a"]
        print(f"\nTesting with input: {lst}")
        print(f"Expected output: {expected}")
        self.assertEqual(get_ordered_duplicates(lst), expected)

    def test_non_character_order(self):
        lst = ["b", "b", "c", "a", "d", "a", "c"]
        expected = ["b", "c", "a"]
        print(f"\nTesting with input: {lst}")
        print(f"Expected output: {expected}")
        self.assertEqual(get_ordered_duplicates(lst), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
