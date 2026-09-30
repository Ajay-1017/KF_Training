SELECT id,
       product_name,
       amount,
       status,
       created_at
FROM public.orders
LIMIT 1000;