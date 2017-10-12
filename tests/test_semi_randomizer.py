import unittest
from semi_randomizer import SemiRandomizer


class TestSemiRandomizer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sr = SemiRandomizer('input/semi_randomizer_test_file.txt', 3)

    def test_slice_index_and_occurrences(self):
        actual = self.sr.slice_index_and_occurrences
        expected = {0: 6, 1: 2, 2: 1, 3: 1}
        self.assertEqual(actual, expected)

    def test_slice_size(self):
        actual = self.sr.slice_size
        expected = 20
        self.assertAlmostEqual(actual, expected)

    def test_lowest_mass(self):
        actual = self.sr.lowest_mass
        expected = 10
        self.assertAlmostEqual(actual, expected)

    def test_highest_mass(self):
        actual = self.sr.highest_mass
        expected = 70
        self.assertAlmostEqual(actual, expected)

    def test_get_mass_from_index(self):
        index = 2
        actual = self.sr.get_mass_from_index(index)
        expected = 60
        self.assertAlmostEqual(actual, expected)

    # TODO: FIX THIS TEST
    # def test_get_semi_slice_index(self):
    #     # This test relies on the fact that the probability of failing is incredibly small
    #     # If it does fail, make sure to run it again
    #     index_and_occurrences = {}
    #     for i in range(100000):
    #         index = self.sr.get_semi_random_mass()
    #         if index in index_and_occurrences:
    #             index_and_occurrences[index] += 1
    #         else:
    #             index_and_occurrences[index] = 1
    #
    #     success = True
    #
    #     for key, value in index_and_occurrences.items():
    #         # value = round(value / 10000)
    #         print(value)
    #         if key == 0:
    #             if value != 6:
    #                 success = False
    #                 print('!')
    #         elif key == 1:
    #             if value != 2:
    #                 success = False
    #                 print('!')
    #         elif key == 2:
    #             if value != 1:
    #                 success = False
    #                 print('!')
    #         elif key == 3:
    #             if value != 1:
    #                 success = False
    #                 print('!')
    #
    #     self.assertTrue(success)

