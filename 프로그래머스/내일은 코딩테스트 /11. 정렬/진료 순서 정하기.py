def solution(emergency):
    emer = [(i, e) for i, e in enumerate(emergency)] # 현재 위치 index 마크
    emer.sort(key = lambda x: x[1], reverse=True) # 응급도 기준 내림차순 정렬
    orders = [(order + 1, i) for order, (i, _) in enumerate(emer)] # 응급도 순으로 순서 기록
    
    # 초기 index 기준으로 재정렬하여 진료 순서만 return
    return [order for (order, _) in sorted(orders, key = lambda x: x[1])]
