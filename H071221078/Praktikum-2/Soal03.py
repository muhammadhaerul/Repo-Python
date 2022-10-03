a, b, c, d, e = input('Masukkan 5 Bilangan: ').split(' ')

p = a.replace('-','')
q = b.replace('-','')
r = c.replace('-','')
s = d.replace('-','')
t = e.replace('-','')

angka_genap = 0
angka_ganjil = 0
angka_positif = 0
angka_negatif = 0

if p.isnumeric() and q.isnumeric() and r.isnumeric() and s.isnumeric() and t.isnumeric():
    if int(a) > 0:
        angka_positif += 1
    elif int(a) < 0:
        angka_negatif += 1

    if int(a)%2 == 0 or int(a) == 0:
        angka_genap += 1
    elif int(a)%2 != 0:
        angka_ganjil += 1

    if int(b) > 0:
        angka_positif += 1
    elif int(b) < 0:
        angka_negatif += 1

    if int(b)%2 == 0 or int(b) == 0:
        angka_genap += 1
    elif int(b)%2 != 0:
        angka_ganjil += 1

    if int(c) > 0:
        angka_positif += 1
    elif int(c) < 0:
        angka_negatif += 1

    if int(c)%2 == 0 or int(c) == 0:
        angka_genap += 1
    elif int(c)%2 != 0:
        angka_ganjil += 1

    if int(d) > 0:
        angka_positif += 1
    elif int(d) < 0:
        angka_negatif += 1

    if int(d)%2 == 0 or int(d) == 0:
        angka_genap += 1
    elif int(d)%2 != 0:
        angka_ganjil += 1

    if int(e) > 0:
        angka_positif += 1
    elif int(e) < 0:
        angka_negatif += 1

    if int(e)%2 == 0 or int(e) == 0:
        angka_genap += 1
    elif int(e)%2 != 0:
        angka_ganjil += 1

    print('%d angka genap' % (angka_genap))
    print('%d angka ganjil' % (angka_ganjil))
    print('%d angka positif' % (angka_positif))
    print('%d angka negatif' % (angka_negatif))

else:
    print('Input tidak valid')