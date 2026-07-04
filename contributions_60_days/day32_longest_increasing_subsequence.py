import bisect

def length_of_lis(nums):
    sub = []
    for x in nums:
        i = bisect.bisect_left(sub, x)
        if i == len(sub): sub.append(x)
        else: sub[i] = x
    return len(sub)

if __name__ == "__main__":
    print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))
