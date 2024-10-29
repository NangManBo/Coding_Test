n = input()


def main(n) -> int:

    
    for i in range(1, n+1) :
       result=0
       a=''
       number = list((map(str, input())))
       
       if((int(number[4]) == 0 and int(number[5]) == 0) or 
          (int(number[6]) == 0 and int(number[7]) == 0)) :
           result = 1
          
       elif (int(number[4]) > 3 | int(number[6])> 3) :
           result = 1
       elif(int(number[5]) == 2) :
           if(int(number[6]) ==2 and int(number[7]) >=9) :
                result = 1
           elif(int(number[6])==3 and int(number[7]) >= 0) :
               result = 1
       if(result == 1) :
           print(f'#{i} -1')
       else :
            number.insert(4,'/')
            number.insert(7,'/')
            anw = ''.join(number)
            print(f'#{i} {anw}')

main(int(n))
