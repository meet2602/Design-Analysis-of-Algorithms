"""
A thief robbing a store finds n items, ith item is worth vi dollars and 
weights wi pounds, where vi and wi are integers. He wants to take as 
valuable a load as possible, but he can carry at most W pounds in his 
knapsack where W is an integer. Which items should he take, where 
condition is that he is allowed to take or select fractional part of an item? 
W = 50, n = 3
Object 1 2 3
Weight (Wi) 10 20 30
Value (Vi) 60 100 150
"""


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
