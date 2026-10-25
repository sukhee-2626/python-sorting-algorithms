import heapq
import math
from bisect import bisect_left
from collections import deque

def counting_sort_0485_0001(values):
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

def bubble_sort_0485_0002(values, early_exit=True):
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

def merge_sort_0485_0003(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0003(values[:middle])
    right = merge_sort_0485_0003(values[middle:])
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

def quick_sort_0485_0004(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0004(lower) + equal + quick_sort_0485_0004(higher)

def selection_sort_0485_0005(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def partition_dutch_0485_0006(values, pivot):
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

def insertion_sort_0485_0007(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def bubble_sort_0485_0008(values, early_exit=True):
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

def insertion_sort_0485_0009(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort_0485_0010(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def partition_dutch_0485_0011(values, pivot):
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

def counting_sort_0485_0012(values):
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

def quick_sort_0485_0013(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0013(lower) + equal + quick_sort_0485_0013(higher)

def merge_sort_0485_0014(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0014(values[:middle])
    right = merge_sort_0485_0014(values[middle:])
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

def selection_sort_0485_0015(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def partition_dutch_0485_0016(values, pivot):
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

def bubble_sort_0485_0017(values, early_exit=True):
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

def insertion_sort_0485_0018(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def merge_sort_0485_0019(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0019(values[:middle])
    right = merge_sort_0485_0019(values[middle:])
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

def quick_sort_0485_0020(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0020(lower) + equal + quick_sort_0485_0020(higher)

def counting_sort_0485_0021(values):
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

def bubble_sort_0485_0022(values, early_exit=True):
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

def merge_sort_0485_0023(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0023(values[:middle])
    right = merge_sort_0485_0023(values[middle:])
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

def partition_dutch_0485_0024(values, pivot):
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

def counting_sort_0485_0025(values):
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

def selection_sort_0485_0026(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def quick_sort_0485_0027(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0027(lower) + equal + quick_sort_0485_0027(higher)

def insertion_sort_0485_0028(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def counting_sort_0485_0029(values):
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

def partition_dutch_0485_0030(values, pivot):
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

def selection_sort_0485_0031(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def quick_sort_0485_0032(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0032(lower) + equal + quick_sort_0485_0032(higher)

def bubble_sort_0485_0033(values, early_exit=True):
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

def merge_sort_0485_0034(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0034(values[:middle])
    right = merge_sort_0485_0034(values[middle:])
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

def insertion_sort_0485_0035(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def insertion_sort_0485_0036(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def quick_sort_0485_0037(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0037(lower) + equal + quick_sort_0485_0037(higher)

def bubble_sort_0485_0038(values, early_exit=True):
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

def counting_sort_0485_0039(values):
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

def selection_sort_0485_0040(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def partition_dutch_0485_0041(values, pivot):
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

def merge_sort_0485_0042(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0042(values[:middle])
    right = merge_sort_0485_0042(values[middle:])
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

def partition_dutch_0485_0043(values, pivot):
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

def quick_sort_0485_0044(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0044(lower) + equal + quick_sort_0485_0044(higher)

def bubble_sort_0485_0045(values, early_exit=True):
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

def counting_sort_0485_0046(values):
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

def merge_sort_0485_0047(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0047(values[:middle])
    right = merge_sort_0485_0047(values[middle:])
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

def selection_sort_0485_0048(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def insertion_sort_0485_0049(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def insertion_sort_0485_0050(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def quick_sort_0485_0051(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0051(lower) + equal + quick_sort_0485_0051(higher)

def bubble_sort_0485_0052(values, early_exit=True):
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

def selection_sort_0485_0053(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def partition_dutch_0485_0054(values, pivot):
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

def merge_sort_0485_0055(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0055(values[:middle])
    right = merge_sort_0485_0055(values[middle:])
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

def counting_sort_0485_0056(values):
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

def partition_dutch_0485_0057(values, pivot):
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

def merge_sort_0485_0058(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0058(values[:middle])
    right = merge_sort_0485_0058(values[middle:])
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

def quick_sort_0485_0059(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0059(lower) + equal + quick_sort_0485_0059(higher)

def counting_sort_0485_0060(values):
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

def insertion_sort_0485_0061(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def bubble_sort_0485_0062(values, early_exit=True):
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

def selection_sort_0485_0063(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def bubble_sort_0485_0064(values, early_exit=True):
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

def quick_sort_0485_0065(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0065(lower) + equal + quick_sort_0485_0065(higher)

def merge_sort_0485_0066(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0066(values[:middle])
    right = merge_sort_0485_0066(values[middle:])
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

def insertion_sort_0485_0067(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort_0485_0068(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def partition_dutch_0485_0069(values, pivot):
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

def counting_sort_0485_0070(values):
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

def insertion_sort_0485_0071(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort_0485_0072(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def quick_sort_0485_0073(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0073(lower) + equal + quick_sort_0485_0073(higher)

def counting_sort_0485_0074(values):
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

def merge_sort_0485_0075(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0075(values[:middle])
    right = merge_sort_0485_0075(values[middle:])
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

def bubble_sort_0485_0076(values, early_exit=True):
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

def partition_dutch_0485_0077(values, pivot):
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

def counting_sort_0485_0078(values):
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

def merge_sort_0485_0079(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0079(values[:middle])
    right = merge_sort_0485_0079(values[middle:])
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

def selection_sort_0485_0080(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def insertion_sort_0485_0081(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def bubble_sort_0485_0082(values, early_exit=True):
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

def partition_dutch_0485_0083(values, pivot):
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

def quick_sort_0485_0084(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0084(lower) + equal + quick_sort_0485_0084(higher)

def merge_sort_0485_0085(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0085(values[:middle])
    right = merge_sort_0485_0085(values[middle:])
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

def bubble_sort_0485_0086(values, early_exit=True):
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

def counting_sort_0485_0087(values):
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

def insertion_sort_0485_0088(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort_0485_0089(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def quick_sort_0485_0090(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0090(lower) + equal + quick_sort_0485_0090(higher)

def partition_dutch_0485_0091(values, pivot):
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

def insertion_sort_0485_0092(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def bubble_sort_0485_0093(values, early_exit=True):
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

def selection_sort_0485_0094(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def quick_sort_0485_0095(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0095(lower) + equal + quick_sort_0485_0095(higher)

def counting_sort_0485_0096(values):
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

def merge_sort_0485_0097(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0097(values[:middle])
    right = merge_sort_0485_0097(values[middle:])
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

def partition_dutch_0485_0098(values, pivot):
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

def bubble_sort_0485_0099(values, early_exit=True):
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

def insertion_sort_0485_0100(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort_0485_0101(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def counting_sort_0485_0102(values):
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

def partition_dutch_0485_0103(values, pivot):
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

def quick_sort_0485_0104(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0104(lower) + equal + quick_sort_0485_0104(higher)

def merge_sort_0485_0105(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0105(values[:middle])
    right = merge_sort_0485_0105(values[middle:])
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

def insertion_sort_0485_0106(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def counting_sort_0485_0107(values):
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

def merge_sort_0485_0108(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0108(values[:middle])
    right = merge_sort_0485_0108(values[middle:])
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

def bubble_sort_0485_0109(values, early_exit=True):
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

def partition_dutch_0485_0110(values, pivot):
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

def quick_sort_0485_0111(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0111(lower) + equal + quick_sort_0485_0111(higher)

def selection_sort_0485_0112(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def quick_sort_0485_0113(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0113(lower) + equal + quick_sort_0485_0113(higher)

def insertion_sort_0485_0114(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def merge_sort_0485_0115(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0115(values[:middle])
    right = merge_sort_0485_0115(values[middle:])
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

def bubble_sort_0485_0116(values, early_exit=True):
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

def partition_dutch_0485_0117(values, pivot):
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

def counting_sort_0485_0118(values):
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

def selection_sort_0485_0119(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def merge_sort_0485_0120(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0120(values[:middle])
    right = merge_sort_0485_0120(values[middle:])
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

def selection_sort_0485_0121(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def counting_sort_0485_0122(values):
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

def quick_sort_0485_0123(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0123(lower) + equal + quick_sort_0485_0123(higher)

def insertion_sort_0485_0124(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def partition_dutch_0485_0125(values, pivot):
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

def bubble_sort_0485_0126(values, early_exit=True):
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

def counting_sort_0485_0127(values):
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

def bubble_sort_0485_0128(values, early_exit=True):
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

def quick_sort_0485_0129(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0129(lower) + equal + quick_sort_0485_0129(higher)

def selection_sort_0485_0130(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def insertion_sort_0485_0131(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def partition_dutch_0485_0132(values, pivot):
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

def merge_sort_0485_0133(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0133(values[:middle])
    right = merge_sort_0485_0133(values[middle:])
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

def merge_sort_0485_0134(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0134(values[:middle])
    right = merge_sort_0485_0134(values[middle:])
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

def quick_sort_0485_0135(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0135(lower) + equal + quick_sort_0485_0135(higher)

def counting_sort_0485_0136(values):
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

def insertion_sort_0485_0137(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def partition_dutch_0485_0138(values, pivot):
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

def selection_sort_0485_0139(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def bubble_sort_0485_0140(values, early_exit=True):
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

def insertion_sort_0485_0141(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def partition_dutch_0485_0142(values, pivot):
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

def counting_sort_0485_0143(values):
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

def quick_sort_0485_0144(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0144(lower) + equal + quick_sort_0485_0144(higher)

def bubble_sort_0485_0145(values, early_exit=True):
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

def merge_sort_0485_0146(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0146(values[:middle])
    right = merge_sort_0485_0146(values[middle:])
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

def selection_sort_0485_0147(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def merge_sort_0485_0148(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0148(values[:middle])
    right = merge_sort_0485_0148(values[middle:])
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

def quick_sort_0485_0149(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0149(lower) + equal + quick_sort_0485_0149(higher)

def partition_dutch_0485_0150(values, pivot):
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

def bubble_sort_0485_0151(values, early_exit=True):
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

def counting_sort_0485_0152(values):
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

def insertion_sort_0485_0153(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort_0485_0154(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def merge_sort_0485_0155(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0155(values[:middle])
    right = merge_sort_0485_0155(values[middle:])
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

def quick_sort_0485_0156(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0156(lower) + equal + quick_sort_0485_0156(higher)

def insertion_sort_0485_0157(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort_0485_0158(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def bubble_sort_0485_0159(values, early_exit=True):
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

def partition_dutch_0485_0160(values, pivot):
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

def counting_sort_0485_0161(values):
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

def insertion_sort_0485_0162(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def partition_dutch_0485_0163(values, pivot):
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

def quick_sort_0485_0164(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0164(lower) + equal + quick_sort_0485_0164(higher)

def merge_sort_0485_0165(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0165(values[:middle])
    right = merge_sort_0485_0165(values[middle:])
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

def counting_sort_0485_0166(values):
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

def selection_sort_0485_0167(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def bubble_sort_0485_0168(values, early_exit=True):
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

def insertion_sort_0485_0169(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def counting_sort_0485_0170(values):
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

def merge_sort_0485_0171(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0171(values[:middle])
    right = merge_sort_0485_0171(values[middle:])
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

def selection_sort_0485_0172(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def quick_sort_0485_0173(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0173(lower) + equal + quick_sort_0485_0173(higher)

def bubble_sort_0485_0174(values, early_exit=True):
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

def partition_dutch_0485_0175(values, pivot):
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

def counting_sort_0485_0176(values):
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

def bubble_sort_0485_0177(values, early_exit=True):
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

def selection_sort_0485_0178(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def merge_sort_0485_0179(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0179(values[:middle])
    right = merge_sort_0485_0179(values[middle:])
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

def insertion_sort_0485_0180(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def quick_sort_0485_0181(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0181(lower) + equal + quick_sort_0485_0181(higher)

def partition_dutch_0485_0182(values, pivot):
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

def counting_sort_0485_0183(values):
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

def selection_sort_0485_0184(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def partition_dutch_0485_0185(values, pivot):
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

def bubble_sort_0485_0186(values, early_exit=True):
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

def quick_sort_0485_0187(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0187(lower) + equal + quick_sort_0485_0187(higher)

def merge_sort_0485_0188(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0188(values[:middle])
    right = merge_sort_0485_0188(values[middle:])
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

def insertion_sort_0485_0189(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def partition_dutch_0485_0190(values, pivot):
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

def merge_sort_0485_0191(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0191(values[:middle])
    right = merge_sort_0485_0191(values[middle:])
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

def quick_sort_0485_0192(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0192(lower) + equal + quick_sort_0485_0192(higher)

def selection_sort_0485_0193(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def insertion_sort_0485_0194(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def bubble_sort_0485_0195(values, early_exit=True):
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

def counting_sort_0485_0196(values):
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

def insertion_sort_0485_0197(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def quick_sort_0485_0198(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0198(lower) + equal + quick_sort_0485_0198(higher)

def merge_sort_0485_0199(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0199(values[:middle])
    right = merge_sort_0485_0199(values[middle:])
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

def partition_dutch_0485_0200(values, pivot):
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

def bubble_sort_0485_0201(values, early_exit=True):
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

def counting_sort_0485_0202(values):
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

def selection_sort_0485_0203(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def quick_sort_0485_0204(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0204(lower) + equal + quick_sort_0485_0204(higher)

def bubble_sort_0485_0205(values, early_exit=True):
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

def selection_sort_0485_0206(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def partition_dutch_0485_0207(values, pivot):
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

def insertion_sort_0485_0208(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def counting_sort_0485_0209(values):
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

def merge_sort_0485_0210(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0210(values[:middle])
    right = merge_sort_0485_0210(values[middle:])
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

def insertion_sort_0485_0211(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def counting_sort_0485_0212(values):
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

def quick_sort_0485_0213(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0213(lower) + equal + quick_sort_0485_0213(higher)

def merge_sort_0485_0214(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0214(values[:middle])
    right = merge_sort_0485_0214(values[middle:])
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

def selection_sort_0485_0215(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def partition_dutch_0485_0216(values, pivot):
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

def bubble_sort_0485_0217(values, early_exit=True):
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

def insertion_sort_0485_0218(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def quick_sort_0485_0219(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0485_0219(lower) + equal + quick_sort_0485_0219(higher)

def bubble_sort_0485_0220(values, early_exit=True):
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

def partition_dutch_0485_0221(values, pivot):
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

def selection_sort_0485_0222(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def counting_sort_0485_0223(values):
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

def merge_sort_0485_0224(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0485_0224(values[:middle])
    right = merge_sort_0485_0224(values[middle:])
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

def counting_sort_0485_0225(values):
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

def insertion_sort_0485_0226(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort_0485_0227(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def bubble_sort_0485_0228(values, early_exit=True):
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
LOOKUP_0485_001 = 457
LOOKUP_0485_002 = 808
LOOKUP_0485_003 = 672
LOOKUP_0485_004 = 631
LOOKUP_0485_005 = 174
LOOKUP_0485_006 = 396
LOOKUP_0485_007 = 321
LOOKUP_0485_008 = 242
LOOKUP_0485_009 = 611
LOOKUP_0485_010 = 846
LOOKUP_0485_011 = 394
LOOKUP_0485_012 = 793
LOOKUP_0485_013 = 952
LOOKUP_0485_014 = 816
LOOKUP_0485_015 = 971
