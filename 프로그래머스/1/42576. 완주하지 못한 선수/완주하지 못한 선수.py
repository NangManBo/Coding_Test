def solution(participant, completion):
    answer =''
    graph = {}
    # dict를 사용해서 해당 이름을 가진사람이 몇명인지 하고 만약에 없으면 우선 1
    for i in participant :
        if i in graph : graph[i] += 1
        else : graph[i] = 1
    
    for j in completion :
        graph[j] -= 1
    
    for i in graph :
        if(graph[i] == 1) :
            answer = i
    return answer