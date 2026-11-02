import random
import statistics
import time
import tracemalloc
import csv


def merge_sort(values):
    """Return a sorted copy by recursively merging two halves."""
    if len(values) <= 1:
        return values[:]
    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(values):
    """Sort a list in place, using the last item as pivot."""
    def partition(low, high):
        pivot = values[high]
        boundary = low - 1
        for j in range(low, high):
            if values[j] <= pivot:
                boundary += 1
                values[boundary], values[j] = values[j], values[boundary]
        values[boundary + 1], values[high] = values[high], values[boundary + 1]
        return boundary + 1

    def sort(low, high):
        # Recurse into the smaller side, iterate over the larger side.
        # This limits Python stack depth, even for sorted input.
        while low < high:
            p = partition(low, high)
            if p - low < high - p:
                sort(low, p - 1)
                low = p + 1
            else:
                sort(p + 1, high)
                high = p - 1
    sort(0, len(values) - 1)
    return values


def benchmark(algorithm, original, repeats=5):
    times = []
    peaks = []
    expected = sorted(original)
    for _ in range(repeats):
        data = original.copy()
        tracemalloc.start()
        start = time.perf_counter()
        result = algorithm(data)
        elapsed = time.perf_counter() - start
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        assert result == expected, 'Incorrect sorting result'
        times.append(elapsed * 1000)
        peaks.append(peak / 1024)
    return round(statistics.median(times), 3), round(statistics.median(peaks), 2)


def main():
    rng = random.Random(42)
    rows = []
    for size in [100, 500, 1000]:
        datasets = {
            'Sorted': list(range(size)),
            'Reverse sorted': list(range(size, 0, -1)),
            'Random': rng.sample(range(size * 10), size),
        }
        for kind, data in datasets.items():
            for name, algorithm in [('Merge Sort', merge_sort), ('Quick Sort', quick_sort)]:
                milliseconds, kib = benchmark(algorithm, data)
                row = [size, kind, name, milliseconds, kib]
                rows.append(row)
                print(f'{size:5} | {kind:14} | {name:10} | {milliseconds:9.3f} ms | {kib:9.2f} KiB')
    with open('sorting_results.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Input size', 'Dataset', 'Algorithm', 'Median time (ms)', 'Median peak traced memory (KiB)'])
        writer.writerows(rows)
    print('Saved sorting_results.csv')


if __name__ == '__main__':
    main()
