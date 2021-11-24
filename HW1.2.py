HW1.2
cube_list=[]
new_cube_list=[]
n=0
sum=0
new_sum=0

while n<1000:
    n=n+1
    m=n**3
    if n%2:
        cube_list.append(m)
print(cube_list)


for ind,val in enumerate(cube_list):
    sum_diggits=0
    while val > 0:
       sum_diggits +=val%10
       val//=10
    if sum_diggits %7==0:
           sum += cube_list[ind]
print(sum)

for s in cube_list:
    new_cube_list.append(s+17)

sum=0

for ind,val in enumerate(new_cube_list):
    sum_diggits=0
    while val > 0:
       sum_diggits +=val%10
       val//=10
    if sum_diggits %7==0:
           sum += new_cube_list[ind]
print(sum)
