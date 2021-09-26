def fractional_knapsack(value, weight, capacity):
    index = list(range(len(value)))
    ratio = [v/w for v, w in zip(value, weight)]
    index.sort(key=lambda i: ratio[i], reverse=True)
    print("ratio = ", index)
    max_value = 0
    for i in index:
        if weight[i] <= capacity:
            max_value += value[i]
            capacity -= weight[i]
        else:
            max_value += value[i]*capacity/weight[i]
            break

    print('items can be carried:', max_value)


weight = [10, 20, 30]
value = [60, 100, 120]
capacity = 50
print("weight = ", weight)
print("value = ", value)
print("capacity = ", capacity)
fractional_knapsack(value, weight, capacity)
