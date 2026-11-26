from collections import Counter

#sol1
def solution(clothes):
    result = 0
    sub = 1
    counter = Counter([kind for _, kind in clothes])
    if len(counter) == 1:
        return len(clothes)
    for value in counter.values():
        sub *= value

    return  sub + sum(counter.values())

#sol2
def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1

if __name__ == "__main__":
    test_cases = [
        ([["yellow_hat", "headgear"],
          ["blue_sunglasses", "eyewear"],
          ["green_turban", "headgear"]], 5),

        ([["crow_mask", "face"],
          ["blue_sunglasses", "face"],
          ["smoky_makeup", "face"]], 3)
    ]

    for i, (clothes, expected) in enumerate(test_cases, 1):
        result = solution(clothes)
        print(f"Test {i}: {result} | Expected: {expected} | {'PASS' if result == expected else 'FAIL'}")