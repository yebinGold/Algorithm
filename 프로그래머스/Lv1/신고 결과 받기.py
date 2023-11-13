def solution(id_list, report, k):
    reports = {} # 신고당한 사람: [신고한 사람 list]
    
    # 중복 신고 제외하고 신고 명단 정리
    for r in set(report):
        reporting, reported = r.split(" ") # 신고한 사람, 신고당한 사람
        if reported in reports:
            reports[reported].append(reporting)
        else:
            reports[reported] = [reporting]
    
    # 신고 횟수 >= k인 list만 뽑아서 1차원 배열로 저장
    results = []
    for _, report in reports.items():
        if len(report) >= k: results += report
    
    # id_list에 저장된 순서대로 신고자 이름 count (= 이메일 보낼 횟수)
    answer = []
    for id in id_list:
        answer.append(results.count(id))

    return answer
