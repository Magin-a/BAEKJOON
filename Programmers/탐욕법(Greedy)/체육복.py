def solution(n, lost, reserve):
    # 여벌 체육복이 있는 학생이 도난당한 경우 처리
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)

    for i in reserve_set:
        if i-1 in lost_set:
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)

    answer = n - len(lost_set)
    return answer


if __name__ == "__main__":

    # 테스트 케이스 1
    print("테스트 케이스 1")
    n = 5
    lost = [2, 4]
    reserve = [1, 3, 5]

    result = solution(n, lost, reserve)
    print(result)  # 3