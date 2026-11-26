#전화번호 목록
# 정렬을 통해 앞자리가 같은 경우를 확인하는 방식으로 구현
# 정렬 후 인접한 요소들만 비교하면 끝

def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)-1):
        word1 = phone_book[i]
        word2 = phone_book[i+1]

        if word1 == word2[:len(word1)]:
            return False

    
    return True

#startwidth를 이용한 방법
def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return True


if __name__ == "__main__":
    # 테스트 케이스 1
    print("테스트 케이스 1")
    phone_book = ["119", "97674223", "1195524421"]

    result = solution(phone_book)
    print(result)  # False


    # 테스트 케이스 2
    print("테스트 케이스 2")
    phone_book = ["123", "456", "789"]

    result = solution(phone_book)
    print(result)  # True


    # 테스트 케이스 3
    print("테스트 케이스 3")
    phone_book = ["12", "123", "1235", "567", "88"]

    result = solution(phone_book)
    print(result)  # False