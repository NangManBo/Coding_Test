def solution(answers):
    answer = []
    # 1, 2, 3, 4, 5
    # 2, 1, 2, 3, 2, 4, 2, 5
    # 3, 3, 1, 1, 2, 2, 4, 4, 5, 5
    arr = list(map(int,answers))
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    count = [0,0,0]
    for i in range(len(arr)) :
        if(arr[i] == a[i % 5]) :
            count[0] += 1
        if(arr[i] == b[i % 8]) :
            count[1] +=1
        if(arr[i] == c[i % 10]) :
            count[2] += 1
    
    max_count = max(count)
    for i in range(3) :
        if(max_count == count[i]) :
            answer.append(i+1)
        
    return answer