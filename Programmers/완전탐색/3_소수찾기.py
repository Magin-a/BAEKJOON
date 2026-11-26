from itertools import permutations
# i 자릿수로 숫자 조합 생성

def solution(numbers):
    answer = 0
    total = set()
    
    for i in range(1, len(numbers) + 1):
        for comb in permutations(numbers, i):
            target = ''
            for i in comb:
                target += i
            total.add(int(target))
    print(total)
    for num in total:
        trg = 0
        if num < 2:
            continue
        for i in range(2, num):
            if num % i == 0:
                trg = 1
                break
        if not(trg):
            answer += 1
        print(num)
    
    return answer

# #SOl2 백트래킹 (길이 k인 순열을 만드는 함수)
# def solution(numbers):
#     n = list(numbers)
#     perm = []

#     for k in range(len(n) +1):
#         perm += makeperm(n, k)

#     perm_int = [int(i) for i in perm]
#     perm_set = set(perm_int)
#     print(perm_set)

#     count =0
#     for s in perm_set:
#         if checkprime(s):
#             count +=1
#     return count


# def makeperm(s, k):
#     if k == 0:
#         return []  # 정수로 변환할 후보가 없는 길이
#     if k == 1:
#         return s

#     result = []
#     for i, digit in enumerate(s):
#         remaining = s[:i] + s[i + 1:]
#         for tail in makeperm(remaining, k - 1):
#             result.append(digit + tail)
#     return result


# def checkprime(n):
#     if n < 2:
#         return False

#     divisor = 2
#     while divisor * divisor <= n:
#         if n % divisor == 0:
#             return False
#         divisor += 1
#     return True


if __name__ == "__main__":
    # 테스트 케이스 1
    print("테스트 케이스 1")
    numbers = "17"
    result = solution(numbers)
    print(result)

    print("테스트 케이스 2")
    numbers = "011"
    result = solution(numbers)
    print(result)
