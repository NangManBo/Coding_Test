function solution(x) {
    var len = x.toString().length;
    var num = x;
    var sum = 0;
    var i = 0;
    for(i; i < len; i++ ){
        sum += num % 10;
         num = Math.floor(num / 10);
        console.log(num, sum)
    }
    
   return (x % sum === 0) ? true : false; 
}