class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        int n = 0;
        int m = 0;
        if(a <= b) {
            n = a;
            m = b;
        }
        else {
            n = b;
            m = a;
        }
        for(int i = n; i < m + 1; i++){
            answer += i;
        }
        return answer;
    }
}