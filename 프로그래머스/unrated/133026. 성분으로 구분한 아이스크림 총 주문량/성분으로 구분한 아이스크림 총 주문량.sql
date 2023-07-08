-- 코드를 입력하세요
SELECT b.ingredient_type, sum(total_order) as total_order
from first_half a
join icecream_info b on a.flavor = b.flavor
group by b.ingredient_type
order by total_order