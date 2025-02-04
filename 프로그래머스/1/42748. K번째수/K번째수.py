def solution(array, commands):
    answer = []
    # i ~ j 번쨰 숫자까지 자르고 정렬
    for command in commands :
        l = []
        for i in range(command[0] - 1, command[1] ) :
            l.append(array[i])
        l.sort()
        print(l, command[2])
        answer.append(l[command[2]-1])
    return answer