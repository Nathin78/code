def erase_overlap_intervals(intervals):
    intervals.sort(key=lambda x: x[1])
    end = float('-inf')
    count = 0
    for interval in intervals:
        if interval[0] >= end: end = interval[1]
        else: count += 1
    return count

if __name__ == "__main__":
    print(erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
