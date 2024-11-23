# keys()
test_1 = {'a' : 1, 'b' : 2}
result_1 = test_1.keys()
print(result_1)
print(type(result_1))

# for t in result_1 :
#     print(t)

# values()
test_2 = {'a' : 1, 'b' : 234}
result_2 = test_2.values()
print(result_2)


# items()
test_3 = {'a' : 1, 'b' : 2}
result_3 = test_3.items()
for r in result_3 :
    print(type(r))


# get()
test_4 = {'a' : 'abc', 1 : 222}
print(test_4.get('a'))
print(test_4.get('ddd'))


# update()
test_5 = {'a' : 'aaa', 'b' : 'bb', 'c' : 1000}
test_5.update({'a' : 1111, 'd' : 'dicafio'})
print(test_5)


# pop()
test_6 = {'a' : 'aaaa', 'b' : 1224}
print(test_6.pop('a','koala3121'))
print(test_6.pop('ddd','koala3121'))
print(test_6)


# popitem()
test_7 = {'abbb' : 'abbb', 1 : '1', 'b' : {'aa' : '1'}}
print(test_7.popitem())
print(test_7)


# clear()
test_8 = {'1': '1111'}
test_8.clear()
print(test_8)


# setdefault()
test_9 = {'a' : 'aaa', 'b' : 222, 'c' : 'cccc'}
test_9.setdefault('a' , 3000)
test_9.setdefault('d', 500)
print(test_9)

print(len(test_7))

