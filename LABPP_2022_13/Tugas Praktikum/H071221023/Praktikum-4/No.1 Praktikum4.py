number = int(input(" "))

def jumlah(number) :
    if number == 0 :
       return 1
    elif number < 0 :
        return "Tidak Terdefenisi"
    else : 
        return number*jumlah(number - 1)

print(jumlah(number))
