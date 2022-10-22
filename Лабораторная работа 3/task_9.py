salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
def sum_money(months, salary, spend, increase, need_money):
    for months in range(10):
        diff = spend - salary
        need_money = need_money + diff
        spend = spend * (1 + increase)
    return need_money

print(round(sum_money(months, salary, spend, increase, need_money)))
