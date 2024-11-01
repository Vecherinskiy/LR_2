money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

num_month = 0
money_capital -= spend
while money_capital >= 0:
    money_capital -= spend
    money_capital += salary
    spend += increase * spend
    spend = round(spend, 5)
    num_month += 1
print("Количество месяцев, которое можно протянуть без долгов:", num_month)
