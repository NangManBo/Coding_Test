class Solution {
    public int solution(int slice, int n) {
        int answer = (int) n / slice;
        
        if(n % slice > 0) {
            answer += 1;
        }
        return answer;
    }
}