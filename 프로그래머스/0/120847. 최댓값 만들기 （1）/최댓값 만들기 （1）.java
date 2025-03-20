class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        int max = 0;
        int sec_max= 0;
        int ind = 0;
        
        // 최댓값과 그 다음 최댓값 찾기
        for (int i =0; i< numbers.length; i++){
            //여기서 최댓값 찾기
            if(numbers[i] > max){
                max = numbers[i];
                ind = i;
            }
        }
        System.out.print(ind);
        for (int i = 0; i<numbers.length; i++){
            if(i != ind && numbers[i] > sec_max){
                sec_max = numbers[i];
            }
        }
       answer = max * sec_max;
        
        return answer;
    }
}