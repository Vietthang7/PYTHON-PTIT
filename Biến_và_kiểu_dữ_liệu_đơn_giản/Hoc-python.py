from math import *

# a = 100
# print(type(a))


# a = 29.93884835
# print('%.2f' % a)
# print('{:.2f}' .format(a))


# a = 3 + 5j
# print(a.real)
# print(a.imag)


# a = "28tech"
# b = "123"
# a, b = b, a
# print(a, b)

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(id(a))
# print(id(b))
# print(a is b)
# print(a is not b)


# s = '28tech c++ python java '
# print('28tech' in s)
# print('28tekh' in s)
# print('28tekh' not in s)

# Nhập thông tin từ bàn phím

# + bằng hàm Input
# s = input() trả về 1 chuỗi
# s = int(input("Vui long nhap so nguyen:"))
# print(s)

# + bằng hàm Map để nhập các số trên 1 dòng
# s = input()
# # trả về 1 chuỗi
# a = s.split()
# x, y, z = map(int, a)
# print(x + y + z)
# x, y, z, t = map(int,input('Nhập 4 số nguyên : ').split())
# print(x + y + z + t)


# if else
# t = 31
# if t == 31:
#     print(31)
# else:
#     print("du lieu khong hop le")


# Vòng for
# for i in range(1, 50):
#     print(i, end=" ")


# for i in range(1, 20):
#     print(i, "vt_cris7")

# a, b = 10, 20
# for i in range(a, b + 1):
#     print(i, "vt_cris7")


# a = 10
# for i in range(a, 0, -1):
#     print(i, "vt_cris7")
# else:
#     print('Vong lap da ket thuc')


# Vòng while


# Viết Hàm


# def tong(a, b):
#     res = a + b
#     return res


# m, n = 10, 20
# print(tong(m, n))


# def xinchao(name1, name2, name3):
#     print("Xin chao", name1, name2, name3)


# xinchao("Teo", "Ty", "Nam")
# print(xinchao("Teo", "Ty", "Nam"))
# Không có câu lệnh return thì sẽ trả về None


# def infor(name, job="Xe om"):
#     print(name, job)


# Code để chạy chương trình
# if __name__ == "__main__":
#     # x, y = map(int, input().split())
#     # print(tong(x, y))
#     infor("vt", "developer")
#     infor("vt")


# Phạm vi của biến trong Python


# List
# a = [1, 2, 3, 4, 5]
# print(a)
# print(type(a))


# s = "28tech"
# a = list(s)
# print(a)

# a = [1, 2, 3, 4, 5]
# print(len(a))

# a = [1, 2, 3, 4, 5]
# Duyệt xuôi
# for i in range(0, len(a)):
#     print(a[i], end=" ")
# print()
# # Duyệt ngược
# for i in range(len(a) - 1, -1, -1):
#     print(a[i], end=" ")
# print()
# # ForEach
# for item in a:
#     print(item, end=" ")
# # Thay đổi 1 phần tử
# a[2] = '28tech'
# print(a)
# # Thêm 1 phần tử vào cuối
# a.append(10)
# print(a)
# # Thêm 1 phàn tử vào vị trí bất kì
# a.insert(10,88234)
# #Vị trí quá lớn thì nó sẽ thêm vào cuối
# a.insert(1,'vtcris')
# print(a)


# Xóa đi 1 phần tử thông qua giá trị
# a.pop(2)
# print(a)

# a.pop()
# # Xóa đi thằng cuối
# print(a)

# del a[1]
# print(a)


# remove : xóa thông qua giá trị , nếu có nhiều giá trị thì chỉ xóa đi phần đầu tiên , nếu giá trị đó không có trong list mà xóa thì sẽ gặp lỗi
# a.remove(5)
# print(a)

# Xoá mọi phần tử
# a.clear()
# print(a)


# Sao chép list

# a = [1, 2, 3]
# b = a * 2
# print(b)

# Tạo 1 mảng có 1000 phần tử bằng 0
# b = [0] * 1000
# print(b)


# Tìm kiếm phần tử trong list


# Cách này có độ phức tạp là O(n)
# a = [1, 2, 3]
# if 1 in a:
#   print("YES")

# Combine list
# a = [1, 2, 3]
# b = [1, 2, 3, 4, 5]
# a.extend(b)
# print(a)
# a+=b
# print(a)

