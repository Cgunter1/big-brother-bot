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

      Static Methods
      -------
      hash(hash_type, value)
        Returns hashed value

      Class Methods
      -------
      create_default_filter()
        Creates and returns a filter object with set bf sizes of 1000 and
        ht size of 30.

      """

    def __init__(self, bf1_size, bf2_size, ht_size):
        try:
            self.bloom_filter1 = [0] * bf1_size
            self.bloom_filter2 = [0] * bf2_size
            self.hash_table = [0] * ht_size
        except TypeError:
            raise ValueError(
                "One of the arguments provided was not an integer.")

    @classmethod
    def create_default_filter(cls):
        """ Creates/Returns a default filter object with set arguments.
        Parameters
        ----------
        cls

        Returns
        -------
        obj
            Returns instance of WordFilter.
        """
        return cls(1000, 1000, 30)

    @staticmethod
    def hash(hash_type, value):
        """ Hashes value given a hash_type and returns it.
        Parameters
        ----------
        hash_type: str
            Type of hash to use for function (256, 384).
        value: str
            String to be hashed.

        Returns
        -------
        int
            Hashed value of value from hash (depending on hash_type).
        """
        pass
