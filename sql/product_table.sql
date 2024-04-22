-- SQLite
SELECT
        P.name,
        P.price,
        sum(POS.count) as cnt,
        sum(P.price * POS.count) as sum
    from bublik_order as O
    inner join bublik_orderposition as POS on POS.order_id = O.id
    inner join bublik_product as P on POS.product_id = P.id
where date(O.created_date, 'localtime') = date('now', 'localtime')
group by P.name, P.price