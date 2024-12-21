# 문자열이 알파벳인지 확인할 수 있음
# print('a'.isalnum())
# 아스키 코드 형태로 바꿀 수 있음
# print(ord('a'))
# 아스키 코드 값을 넣어주면 chr은 문자로 바꿔줌
# print(chr(97))

# 다음과 같은 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오
def find_max_occurred_alphabet(string):
  # 이 부분을 채워보세요!
  alphabet_occurrence_array  = [0] * 26
  return "a"


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))