# Các phương thức của list

# Hàm copy tạo ra 1 list mới có nội dung giống như list ban đầu nhưng không phải là list ban đầu
# a = [1, 2, 3]
# c = a.copy()
# print(c)
# Nghĩa là list c sẽ không cùng địa chỉ với list a

# a = [1, 2, 3, 4, 1, 2, 3]
# print(a.count(1))

# print(a.index(2))
# print(a.index(1000))


# Lật ngược O(n)
# a.reverse()
# print(a)

# Sort O(nlog(n))
# a.sort()
# print(a)


# Tính tổng
# print(sum(a))


# b = sorted(a)
# print(a)
# print(b)

# min
# max

# cùng địa chỉ id
# a = [1, 2, 3, 4]
# b = a
# print(a)
# print(b)
# b[0] = 1000
# print(id(a))
# print(id(b))


# a = [1, 2, 3, 4]
# b = a.copy()
# b[0] = 1000
# print(a)
# print(b)

# print(id(a))
# print(id(b))


# def change(arr):
#     arr[0] = 1000


# a = [1, 2, 3, 4]
# change(a)
# print(a)


# def change(a):
#     a = 1000


# a = 10
# change(a)
# print(a)


# List Sclicing


# a[start:stop:step]
# a = [10, 20, 30, 40, 50, 60]
# b = a[2:5:2]
# # không truyền step thì mặc định là 1
# # không truyền stop thì mặc định là chỉ số cuối cùng
# # không truyền start thì mặc định là chỉ số 0
# b = a[2:5]
# b = a[2:-2]
# print(b)


# Lật ngược list
# a = [10, 20, 30, 40, 50, 60]
# b = a[::-1]
# print(a)
# print(b)


# Thay đổi giá trị trong một đoạn
# a = [10, 20, 30, 40, 50, 60]
# a[2:5] = [100]
# a[2:5] = [1, 2, 3]
# a[2:5] = []
# print(a)


# Chèn vào đầu
# a = [10, 20, 30, 40, 50, 60]
# a[:0] = [1, 2, 3]
# print(a)

# Chèn vào cuối
# a[len(a) :] = [3, 4, 5]
# print(a)

# shallow copy
# a = [10, 20, 30, 40, 50, 60]
# b = a[:]
# print(b)
# print(a is b)


# LAMBDA FUNCTION
# ví dụ 1:
# func = lambda x: x * 2
# print(func(10))

# Ví dụ 2
# res = (lambda x: x**2)(10)
# print(res)


# a = [1, 2, 3, 4, 5]
# b = list(map(lambda x: x**2, a))
# print(b)


# a = [1, 2, 3, 4, 5]
# b = list(filter(lambda x: x % 2 == 0, a))
# print(b)


# if else và lambda
# findMax = lambda x, y: x if x > y else y
# print(findMax(100, 200))


# List Comprehension
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# b = [x + 3 for x in a]
# print(b)


# a = [x**3 for x in range(5)]
# print(a)


# a = [1, 233, 43, 435, 445, 34, 12]


# def sum_digit(n):
#     tong = 0
#     while n != 0:
#         tong += n % 10
#         n //= 10
#     return tong


# b = [sum_digit(x) for x in a]
# print(b)

# a = [1, -233, 30, -4, 99]
# b = [x for x in a if x % 2 == 0]
# print(b)

# Nested List
# a = [[1, 2, 3], [4, 5], [6, 7, 8]]
# b = [x for small_list in a for x in small_list]
# print(b)


# Unpacking
# a = [1, 2, 3]
# x, y, z = a
# print(x, y, z)

# data = ("CR7", "MANUTD", 1985, "BDN")
# name, club, _, _ = data
# print(name, club)


# s = "CR7"
# a, b, c = s
# print(a, b, c)

# a = [["A", 65], ["B", 66], ["C", 67]]
# for kitu, ma in a:
#     print(kitu, ma)

# a = [1, 2, 3, 4]
# x, y, *z = a
# print(x)
# print(y)
# print(z)


# Tuple
# a = (1, 2, 3)
# b = (2804,)
# print(type(a))
# print(type(b))


# s = "vtcris"
# b = tuple(s)
# print(b)

# a = ("vtcris", (1, 2, 3), 38473)
# print(type(a))

