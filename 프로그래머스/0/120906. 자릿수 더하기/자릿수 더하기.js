function solution(n) {
    var num = n;
    var len = n.toString().length;
    var answer = 0;
    for(var i = 0; i<len; i++){
        answer += num % 10;
        num = Math.floor(num / 10);
    }
    return answer;
}