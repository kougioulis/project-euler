#Project Euler Problem 700 - Eulercoins 

#first 14 eulercoins

#eulercoins starting with n=0,n=3,... 
eulercoins = [1504170715041707, 8912517754604,
        2044785486369,1311409677241,
        578033868113, 422691927098,
        267349986083, 112008045068,
        68674149121, 25340253174,
        7346610401, 4046188430,
        745766459, 428410324]

#second final eulercoin is 1, obtained by multiplying with 
#the inverse of 1504170715041707 mod 4503599627370517

a_minus = pow(1504170715041707, -1, 4503599627370517)
n = 2
while True:
    e = 1
    M = 4504599627370517
    while e != 428410324: 
        #an mod b = e => an = e mod b => n = a^{-1}e mod b
        n = (a_minus*e) % 4503599627370517
        if n < M and (e not in eulercoins):
            M = n
            eulercoins.append(e)
            print("n:",n, "Eulercoin:",e)
        e+=1
    break
n += 1
        
print(sum(eulercoins))
