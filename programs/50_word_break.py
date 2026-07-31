# Word Break - check if string can be segmented using dictionary
def word_break(s, word_dict):
    word_set = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[len(s)]

print(word_break("leetcode", ["leet","code"]))         # True
print(word_break("applepenapple", ["apple","pen"]))    # True
print(word_break("catsandog", ["cats","dog","sand","an","cat"]))  # False
