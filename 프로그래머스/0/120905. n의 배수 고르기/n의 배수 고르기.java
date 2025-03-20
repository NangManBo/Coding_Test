import java.util.*;

class Solution {
    public ArrayList<Integer> solution(int n, int[] numlist) {
        ArrayList<Integer> list = new ArrayList<>();
        
        for (int i : numlist){
            if(i % n == 0){
                list.add(i);
            }
        }
        
        // int[] answer = list.toArray(new int[0]);
        // return Arrays.toString(answer);
        return list;
    }
}