SELECT
  product_id,
  qty,
  CASE WHEN qty < 5 THEN 1 ELSE 0 END AS stockout_risk
FROM ecommerce.inventory_raw