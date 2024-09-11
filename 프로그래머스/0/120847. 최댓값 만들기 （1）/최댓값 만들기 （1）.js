function solution(numbers) {
    var len = numbers.length;
    
    numbers.sort(function(a,b){return a- b;})
    
    
    return numbers[len-1] * numbers[len-2];
}