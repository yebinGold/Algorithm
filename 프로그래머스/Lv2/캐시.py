# 2018 KAKAO BLIND RECRUITMENT
def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower()
        
        # cache hit
        if city in cache:
            cache.remove(city); cache.append(city)
            answer += 1
        
        # cache miss
        else:
            if len(cache) == cacheSize:
                cache.pop(0)
            
            cache.append(city)
            answer += 5
    
    return answer


"""

찾는 도시 이름이 캐시에 저장되어 있다면 그대로 가져오고 +1

캐시에 없다면 데이터베이스에서 가져온 후 캐시에 해당 이름을 새롭게 저장하고 +5
이때 만약 캐시가 꽉 차 있다면 맨 앞(가장 최근에 참조되지 않은) 데이터를 삭제해서 공간을 만든다. 

캐시 교체 알고리즘 (LRU) 적용을 위해
cache hit의 경우에도 캐시에서 해당 도시 이름을 삭제하고 다시 맨 뒤로 보내준다.

"""
