a = 20
b = 30

print(not a < b)
print(a < b and a != b)
print(a == b or a != b) # 논리에서 앞의 연산 true, 뒤의 연산은 생략.

# True -> 1, False -> 0
print(True + 1)
print((a < b) + 1)

# bool 캐스팅
print(bool(10), bool(0))
print(bool(3.14), bool(0.))
print(bool([1, 2, 3]), bool([]))
print(bool({"a": 10}), bool({}))
print(bool(None)) # 파이썬에서는 Null이 아닌 None

# 논리식의 계산 순서
print([] or 'hello')
print('hello' or 'world')
print('' or 'world')
print(None and 1)

s = "hello world"
s = '' # ''이면 출력안함
s and print(s) # s가 비어있지 않으면(and 연결) 출력
