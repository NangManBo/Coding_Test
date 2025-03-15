class Solution {
    public String[] solution(String[] names) {
        int len = (int) names.length / 5 + 1;
        if(names.length % 5 == 0) {
            len = (int) names.length / 5;
        }
        
        String[] answer = new String[len];
        
        for(int i = 0; i < len; i++){
            answer[i] = names[i * 5];
        }
        return answer;
    }
}