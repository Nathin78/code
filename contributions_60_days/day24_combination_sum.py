def combination_sum(candidates, target):
    res = []
    def backtrack(remain, combo, start):
        if remain == 0:
            res.append(list(combo))
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remain: continue
            combo.append(candidates[i])
            backtrack(remain - candidates[i], combo, i)
            combo.pop()
    backtrack(target, [], 0)
    return res

if __name__ == "__main__":
    print(combination_sum([2, 3, 6, 7], 7))
