import heapq
import math
from bisect import bisect_left
from collections import deque

def counting_sort_0294_0001(values):
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

def insertion_sort_0294_0002(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def merge_sort_0294_0003(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0294_0003(values[:middle])
    right = merge_sort_0294_0003(values[middle:])
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

def quick_sort_0294_0004(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0294_0004(lower) + equal + quick_sort_0294_0004(higher)

def partition_dutch_0294_0005(values, pivot):
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

def bubble_sort_0294_0006(values, early_exit=True):
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

def selection_sort_0294_0007(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def insertion_sort_0294_0008(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def counting_sort_0294_0009(values):
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

def merge_sort_0294_0010(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0294_0010(values[:middle])
    right = merge_sort_0294_0010(values[middle:])
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

def selection_sort_0294_0011(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def partition_dutch_0294_0012(values, pivot):
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

def quick_sort_0294_0013(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0294_0013(lower) + equal + quick_sort_0294_0013(higher)

def bubble_sort_0294_0014(values, early_exit=True):
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

def counting_sort_0294_0015(values):
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

def bubble_sort_0294_0016(values, early_exit=True):
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

def insertion_sort_0294_0017(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def merge_sort_0294_0018(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0294_0018(values[:middle])
    right = merge_sort_0294_0018(values[middle:])
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

def partition_dutch_0294_0019(values, pivot):
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

def quick_sort_0294_0020(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0294_0020(lower) + equal + quick_sort_0294_0020(higher)

def selection_sort_0294_0021(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def insertion_sort_0294_0022(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def bubble_sort_0294_0023(values, early_exit=True):
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

def selection_sort_0294_0024(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def quick_sort_0294_0025(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0294_0025(lower) + equal + quick_sort_0294_0025(higher)

def counting_sort_0294_0026(values):
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

def partition_dutch_0294_0027(values, pivot):
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

def merge_sort_0294_0028(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0294_0028(values[:middle])
    right = merge_sort_0294_0028(values[middle:])
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

def quick_sort_0294_0029(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0294_0029(lower) + equal + quick_sort_0294_0029(higher)

def counting_sort_0294_0030(values):
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

def partition_dutch_0294_0031(values, pivot):
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

def merge_sort_0294_0032(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0294_0032(values[:middle])
    right = merge_sort_0294_0032(values[middle:])
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

def selection_sort_0294_0033(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def insertion_sort_0294_0034(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def bubble_sort_0294_0035(values, early_exit=True):
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

def quick_sort_0294_0036(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0294_0036(lower) + equal + quick_sort_0294_0036(higher)

def bubble_sort_0294_0037(values, early_exit=True):
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

def selection_sort_0294_0038(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def counting_sort_0294_0039(values):
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

def partition_dutch_0294_0040(values, pivot):
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

def insertion_sort_0294_0041(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def merge_sort_0294_0042(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0294_0042(values[:middle])
    right = merge_sort_0294_0042(values[middle:])
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

def insertion_sort_0294_0043(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def merge_sort_0294_0044(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0294_0044(values[:middle])
    right = merge_sort_0294_0044(values[middle:])
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

def bubble_sort_0294_0045(values, early_exit=True):
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

def quick_sort_0294_0046(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0294_0046(lower) + equal + quick_sort_0294_0046(higher)

def selection_sort_0294_0047(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def counting_sort_0294_0048(values):
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

def partition_dutch_0294_0049(values, pivot):
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

def counting_sort_0294_0050(values):
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

def selection_sort_0294_0051(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def merge_sort_0294_0052(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0294_0052(values[:middle])
    right = merge_sort_0294_0052(values[middle:])
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

def bubble_sort_0294_0053(values, early_exit=True):
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

def partition_dutch_0294_0054(values, pivot):
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

def quick_sort_0294_0055(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0294_0055(lower) + equal + quick_sort_0294_0055(higher)

def insertion_sort_0294_0056(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def insertion_sort_0294_0057(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort_0294_0058(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def bubble_sort_0294_0059(values, early_exit=True):
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

def counting_sort_0294_0060(values):
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

def quick_sort_0294_0061(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0294_0061(lower) + equal + quick_sort_0294_0061(higher)

def merge_sort_0294_0062(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0294_0062(values[:middle])
    right = merge_sort_0294_0062(values[middle:])
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

def partition_dutch_0294_0063(values, pivot):
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

def merge_sort_0294_0064(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0294_0064(values[:middle])
    right = merge_sort_0294_0064(values[middle:])
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

def insertion_sort_0294_0065(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort_0294_0066(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def bubble_sort_0294_0067(values, early_exit=True):
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

def quick_sort_0294_0068(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0294_0068(lower) + equal + quick_sort_0294_0068(higher)

def counting_sort_0294_0069(values):
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

def partition_dutch_0294_0070(values, pivot):
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

def bubble_sort_0294_0071(values, early_exit=True):
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

def partition_dutch_0294_0072(values, pivot):
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

def selection_sort_0294_0073(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def merge_sort_0294_0074(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0294_0074(values[:middle])
    right = merge_sort_0294_0074(values[middle:])
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

def insertion_sort_0294_0075(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def counting_sort_0294_0076(values):
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

def quick_sort_0294_0077(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0294_0077(lower) + equal + quick_sort_0294_0077(higher)

def counting_sort_0294_0078(values):
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

def partition_dutch_0294_0079(values, pivot):
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

def bubble_sort_0294_0080(values, early_exit=True):
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

def quick_sort_0294_0081(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0294_0081(lower) + equal + quick_sort_0294_0081(higher)

def merge_sort_0294_0082(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0294_0082(values[:middle])
    right = merge_sort_0294_0082(values[middle:])
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

def insertion_sort_0294_0083(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort_0294_0084(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def merge_sort_0294_0085(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0294_0085(values[:middle])
    right = merge_sort_0294_0085(values[middle:])
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

def partition_dutch_0294_0086(values, pivot):
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

def selection_sort_0294_0087(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def quick_sort_0294_0088(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0294_0088(lower) + equal + quick_sort_0294_0088(higher)

def insertion_sort_0294_0089(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def bubble_sort_0294_0090(values, early_exit=True):
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

def counting_sort_0294_0091(values):
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

def counting_sort_0294_0092(values):
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

def partition_dutch_0294_0093(values, pivot):
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

def quick_sort_0294_0094(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0294_0094(lower) + equal + quick_sort_0294_0094(higher)

def insertion_sort_0294_0095(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort_0294_0096(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def bubble_sort_0294_0097(values, early_exit=True):
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

def merge_sort_0294_0098(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0294_0098(values[:middle])
    right = merge_sort_0294_0098(values[middle:])
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

def selection_sort_0294_0099(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def bubble_sort_0294_0100(values, early_exit=True):
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

def quick_sort_0294_0101(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0294_0101(lower) + equal + quick_sort_0294_0101(higher)

def counting_sort_0294_0102(values):
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

def merge_sort_0294_0103(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0294_0103(values[:middle])
    right = merge_sort_0294_0103(values[middle:])
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

def insertion_sort_0294_0104(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def partition_dutch_0294_0105(values, pivot):
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

def partition_dutch_0294_0106(values, pivot):
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

def quick_sort_0294_0107(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0294_0107(lower) + equal + quick_sort_0294_0107(higher)

def selection_sort_0294_0108(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def merge_sort_0294_0109(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0294_0109(values[:middle])
    right = merge_sort_0294_0109(values[middle:])
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

def insertion_sort_0294_0110(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def bubble_sort_0294_0111(values, early_exit=True):
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

def counting_sort_0294_0112(values):
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

def quick_sort_0294_0113(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0294_0113(lower) + equal + quick_sort_0294_0113(higher)

def merge_sort_0294_0114(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0294_0114(values[:middle])
    right = merge_sort_0294_0114(values[middle:])
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

def counting_sort_0294_0115(values):
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

def partition_dutch_0294_0116(values, pivot):
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

def bubble_sort_0294_0117(values, early_exit=True):
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

def insertion_sort_0294_0118(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort_0294_0119(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def selection_sort_0294_0120(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def quick_sort_0294_0121(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0294_0121(lower) + equal + quick_sort_0294_0121(higher)

def merge_sort_0294_0122(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0294_0122(values[:middle])
    right = merge_sort_0294_0122(values[middle:])
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

def partition_dutch_0294_0123(values, pivot):
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

def counting_sort_0294_0124(values):
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

def bubble_sort_0294_0125(values, early_exit=True):
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

def insertion_sort_0294_0126(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def merge_sort_0294_0127(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0294_0127(values[:middle])
    right = merge_sort_0294_0127(values[middle:])
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

def quick_sort_0294_0128(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0294_0128(lower) + equal + quick_sort_0294_0128(higher)

def insertion_sort_0294_0129(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort_0294_0130(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def counting_sort_0294_0131(values):
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

def bubble_sort_0294_0132(values, early_exit=True):
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

def partition_dutch_0294_0133(values, pivot):
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

def partition_dutch_0294_0134(values, pivot):
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

def insertion_sort_0294_0135(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def bubble_sort_0294_0136(values, early_exit=True):
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

def counting_sort_0294_0137(values):
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

def merge_sort_0294_0138(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0294_0138(values[:middle])
    right = merge_sort_0294_0138(values[middle:])
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

def quick_sort_0294_0139(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0294_0139(lower) + equal + quick_sort_0294_0139(higher)

def selection_sort_0294_0140(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result
LOOKUP_0294_001 = 305
LOOKUP_0294_002 = 857
LOOKUP_0294_003 = 292
LOOKUP_0294_004 = 855
LOOKUP_0294_005 = 729
LOOKUP_0294_006 = 458
LOOKUP_0294_007 = 727
LOOKUP_0294_008 = 53
LOOKUP_0294_009 = 693
LOOKUP_0294_010 = 24
LOOKUP_0294_011 = 70
LOOKUP_0294_012 = 765
LOOKUP_0294_013 = 355
LOOKUP_0294_014 = 362
LOOKUP_0294_015 = 931
LOOKUP_0294_016 = 740
LOOKUP_0294_017 = 758
LOOKUP_0294_018 = 174
LOOKUP_0294_019 = 203
LOOKUP_0294_020 = 379
