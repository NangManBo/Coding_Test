function solution(n) {
    
    return Array.from({length : (n % 2 == 0 ) ? Math.floor(n / 2) : Math.floor(n / 2) + 1}
                      ,(_,i)=> i * 2 + 1);
}