print("Здравствуйте! Вас приветствует программа 'Конвертер секунд'!")
1
duracion = int(input("Введите продолжительность времени в секундах!"))

m=duracion//60%60
s=duracion%60
h=duracion//60//60%24
d=duracion//60//60//24

if duracion<=60:
    print(d,"дн",h,"час",m,"мин",s,"сек")
elif duracion>60 and duracion<3600:
    print(d,"дн",h,"час",m,"мин",s,"сек")
elif duracion>=3600 and duracion<86400:
    print(d,"дн",h,"час",m,"мин",s,"сек")
elif duracion>=86400:
    print(d,"дн",h,"час",m,"мин",s,"сек")