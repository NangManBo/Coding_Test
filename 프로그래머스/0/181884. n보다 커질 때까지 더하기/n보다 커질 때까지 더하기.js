function solution(numbers, n) {
    return numbers.reduce((sum,num)=>(sum<=n)?sum+num:sum)
}