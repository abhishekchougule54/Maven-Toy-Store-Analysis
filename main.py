#importing libraries
from sqlalchemy import create_engine
import pandas as pd

#reading csv files
df_inventory=pd.read_csv('F:/0_Fun Projects/06_MavenAnalytics_Toy_sales/Dataset/Maven Toys Data/inventory.csv')
df_products=pd.read_csv('F:/0_Fun Projects/06_MavenAnalytics_Toy_sales/Dataset/Maven Toys Data/products.csv')
df_sales=pd.read_csv('F:/0_Fun Projects/06_MavenAnalytics_Toy_sales/Dataset/Maven Toys Data/sales.csv')
df_stores=pd.read_csv('F:/0_Fun Projects/06_MavenAnalytics_Toy_sales/Dataset/Maven Toys Data/stores.csv')

#cleaning/transformation
df_products['Product_Price'] = df_products['Product_Price'].str.replace('$', '')
df_products['Product_Cost'] = df_products['Product_Cost'].str.replace('$', '')
df_products = df_products.astype({"Product_Price": float,"Product_Cost": float})
df_sales = df_sales.astype({"Units": int})

#merging datasets to create a  table with all the required values
sales_revenue_per_product = pd.merge(df_products, df_sales, on=['Product_ID'])
sales_revenue_per_product = pd.merge(sales_revenue_per_product,df_stores, on=['Store_ID'])
sales_revenue_per_product.drop('Store_Open_Date', axis=1, inplace=True)

#renaming columns for standardization
rename_cols_dict =  {'Product_ID':'product_id',
 'Product_Name':'product_name', 
 'Product_Category':'product_category',
 'Product_Cost':'product_purchase_price', 
 'Product_Price':'product_selling_price',
 'Sale_ID':'sale_id', 
 'Date':'sale_date', 
 'Store_ID':'store_id', 
 'Units':'product_units_sold', 
 'Store_Name':'store_name', 
 'Store_City':'store_city', 
 'Store_Location':'store_location'}
sales_revenue_per_product.rename(columns=rename_cols_dict,inplace=True)

#addition of calculated columns
sales_revenue_per_product['revenue_generated_per_product'] = sales_revenue_per_product['product_selling_price'] * sales_revenue_per_product['product_units_sold']
sales_revenue_per_product['profit_generated_per_product'] = (sales_revenue_per_product['product_selling_price'] - sales_revenue_per_product['product_purchase_price']) * sales_revenue_per_product['product_units_sold']

#storing the dataset to postgres table
engine = create_engine('postgresql://postgres:root@localhost:5432/maven_toystore')
sales_revenue_per_product.to_sql('sales_revenue_per_product', engine,if_exists='append', index=False)
