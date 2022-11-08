<<<<<<< HEAD:P2/TP02_02.py
#Program02
category = input('Golongan = ')
power = int(input('Daya = '))
consumption = int(input('Pemakaian = '))

bill = 0
c_bill = True

match category:
  case 'R1':
    if power == 900:
      bill = consumption*1352
    elif power == 1300 and power == 2200:
      bill == consumption*1444.70
    else:
      c_bill = False
      print('Data tidak valid')
  case 'R2':
    if 3500 <= power and power <= 5500:
      bill = consumption*1699.53
    else:
      c_bill = False
      print('Data tidak valid')
  case 'R3':
    if 6600 <= power:
      bill = consumption*1699.53
    else:
      c_bill = False
      print('Data tidak valid')
  case 'B2':
    if 6600 <= power and power <= 200000:
      bill = consumption*1444.70
    else:
      c_bill = False
      print('Data tidak valid')
  case 'B3':
    if 200000 < power:
      bill = consumption*1114.74
    else:
      c_bill = False
      print('Data tidak valid')
  case 'I3':
    if 200000 <= power:
      bill = consumption*1314.12
    else:
      c_bill = False
      print('Data tidak valid')
  case 'P1':
    if 6600 <= power and power <= 200000:
      bill = consumption*1523.28
  case _:
    c_bill = False
    print('Data tidak valid')

if c_bill == True:
  output = '> Jumlah tagihan: {}'
  print('> Jumlah tagihan:', "{:,}".format(bill))

=======
#Program02
category = input('Golongan = ')
power = int(input('Daya = '))
consumption = int(input('Pemakaian = '))

bill = 0
c_bill = True

match category:
  case 'R1':
    if power == 900:
      bill = consumption*1352
    elif power == 1300 and power == 2200:
      bill == consumption*1444.70
    else:
      c_bill = False
      print('Data tidak valid')
  case 'R2':
    if 3500 <= power and power <= 5500:
      bill = consumption*1699.53
    else:
      c_bill = False
      print('Data tidak valid')
  case 'R3':
    if 6600 <= power:
      bill = consumption*1699.53
    else:
      c_bill = False
      print('Data tidak valid')
  case 'B2':
    if 6600 <= power and power <= 200000:
      bill = consumption*1444.70
    else:
      c_bill = False
      print('Data tidak valid')
  case 'B3':
    if 200000 < power:
      bill = consumption*1114.74
    else:
      c_bill = False
      print('Data tidak valid')
  case 'I3':
    if 200000 <= power:
      bill = consumption*1314.12
    else:
      c_bill = False
      print('Data tidak valid')
  case 'P1':
    if 6600 <= power and power <= 200000:
      bill = consumption*1523.28
  case _:
    c_bill = False
    print('Data tidak valid')

if c_bill == True:
  output = '> Jumlah tagihan: {}'
  print('> Jumlah tagihan:', "{:,}".format(bill))

>>>>>>> 1039364f47d26e616deb34a1ae0dc0caf8620653:P02/TP02_02.py
