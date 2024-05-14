def knapsackDP(items, weight, values, capacity):
    n, m = len(items), capacity
    v = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(n + 1):
        for w in range(m + 1):
            if i == 0 or w == 0:
                v[i][w] = 0
            elif weight[i - 1] <= w:
                v[i][w] = max(v[i - 1][w], values[i - 1] + v[i - 1][w - weight[i - 1]])
            else:
                v[i][w] = v[i - 1][w]

    print("Selected items:",backtracking(v, weight, n, m))
    return v[n][m]


def backtracking(v, weight, i, w):  # n and m
    r = [0 for a in range(i)]
    while i > 0 and w > 0:
        if v[i][w] != v[i - 1][w]:
            r[i - 1] = 1
            w = w - weight[i - 1]
            i -= 1
        else:
            i -= 1
    return r


def sort(items, weight, profit):
    n = len(items)
    fraction = []
    for i in range(n):
        fraction.append(profit[i] / weight[i])
    values = zip(fraction, items, weight, profit)
    sorted_values = sorted(values)
    new_items = [value[1] for value in sorted_values]
    new_weight = [value[2] for value in sorted_values]
    new_profit = [value[3] for value in sorted_values]
    new_items.reverse(), new_weight.reverse(), new_profit.reverse()
    return new_items, new_weight, new_profit


def knapsackGR(profit, weight, items, capacity):
    items, weight, profit = sort(items, weight, profit)
    n = len(items)
    remaining_cap = capacity
    x = [0 for i in range(n)]
    i = 0
    for i in range(n):
        if weight[i] > remaining_cap:
            break
        x[i] = 1
        remaining_cap = remaining_cap - weight[i]
    if i <= n:
        x[i] = (remaining_cap / weight[i])
    print("Max Profit =", maxprofit(profit, x))
    return x


def maxprofit(profit, x):
    max = 0
    for i in range(len(x)):
        max += (profit[i] * x[i])
    return max


weight = [3, 2, 4, 1]
weight1 = [5, 2, 1, 3, 4, 6]
items = ["I1", "I2", "I3", "I4"]
items1 = ["I1", "I2", "I3", "I4", "I5", "I6"]
values = [100, 20, 60, 40]
values1 = [20, 50, 10, 40, 30, 100]
c = 5
c1 = 10

# print("Max Profit =",knapsackDP(items,weight,values,c))
# print("Selected items:",knapsackGR(values,weight,items,c))
# print("Max Profit =",knapsackDP(items1,weight1,values1,c1))
print("Selected items:",knapsackGR(values1, weight1, items1, c1))
