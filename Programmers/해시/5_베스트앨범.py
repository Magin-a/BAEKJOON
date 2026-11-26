def solution(genres, plays):
    result = []
    for i in range(len(plays)):
        plays[i] = (plays[i], i)

    genre_dict = {}
    for i in range(len(genres)):
        if genres[i] not in genre_dict:
            genre_dict[genres[i]] = [plays[i]]
        else:
            genre_dict[genres[i]].append(plays[i])

    genre_dict = dict(sorted(genre_dict.items(), key=lambda x: sum([play[0] for play in x[1]]), reverse=True))
    print(genre_dict)
    for genre, play_list in genre_dict.items():
        # print(f"장르: {genre}, 재생횟수: {play_list}")
        play_list.sort(key=lambda x: (-x[0], x[1]))# 재생횟수는 내림차순, 고유번호는 오름차순
        # result.extend([play[1] for play in play_list[:2]])
        for paly in play_list[:2]:
                result.append(paly[1])
    return result



if __name__ == "__main__":

    # 테스트 케이스 1
    print("테스트 케이스 1")
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    result = solution(genres, plays)
    print(result) 