class WordFilter:
    """
      A class used to represent a word filter
      that filters words through its filters and
      hashtables.
      ...

      Attributes
      ----------
      bloom_filter_256 : arr
          Is a bloom filter that uses AES256 to hash words and map
          them into a 1000 length array.
      bloom_filter_384 : arr
          Is a bloom filter that uses AES384 to hash words and map
          them into a 1000 length array.
      hash_table : arr
          Is a implementation of a hashtable using an array and AES256
          to hash words and map them to an array, where each part of the
          array is either None or a linked list.

      Methods
      -------
      add_passage(passage):
        Adds passage to the 2 bloom filters and hashtable.

      check_passage(passage):
        Checks if the passage exists in the filters and hashtable, sequentially.
        The first filter in does not exist ends the method with False, otherwise
        True.
      """

    def __init__(self, bf1_size, bf2_size, ht_size):
        try:
            self.bloom_filter1 = [0] * bf1_size
            self.bloom_filter2 = [0] * bf2_size
            self.hash_table = [0] * ht_size
        except TypeError:
            raise ValueError(
                "One of the arguments provided was not an integer.")
