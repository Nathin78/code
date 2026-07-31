# Frequency counter using HashMap
def frequency_count(arr):
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    return freq

def most_frequent(arr):
    freq = frequency_count(arr)
    return max(freq, key=freq.get)

words = ["apple","banana","apple","cherry","banana","apple"]
print(frequency_count(words))
print(most_frequent(words))  # apple
