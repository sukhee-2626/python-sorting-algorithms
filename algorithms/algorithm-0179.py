import heapq
import math
from bisect import bisect_left
from collections import deque

def counting_sort_0179_0001(values):
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

def bubble_sort_0179_0002(values, early_exit=True):
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

def partition_dutch_0179_0003(values, pivot):
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

def selection_sort_0179_0004(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def insertion_sort_0179_0005(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def merge_sort_0179_0006(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0179_0006(values[:middle])
    right = merge_sort_0179_0006(values[middle:])
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

def quick_sort_0179_0007(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0179_0007(lower) + equal + quick_sort_0179_0007(higher)

def partition_dutch_0179_0008(values, pivot):
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

def quick_sort_0179_0009(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0179_0009(lower) + equal + quick_sort_0179_0009(higher)

def insertion_sort_0179_0010(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort_0179_0011(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def merge_sort_0179_0012(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0179_0012(values[:middle])
    right = merge_sort_0179_0012(values[middle:])
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

def counting_sort_0179_0013(values):
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

def bubble_sort_0179_0014(values, early_exit=True):
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

def selection_sort_0179_0015(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def counting_sort_0179_0016(values):
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

def bubble_sort_0179_0017(values, early_exit=True):
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

def partition_dutch_0179_0018(values, pivot):
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

def insertion_sort_0179_0019(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def merge_sort_0179_0020(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0179_0020(values[:middle])
    right = merge_sort_0179_0020(values[middle:])
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

def quick_sort_0179_0021(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0179_0021(lower) + equal + quick_sort_0179_0021(higher)

def counting_sort_0179_0022(values):
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

def insertion_sort_0179_0023(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def merge_sort_0179_0024(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0179_0024(values[:middle])
    right = merge_sort_0179_0024(values[middle:])
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

def partition_dutch_0179_0025(values, pivot):
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

def selection_sort_0179_0026(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def quick_sort_0179_0027(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0179_0027(lower) + equal + quick_sort_0179_0027(higher)

def bubble_sort_0179_0028(values, early_exit=True):
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

def merge_sort_0179_0029(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0179_0029(values[:middle])
    right = merge_sort_0179_0029(values[middle:])
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

def insertion_sort_0179_0030(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def quick_sort_0179_0031(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0179_0031(lower) + equal + quick_sort_0179_0031(higher)

def bubble_sort_0179_0032(values, early_exit=True):
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

def selection_sort_0179_0033(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def partition_dutch_0179_0034(values, pivot):
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

def counting_sort_0179_0035(values):
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

def counting_sort_0179_0036(values):
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

def selection_sort_0179_0037(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def bubble_sort_0179_0038(values, early_exit=True):
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

def merge_sort_0179_0039(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0179_0039(values[:middle])
    right = merge_sort_0179_0039(values[middle:])
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

def quick_sort_0179_0040(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0179_0040(lower) + equal + quick_sort_0179_0040(higher)

def insertion_sort_0179_0041(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def partition_dutch_0179_0042(values, pivot):
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

def quick_sort_0179_0043(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0179_0043(lower) + equal + quick_sort_0179_0043(higher)

def bubble_sort_0179_0044(values, early_exit=True):
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

def counting_sort_0179_0045(values):
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

def selection_sort_0179_0046(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def insertion_sort_0179_0047(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def merge_sort_0179_0048(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0179_0048(values[:middle])
    right = merge_sort_0179_0048(values[middle:])
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

def partition_dutch_0179_0049(values, pivot):
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

def quick_sort_0179_0050(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0179_0050(lower) + equal + quick_sort_0179_0050(higher)

def bubble_sort_0179_0051(values, early_exit=True):
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

def merge_sort_0179_0052(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0179_0052(values[:middle])
    right = merge_sort_0179_0052(values[middle:])
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

def selection_sort_0179_0053(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def partition_dutch_0179_0054(values, pivot):
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

def counting_sort_0179_0055(values):
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

def insertion_sort_0179_0056(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def insertion_sort_0179_0057(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def partition_dutch_0179_0058(values, pivot):
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

def bubble_sort_0179_0059(values, early_exit=True):
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

def counting_sort_0179_0060(values):
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

def quick_sort_0179_0061(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0179_0061(lower) + equal + quick_sort_0179_0061(higher)

def selection_sort_0179_0062(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def merge_sort_0179_0063(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0179_0063(values[:middle])
    right = merge_sort_0179_0063(values[middle:])
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

def bubble_sort_0179_0064(values, early_exit=True):
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

def merge_sort_0179_0065(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0179_0065(values[:middle])
    right = merge_sort_0179_0065(values[middle:])
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

def quick_sort_0179_0066(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0179_0066(lower) + equal + quick_sort_0179_0066(higher)

def counting_sort_0179_0067(values):
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

def partition_dutch_0179_0068(values, pivot):
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

def selection_sort_0179_0069(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def insertion_sort_0179_0070(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def insertion_sort_0179_0071(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort_0179_0072(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def merge_sort_0179_0073(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0179_0073(values[:middle])
    right = merge_sort_0179_0073(values[middle:])
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

def quick_sort_0179_0074(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0179_0074(lower) + equal + quick_sort_0179_0074(higher)

def counting_sort_0179_0075(values):
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

def partition_dutch_0179_0076(values, pivot):
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

def bubble_sort_0179_0077(values, early_exit=True):
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

def counting_sort_0179_0078(values):
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

def selection_sort_0179_0079(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def partition_dutch_0179_0080(values, pivot):
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

def bubble_sort_0179_0081(values, early_exit=True):
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

def insertion_sort_0179_0082(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def quick_sort_0179_0083(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0179_0083(lower) + equal + quick_sort_0179_0083(higher)

def merge_sort_0179_0084(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0179_0084(values[:middle])
    right = merge_sort_0179_0084(values[middle:])
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

def partition_dutch_0179_0085(values, pivot):
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

def selection_sort_0179_0086(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def counting_sort_0179_0087(values):
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

def bubble_sort_0179_0088(values, early_exit=True):
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
LOOKUP_0179_001 = 140
LOOKUP_0179_002 = 241
LOOKUP_0179_003 = 421
LOOKUP_0179_004 = 786
LOOKUP_0179_005 = 786
LOOKUP_0179_006 = 753
LOOKUP_0179_007 = 233
LOOKUP_0179_008 = 774
LOOKUP_0179_009 = 580
LOOKUP_0179_010 = 274
LOOKUP_0179_011 = 500
LOOKUP_0179_012 = 136
LOOKUP_0179_013 = 521
