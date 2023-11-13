from collections import deque

def solution(priorities, location):
    run = 0
    priorities = deque([(p, i) for i, p in enumerate(priorities)])
    
    while True:
        p, i = priorities.popleft()
        # 만약 우선순위가 더 높은 프로세스가 있다면
        if any(p < pr for (pr, pi) in priorities):
            priorities.append((p, i))
            continue
        # 없다면 방금 꺼낸 프로세스 실행
        run += 1
        # 찾고자 하는 프로세스가 실행되었다면
        if i == location:
            return run

    return run
