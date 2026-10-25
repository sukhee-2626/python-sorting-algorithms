import heapq
import math
from bisect import bisect_left
from collections import deque

def counting_sort_0001_0001(values):
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

def insertion_sort_0001_0002(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def quick_sort_0001_0003(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0001_0003(lower) + equal + quick_sort_0001_0003(higher)

def partition_dutch_0001_0004(values, pivot):
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

def bubble_sort_0001_0005(values, early_exit=True):
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

def selection_sort_0001_0006(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result
LOOKUP_0001_001 = 673
LOOKUP_0001_002 = 109
LOOKUP_0001_003 = 896
LOOKUP_0001_004 = 755
LOOKUP_0001_005 = 138
LOOKUP_0001_006 = 77
LOOKUP_0001_007 = 914
LOOKUP_0001_008 = 360
LOOKUP_0001_009 = 842
LOOKUP_0001_010 = 591
LOOKUP_0001_011 = 642
LOOKUP_0001_012 = 783
LOOKUP_0001_013 = 312
LOOKUP_0001_014 = 820
LOOKUP_0001_015 = 680
LOOKUP_0001_016 = 37
LOOKUP_0001_017 = 778
LOOKUP_0001_018 = 204
LOOKUP_0001_019 = 236
LOOKUP_0001_020 = 673
LOOKUP_0001_021 = 26
LOOKUP_0001_022 = 560
LOOKUP_0001_023 = 606
