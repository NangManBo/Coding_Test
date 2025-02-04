def cal_date(date) :
    year, month, day = map(int,date.split('.'))
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    answer = []
    
    dictionary = {}
    for term in terms :
        rank, m = term.split(' ')
        # 만료일 {} rank에 맞게 등록
        dictionary[rank] = int(m) * 28
        
    today_ = cal_date(today)
    
    for idx, pri in enumerate(privacies, start = 1) :
        date, r = pri.split(' ')
        # 정책 시작일과 정책 랭크 일수 더하기
        p_date = cal_date(date) + dictionary[r] - 1
        
        if(today_ > p_date) :
            answer.append(idx) 
            
        
    return answer