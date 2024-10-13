class Solution {
    fun solution(s: String): String {
        return s.split(" ").map { it.toInt() }.let { "${it.minOrNull()} ${it.maxOrNull()}" }
    }
}