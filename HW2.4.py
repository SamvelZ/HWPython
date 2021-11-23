positions = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in positions:
    names=i.split()[-1]
    trueNames=names.title()
    print("Привет, ", trueNames, "!")