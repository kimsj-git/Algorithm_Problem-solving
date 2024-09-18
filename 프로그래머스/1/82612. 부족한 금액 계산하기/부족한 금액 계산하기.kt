class Solution {
    fun solution(price: Int, money: Int, count: Int): Long {
        val totalCost = (1..count).map { it.toLong() * price }.sum()      
        return if (totalCost > money) totalCost - money else 0L
    }
}