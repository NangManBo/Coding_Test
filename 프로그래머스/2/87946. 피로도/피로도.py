from itertools import permutations

def solution(k, dungeons):
    answer = 0
    arr = []
    for words in permutations(dungeons) :
        # 모든 경우의 수 돌기 k는 계속 초기화 해줄 것
        life = k
        count = 0
        # ex) [[80,20], [50,40], [30,10]]
        for word in words :
            if word[0] <= life : 
                life -= word[1]
                count += 1
        arr.append(count)
    
    answer = max(arr)
    return answer