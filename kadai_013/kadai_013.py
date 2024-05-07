def calc_tax(money,tax):
    tax = tax/100
    result = money + money*tax
    print(f"{result}円")

calc_tax(100,8)
    