def solution(players, callings):
    # 배열 인덱스를 참조하기 위한 딕셔너리
    index = {p: i for i, p in enumerate(players)} # player: index

    for name in callings:
        i = index[name]
        
        # players 배열에서 이름 순서 교환
        players[i-1], players[i] = players[i], players[i-1]
        # index 딕셔너리에 저장된 인덱스 교환
        index[players[i-1]], index[players[i]] = index[players[i]], index[players[i-1]]
    
    return players
