function solution(num_list, n) {
    var len = num_list.length;
    return Array.from({length : len},(_,i)=> num_list[(i+n) % len]);
}