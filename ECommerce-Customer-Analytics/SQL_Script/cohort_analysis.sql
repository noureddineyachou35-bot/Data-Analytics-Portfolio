WITH Cohort_Base AS (
    SELECT customer_id, MIN(order_date) AS first_purchase_date
    FROM dbo.online_retail WHERE customer_id != 0
    GROUP BY customer_id
),
Cohort_Index AS (
    SELECT DISTINCT
        t.customer_id,
        FORMAT(b.first_purchase_date, 'yyyy-MM') AS Cohort_Month,
        DATEDIFF(month, b.first_purchase_date, t.order_date) AS month_number
    FROM dbo.online_retail t
    JOIN Cohort_Base b ON t.customer_id = b.customer_id
)
SELECT *
FROM (
    SELECT Cohort_Month, month_number, customer_id
    FROM Cohort_Index
) AS SourceTable
PIVOT (
    COUNT(customer_id) -- Pas de DISTINCT ici, il est déjà fait au-dessus
    FOR month_number IN ([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12])
) AS PivotTable
ORDER BY Cohort_Month;