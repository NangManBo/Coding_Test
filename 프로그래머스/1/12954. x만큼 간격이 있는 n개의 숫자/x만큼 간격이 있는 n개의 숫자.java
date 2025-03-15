import java.util.*;
class Solution {
    public long[] solution(int x, int n) {
        long[] list = new long[n];
        
        for(int i = 0; i < n ; i++){
            list[i] = (long)(i + 1) * x;
        }
        return list;
    }
}