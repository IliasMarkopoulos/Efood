select user_id, sum(basket) as total_amount, avg(basket) as avg_amount, count(order_id) as Breakfast_orders, 
count(CAST(submit_dt AS DATE)) as no_days, sum(basket)/count(order_id) as amount_per_order

from  `bi-2019-test.ad_hoc.orders_jan2021`
where cuisine_parent = 'Breakfast'
group by user_id
