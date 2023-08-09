names: list[str] = ["Egor", "Alexander", "Kostya"]
salaries: list[int] = [1500, 2500, 3500]
bonuses: list[str] = ["10.55%", "8.5%", "23.5%"]

print({name: (salary * float(bonus[:-1])/100) for name, salary, bonus in zip(names, salaries, bonuses)})