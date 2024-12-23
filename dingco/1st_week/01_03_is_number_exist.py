#  다음과 같은 숫자로 이루어진 배열이 있을 때, 이 배열 내에 특정 숫자가 존재한다면 True,
#  존재하지 않다면 False 를 반환하시오.
# [3, 5, 6, 1, 2, 4]

def is_number_exist(number, array):
  # 이 부분을 채워보세요!
  for e in array:   # array 의 길이만큼 아래 연산 실행
    if e == number: # 비교 연산 1번 실행
      return True   # 시간 복잡도는 N만큼 걸린다.
  return False


result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3, 5, 6, 1, 2, 4]))
print("정답 = Flase 현재 풀이 값 =", result(7, [6, 6, 6]))
print("정답 = True 현재 풀이 값 =", result(2, [6, 9, 2, 7, 1888]))

# 빅오 -> 최악의 경우.
# 빅오메가 -> 최선의 경우

# 1. 입력값에 비례해서 얼마나 늘어날지 파악해보자. 1 ? $N ? N^2 ?
# 2. 공간복잡도 보다는 시간 복잡도를 더 줄이기 위해 고민하자.
# 3. 최악의 경우에 시간이 얼마나 소요될지(빅오 표기법)에 대해 고민하자