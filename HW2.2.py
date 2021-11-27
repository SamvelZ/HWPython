list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []

for s in list:
    if s.replace("+","").isdigit():
        if s.isdigit():
            new_list.append(f"'{int(s):02}'")
        else:
            new_list.append(f"'{s[0]}{int(s[1:]):02}'")
    else:
        new_list.append(s)

print(new_list)
print(" ".join(new_list))