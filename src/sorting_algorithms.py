import random



class SortingAlgorithms:

    """
    1. Bubble sort

    https://realpython.com/sorting-algorithms-python/#the-bubble-sort-algorithm-in-python

    worst-case complexity of O(n2).
    """
    def bubble_sort_optimized(self, arr):
        n = len(arr)
        for i in range(len(arr)):
            already_sorted = True
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    already_sorted = False
            if already_sorted:
                break
        return arr

    """
    Unlike bubble sort, this implementation of insertion sort constructs 
    the sorted list by pushing smaller items to the left. 
    
     O(n2) runtime complexity on the average case
    """
    def insertion_sort(self, arr):
        # traverse from 1st element to last (note, range doesn't include last num in range)
        for i in range(1, len(arr)):
            # remember key_element, it will be positioned
            key_element = arr[i]
            # initialize j, it points to the left of key_element
            j = i -1

            # compare key_element with each item to its left
            while j >=0 and arr[j] > key_element:
                # move bigger value to the right
                arr[j+1] = arr[j]
                # move j to the left
                # to compare each element to the left of the key_element with key_el value
                j -= 1

            # no more smaller values to the left, insert the key_value
            arr[j+1] = key_element

        return arr

    """
    Merge sort is a very efficient sorting algorithm. O(n log n)
    It’s based on the divide-and-conquer approach, a powerful algorithmic technique 
    used to solve complex problems.
    
    The second step splits the input array recursively and calls merge() for each half. Since the array is halved until a single element remains, the total number of halving operations performed by this function is log2n. Since merge() is called for each half, we get a total runtime of O(n log2n).

    Interestingly, O(n log n) is the best possible worst-case runtime that can be achieved by a sorting algorithm.

    Limitations:
    Another drawback of merge sort is that it creates copies of the array 
    when calling itself recursively. It also creates a new list inside merge() 
    to sort and return both input halves. 
    This makes merge sort use much more memory than bubble sort and insertion sort, 
    which are both able to sort the list in place.

    Due to this limitation, you may not want to use merge sort to sort large lists in 
    memory-constrained hardware.

    """
    def merge(self,left, right):
        if len(left) == 0:
            return right
        if len(right) == 0:
            return left
        result = []
        ind_left = ind_right = 0
        while len(result) < len(left)+len(right):
            if left[ind_left] <= right[ind_right]:
                result.append(left[ind_left])
                ind_left += 1
            else:
                result.append(right[ind_right])
                ind_right += 1

            # if I reached the end of array
            if ind_right == len(right):
                result+= left[ind_left:]
                break
            if ind_left == len(left):
                result += right[ind_right:]
                break
        return result

    def merge_sort(self, arr):

        if len(arr) < 2:
            return arr

        midpoint = len(arr) // 2

        return self.merge(self.merge_sort(arr[:midpoint]),
                          self.merge_sort(arr[midpoint:]))

    """
    Quick sort 
    """
    def quick_sort(self,arr):
        if len(arr) < 2:
            return arr

        # create three lists
        low,same,high = [],[],[]
        # choose a pivot, say, it's in the middle
        piv = len(arr)//2

        for i in arr:
            if i < arr[piv]:
                low.append(i)
            elif i > arr[piv]:
                high.append(i)
            else:
                same.append(i)

        return self.quick_sort(low) + same + self.quick_sort(high)


    """
    
    Timsort algorithm  
    
    On average, the complexity of Timsort is O(n log2n), just like merge sort and quicksort
    https://realpython.com/sorting-algorithms-python/#the-timsort-algorithm-in-python
      
    """


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list = [2, 4, 6, 7, 19, 34, 53, 60, 61, 62, 69, 72]
    list1 = [34, 121, 69, 72, 53, 7, 19, 99, 5, 2, 4, 66, 0, 61, 62]
    list2 = [8, 3, 1, 5, 6, 4]
    rl = []
    for i in range(1000):
        rl.append(random.randint(0, 1000))
    rl2 = [random.randint(1, 100) for x in range(100)]
    # print(f'my random list of ints: {rl2}, num elements: {len(rl2)}')
    sa = SortingAlgorithms()
    # print(sa.bubble_sort_optimized(rl))
    # print(sa.insertion_sort(list2))
    print(sa.merge_sort(list2))
    print(sa.quick_sort(list2))