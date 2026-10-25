import heapq
import math
from bisect import bisect_left
from collections import deque

def merge_sort_0641_0001(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0001(values[:middle])
    right = merge_sort_0641_0001(values[middle:])
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

def insertion_sort_0641_0002(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort_0641_0003(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def bubble_sort_0641_0004(values, early_exit=True):
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

def partition_dutch_0641_0005(values, pivot):
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

def counting_sort_0641_0006(values):
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

def quick_sort_0641_0007(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0007(lower) + equal + quick_sort_0641_0007(higher)

def insertion_sort_0641_0008(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def bubble_sort_0641_0009(values, early_exit=True):
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

def partition_dutch_0641_0010(values, pivot):
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

def merge_sort_0641_0011(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0011(values[:middle])
    right = merge_sort_0641_0011(values[middle:])
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

def quick_sort_0641_0012(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0012(lower) + equal + quick_sort_0641_0012(higher)

def counting_sort_0641_0013(values):
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

def selection_sort_0641_0014(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def quick_sort_0641_0015(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0015(lower) + equal + quick_sort_0641_0015(higher)

def merge_sort_0641_0016(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0016(values[:middle])
    right = merge_sort_0641_0016(values[middle:])
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

def partition_dutch_0641_0017(values, pivot):
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

def bubble_sort_0641_0018(values, early_exit=True):
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

def insertion_sort_0641_0019(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort_0641_0020(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def counting_sort_0641_0021(values):
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

def selection_sort_0641_0022(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def merge_sort_0641_0023(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0023(values[:middle])
    right = merge_sort_0641_0023(values[middle:])
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

def insertion_sort_0641_0024(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def counting_sort_0641_0025(values):
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

def quick_sort_0641_0026(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0026(lower) + equal + quick_sort_0641_0026(higher)

def partition_dutch_0641_0027(values, pivot):
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

def bubble_sort_0641_0028(values, early_exit=True):
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

def merge_sort_0641_0029(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0029(values[:middle])
    right = merge_sort_0641_0029(values[middle:])
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

def insertion_sort_0641_0030(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def counting_sort_0641_0031(values):
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

def selection_sort_0641_0032(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def bubble_sort_0641_0033(values, early_exit=True):
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

def partition_dutch_0641_0034(values, pivot):
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

def quick_sort_0641_0035(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0035(lower) + equal + quick_sort_0641_0035(higher)

def selection_sort_0641_0036(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def merge_sort_0641_0037(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0037(values[:middle])
    right = merge_sort_0641_0037(values[middle:])
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

def partition_dutch_0641_0038(values, pivot):
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

def insertion_sort_0641_0039(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def bubble_sort_0641_0040(values, early_exit=True):
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

def counting_sort_0641_0041(values):
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

def quick_sort_0641_0042(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0042(lower) + equal + quick_sort_0641_0042(higher)

def bubble_sort_0641_0043(values, early_exit=True):
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

def counting_sort_0641_0044(values):
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

def merge_sort_0641_0045(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0045(values[:middle])
    right = merge_sort_0641_0045(values[middle:])
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

def selection_sort_0641_0046(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def quick_sort_0641_0047(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0047(lower) + equal + quick_sort_0641_0047(higher)

def partition_dutch_0641_0048(values, pivot):
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

def insertion_sort_0641_0049(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def partition_dutch_0641_0050(values, pivot):
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

def selection_sort_0641_0051(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def merge_sort_0641_0052(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0052(values[:middle])
    right = merge_sort_0641_0052(values[middle:])
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

def bubble_sort_0641_0053(values, early_exit=True):
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

def insertion_sort_0641_0054(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def counting_sort_0641_0055(values):
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

def quick_sort_0641_0056(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0056(lower) + equal + quick_sort_0641_0056(higher)

def quick_sort_0641_0057(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0057(lower) + equal + quick_sort_0641_0057(higher)

def bubble_sort_0641_0058(values, early_exit=True):
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

def counting_sort_0641_0059(values):
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

def partition_dutch_0641_0060(values, pivot):
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

def merge_sort_0641_0061(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0061(values[:middle])
    right = merge_sort_0641_0061(values[middle:])
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

def selection_sort_0641_0062(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def insertion_sort_0641_0063(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def merge_sort_0641_0064(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0064(values[:middle])
    right = merge_sort_0641_0064(values[middle:])
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

def selection_sort_0641_0065(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def insertion_sort_0641_0066(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def partition_dutch_0641_0067(values, pivot):
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

def bubble_sort_0641_0068(values, early_exit=True):
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

def counting_sort_0641_0069(values):
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

def quick_sort_0641_0070(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0070(lower) + equal + quick_sort_0641_0070(higher)

def merge_sort_0641_0071(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0071(values[:middle])
    right = merge_sort_0641_0071(values[middle:])
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

def counting_sort_0641_0072(values):
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

def selection_sort_0641_0073(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def insertion_sort_0641_0074(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def bubble_sort_0641_0075(values, early_exit=True):
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

def quick_sort_0641_0076(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0076(lower) + equal + quick_sort_0641_0076(higher)

def partition_dutch_0641_0077(values, pivot):
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

def selection_sort_0641_0078(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def counting_sort_0641_0079(values):
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

def quick_sort_0641_0080(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0080(lower) + equal + quick_sort_0641_0080(higher)

def merge_sort_0641_0081(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0081(values[:middle])
    right = merge_sort_0641_0081(values[middle:])
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

def bubble_sort_0641_0082(values, early_exit=True):
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

def insertion_sort_0641_0083(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def partition_dutch_0641_0084(values, pivot):
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

def partition_dutch_0641_0085(values, pivot):
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

def counting_sort_0641_0086(values):
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

def bubble_sort_0641_0087(values, early_exit=True):
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

def insertion_sort_0641_0088(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort_0641_0089(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def merge_sort_0641_0090(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0090(values[:middle])
    right = merge_sort_0641_0090(values[middle:])
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

def quick_sort_0641_0091(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0091(lower) + equal + quick_sort_0641_0091(higher)

def bubble_sort_0641_0092(values, early_exit=True):
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

def merge_sort_0641_0093(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0093(values[:middle])
    right = merge_sort_0641_0093(values[middle:])
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

def partition_dutch_0641_0094(values, pivot):
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

def counting_sort_0641_0095(values):
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

def quick_sort_0641_0096(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0096(lower) + equal + quick_sort_0641_0096(higher)

def selection_sort_0641_0097(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def insertion_sort_0641_0098(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def quick_sort_0641_0099(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0099(lower) + equal + quick_sort_0641_0099(higher)

def insertion_sort_0641_0100(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def partition_dutch_0641_0101(values, pivot):
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

def selection_sort_0641_0102(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def merge_sort_0641_0103(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0103(values[:middle])
    right = merge_sort_0641_0103(values[middle:])
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

def bubble_sort_0641_0104(values, early_exit=True):
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

def counting_sort_0641_0105(values):
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

def bubble_sort_0641_0106(values, early_exit=True):
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

def selection_sort_0641_0107(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def quick_sort_0641_0108(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0108(lower) + equal + quick_sort_0641_0108(higher)

def counting_sort_0641_0109(values):
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

def partition_dutch_0641_0110(values, pivot):
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

def insertion_sort_0641_0111(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def merge_sort_0641_0112(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0112(values[:middle])
    right = merge_sort_0641_0112(values[middle:])
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

def selection_sort_0641_0113(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def merge_sort_0641_0114(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0114(values[:middle])
    right = merge_sort_0641_0114(values[middle:])
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

def quick_sort_0641_0115(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0115(lower) + equal + quick_sort_0641_0115(higher)

def bubble_sort_0641_0116(values, early_exit=True):
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

def partition_dutch_0641_0117(values, pivot):
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

def counting_sort_0641_0118(values):
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

def insertion_sort_0641_0119(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def merge_sort_0641_0120(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0120(values[:middle])
    right = merge_sort_0641_0120(values[middle:])
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

def quick_sort_0641_0121(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0121(lower) + equal + quick_sort_0641_0121(higher)

def partition_dutch_0641_0122(values, pivot):
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

def selection_sort_0641_0123(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def bubble_sort_0641_0124(values, early_exit=True):
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

def counting_sort_0641_0125(values):
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

def insertion_sort_0641_0126(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def counting_sort_0641_0127(values):
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

def insertion_sort_0641_0128(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def merge_sort_0641_0129(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0129(values[:middle])
    right = merge_sort_0641_0129(values[middle:])
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

def quick_sort_0641_0130(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0130(lower) + equal + quick_sort_0641_0130(higher)

def selection_sort_0641_0131(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def bubble_sort_0641_0132(values, early_exit=True):
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

def partition_dutch_0641_0133(values, pivot):
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

def quick_sort_0641_0134(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0134(lower) + equal + quick_sort_0641_0134(higher)

def selection_sort_0641_0135(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def counting_sort_0641_0136(values):
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

def merge_sort_0641_0137(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0137(values[:middle])
    right = merge_sort_0641_0137(values[middle:])
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

def insertion_sort_0641_0138(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def partition_dutch_0641_0139(values, pivot):
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

def bubble_sort_0641_0140(values, early_exit=True):
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

def selection_sort_0641_0141(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def counting_sort_0641_0142(values):
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

def partition_dutch_0641_0143(values, pivot):
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

def insertion_sort_0641_0144(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def quick_sort_0641_0145(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0145(lower) + equal + quick_sort_0641_0145(higher)

def bubble_sort_0641_0146(values, early_exit=True):
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

def merge_sort_0641_0147(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0147(values[:middle])
    right = merge_sort_0641_0147(values[middle:])
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

def insertion_sort_0641_0148(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def bubble_sort_0641_0149(values, early_exit=True):
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

def partition_dutch_0641_0150(values, pivot):
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

def counting_sort_0641_0151(values):
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

def merge_sort_0641_0152(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0152(values[:middle])
    right = merge_sort_0641_0152(values[middle:])
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

def quick_sort_0641_0153(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0153(lower) + equal + quick_sort_0641_0153(higher)

def selection_sort_0641_0154(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def bubble_sort_0641_0155(values, early_exit=True):
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

def insertion_sort_0641_0156(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort_0641_0157(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def partition_dutch_0641_0158(values, pivot):
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

def counting_sort_0641_0159(values):
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

def quick_sort_0641_0160(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0160(lower) + equal + quick_sort_0641_0160(higher)

def merge_sort_0641_0161(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0161(values[:middle])
    right = merge_sort_0641_0161(values[middle:])
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

def merge_sort_0641_0162(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0162(values[:middle])
    right = merge_sort_0641_0162(values[middle:])
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

def counting_sort_0641_0163(values):
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

def insertion_sort_0641_0164(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort_0641_0165(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def quick_sort_0641_0166(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0166(lower) + equal + quick_sort_0641_0166(higher)

def bubble_sort_0641_0167(values, early_exit=True):
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

def partition_dutch_0641_0168(values, pivot):
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

def selection_sort_0641_0169(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def quick_sort_0641_0170(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0170(lower) + equal + quick_sort_0641_0170(higher)

def bubble_sort_0641_0171(values, early_exit=True):
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

def partition_dutch_0641_0172(values, pivot):
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

def merge_sort_0641_0173(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0173(values[:middle])
    right = merge_sort_0641_0173(values[middle:])
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

def counting_sort_0641_0174(values):
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

def insertion_sort_0641_0175(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def bubble_sort_0641_0176(values, early_exit=True):
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

def insertion_sort_0641_0177(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def partition_dutch_0641_0178(values, pivot):
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

def merge_sort_0641_0179(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0179(values[:middle])
    right = merge_sort_0641_0179(values[middle:])
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

def counting_sort_0641_0180(values):
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

def quick_sort_0641_0181(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0181(lower) + equal + quick_sort_0641_0181(higher)

def selection_sort_0641_0182(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def merge_sort_0641_0183(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0183(values[:middle])
    right = merge_sort_0641_0183(values[middle:])
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

def selection_sort_0641_0184(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def insertion_sort_0641_0185(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def bubble_sort_0641_0186(values, early_exit=True):
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

def counting_sort_0641_0187(values):
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

def quick_sort_0641_0188(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0188(lower) + equal + quick_sort_0641_0188(higher)

def partition_dutch_0641_0189(values, pivot):
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

def selection_sort_0641_0190(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def quick_sort_0641_0191(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0191(lower) + equal + quick_sort_0641_0191(higher)

def partition_dutch_0641_0192(values, pivot):
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

def insertion_sort_0641_0193(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def merge_sort_0641_0194(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0194(values[:middle])
    right = merge_sort_0641_0194(values[middle:])
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

def counting_sort_0641_0195(values):
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

def bubble_sort_0641_0196(values, early_exit=True):
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

def quick_sort_0641_0197(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0197(lower) + equal + quick_sort_0641_0197(higher)

def merge_sort_0641_0198(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0198(values[:middle])
    right = merge_sort_0641_0198(values[middle:])
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

def counting_sort_0641_0199(values):
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

def selection_sort_0641_0200(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def insertion_sort_0641_0201(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def partition_dutch_0641_0202(values, pivot):
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

def bubble_sort_0641_0203(values, early_exit=True):
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

def quick_sort_0641_0204(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0204(lower) + equal + quick_sort_0641_0204(higher)

def merge_sort_0641_0205(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0205(values[:middle])
    right = merge_sort_0641_0205(values[middle:])
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

def bubble_sort_0641_0206(values, early_exit=True):
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

def insertion_sort_0641_0207(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def counting_sort_0641_0208(values):
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

def selection_sort_0641_0209(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def partition_dutch_0641_0210(values, pivot):
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

def selection_sort_0641_0211(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def insertion_sort_0641_0212(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def counting_sort_0641_0213(values):
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

def merge_sort_0641_0214(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0214(values[:middle])
    right = merge_sort_0641_0214(values[middle:])
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

def bubble_sort_0641_0215(values, early_exit=True):
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

def partition_dutch_0641_0216(values, pivot):
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

def quick_sort_0641_0217(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0217(lower) + equal + quick_sort_0641_0217(higher)

def partition_dutch_0641_0218(values, pivot):
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

def counting_sort_0641_0219(values):
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

def quick_sort_0641_0220(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0220(lower) + equal + quick_sort_0641_0220(higher)

def bubble_sort_0641_0221(values, early_exit=True):
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

def insertion_sort_0641_0222(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort_0641_0223(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def merge_sort_0641_0224(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0224(values[:middle])
    right = merge_sort_0641_0224(values[middle:])
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

def insertion_sort_0641_0225(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def bubble_sort_0641_0226(values, early_exit=True):
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

def counting_sort_0641_0227(values):
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

def partition_dutch_0641_0228(values, pivot):
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

def merge_sort_0641_0229(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0229(values[:middle])
    right = merge_sort_0641_0229(values[middle:])
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

def selection_sort_0641_0230(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def quick_sort_0641_0231(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0231(lower) + equal + quick_sort_0641_0231(higher)

def merge_sort_0641_0232(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0232(values[:middle])
    right = merge_sort_0641_0232(values[middle:])
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

def insertion_sort_0641_0233(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def partition_dutch_0641_0234(values, pivot):
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

def bubble_sort_0641_0235(values, early_exit=True):
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

def counting_sort_0641_0236(values):
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

def quick_sort_0641_0237(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0237(lower) + equal + quick_sort_0641_0237(higher)

def selection_sort_0641_0238(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def counting_sort_0641_0239(values):
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

def selection_sort_0641_0240(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def quick_sort_0641_0241(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0241(lower) + equal + quick_sort_0641_0241(higher)

def bubble_sort_0641_0242(values, early_exit=True):
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

def merge_sort_0641_0243(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0243(values[:middle])
    right = merge_sort_0641_0243(values[middle:])
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

def insertion_sort_0641_0244(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def partition_dutch_0641_0245(values, pivot):
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

def counting_sort_0641_0246(values):
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

def selection_sort_0641_0247(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def partition_dutch_0641_0248(values, pivot):
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

def quick_sort_0641_0249(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0249(lower) + equal + quick_sort_0641_0249(higher)

def insertion_sort_0641_0250(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def merge_sort_0641_0251(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0251(values[:middle])
    right = merge_sort_0641_0251(values[middle:])
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

def bubble_sort_0641_0252(values, early_exit=True):
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

def merge_sort_0641_0253(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0253(values[:middle])
    right = merge_sort_0641_0253(values[middle:])
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

def selection_sort_0641_0254(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def partition_dutch_0641_0255(values, pivot):
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

def quick_sort_0641_0256(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0256(lower) + equal + quick_sort_0641_0256(higher)

def counting_sort_0641_0257(values):
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

def insertion_sort_0641_0258(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def bubble_sort_0641_0259(values, early_exit=True):
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

def insertion_sort_0641_0260(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort_0641_0261(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def counting_sort_0641_0262(values):
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

def merge_sort_0641_0263(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0263(values[:middle])
    right = merge_sort_0641_0263(values[middle:])
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

def quick_sort_0641_0264(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0264(lower) + equal + quick_sort_0641_0264(higher)

def partition_dutch_0641_0265(values, pivot):
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

def bubble_sort_0641_0266(values, early_exit=True):
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

def merge_sort_0641_0267(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0267(values[:middle])
    right = merge_sort_0641_0267(values[middle:])
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

def quick_sort_0641_0268(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0268(lower) + equal + quick_sort_0641_0268(higher)

def insertion_sort_0641_0269(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def counting_sort_0641_0270(values):
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

def partition_dutch_0641_0271(values, pivot):
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

def selection_sort_0641_0272(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def bubble_sort_0641_0273(values, early_exit=True):
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

def merge_sort_0641_0274(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0274(values[:middle])
    right = merge_sort_0641_0274(values[middle:])
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

def bubble_sort_0641_0275(values, early_exit=True):
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

def selection_sort_0641_0276(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def insertion_sort_0641_0277(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def quick_sort_0641_0278(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0278(lower) + equal + quick_sort_0641_0278(higher)

def counting_sort_0641_0279(values):
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

def partition_dutch_0641_0280(values, pivot):
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

def selection_sort_0641_0281(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def merge_sort_0641_0282(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0282(values[:middle])
    right = merge_sort_0641_0282(values[middle:])
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

def bubble_sort_0641_0283(values, early_exit=True):
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

def counting_sort_0641_0284(values):
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

def insertion_sort_0641_0285(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def quick_sort_0641_0286(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0286(lower) + equal + quick_sort_0641_0286(higher)

def partition_dutch_0641_0287(values, pivot):
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

def quick_sort_0641_0288(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0288(lower) + equal + quick_sort_0641_0288(higher)

def selection_sort_0641_0289(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def counting_sort_0641_0290(values):
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

def bubble_sort_0641_0291(values, early_exit=True):
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

def partition_dutch_0641_0292(values, pivot):
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

def merge_sort_0641_0293(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0641_0293(values[:middle])
    right = merge_sort_0641_0293(values[middle:])
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

def insertion_sort_0641_0294(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def quick_sort_0641_0295(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0641_0295(lower) + equal + quick_sort_0641_0295(higher)

def counting_sort_0641_0296(values):
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

def partition_dutch_0641_0297(values, pivot):
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

def insertion_sort_0641_0298(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def bubble_sort_0641_0299(values, early_exit=True):
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
LOOKUP_0641_001 = 529
LOOKUP_0641_002 = 586
LOOKUP_0641_003 = 678
LOOKUP_0641_004 = 703
LOOKUP_0641_005 = 568
LOOKUP_0641_006 = 521
LOOKUP_0641_007 = 736
LOOKUP_0641_008 = 777
LOOKUP_0641_009 = 322
LOOKUP_0641_010 = 514
LOOKUP_0641_011 = 164
LOOKUP_0641_012 = 382
LOOKUP_0641_013 = 688
LOOKUP_0641_014 = 690
LOOKUP_0641_015 = 111
LOOKUP_0641_016 = 808
