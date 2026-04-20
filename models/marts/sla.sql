SELECT
  order_id,
  COUNT(*) AS breaches
FROM ecommerce.sla_alerts
GROUP BY order_id