# 입력을 받고 (디테일)

# Default input 스트링 타입, 문자열 타입으로 받아와주도록 만들어짐!

# 배열!
# list = [0, 0, 0, 0]
# list = ["hello", "world", "python", "java"]

# Case 1 : 단순히 정수 일 때,
# number = int(input())

# Case 2 : 수열!
# First, Second, Third = map(int, input().split())
list1 = list(map(int, input().split()))

# 괄호 없이 [1, 2, 3, 4, 5, 6, 7] 안에있는 내용만 출력하고싶으면 *를 붙이면됨
print(*list1)

# Case 3 : 단순히 문자 일 때,
# string = input()

# Case 4 : 문자열

list2 = list(map(str, input().split()))
print(list2)

# 계산을 하고


# 출력을 한다.
# print(number + number)
# print(string + string)
