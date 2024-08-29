function solution(num_list, n) {
    return Array.from({length:n},(_, i) => num_list[i]);
}