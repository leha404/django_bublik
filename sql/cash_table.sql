-- SQLite
SELECT
        sum(POS.count * P.price) as main,
        sum(case when O.payment_type = 'cash' then POS.count * P.price else 0 end) as cash,
        sum(case when O.payment_type = 'card' then POS.count * P.price else 0 end) as card,
        sum(case when O.payment_type = 'perevod' then POS.count * P.price else 0 end) as perevod
    from bublik_order as O
    inner join bublik_orderposition as POS on POS.order_id = O.id
    inner join bublik_product as P on POS.product_id = P.id
where O.created_date > date('now')