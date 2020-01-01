from unittest import TestCase, mock, main
from big_brother_bot.word_filter import WordFilter


class WordFilterTest(TestCase):

    def test_class_initialization(self):
        """Test if class is initialized properly
        with all its attributes like bloomfilters
        and hashtable. Then test if arguments are
        valid integers.

        """
        wf = WordFilter(1000, 1000, 20)

        self.assertEqual(len(wf.bloom_filter1), 1000)
        self.assertEqual(len(wf.bloom_filter2), 1000)
        self.assertEqual(len(wf.hash_table), 20)

        with self.assertRaises(ValueError):
            WordFilter(None, "1000", 'd')
        with self.assertRaises(ValueError):
            WordFilter(1000, "1000", 'd')
        with self.assertRaises(ValueError):
            WordFilter(None, 1000, 2.1)

    def test_default_class_initialization(self):
        """Test if class is initialized properly
         with the create_default_filter.
         """

        wf = WordFilter.create_default_filter()

        self.assertEqual(len(wf.bloom_filter1), 1000)
        self.assertEqual(len(wf.bloom_filter2), 1000)
        self.assertEqual(len(wf.hash_table), 30)

    def test_hash_function(self):
        """Tests the hash function for valid and invalid values.
        """
