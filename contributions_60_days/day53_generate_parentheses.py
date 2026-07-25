def generate_parenthesis(n):
    res = []
    def backtrack(open_c, close_c, path):
        if len(path) == 2 * n:
            res.append(path)
            return
        if open_c < n:
            backtrack(open_c + 1, close_c, path + "(")
        if close_c < open_c:
            backtrack(open_c, close_c + 1, path + ")")
    backtrack(0, 0, "")
    return res

if __name__ == "__main__":
    print(generate_parenthesis(3))
