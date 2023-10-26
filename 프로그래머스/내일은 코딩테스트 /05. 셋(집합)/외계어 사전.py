def solution(spell, dic):
    for word in dic:
        all = True
        for w in spell:
            if w not in word:
                all = False
              
        if all == True:
            return 1
    
    return 2
  
# 어렵지는 않지만 set()을 어디서 써야할지 모르겠음
