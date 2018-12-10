


# 수치형 이외의 다른 타입의 객체 비교
print("abcd" > "abd")
print((1, 2, 4) < (1, 3, 1))
print([1, 2, 4] < [1, 2, 0])

# 동질성 비교(값 체크) : ==, 동일성 비교(레퍼런스 체크) : is
a = 10
b = 20
c = a
print(a == b)
print(a is b)
print(a is c)
print(a == c)











