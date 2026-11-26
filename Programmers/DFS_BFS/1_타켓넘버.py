def solution(numbers, target):
    answer = 0
    # DFS를 사용하여 모든 가능한 경우의 수를 탐색
    for i in range(2 ** len(numbers)):
        total = 0
        for j in range(len(numbers)):
            # i의 j번째 비트가 1이면 numbers[j]를 더하고, 0이면 빼기
            if (i & (1 << j)) > 0:
                total += numbers[j]
            else:
                total -= numbers[j]
        # 최종 합이 target과 같으면 answer 증가
        if total == target:
            answer += 1
    return answer

def solution(numbers, target): 
    answer = 0
    
    def dfs(idx, total):
        nonlocal answer
        
        if idx == len(numbers):
            if total == target:
                answer += 1
            return
        
        dfs(idx + 1, total + numbers[idx])
        dfs(idx + 1, total - numbers[idx])
    
    dfs(0, 0)
    return answer



if __name__ == "__main__":
    # 테스트 케이스 1
    print("테스트 케이스 1")
    numbers = [1, 1, 1, 1, 1]
    target = 3
    result = solution(numbers, target)
    print(result)

    # 테스트 케이스 2
    print("테스트 케이스 1")
    numbers = [4, 1, 2, 1]
    target = 4
    result = solution(numbers, target)
    print(result)