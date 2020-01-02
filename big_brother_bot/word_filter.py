from hashlib import sha256, sha384


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
      add_passage_wout_translation(passage):
        Adds passage to the 2 bloom filters and hashtable without translation.

      add_passage_with_translation(passage):
        Adds passage to the 2 bloom filters and hashtable without translation.

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
            self.hash_table = [None] * ht_size
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

        try:
            value = value.encode()
        except AttributeError:
            raise ValueError("Value argument is not string")

        if (hash_type == "256"):
          # 681
            sha_value = sha256()
            sha_value.update(value)
            hashed_value = sha_value.hexdigest()
            return int(hashed_value, 16)
        elif (hash_type == "384"):
          # 674
            sha_value = sha384()
            sha_value.update(value)
            hashed_value = sha_value.hexdigest()
            return int(hashed_value, 16)
        else:
            raise ValueError("Hash_type argument not 256 or 384")

    def add_passage_wout_translation(self, value):
        """ Adds value to both bloom filters and to the hash
        table in a linked list to cover for collisons.
        Parameters
        ----------
        value: str
            String to added.

        Returns
        -------
        bool
            Returns True if the passage is put in and false if not.
        """

        hash_256_value = self.hash("256", value)
        hash_384_value = self.hash("384", value)

        # Sets the passage for the bloomfilters.
        bf1_index = hash_256_value % len(self.bloom_filter1)
        self.bloom_filter1[bf1_index] = 1
        bf2_index = hash_384_value % len(self.bloom_filter2)
        self.bloom_filter2[bf2_index] = 1

        passage_obj = {"word": value, "next": None}

        # Value in hash_table.
        ht_index = hash_256_value % len(self.hash_table)
        hash_table_value = self.hash_table[ht_index]

        if (hash_table_value == None):
            self.hash_table[ht_index] = passage_obj
        else:
            while (hash_table_value.next != None):
                hash_256_value = hash_table_value.next
            hash_table_value.next = passage_obj
