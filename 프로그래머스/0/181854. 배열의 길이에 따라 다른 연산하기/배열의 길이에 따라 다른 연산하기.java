class Solution {
    public int[] solution(int[] arr, int n) {
        int[] answer = new int[arr.length];
        
        for (int i = 0; i < arr.length; i++) {
            if (arr.length % 2 == 1) {
                answer[i] = arr[i] + (i % 2 == 0 ? n : 0);
            } else {
                answer[i] = arr[i] + (i % 2 == 1 ? n : 0);
            }
        }
        
        return answer;
    }
}