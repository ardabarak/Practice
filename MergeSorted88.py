class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if (nums1 == []) or (m == 0):
            nums1[:] = nums2
        elif nums2 == []:
            print("oi")
        else:
            mn = m + n
            temp1 = (m-1) # temp elem for list1 i
            temp2 = (n-1) # temp elem for list2 i
            # for i in range(mn):
            i = (mn - 1)
            while i >= 0: # looping backwards
                n1 = nums1[temp1] # tmp for the pointed index 1
                n2 = nums2[temp2] # tmp for the pointed index 2
                if (temp1 < 0) or (temp2 < 0): #if either reaches end of list, continue with other remaining list
                    if temp1 < 0:
                        nums1[i] = n2
                        temp2 -= 1
                    elif temp2 < 0:
                        nums1[i] = n1
                        temp1 -= 1
                # put the bigger number as looping backwards
                elif (n1 > n2): 
                    print("a1")
                    nums1[i] = n1
                    temp1 -= 1
                elif (n1 < n2) or (n1 == n2):
                    print("a2")
                    nums1[i] = n2
                    temp2 -= 1
                i -= 1

