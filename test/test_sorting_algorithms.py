import pytest
import time
from random import randint

import src.algorithms.sorting_algorithms as sa

list1 = [34, 121, 69, 72, 53, 7, 19, 99, 5, 2, 4, 66, 0, 61, 62]

"""
  run this test from ~/P/S/test> pytest -vs -m perf

"""
class TestSortingAlorithms:

    @pytest.mark.perf
    def test_sorting_algorithms_performance(self):
        ARRAY_LENGTH = 5000
        # generate a long list of unsorted ints
        arr =  [randint(0, ARRAY_LENGTH) for x in range(ARRAY_LENGTH)]
        arr1 = [randint(0, ARRAY_LENGTH) for x in range(ARRAY_LENGTH)]
        arr2 = [randint(0, ARRAY_LENGTH) for x in range(ARRAY_LENGTH)]
        arr3 = [randint(0, ARRAY_LENGTH) for x in range(ARRAY_LENGTH)]

        bs = sa.SortingAlgorithms()

        tic = time.perf_counter()
        bs.bubble_sort_optimized(arr)
        toc = time.perf_counter()
        print(f'Bubble sort: {toc - tic:0.4f} seconds')

        tic = time.perf_counter()
        bs.insertion_sort(arr1)
        toc = time.perf_counter()
        print(f'Insertion sort: {toc - tic:0.4f} seconds')

        tic = time.perf_counter()
        bs.merge_sort(arr2)
        toc = time.perf_counter()
        print(f'Merge sort: {toc - tic:0.4f} seconds')

        tic = time.perf_counter()
        bs.quick_sort(arr3)
        toc = time.perf_counter()
        print(f'Quick sort: {toc - tic:0.4f} seconds')

    test_data = [([4, 2, 6, 1, 8, 5, 0, -6, -1], [-6, -1, 0, 1, 2, 4, 5, 6, 8]),
                 ([-2, 9, -4],[-4, -2, 9])
                 ]
    @pytest.mark.test_sorting
    @pytest.mark.parametrize("input_arr, output_arr", test_data)
    def test_bubble_sort(self, input_arr, output_arr):
        bs = sa.SortingAlgorithms()
        assert bs.bubble_sort_optimized(input_arr) == output_arr, f'Expected identical arrays'
