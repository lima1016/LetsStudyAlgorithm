# 내 풀이
# arry = [3, 5, 6, 1 , 2, 4]
# arry.sort()
# print(arry[-1])

# 선생님 풀이
# 1. 하나의 원소를 다른 원소들과 비교해서 최대값인지 분석하는 방법.
# 2. 하나의 변수를 잡아서 그 변수와 비교하며 가장 큰 수를 찾는 방법.
# def find_max_num(array):
  # 이 부분을 채워보세요!
  # array.sort()
  # return array[-1]

def find_max_num(array):
  max_num = array[0]
  for e in array:
    if e > max_num:
      max_num = e
  return max_num


print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))