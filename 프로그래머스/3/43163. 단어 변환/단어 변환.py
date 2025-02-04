from collections import deque

def check(w1, w2) :
    count = 0
    for a, b in zip(w1, w2) :
        if(a != b) :
            count += 1
    
    if(count == 1) :
        return 1
    else :
        return 0

def solution(begin, target, words):    
    queue = deque([(begin,0)])
    visit = set()
    while queue :
        current, count = queue.popleft()
        
        if(current == target) :
            return count
        
        for word in words :
            if(word not in visit and check(word,current) == 1) :
                queue.append((word, count + 1))
                visit.add(word)
                
    return 0