select product_code, sum(price * sales_amount) as sales
from product join offline_sale using(product_id)
group by product_code
order by sales desc, product_code asc