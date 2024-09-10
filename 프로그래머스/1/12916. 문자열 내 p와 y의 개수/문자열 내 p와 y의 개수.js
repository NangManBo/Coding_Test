function solution(s){
    var p = s.match(/p/g)?.length;
    var P = s.match(/P/g)?.length;
    var y = s.match(/y/g)?.length;
    var Y = s.match(/Y/g)?.length;
    
    var sumP = 0;
    var sumY = 0;
    
    if(p == undefined){
        sumP = P;
    }
    else if(P == undefined)
    {
        sumP = p;
    }
    else 
        sumP = p+P;
    
    if(y == undefined){
        sumY = Y;
    }
    else if(Y == undefined)
    {
        sumY = y;
    }
    else 
        sumY = y+Y;
    console.log(p,P,y,Y)
    console.log(sumP, sumY);
    return (sumP == sumY) ? true : false;
}