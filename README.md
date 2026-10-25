<div align="center">

# 🐍 Python Sorting Algorithms

**A 1,000-file synthetic Python corpus of sorting implementations,
built to train and evaluate code language models.**

![Files](https://img.shields.io/badge/Files-1%2C000-2563eb?style=for-the-badge)
![Lines](https://img.shields.io/badge/Lines-1,739,445-16a34a?style=for-the-badge)
![Size](https://img.shields.io/badge/Size-54_MB-7c3aed?style=for-the-badge)
![Algorithms](https://img.shields.io/badge/Algorithms-7-db2777?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)

</div>

---

> **Synthetic dataset.** Every module is machine-generated from a template bank of
> algorithm implementations. It is training data for a custom code model, not
> production library code.

## Overview

This repository is one of a ten-part thematic corpus. It contains **1,000 standalone
Python modules** covering sorting algorithms: bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort, counting_sort, partition_dutch.

Each file ranges from **100 to 4,000 lines**; every module compiles and every symbol
is namespaced with a file/block suffix so the whole corpus can be imported together.

## At a glance

| Property | Value |
| :-- | --: |
| Files (`.py`) | **1,000** |
| Total lines | **1,739,445** |
| Total size | **54.3 MiB** |
| Lines per file | **100 – 4,000** |
| Algorithms | **7** |
| Compile pass rate | **1,000 / 1,000** |
| Encoding / newlines | **UTF-8 / LF** |

## Algorithms

| Symbol | Algorithm | Average time | Variants |
| :-- | :-- | :-- | --: |
| `bubble_sort` | Bubble Sort | `O(n^2)` | 18,723 |
| `insertion_sort` | Insertion Sort | `O(n^2)` | 18,739 |
| `selection_sort` | Selection Sort | `O(n^2)` | 18,717 |
| `merge_sort` | Merge Sort | `O(n log n)` | 18,673 |
| `quick_sort` | Quick Sort | `O(n log n)` | 18,714 |
| `counting_sort` | Counting Sort | `O(n + k)` | 18,713 |
| `partition_dutch` | Dutch Partition | `O(n)` | 18,703 |

## File layout

```
algorithms/algorithm-XXXX.py
├── imports            # heapq, math, bisect, collections
├── ALGORITHM BLOCKS   # shuffled definitions, suffixed _XXXX_YYYY
├── LOOKUP_XXXX_NNN    # module constants for the exact line count
```

**Naming convention:** `{algorithm}_{file_index}_{block_index}` — for example,
`bubble_sort_0042_0001`. The suffix makes every symbol in the corpus unique.

## Sample

Excerpt from `algorithms/algorithm-0042.py`:

```python
def counting_sort_0042_0001(values):
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
```

## Quality gates

- ✅ **Compiles cleanly** — every module passed `compile(source, path, "exec")`.
- ✅ **Exact line budget** — each file hits its 100–4,000 line target to the line.
- ✅ **Pure code** — no comments, no docstrings, no prose.
- ✅ **Deterministic** — a per-file seeded RNG reproduces the corpus.
- ✅ **Collision-free symbols** — all definitions carry a unique suffix.

## Intended use

Fine-tuning and pretraining code models; synthetic-data, tokenizer, retrieval, and
version-control experiments. Not suitable as production code or as a benchmark of
human-written style.

## License

No license has been specified yet. Until one is added, treat the content as all
rights reserved by the repository owner.
