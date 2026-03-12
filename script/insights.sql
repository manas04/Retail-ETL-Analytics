-- #########################################
-- ----------- Data Analysis ---------------
-- #########################################

-- reviewing data from train table
select * from train limit 10;

-- reviewing data from transactions table
select * from transactions t  limit 10;

-- reviewing data from stores table
select * from stores limit 10;



-- Product Category wise sales and on promotional values from train data

select family, round(sum(sales),2) as total_sales, round(sum(onpromotion),2) as onpromotion_items
from train
group by family
order by total_sales desc;

-- State Wise total sales in descending order 
select s.state, count(distinct s.store_nbr) as store_count, 
round(sum(t.sales),2) as total_sales
from train as t 
join stores as s
on t.store_nbr  = s.store_nbr
group by s.state 
order by total_sales desc;


-- City Wise total sales in descending order 
select s.city, round(sum(t.sales),2) as total_sales
from train as t 
join stores as s
on t.store_nbr  = s.store_nbr
group by s.city
order by total_sales desc;

-- Grouping by state first and then city with total sales in descending order
select s.state, s.city, round(sum(t.sales),2) as total_sales
from train as t 
join stores as s
on t.store_nbr  = s.store_nbr
group by s.state, s.city
order by total_sales desc;

-- Top 10 performing stores by sales
select t.store_nbr, s.state, s.city, round(sum(t.sales),2) as total_sales
from train as t
join stores as s 
on t.store_nbr = s.store_nbr
group by t.store_nbr, s.state, s.city
order by total_sales desc
limit 10;

-- Monthly sales trends
select date_trunc('month', date) as sales_month, round(sum(sales),2) from train
group by sales_month;

-- Promoted and non-promoted sales
with promotion_cte as(
select *, 
case when onpromotion > 0 then 'Promoted'
else 'Not promoted'
end as promotion_flag
from train
)

select promotion_flag, count(*) as total_records, 
round(avg(sales)) as avg_sales, 
round(sum(sales),2) as total_sales
from promotion_cte
group by promotion_flag
order by total_sales desc;

-- Sales lift due to products on promotion

select family,
round(avg(case when onpromotion > 0 then sales end),2) as avg_sales_promoted,
round(avg(case when onpromotion = 0 then sales end),2) as avg_sales_not_promoted,
round(
avg(case when onpromotion > 0 then sales end) - avg(case when onpromotion = 0 then sales end)
,2)as sales_lift
from train
group by family
ORDER BY sales_lift DESC NULLS LAST;









