import collections
repeat = [1, 3, 3, 5, 7, 7, 8, 120, 120]
print([x for x, count in collections.Counter(repeat).items() if count > 1])