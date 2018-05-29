from time import sleep
import pifacedigitalio as pfd
pfd.init()

p = pfd.digital_read(0)
q = pfd.digital_read(1)
r = pfd.digital_read(2)
s = pfd.digital_read(3)
t = pfd.digital_read(4)
u = pfd.digital_read(5)
v = pfd.digital_read(6)
mode = pfd.digital_read(7)
pintu = 2
auto = 0
man = 1
while(pintu == 2):

    p = pfd.digital_read(0)
    q = pfd.digital_read(1)
    r = pfd.digital_read(2)
    s = pfd.digital_read(3)
    t = pfd.digital_read(4)
    u = pfd.digital_read(5)
    v = pfd.digital_read(6)
    mode = pfd.digital_read(7)  #READ NILAI SENSOR KE VARIABLE

    if(pintu == 1): #MEMBUKA & MENUTUP PINTU
        pfd.digital_write(0,1)
        pfd.digital_write(1,0)
    if(pintu == 2):
        pfd.digital_write(1,1)
        pfd.digital_write(0,0)
    
    if(r == 1): #MENGHENTIKAN PINTU KETIKA TERBUKA PENUH
         pfd.digital_write(0,0)
         pintu = 0
    if(s == 1): #MENGHENTIKAN PINTU KETIKA TERTUTUP PENUH
         pfd.digital_write(1,0)
         pintu = 0
    
    if(auto == 1):
        pfd.digital_write(3,1)
        pfd.digital_write(4,0)
    if(man == 1):
        pfd.digital_write(3,0)
        pfd.digital_write(4,1)  #LAMPU MODE

    if(pintu == 1):  #NYALA BUZZER
        pfd.digital_write(2,1)
        sleep(0.3)
        pfd.digital_write(2,0)
        sleep(0.4)
    if(pintu == 2):
        pfd.digital_write(2,1)
        sleep(0.2)
        pfd.digital_write(2,0)
        sleep(0.1)
