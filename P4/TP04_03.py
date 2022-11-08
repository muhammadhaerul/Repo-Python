#Program03: MyDay

day = int(input())

def myDay(day):
  year = day // 365
  month = (day % 365) // 30
  day = (day % 365) % 30
  print(f'{year} tahun')
  print(f'{month} bulan')
  print(f'{day} hari')

myDay(day)