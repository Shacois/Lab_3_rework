salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
a = 1
b = 3
def sum_money(a, b, c, d, e):
    while(a > 0):
        r = c - b
        e = e + r
        c = c * (1 + d)
        a = a - 1
    return e
print(round(sum_money(months, salary, spend, increase, need_money)))
