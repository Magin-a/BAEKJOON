def solution(sizes):

    card_size = sorted ([sorted(size) for size in sizes])
    print(card_size)
    max_width = max([size[0] for size in card_size])
    max_height = max([size[1] for size in card_size])
    answer = max_width * max_height
    return answer

if __name__ == "__main__":
    # 테스트 케이스 1
    print("테스트 케이스 1")
    sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

    result = solution(sizes)
    print(result)

    # 테스트 케이스 2
    print("테스트 케이스 2")
    sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]

    result = solution(sizes)
    print(result) 

    # 테스트 케이스 3
    print("테스트 케이스 3")
    sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

    result = solution(sizes)
    print(result)