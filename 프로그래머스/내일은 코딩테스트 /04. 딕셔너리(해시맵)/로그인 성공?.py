def solution(id_pw, db):
    [id, pw] = id_pw
    
    for [corr_id, corr_pw] in db:
        if id == corr_id and pw == corr_pw:
            return 'login'
        if id == corr_id and pw != corr_pw:
            return 'wrong pw'
    
    return 'fail'
