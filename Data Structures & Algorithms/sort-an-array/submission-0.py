class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        
        def merge(arr: list[int], Left: int, Middle: int, Right: int):
            l, r = arr[Left:Middle+1], arr[Middle+1:Right+1]
            i, j, k = Left, 0, 0

            while j < len(l) and k < len(r):
                if l[j] <= r[k]:
                    arr[i] = l[j]
                    j += 1
                else:
                    arr[i] = r[k]
                    k += 1
                i += 1
            while j < len(l):
                arr[i] = l[j]
                j += 1
                i += 1
            while k < len(r):
                arr[i] = r[k]
                k += 1
                i += 1

        def mergeSort(array: list[int], left: int, right: int):
            if left == right:
                return array
            
            middle = (left + right) // 2
            mergeSort(array, left, middle)
            mergeSort(array, middle + 1, right)
            merge(array, left, middle, right)
            return array

        return mergeSort(nums, 0, len(nums) - 1)
