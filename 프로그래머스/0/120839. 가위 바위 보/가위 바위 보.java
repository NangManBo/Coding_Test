class Solution {
    public String solution(String rsp) {
        String[] answer = new String[rsp.length()];
        
        for (int i = 0; i < rsp.length(); i++){
            if(rsp.charAt(i) == '2'){
                answer[i] = "0";
            }
            else if(rsp.charAt(i) == '0'){
                answer[i] = "5";
            }
            else if(rsp.charAt(i) == '5'){
                answer[i] = "2";
            }
        }
        return String.join("", answer);
    }
}