def max_profit(prices):
    min_price = float('inf')
    max_p = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_p:
            max_p = price - min_price
    return max_p

if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))
