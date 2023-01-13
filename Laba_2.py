import numpy as numpic
import random
import matplotlib.pyplot as py
def resualt_recoid_txt(arr_strings):
        arr_strings = list()
        with open("resualt.txt","w") as file:
            file.write(arr_strings)
try:
    def graph(array,pod_matr,pl_1,pl_2,pl_3):
        py.subplot(pl_1,pl_2,pl_3)
        csize = len(array) * len(array[0])
        x = numpic.linspace(0, csize, csize)
        y = numpic.asarray(array).reshape(-1)
        py.plot(x,y,'ro')
        py.title("подматрица " + pod_matr)
except:
    print("График не сработал...")

try:
    def matrix_print(e,b,d,c):
        print ("=====================")
        print("Подматрица e")
        print(e)
        print("Подматрица b")
        print(b)
        print("Подматрица d")
        print(d)
        print("Подматрица c")
        print(c)
        print ("=====================")
except:
    print("Не могу вывести подматрицы..")

try:
    print("Введите множитель")
    k = int(input())
    if (k %  2 == 0):
        print("Требуется ввести разменость начальной матрицы:")
        n = int(input())
        a = numpic.array([[random.randint(2-10, 10) for j in range(n)] for i in range(n)])
        print("Матрица A")
        print(a)
    else:
        print("Стоит попробовать снова! (нечетн)")
except:
    print("Стоит попробовать снова!")

e_mat = a[0: n // 2, 0: n // 2]
b_mat = a[0: n // 2, n // 2:]
d_mat = a[n // 2:, 0:n // 2]
c_mat = a[n // 2:, n // 2:]
matrix_print(e_mat,b_mat,d_mat,c_mat)

f = a.copy()
firstpart = numpic.tril(a, k=0)
secondpart = numpic.tril(a.transpose(), k=0)
test = (firstpart==secondpart).all()
if (test):
    b_mat = numpic.flipud(a[0: n // 2, 0: n // 2])
    d_mat = a[n // 2:, 0:n // 2]
else:
    e_mat = numpic.flipud(a[n // 2:, 0:n // 2])
    d_mat = a[n // 2:, n // 2:]
print("Подматрицы F")
matrix_print(e_mat,b_mat,d_mat,c_mat)

f = numpic.concatenate((numpic.concatenate((b_mat, c_mat), axis=0), numpic.concatenate((d_mat, e_mat), axis=0)), axis=1);
print("Матрица F")
print(f)
print("Определитель матрицы A")
det_mt = numpic.linalg.det(a)
print(det_mt)
print("Сумма диагональных элементов F")
dia_mt = numpic.trace(f)
print(dia_mt)
if det_mt > dia_mt:
    ainv = numpic.linalg.inv(a)
    at = numpic.transpose(a)
    finv = numpic.linalg.inv(f)
    result = numpic.subtract(numpic.multiply(ainv, at), numpic.multiply(k, finv))
else:
    at = numpic.transpose(a)
    g = numpic.tril(a)
    ft = numpic.transpose(f)
    result = numpic.multiply(numpic.subtract(numpic.add(at, g), ft), k)
print("Результат")
print(result)

# вывод графиков
py.figure()
graph(e_mat,"e",2,2,1)
graph(b_mat,"b",2,2,2)
graph(d_mat,"d",2,2,3)
graph(c_mat,"c",2,2,4)
py.show()