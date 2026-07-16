import time
import board
import adafruit_dht
import pymysql

# 1. Cau hinh cam bien DHT11 tren chan GPIO17 (Chan vat ly so 11)
try:
    dhtDevice = adafruit_dht.DHT11(board.D17)
except Exception as e:
    print(f"Loi khi khoi tao cam bien: {e}")

# Chan LED  hinh de danh cho cau sau (GPIO27 - Chan vat ly so 13)
pin_led = 27 

# 2. Cau hinh ket noi Co so du lieu MariaDB
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',  # Mat khau Tien da dat o cau 1
    'db': 'iot_data',      # Database Tien da tao
    'charset': 'utf8mb4'
}

print("Bat dau doc cam bien DHT11 (GPIO17) va luu vao CSDL... (Nhan Ctrl+C de dung)")

while True:
    try:
        # Doc gia tri tu cam bien
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        
        if humidity is not None and temperature is not None:
            print(f"Doc duoc - Nhiet do: {temperature:.1f}C | Do am: {humidity:.1f}%")
            
            led_status = 0 
            
            # Ket noi vao MariaDB
            conn = pymysql.connect(**db_config)
            cursor = conn.cursor()
            
            # Cau lenh SQL INSERT du lieu vao bang
            sql = """INSERT INTO sensor_measurements (temperature, humidity, led_status) 
                     VALUES (%s, %s, %s)"""
            
            try:
                # Thuc thi lenh va luu (commit) vao DB
                cursor.execute(sql, (temperature, humidity, led_status))
                conn.commit()
                print("-> Da luu du lieu vao MariaDB thanh cong!")
            except Exception as db_error:
                print(f"Loi khi chen du lieu vao CSDL: {db_error}")
                conn.rollback()
            finally:
                cursor.close()
                conn.close()
                
    except RuntimeError as error:
        # DHT11 thi thoang doc loi nhip xung (loi nay cua phan cung, rat hay gap)
        # Chi can bo qua va cho luot doc ke tiep sau 5 giay
        print(f"Dang doc lai cam bien... ({error.args[0]})")
    except Exception as e:
        print(f"Loi he thong: {e}")
        
    # Doi 5 giay theo dung yeu cau tai lieu[cite: 1]
    time.sleep(1)
