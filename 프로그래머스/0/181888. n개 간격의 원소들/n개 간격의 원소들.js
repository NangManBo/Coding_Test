function solution(num_list, n) {
    var i =0;
    var anwser = [];
    num_list.map((num,index)=>{
        if(index % n === 0){
            anwser[i] = num;
            i++;
        }            
    });
    return anwser;
}