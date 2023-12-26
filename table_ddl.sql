CREATE TABLE IF NOT EXISTS sales_revenue_per_product
(
	sale_id int,
	store_id  int ,
	store_name varchar(250),
	store_city varchar(250),
	store_location varchar(250),
	sale_date date,
    product_id int,
	product_name varchar(250),
	product_category varchar(250),
	product_purchase_price NUMERIC(6, 2),
	product_selling_price NUMERIC(6, 2), 
    product_units_sold int,
	revenue_generated_per_product NUMERIC(6, 2),
	profit_generated_per_product NUMERIC(6, 2)
)