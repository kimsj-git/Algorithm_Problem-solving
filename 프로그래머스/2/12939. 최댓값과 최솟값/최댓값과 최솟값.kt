class Solution {
    fun solution(s: String): String {
        val nums = s.split(" ").map { it.toInt() }
        val minNum = nums.minOrNull()
        val maxNum = nums.maxOrNull()
        return "$minNum $maxNum"
    }
}