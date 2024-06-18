public class Solution {
    public int solution(int n) {
        int div = n / 10;
        int mod = n % 10;
        
        int sum = mod;
        while (div > 0) {
            mod = div % 10;
            sum += mod;
            div /= 10;
        }
        
        return sum;
    }
}