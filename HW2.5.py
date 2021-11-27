prices = [48.2, 78.25, 75, 95.02, 44.58, 70, 28.9, 32.08, 78, 96.48, 71.5, 84, 71.58, 83.9, 41.2]
new_prices = []

print("*"*30, "A")
for i in prices:
    rub, kop = f"{i:.2f}".split(".")
    new_prices.append(f"{rub} руб {kop} коп,")
print(' '.join(new_prices))



print("*"*30, "B")

prices.sort()
print(prices)

print("*"*30, "C")

new_sorted_price=[]
sorted(prices, reverse=True)
new_sorted_price=sorted(prices, reverse=True)
print(new_sorted_price)


print("*"*30, "D")

print(prices[-5:])