def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == s1[i % len(s1)]:
            score[0] += 1
        if answers[i] == s2[i % len(s2)]:
            score[1] += 1
        if answers[i] == s3[i % len(s3)]:
            score[2] += 1

    max_score = max(score)
    
    for i, s in enumerate(score):
        if s == max_score:
            answer.append(i + 1)
    return answer

if __name__ == "__main__":
    # 테스트 케이스 1
    print("테스트 케이스 1")
    answers = [1, 2, 3, 4, 5]
    result = solution(answers)
    print(result)

    print("테스트 케이스 2")
    answers = [1, 3, 2, 4, 2]
    result = solution(answers)
    print(result)
