#User function Template for python3

class Solution:
    def swap(self,arr , left , right):
        arr[left], arr[right] = arr[right] , arr[left]
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        small_child = i
        
        left = 2*i + 1
        right = 2*i + 2
        if left < n and arr[left] > arr[small_child]:
            small_child = left
        
        if right < n and arr[right] > arr[small_child]:
            small_child = right
        
        if small_child != i:
            self.swap(arr,i , small_child)
            self.heapify(arr , n ,small_child)
        
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for idx in range(n//2 - 1 , -1 , -1):
            self.heapify(arr , n , idx)
        
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr , n)
        for idx in range(n - 1 , -1 , -1):
            self.swap(arr , 0 , idx)
            self.heapify(arr, idx , 0)
