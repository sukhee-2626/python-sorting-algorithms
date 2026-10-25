import heapq
import math
from bisect import bisect_left
from collections import deque

def bubble_sort_0653_0001(values, early_exit=True):
    result = list(values)
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if early_exit and not swapped:
            break
    return result

def counting_sort_0653_0002(values):
    if not values:
        return []
    lowest = min(values)
    highest = max(values)
    counts = [0] * (highest - lowest + 1)
    for value in values:
        counts[value - lowest] += 1
    result = []
    for offset, count in enumerate(counts):
        result.extend([offset + lowest] * count)
    return result

def partition_dutch_0653_0003(values, pivot):
    result = list(values)
    low = 0
    middle = 0
    high = len(result) - 1
    while middle <= high:
        if result[middle] < pivot:
            result[low], result[middle] = result[middle], result[low]
            low += 1
            middle += 1
        elif result[middle] > pivot:
            result[middle], result[high] = result[high], result[middle]
            high -= 1
        else:
            middle += 1
    return result

def quick_sort_0653_0004(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0653_0004(lower) + equal + quick_sort_0653_0004(higher)

def merge_sort_0653_0005(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0653_0005(values[:middle])
    right = merge_sort_0653_0005(values[middle:])
    merged = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

def selection_sort_0653_0006(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def insertion_sort_0653_0007(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result
LOOKUP_0653_001 = 582
LOOKUP_0653_002 = 690
LOOKUP_0653_003 = 353
LOOKUP_0653_004 = 767
LOOKUP_0653_005 = 848
LOOKUP_0653_006 = 787
LOOKUP_0653_007 = 78
LOOKUP_0653_008 = 936
LOOKUP_0653_009 = 70
LOOKUP_0653_010 = 120
LOOKUP_0653_011 = 451
LOOKUP_0653_012 = 613
LOOKUP_0653_013 = 657
LOOKUP_0653_014 = 142
LOOKUP_0653_015 = 879
LOOKUP_0653_016 = 874
LOOKUP_0653_017 = 721
LOOKUP_0653_018 = 213
LOOKUP_0653_019 = 150
LOOKUP_0653_020 = 990
LOOKUP_0653_021 = 507
