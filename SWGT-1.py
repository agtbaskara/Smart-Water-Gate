from time import sleep
import pifacedigitalio as pfd
pin0 = pin1 = pin2 = pin3 = 0
pfd.init()

p = pfd.digital_read(0)
q = pfd.digital_read(1)
r = pfd.digital_read(2)
s = pfd.digital_read(3)
t = pfd.digital_read(4)
u = pfd.digital_read(5)
v = pfd.digital_read(6)
mode = pfd.digital_read(7)
pintu = stop
auto = 1
man = 0
while(True):

    p = pfd.digital_read(0)
    q = pfd.digital_read(1)
    r = pfd.digital_read(2)
    s = pfd.digital_read(3)
    t = pfd.digital_read(4)
    u = pfd.digital_read(5)
    v = pfd.digital_read(6)
    mode = pfd.digital_read(7)  #READ NILAI SENSOR KE VARIABLE

    if(pintu == buka): #MEMBUKA & MENUTUP PINTU
        pfd.digital_write(0,1)
    else:
        if(pintu == tutup):
            pfd.digital_write(1,1)
    
    if(r == 1): #MENGHENTIKAN PINTU KETIKA TERBUKA PENUH
         pfd.digital_write(0,0)
         pintu = stop
    if(s == 1): #MENGHENTIKAN PINTU KETIKA TERTUTUP PENUH
         pfd.digital_write(1,0)
         pintu = stop
    
    if(auto == 1):
        pfd.digital_write(3,1)
        pfd.digital_write(4,0)
    if(man == 1):
        pfd.digital_write(3,0)
        pfd.digital_write(4,1)  #LAMPU MODE
        
    if(mode == 1):  #DETEKSI MODE
        if(auto == 1):
            auto = 0
            man = 1
            pfd.digital_write(3,1)
            pfd.digital_write(4,0)
        else:
            if(man == 1):
                auto = 1
                man = 0
                pfd.digital_write(3,0)
                pfd.digital_write(4,1)
        sleep(0.3)

    if(man == 1):   #MODE MANUAL
        if(u == 1):
            if(r == 0):
                pintu = buka
        if(v == 1):
            if(s == 0):
                pintu = tutup

    if(auto == 1):  #MODE AUTO
        if(p == 1):
            if(r == 0):
                if(t == 1):
                    pintu = buka
                else:
                    pintu = stop
            else:
               pintu = stop
        else:
            pintu = stop
            
        if(q == 0):
            if(s == 0):
                if(t == 0):
                    pintu = tutup
                else:
                    pintu = stop
            else:
               pintu = stop
        else:
            pintu = stop

    if(pintu == buka):  #NYALA BUZZER
        pfd.digital_write(2,1)
        sleep(0.3)
        pfd.digital_write(2,0)
        sleep(0.4)
    if(pintu == tutup):
        pfd.digital_write(2,1)
        sleep(0.2)
        pfd.digital_write(2,0)
        sleep(0.1)
