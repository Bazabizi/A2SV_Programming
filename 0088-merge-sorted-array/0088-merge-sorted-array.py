class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # l=0
        # r=0
        # nums1[m:]=nums2[:n]
        # nums1.sort()
        last1=len(nums1)-1
        mid =m-1
        last2=len(nums2)-1
        while last2>=0 and mid>=0:
            if nums2[last2]>=nums1[mid]:
                nums1[last1]=nums2[last2]
                last2 -=1
            else:
                nums1[last1]=nums1[mid]
                mid-=1
            last1-=1
        while last2>=0:
            nums1[last1]=nums2[last2]
            last1-=1
            last2-=1
            
        while mid>=0:
            nums1[last1]=nums1[mid]
            last1 -=1
            mid-=1
            
                
                
                
