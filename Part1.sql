select count(distinct order_id) as Breakfast_Orders, 
count(distinct user_id) as Breakfast_Users,
avg(basket) as avg_basket,
a.city
from

(select *
from  `bi-2019-test.ad_hoc.orders_jan2021`
where cuisine_parent = 'Breakfast'
)a
inner join
(select city, count(order_id) as no_orders_cities
from  `bi-2019-test.ad_hoc.orders_jan2021`
GROUP BY city
having no_orders_cities >=500
)c
on a.city = c.city
group by city
order by Breakfast_Orders desc 
limit 10