# a = (1, 2, 3, 4, 5)
# for i in range(len(a)):
#     print(a[i])
# for x in a:
#     print(x, end=" ")

# a = (1, 2, 3, 4, 5)
# if 1 in a:
#     print("Found")
# else:
#     print("not found")

# a = (1, 2, 3, 4, 5)
# # không được thay đổi phần tử trong tuple
# a[0] = 100 như này là sai

# a = ("28tech", [1, 2, 3], "java", 1828)
# a[1][0] = 1000
# print(a)


# a = ("28tech", "java", "C++")
# b = ("python", "C++")
# c = a + b
# print(c)


# a = ("python", "C++")
# b = a * 3
# print(b)

# a = (1, 2, 3, 4, 5, 8, 4)
# a = tuple(sorted(a))
# print(a)


# a = (1, 2, 3, 4, 5, 8, 4)
# b = list(a)
# b.sort()
# print(b)
# a = tuple(b)
# print(a)

# a = (1, 2, 3, 4, 5, 8, 4)
# print(a.count(4))
# print(a.index(1))


# Map

# a = [-100, 20, -30, 40, -59]

# # a = [abs(x) for x in a]
# # print(a)
# a = list(map(abs, a))
# a = list(map(lambda x: x**2, a))
# print(a)

# s = "28tech"
# b = list(map(ord, s))
# print(ord('0'))
# print(b)


# def add(a, b):
#     return a + b


# if __name__ == "__main__":
#     a = [1, 2, 3, 4]
#     b = [2, 3, 4, 5]
#     #     c = list(map(add, a, b))
#     #     print(c)
#     c = list(map(lambda x, y: x + y, a, b))
#     print(c)


# Filter
# def nt(n):
#     if n < 2:
#         return False
#     for i in range(2, isqrt(n) + 1):
#         if n % i == 0:
#             return False
#     return True


# a = [2, 3, 1, 5, 7, 17, 10, 14]
# # nt_a = [x for x in a if nt(x)]
# # print(nt_a)
# nt_a = list(filter(nt, a))
# print(nt_a)

# odd = list(filter(lambda x: x % 2 == 1, a))
# print(odd)

# Sort : Tim-sort O(nlog(n))
# Sort key ,reveser
# có tính stable
# a = [1, 3, 5, 4, 6, 2, 3]
# a.sort()
# print(a)

# Sắp xếp giảm dần
# a.sort(reverse=True)
# print(a)


# a = [-1, 3, -5, -4, 6, 2, -3]
# a.sort(key=abs)
# a.sort(key=lambda x:abs(x))
# print(a)

# Sort vs lambda
# a = [[1, 2], [3, 2], [5, 2], [4, 1], [3, 6]]
# a.sort(key=lambda x: x[0])
# Giảm dần
# a.sort(key=lambda x: -x[0])
# a.sort(key=lambda x: x[0] ,reverse=True)
# print(a)
# Sắp xếp theo 2 tiêu chí
# a.sort(key=lambda x: (x[0], -x[1]))
# print(a)


# a = (1, 2, 3, 6, 5)
# b = sorted(a, reverse=True)
# print(b)
# print(a is b)


# Bài 75 cmp to key


from functools import cmp_to_key

# 1,-1,0
# Nếu a là thằng đứng trước , b là thằng đứng sau sau khi mà bạn sắp xếp
#  Nếu a và b đã đúng thứ tự mà bạn muốn thì trả về -1 , ngược lại là 1


# def cmp(a, b):
#     if a < b:
#         return 1
#     else:
#       return -1
# return a-b
# return b-a
# a = [10, 2, 3, 1, 4, 5, 6, 3, 0]
# a.sort(key=cmp_to_key(cmp))
# print(a)


# Sắp xếp các phần tử trong mảng theo thứ tự tổng chữ số tăng dần nếu 2 số có cùng tổng chữ số thì số nhỏ hơn sẽ xếp trc
# def tong(n):
#     res = 0
#     while n != 0:
#         res += n % 10
#         n //= 10
#     return res


# def cmp(a, b):
#     tong1 = tong(a)
#     tong2 = tong(b)
#     if tong1 != tong2:
#         return tong1 - tong2
#     else:
#         # return a - b
#         return b - a


# a = [40, 22, 55, 41, 30, 21]
# a.sort(key=cmp_to_key(cmp))
# print(a)

# sorted cũng áp dụng được
