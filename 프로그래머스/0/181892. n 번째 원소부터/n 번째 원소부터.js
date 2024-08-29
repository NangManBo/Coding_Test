function solution(num_list, n) {
   return Array.from({length : num_list.length - n + 1},(_,i)=> num_list[n-1+i]);
}