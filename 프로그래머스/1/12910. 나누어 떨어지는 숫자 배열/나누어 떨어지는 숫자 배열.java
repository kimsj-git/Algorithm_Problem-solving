import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        
        ArrayList<Integer> arrayList = new ArrayList<>();
        for (int num: arr) {
            if (num % divisor == 0) {
                arrayList.add(num);
            }
        }
        
        Collections.sort(arrayList);
        
        int[] answer = new int[arrayList.size()];
        for (int i = 0; i < arrayList.size(); i++) {
            answer[i] = arrayList.get(i);
        }
        
        if (answer.length > 0) return answer;
        else return new int[]{-1};
    }
}