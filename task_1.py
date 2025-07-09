# TODO 1.	Оценить асимптотическую сложность приведенного ниже алгоритма:
a = len(arr) - 1 #O(1)
out = list() #O(1)
while a > 0 #O(log(N))
    out.append(arr[a]) #O(1)
    a = a // 1.7 #O(1)
out.merge_sort() #O(N∗log(N))

# O(1) + O(1) + ((O(log(N)) * O(1) + O(1)) * log (O(log(N)) * O(1) + O(1))) ->
# O(log(N) * log(log(N)))