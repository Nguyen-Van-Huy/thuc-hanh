lst = []
num = int(input('Co bao nhieu gia tri: '))
for n in range(num):
    gia_tri = input('Nhap gia tri: ')
    lst.append(gia_tri)
    print(lst)
print("Phan tu lon nhat :", max(lst))
