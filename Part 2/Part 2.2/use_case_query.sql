select CustomerName, round(sum(SalesAmount),2) as SalesAmount, round(sum(SalesAmount)*0.5,2) as ReturnAmount
from [dbo].[customers] c
inner join [dbo].[orders] o on c.CustomerID = o.CustomerID 
inner join [dbo].[product_sales_amount_by_month] psa on o.OrderID = psa.OrderID
where YEAR(CURRENT_TIMESTAMP) - Year(BirthDate) > 50
group by CustomerName
