money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
def number_of_months(a, b, c, d, e):
    while a > c:
        r = c - b
        a = a - r
        c = c * (1 + d)
        e += 1
    return e
print(number_of_months(money_capital, salary, spend, increase, month))
