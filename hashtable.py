class hashTable:
    def __init__(self):
        self.__MAX=15
        self.table=[None]*self.__MAX

    def get_hash(self, value):
        """
        The function get_hash will get a value and will use the built-in function in Python
        to hash this value. the function will return the hash mod the length of the list
        :param value: input from the user
        :return: hash value
        """
        print(f"the hash to {value} = ", hash(value)%self.__MAX)
        return hash(value)%self.__MAX

    def insert(self, value):
        """
        the function insert will get a value as a paprameter and will insert this value into the corect location in the hash table.
        :param value: input from the user (any data type)
        :return: void
        """
        hash_loc = self.get_hash(value)
        """
        there are 3 possible state for any hash table location
        1- the location is empty or has none
        2- the location has a list (there are multiple value already there)
        3- the location has ONLY ONe value
        """
        if self.table[hash_loc]==None: # meaning the location is empty
            self.table[hash_loc]= value
        elif type(self.table[hash_loc])== list: # if the location has already a list
            self.table[hash_loc].append(value)
        else:
            self.table[hash_loc] =  [self.table[hash_loc] , value] # the right size will create a list
            # with two location, the first location will be the old value in the hash table,
            # while the second lcoation will have the new value
