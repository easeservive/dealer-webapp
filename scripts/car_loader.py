import binascii
import os
import pymysql.cursors

connection = pymysql.connect(host='localhost', user='root', password='404lollypop', db='easedb_1', cursorclass=pymysql.cursors.DictCursor)


all_cars = {'HYUNDAI': ['ACCENT', 'ELANTRA', 'ELITE i20', 'EON', 'CRETA', 'FLUIDIC VERNA', 'GRAND i10', 'GETZ', 'i10', 'i20 ACTIVE', 'SANTRO', 'SANTA FE', 'SONATA', 'TUCSON', 'X CENT'], 'LAND ROVER': ['DISCOVERY', 'DISCOVERY SPORT', 'FREE LANDER 2', 'RANGE ROVER EVOQUE', 'RANGE ROVER LWB', 'RANGE ROVER SPORT'], 'PORSCHE': ['911', 'BOXTER', 'CAYENNE', 'CAYMAN', 'MACAN', 'PANAMERA'], 'MAHINDRA': ['BOLERO', 'BOLERO PIK UP', 'BOLERO BIG PIK UP', 'BOLERO CAMPER', 'e2o', 'e20 PLUS', 'IMPERIO', 'NAVOSPORT', 'QUNTO', 'TUV300', 'KUV100', 'SCORPIO', 'SUPRO', 'THAR', 'e-VERITO', 'VERITO', 'VERITO VIBE', 'XUV 500', 'XYLO'], 'NISSAN': ['EVALIA', 'GT-R', 'MICRA ACTIVE', 'MICRA', 'SUNNY', 'TERRANO'], 'SSANGYONG': ['REXTON W', 'REXTON'], 'MERCEDES BENZ': ['A- CLASS', 'B- CLASS', 'C- CLASS', 'AMG SLC 43', 'AMG C 43', 'AMG C 63', 'AMG GL 63', 'AMG G 63', 'AMG GLA 45', 'AMG- E63', 'AMG GT-S', 'AMG S 63 COUPE', 'AMG S 63', 'AMG GLE COUPE', 'CLA CLASS', 'CLA 45 AMG', 'CLS', 'E- CLASS', 'GLC', 'GLS', 'GLE', 'GL', 'GL-63 AMG', 'GLA', 'M- CLASS', 'ML 63AMG', 'S- CLASS', 'SLK- CLASS'], 'DC': ['AVANTI'], 'ROLLS-ROYCE': ['WRAITH', 'PHANTOM', 'GHOST', 'DAWN'], 'RENAULT': ['DUSTER', 'FLUENCE', 'KOLEOS', 'KWID', 'LODGY', 'PULSE', 'SCALA'], 'JAGUAR': ['F TYPE', 'F PACE', 'XE', 'XF', 'XJ L'], 'TOYOTA': ['CAMRY', 'COROLLA ALTIS', 'ETIOS', 'ETIOS CROSS', 'PLATINUM ETIOS', 'ETIOS LIVA', 'FORTUNER', 'INNOVA', 'INNOVA CRYSTA', 'LAND CRUISER', 'LAND CRUISER PARDO', 'PRIUS'], 'ICML': ['RHINO', 'EXTREME'], 'FORD': ['CLASSIC', 'ECO SPORTS', 'ENDEAVOUR', 'FIESTA', 'FIGO', 'FIGO ASPIRE', 'FUSION', 'MUSTANG', 'IKON'], 'VOLVO': ['S60', 'S60 CROSS COUNTRY', 'S80', 'S90', 'V40', 'V40 CROSS COUNTRY', 'XC60', 'XC90'], 'FORCE MOTORS': ['FORCE ONE', 'GURKHA'], 'SKODA': ['OCTAVIA', 'RAPID', 'SUPERB', 'YETI'], 'FERRARI': ['CALIFORNIA', 'FF'], 'VOLKSWAGEN': ['CROSS POLO', 'BEETLE', 'AMEO', 'JETTA', 'POLO GTI', 'POLO GT', 'POLO', 'VENTO'], 'ASTON MARTIN': ['RAPIDE', 'DB9', 'V8 VANTAGE', 'V12 VANTAGE', 'V12 VANQUISH', 'DB11'], 'DATSUN': ['GO', 'REDI GO', 'GO PLUS'], 'BENTLEY': ['FLYING SPUR', 'CONTINENTAL', 'MULSANNE', 'BENTAYGA'], 'CHEVROLET': ['BEAT', 'CAPTIVA', 'CRUZE', 'ENJOY', 'SAIL', 'SAIL HATCH BACK', 'SPARK', 'TRAILBLAZER', 'TAVERA'], 'TATA': ['ARIA', 'BOLT', 'HEXA', 'INDICA V2', 'INDICA eV2', 'INDIGO eCS', 'MANZA', 'MOVUS', 'NANO', 'SAFARI', 'SAFARI DICOR', 'SAFARI STORME', 'SUMO VICTA', 'SUMO GOLD', 'SUMO GRAND E', 'TIAGO', 'VENTURE', 'VISTA', 'XENON YODHA', 'XENON', 'ZEST'], 'BMW': ['1 SERIES', '3 SERIES', '3 SERIES GT', '5 SERIES', '6 SERIES', '7 SERIES', 'BMW M3', 'BMW M4', 'BMW M5', 'BMW M6', 'BMW i8', 'X1', 'X3', 'X5', 'X6', 'Z4'], 'MASERATI': ['GHIBLI', 'GRAN TURISMO', 'QUATTROPORTE', 'GRANCABRIO'], 'FIAT': ['AVVENTURA', 'LINEA', 'LINEA CLASSIC', '500- ABBARTH', 'URBAN CROSS', 'PUNTO PURE', 'PUNTO EVO', 'PUNTO'], 'MARUTI SUZUKI': ['ALTO', 'ALTO 800', 'ALTO K10', 'BALENO', 'CELERIO', 'CIAZ', 'Eeco', 'ERTIGA', 'GRAND VITARA', 'GYPSY', 'OMNI', 'RITZ', 'S CROSS', 'STINGRAY', 'SWIFT', 'SWIFT DZIRE', 'VITARA BREZZA', 'IGNIS', 'WAGON R'], 'MINI': ['COOPER', 'COOPER CONVERTIBLE', 'COOPER COUNTRYMAN', 'CLUBMAN', '3 DOOR', '5 DOOR', 'COOPER S'], 'JEEP': ['WRANGLER CHEROKEE', 'GRAND CHEROKEE'], 'ISUZU': ['D-MAX V-CROSS', 'MU 7'], 'MITSUBISHI': ['LANCER', 'MONTERRO', 'PAJERO SPORT', 'PAJERO'], 'HONDA': ['AMAZE', 'ACCORD', 'BRIO', 'CITY', 'BR-V', 'JAZZ', 'CR-V', 'MOBILIO'], 'AUDI': ['A3', 'A3 CABRIOLET', 'A4', 'A6', 'A8 L', 'Q3', 'Q5', 'Q7', 'R8', 'RS5', 'RS6', 'RS7 SPORT BACK', 'S5', 'S6', 'TT']}


for brand, cars in all_cars.items():

    for car in cars:

        vehicle_model_id = binascii.hexlify(os.urandom(4)).decode()

        unique_id = True
        while unique_id:
            sql_command = "SELECT `model_name` FROM `core_vehiclemodels` WHERE `vehicle_model_id`=%s"
            connection.cursor().execute(sql_command, (vehicle_model_id))
            result = connection.cursor().execute(sql_command, ("assaas"))
            if result == 0:
                unique_id = False

        sql_command = "INSERT INTO `core_vehiclemodels` (`vehicle_model_id`, `model_name`, `brand_name`, `vehicle_type`) VALUES (%s, %s, %s, %s)"
        connection.cursor().execute(sql_command, (vehicle_model_id, car, brand, "Car"))
        connection.commit()

    print("%s completed" % brand)

print("Task Completed")