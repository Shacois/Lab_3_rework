money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
def number_of_months(money_capital, salary, spend, increase, month):
    while money_capital > spend:
        diff = spend - salary
        money_capital = money_capital - diff
        spend = spend * (1 + increase)
        month += 1
    return month

print(number_of_months(money_capital, salary, spend, increase, month))
