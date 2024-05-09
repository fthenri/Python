def tax(salary):
    if salary <= 2000.00:
        return 'Isento'
    elif 2000.01 <= salary <= 3000.00:
        tax1 = (salary - 2000.00) * 0.08
        return f'R$ {tax1:.2f}'
    elif 3000.01 <= salary <= 4500.00:
        tax2 = (salary - 3000.00) * 0.18 + 1000 * 0.08
        return f'R$ {tax2:.2f}'
    elif salary > 4500.00:
        tax3 = (salary - 4500) * 0.28 + 1500 * 0.18 + 1000 * 0.08
        return f'R$ {tax3:.2f}'

salary = float(input())
print(tax(salary))
