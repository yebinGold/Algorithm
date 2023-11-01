def solution(array):
    if len(set(array)) == 1:
        return array[0]
    
    most_freq = 0
    counts = []
    for x in set(array):
        c = array.count(x)
        most_freq = max(most_freq, c)
        counts.append((x, c))
        
    counts.sort(key=lambda x: x[1], reverse=True)
    if counts[1][1] == most_freq:
        return -1
            
    return counts[0][0]
