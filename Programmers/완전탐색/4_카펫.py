from math import isqrt


def solution(brown, yellow):
    total = brown + yellow

    for height in range(3, isqrt(total) + 1):
        if total % height != 0:
            continue

        width = total // height
        if (width - 2) * (height - 2) == yellow:
            return [width, height]


if __name__ == "__main__":
    # 테스트 케이스 1
    print("테스트 케이스 1")
    brown = 22
    yellow = 14
    result = solution(brown, yellow)
    print(result)

    print("테스트 케이스 2")
    brown = 8
    yellow = 1
    result = solution(brown, yellow)
    print(result)

    print("테스트 케이스 3")
    brown = 18
    yellow = 6
    result = solution(brown, yellow)
    print(result)
