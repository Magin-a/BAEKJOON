# #sol1
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()

#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]

#     return participant[-1]

# #sol1 미완주자가 여러명인 경우
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()

#     answer = []

#     i = 0  # participant 인덱스
#     j = 0  # completion 인덱스

#     while i < len(participant):
#         if j >= len(completion):
#             answer.extend(participant[i:])
#             break

#         if participant[i] == completion[j]:
#             i += 1
#             j += 1
#         else:
#             answer.append(participant[i])
#             i += 1

#     return answer


#sol2
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# Comment
# Counter는 딕셔너리 형태로 값을 저장함. 이를 서로 빼면, participant에만 있는 값이 남게 됨.
# 딕션너리의 키값이 0이면, 그 키값은 삭제됨. 따라서 0인 키값을 살려서 보고싶으면 subtract를 사용


if __name__ == "__main__":

    # 테스트 케이스 1
    print("테스트 케이스 1")
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]

    result = solution(participant, completion)
    print(result)  # leo


    # 테스트 케이스 2
    print("테스트 케이스 2")
    participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
    completion = ["josipa", "filipa", "marina", "nikola"]

    result = solution(participant, completion)
    print(result)  # vinko


    # 테스트 케이스 3
    print("테스트 케이스 3")
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["ana", "mislav"]

    result = solution(participant, completion)
    print(result)  # mislav