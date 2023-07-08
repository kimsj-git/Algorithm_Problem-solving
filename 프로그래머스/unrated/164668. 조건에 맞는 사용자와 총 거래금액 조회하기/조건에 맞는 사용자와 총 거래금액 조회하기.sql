-- 코드를 입력하세요
SELECT a.user_id, a.nickname, sum(b.price) as total_sales
from used_goods_user a
join used_goods_board b on a.user_id = b.writer_id
where b.status = 'DONE'
group by a.user_id
having sum(b.price) >= 700000
order by total_sales