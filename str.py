# 한 줄 문자열 정의
s = ''
str1 = 'hello world'
str2 = "hello world"
print(type(s), type(str1), type(str2))

# 여러줄 문자열 정의
str3 = """ABC
DEF
가나다라마바사
아자차카타파하
"""
print(str3)

# 여러줄 주석
# 여러줄 문자열 사용 / 객체는 생성되지만, 일시적인 생성임.
"""
주석1
주석2
주석3
"""

# escape
print('hello\nworld\nI say \"Hello World\"')

#
# 문자열 연산
#

str1 = "First String"
str2 = "Second String"

# 1. 인덱싱

print(str1[0], str1[2], str1[4])

# 2. 슬라이싱
str3 = str2[2:5] # [2: ] :아무것도 없으면 2~끝까지 범위로 간주.
print(str3)
print(str2[2:])

# 3. 연결(+), + 생략 가능하담(단, 리터럴일 때)
print(str1 + " " + str2)
print("First String" "" "Second String")

# 주의. 문자열 객체와 정수형 객체는 "+(연결)" 연산을 할 수 없음.
name = "길동"
age = 40
# print("->1")
# print(name + 40)
# print("->2")
print(name + str(40))

# 4. 반복(*)
print(str1*3)

# len 함수
print(len(str2))

# in, not in
print("S" in str2)
print("S" not in str2)

# 문자열 객체는 변경할 수 없다(immutable). 시퀀스와 관계없음.
# str1[0] = "F"

# 서식(formatting) - format() 함수
print("name : " + name + " age : " + format(age, "d"))
print("name : " + format(name, "s") + " age : " + format(age, "d"))

# 튜플을 이용한 서식 (별 5개) - 튜플로 들어온 데이터를 하기와 같이 출력
f = "name : %s, age : %d"
print(f % (name, age))
print("name : %s, age : %d" % (name, age))

# cf C 스타일
# printf("name : %s, age : %d", name, age)

# 서식 - 딕셔너리를 이용한 포맷팅 - 딕셔너리로 들어온 데이터를 하기와 같이 출력
f = "name : %(n)s, age : %(a)d"
print(f % {"n" : "둘리", "a" : 30})
print(f % {"n" : "마이콜", "a" : 20})