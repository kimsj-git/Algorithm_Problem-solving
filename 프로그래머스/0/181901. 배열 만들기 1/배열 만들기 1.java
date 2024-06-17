class Solution {
    public int[] solution(int n, int k) {
        int count = n / k;
        int[] answer = new int[count];
        
        for (int i = 1; i * k <= n; i++) {
            answer[i-1] = i * k;
        }
        return answer;
    }
}