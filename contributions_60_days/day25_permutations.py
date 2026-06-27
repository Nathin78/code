def permute(nums):
    res = []
    def backtrack(first=0):
        if first == len(nums):
            res.append(nums[:])
            return
        for i in range(first, len(nums)):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]
    backtrack()
    return res

if __name__ == "__main__":
    print(permute([1, 2, 3]))
