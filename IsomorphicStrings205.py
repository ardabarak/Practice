class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): # if words are of different sizes
            return False

        dict1 = {}                          # dictionary to store indexes of input1
        dict2 = {}                          # dictionary to store indexes of input2
        for index, char in enumerate(s):    # mapping each letter to a dict entry of occurence indexes
            dict1.setdefault(char, []).append(index) 
        for index, char in enumerate(t):    # mapping each letter to a dict entry of occurence indexes
            dict2.setdefault(char, []).append(index) 

        if (len(dict1) != len(dict2)):      # if resulting dicts have different unique number of letters
            return False
        else:
            for v1, v2 in zip(dict1.values(), dict2.values()): #iterating through both dicts by key
                if (v1 != v2):              # if the iterated values are different, they are of different pattern
                    return False
            return True                     # if no difference is found after the loop, they're the same pattern
        return False
