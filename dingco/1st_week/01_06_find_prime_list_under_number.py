# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.
# 20이 입력된다면, 아래와 같이 반환해야 합니다!
# [2, 3, 5, 7, 11, 13, 17, 19]

# 내 풀이
# def find_prime_list_under_number(number):
#     # 이 부분을 채워보세요!
#     result = []
#     for i in range(2, number):
#         if i == 2:
#             result.append(i)
#         elif number % i != 0 and i > 2 and i % 2 != 0:
#             result.append(i)
#     return result

# for x in [1,2,3,4]:
# else: for문이 끝나고 무조건 호출 근데 for문 안에 if가 있으면 호출 X

# 소수는 자기 자신과 1외 에는 아무것도 나눌 수 없다.
# 선생님 풀이 (효율적인 방법이 X)
def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    prime_list = []

    # 2 ~ 20 까지 찾아서 이것들이 소수인가? 소수라면 prime_list에 넣어라
    for n in range(2, number + 1):  # 2 ~ n 까지의 숫자들이 n에 들어가는 것을 반복한다.
        # for i in range(2, n):     # 2 부터 n - 1 까지를 i에 들어가는 것을 반복한다.
        for i in prime_list:        # 새로 추가
            # if n % i == 0:        # n = 2, 3, 4, ... 20
            if i * i <= n and n % i == 0:          # 새로 추가 모든 연산 필요없이 2, 3, 5 까지만 해도 된다.
                break               # 소수가 아님 / n = 2 i = x -> 얘는 아무일도 안일어나고 for문 들어감
        else:                       # n = 4 i = 3, 2 -> break 문이 수행되게 되면, for else 의 else가 실행되지 않는다. prime_list에 들어가지 않음
            prime_list.append(n)    # for문에서 아무일도 일어나지 않았다면 n은 소수이다.
    return prime_list



result = find_prime_list_under_number(20)
print(result)