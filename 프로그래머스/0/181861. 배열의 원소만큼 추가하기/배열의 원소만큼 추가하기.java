import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr) {
        int sum = Arrays.stream(arr).sum();
        int[] answer = new int[sum];
        
        int i = 0;
        for (int n: arr) {
            for (int j = 0; j < n; j++) {
                answer[i + j] = n; 
            }
            i += n;
        }
        
        return answer;
    }
}