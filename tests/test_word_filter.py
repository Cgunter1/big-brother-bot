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

        # Both values must be the same, if not the hash does
        # not work.
        hashed_value1 = WordFilter.hash("256", "Hello World!")
        hashed_value2 = WordFilter.hash("256", "Hello World!")

        self.assertNotEqual(hashed_value1, "Hello World!")
        self.assertEqual(hashed_value1, hashed_value2)

        # Test values with 384 hash.
        hashed_value1 = WordFilter.hash("384", "Hello World!")
        hashed_value2 = WordFilter.hash("384", "Hello World!")

        self.assertNotEqual(hashed_value1, "Hello World!")
        self.assertEqual(hashed_value1, hashed_value2)

        # Test values with invalid inputs
        with self.assertRaises(ValueError):
            WordFilter.hash("256", None)
        with self.assertRaises(ValueError):
            WordFilter.hash("256", 12)
        with self.assertRaises(ValueError):
            WordFilter.hash(None, "hello")

    def test_add_passage(self):
        """Tests the add_passage method with a normal input.
        """
        wf = WordFilter.create_default_filter()
        wf.add_passage("Hello World", "Goodbye")

        # Makes sure that it exists in both bloom filters
        self.assertTrue(1 in wf.bloom_filter1)
        self.assertTrue(1 in wf.bloom_filter2)

        # Makes sure it only exists once and not multiple times.
        self.assertEqual(wf.bloom_filter1.count(1), 1)
        self.assertTrue(wf.bloom_filter2.count(1), 1)

        # Makes sure that the passage exists in the hashtable.
        self.assertEqual(wf.hash_table[4]["word"], "Hello World")
        self.assertEqual(wf.hash_table[4]["translation"], "Goodbye")
        self.assertEqual(wf.hash_table[4]["next"], None)

    def test_add_passage_and_dup(self):
        """Tests the add_passage method with adding duplicate
        words to the word filter.
        """
        wf = WordFilter.create_default_filter()
        wf.add_passage("Hello World", None)
        wf.add_passage("Hello World", None)

        # Makes sure that the hashtable does not add duplicates.
        self.assertEqual(wf.hash_table[4]["next"], None)


if __name__ == "__main__":
    main()
