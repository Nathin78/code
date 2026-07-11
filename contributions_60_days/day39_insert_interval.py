def insert_interval(intervals, newInterval):
    res = []
    for i, interval in enumerate(intervals):
        if newInterval[1] < interval[0]:
            return res + [newInterval] + intervals[i:]
        elif newInterval[0] > interval[1]:
            res.append(interval)
        else:
            newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
    res.append(newInterval)
    return res

if __name__ == "__main__":
    print(insert_interval([[1, 3], [6, 9]], [2, 5]))
