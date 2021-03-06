import binascii
import os
import pymysql.cursors

connection = pymysql.connect(host='localhost', user='root', password='404lollypop', db='vehicles', cursorclass=pymysql.cursors.DictCursor)


all_bikes = {'YAMAHA': ['ALPHA', 'CRUX', 'CYGNUS RAY ZR', 'FASCINO', 'FAZER', 'FAZER FI V 2.0', 'FZ', 'FZS', 'FZ25', 'FZS V 2.0 FI', 'FZS V 2.0', 'FZ V 2.0', 'FZ1', 'FZ16', 'MT -09', 'RAY', 'RAY- Z', 'SALUTO', 'SALUTO RX', 'SS 125', 'SZ RR V 2.0', 'SZ- RR', 'SZ- S', 'VMAX', 'YBR 110', 'YBR 125', 'YZF R3', 'YZF R15', 'YZF R15S', 'YZF R1', 'YZF R1M'], 'OKINAWA': ['RIDGE'], 'DSK BENELLI': ['TNT 889', 'TNT 600i', 'TNT 600 GT', 'TNT 25', 'TNT R', 'TNT 300'], 'VESPA': ['LX', 'S', '70 TH ANNIVESARY EDITION', '150', '946', 'VX 125'], 'MAHINDRA': ['CENTURO', 'CENTURO ROCKSTAR', 'DURO DZ', 'FLYTE', 'GUSTO', 'GUSTO 125', 'MOJO', 'KINE', 'PANTERO', 'RODEO RZ', 'RODEO UZO 125'], 'KAWASAKI': ['ER- 6n', 'NINJA 1000', 'NINJA 300', 'NINJA 650', 'NINJA H2', 'NINJA ZX- 10 R', 'NINJA ZX- 14 R', 'VERSYS 650', 'VERSYS 1000', 'Z1000', 'Z250', 'Z800'], 'BAJAJ': ['AS(AVENGER STREET) 220', 'AS(AVENGER STREET) 200', 'AS(AVENGER STREET) 150', 'AVENGER 220', 'AVENGER  CRUISE 220', 'CT100', 'DISCOVER 100', 'DISCOVER 100 M', 'DISCOVER 125', 'DISCOVER 125 M', 'DISCOVER 150 F', 'DISCOVER 150 S', 'DOMINAR 400', 'V12', 'V15', 'PLATINA 100', 'PLATINA 100 ES', 'PULSAR 135 LS', 'PULSAR 150 DTS-i', 'PULSAR 180 DTS-i', 'PULSAR 220F', 'PULSAR AS150', 'PULSAR AS200', 'PULSAR NS200', 'PULSAR RS200'], 'INDIAN': ['CHIEFTAIN DARK HORSE', 'CHIEF VINTAGE', 'CHIEF CLASSIC', 'CHIEFTAIN', 'ROADMASTER', 'SCOUT', 'SCOUT SIXTY', 'SPRING FIELD'], 'ROYAL ENFIELD': ['BULLET 350 TWINSPARK', 'BULLET 500', 'BULLET ELECTRA TWINSPARK', 'CLASSIC 350', 'CLASSIC 500', 'CLASSIC CHROME', 'CLASSIC BATTLE GREEN', 'CLASSIC DESSERT STORM', 'CONTINENTAL GT(CAFÉ RACER)', 'HIMALAYAN', 'THUNDER BIRD 350', 'THUNDER BIRD 500'], 'MOTO GUZZI': ['AUDACE', 'ELDORADO', 'MGX-21', 'V9 BOBBER', 'V9 ROAMER'], 'TVS': ['APACHE RTR 160', 'APACHE RTR 180', 'APACHE RTR 180 ABS', 'APACHE RTR 200 4V', 'HEAVY DUTY SUPER XL', 'JUPITER', 'MAX 4R', 'PHOENIX', 'PHOENIX 125', 'SCOOTY PEP PLUS', 'SCOOTY STREAK', 'SCOOTY ZEST 110', 'STAR CITY PLUS', 'STAR SPORT', 'SPORT', 'VICTOR', 'VICTOR GLX', 'XL HD', 'XL 100', 'WEGO'], 'TRIUMPH': ['STREET TWIN', 'STREET TRIPLE', 'DAYTONA 675', 'DAYTONA 675R', 'SPEED TRIPLE', 'THRUXTON', 'BONNEVILLE', 'BONNEVILLE T100', 'BONNEVILLE T120', 'THUNDERBIRD', 'TIGER 800', 'THRUXTON R'], 'BMW': ['S 1000 R', 'R NINE T', 'S 1000 RR', 'K 1600', 'K 1300 R', 'R 1200 GS', 'K 1300 S'], 'DUCATI': ['XDIAVEL', 'DIAVEL', 'SCRAMBLER', 'MONSTER 821', 'HYPERMOTARD', '959 PANIGALE', 'MULTISTRADA 1200S', 'MULTISTRADA 1200 ENDURO'], 'HONDA': ['ACTIVA 125', 'ACTIVA 3G', 'ACTIVA-i', 'AVIATOR', 'CB SHINE', 'CB SHINE SP', 'CB TRIGGER', 'CB TWISTER', 'CB UNICORN 150', 'CB UNICORN 160', 'CB 1000 R', 'CB HORNET 160 R', 'CBF STUNNER', 'CBR 150 R', 'CBR 650F', 'CBR 250 R', 'CBR 1000 RR', 'CD 110 DREAM', 'DIO', 'DREAM NEO', 'DREAM YUGA', 'GOLD WING GL 1800', 'LIVO', 'NAVI', 'VFR 1200F', 'VT 1300CX'], 'SUZUKI': ['ACCESS 125', 'ACCESS 125 SE', 'BANDIT 1250SA', 'GIXXER', 'GIXXER SF', 'GIXXER XF', 'GS 150R', 'GSX- R1000', 'GSX-S1000', 'GSX- S1000F', 'HAYABUSA', 'HAYABUSA Z', 'HAYATE', 'HAYATE EP', 'INAZUMA 250', 'INTRUDER M800', 'INTRUDER M1800R', 'INTRUDER M1800R(BOSS)', 'LETS', 'M1800 R', 'M800', 'SLINGSHOT PLUS', 'SWISH 125 FACELIFT', 'V- STROM 1000'], 'HERO': ['ACHIEVER', 'DUET', 'ELECTRIC MAXI', 'ELECTRIC ZION', 'ELECTRIC PHOTON', 'ELECTRIC CRUZ', 'ELECTRIC OPTIMA PLUS', 'ELECTRIC NYX', 'GLAMOUR', 'GLAMOUR FI', 'HF DAWN', 'HF DELUXE', 'HF DELUXE ECO', 'HUNK', 'IGNITOR', 'IMPULSE', 'KARIZMA', 'KARIZMA ZMR', 'MAESTRO', 'MAESTRO EDGE', 'PASSION PROi3S', 'PASSION PRO', 'PASSION PRO TR', 'PASSION X PRO', 'PLEASURE', 'SPLENDOR I SMART 110', 'SPLENDER i SMART', 'SPLENDER PLUS', 'SPLENDER PRO', 'SPLENDER PRO CLASSIC', 'SUPER SPLENDER', 'XTREME', 'XTREME SPORTS'], 'HARLEY DAVIDSON': ['BREAKOUT', 'CVO LIMITED', '1200 CUSTOM', 'FAT BOB', 'FAT BOY', 'FAT BOY SPECIAL', 'FORTY EIGHT', 'HERITAGE SOFTAIL CLASSIC', 'IRON 883', 'NIGHT ROD', 'NIGHT ROD SPECIAL', 'ROADSTER', 'ROAD GLIDE', 'ROAD KING', 'STREET 750', 'STREET BOB', 'STREET GLIDE', 'STREET GLIDE SPECIAL', 'SUPER LOW', 'V ROD'], 'KTM': ['390 DUKE ABS', 'DUKE 200', 'RC200', 'RC390']}

for brand, bikes in all_bikes.items():

    for bike in bikes:

        vehicle_model_id = binascii.hexlify(os.urandom(4)).decode()

        unique_id = True
        while unique_id:
            sql_command = "SELECT `model_name` FROM `core_vehiclemodels` WHERE `vehicle_model_id`=%s"
            connection.cursor().execute(sql_command, (vehicle_model_id))
            result = connection.cursor().execute(sql_command, ("assaas"))
            if result == 0:
                unique_id = False
            else:
                print("Duplicate found")

        sql_command = "INSERT INTO `core_vehiclemodels` (`vehicle_model_id`, `model_name`, `brand_name`, `vehicle_type`) VALUES (%s, %s, %s, %s)"
        connection.cursor().execute(sql_command, (vehicle_model_id, bike, brand, "Bike"))
        connection.commit()

    print("%s completed" % brand)

print("Task Completed")