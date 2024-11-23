# append
test_1 = [1,2,3,4,5]
test_1.append({'koe' : '111'})
print(test_1)


# extend
test_2 = [1,2,4]
ttt = (1,3,5,6)
test_2.extend(ttt)
print(test_2)


# insert
test_3 = [1,2,3,4,5]
test_3.insert(2, 10)
print(test_3)


# remove
test_4 = [1,2,10]
test_4.remove(10)
print(test_4)


# pop 
test_5 = [1,2,3,100]
# test_5.pop()
test_5.pop(1)
print(test_5)


# clear
test_6 = ['a', 'b', 'c']
test_6.clear()
print(test_6)

# index
test_7 = [1,2,3,4]
print(test_7.index(2))

# count
test_8 = [100,1000,1000,1000,100]
print(test_8.count(1000))


# sort/reverse
test_9 = [1,2,3,4,5,6,7,1,2,3,4,8,9,10]
test_9.sort()
print(test_9)
test_9.reverse()
print(test_9)


# copy
test_10 = test_9.copy()
print(test_10)


# join
list = ['apple', 'banananan']
result = ', '.join(list)
print(result)