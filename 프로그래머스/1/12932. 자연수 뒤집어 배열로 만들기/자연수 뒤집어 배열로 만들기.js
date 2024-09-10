function solution(n) {
    return Array.from({length: n.toString().length},(_,i) => Math.floor((n % (10 ** (i+1))) / (10 ** (i))));
}