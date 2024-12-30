# Q.
# 0과 1로만 이루어진 문자열이 주어졌을 때, 이 문자열에 있는 모든 숫자를 전부 같게 만들려고 한다.
# 할 수 있는 행동은 문자열에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다.
# 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.
# 예를 들어 S=0001100 일 때,
# 전체를 뒤집으면 1110011이 된다.
# 4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다.
# 하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면
# 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.
# 주어진 문자열을 모두 0 혹은 모두 1로 같게 만드는 최소 횟수를 반환하시오.
# "0001100"

# 0 에서 1을 마주쳤을때 뒤집는다 -> 전체를 0으로 만들기 위한 작업
# 1 에서 0을 마주쳤을때 뒤집는다 -> 전체를 1으로 만들기 위한 작업
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    # 맨 처음 숫자는 뒤집지 안아서 이부분을 반영해줘야 한다.
    if string[0] == "0":
        count_to_all_one += 1       # 맨앞이 0이라면 0을 1로 뒤집는 숫자 추가
    elif string[0] == "1":
        count_to_all_zero += 1      # 맨앞이 1이라면 1을 0로 뒤집는 숫자 추가

    for i in range(len(string) - 1):        # i 는 0부터 문자열의 길이 -2 까지가 된다.
        if string[i] != string[i + 1]:      # 앞의 숫자와 뒤에 숫자가 다르다면
            if string[i + 1] == "1":
                count_to_all_zero += 1
            if string[i + 1] == "0":
                count_to_all_one += 1
    return min(count_to_all_zero, count_to_all_one)     # 최소값을 반환하는 함수 min()


input = "0001100"
result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)