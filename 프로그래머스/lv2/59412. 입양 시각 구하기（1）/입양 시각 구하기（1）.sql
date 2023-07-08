-- 코드를 입력하세요
SELECT date_format(datetime, '%H') as hour, count(animal_id) as count
from animal_outs
group by hour
having hour between 9 and 19
order by hour