from flask import Flask, render_template, jsonify
import pymysql
import RPi.GPIO as GPIO

app = Flask(__name__)

# 1. Cau hinh chan GPIO cho den LED
GPIO.setmode(GPIO.BCM)
LED = 27  # Chan LED la 27 theo thuc te cua Tien
GPIO.setup(LED, GPIO.OUT)

# 2. Cau hinh dung thong tin CSDL giong het file cua Tien o Bai 2
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',  # Mat khau cua Tien o cau 1
    'db': 'iot_data',      # Database Tien da tao o Bai 1/2
    'charset': 'utf8mb4'
}

@app.route("/")
def home():
    # Ket noi vao MariaDB bang pymysql giong y chang Bai 2
    db = pymysql.connect(**db_config)
    cursor = db.cursor()

    # Lay 10 dong du lieu moi nhat tu bang sensor_measurements
    cursor.execute("""
        SELECT timestamp, temperature, humidity
        FROM sensor_measurements
        ORDER BY id DESC
        LIMIT 10
    """)

    data = cursor.fetchall()
    data = list(data)
    data.reverse()  # Dao nguoc de bieu do chay dung thu tu thoi gian tu trai sang phai

    cursor.close()
    db.close()

    labels = []
    temp = []
    hum = []

    for row in data:
        labels.append(str(row[0]))  # Lay ngay - gio (timestamp)
        temp.append(row[1])         # Lay nhiet do (temperature)
        hum.append(row[2])          # Lay do am (humidity)

    # Doc trang thai thuc te hien tai cua den LED (0 la TAT, 1 la BAT)
    led_status = GPIO.input(LED)

    return render_template(
        "index.html",
        labels=labels,
        temp=temp,
        hum=hum,
        led=led_status
    )

@app.route("/toggle")
def toggle():
    # Dao trang thai chan LED 27 thuc te
    if GPIO.input(LED):
        GPIO.output(LED, GPIO.LOW)
    else:
        GPIO.output(LED, GPIO.HIGH)

    # Tra ve trang thai LED thoi gian thuc ve cho Web bang kieu JSON
    return jsonify({"status": GPIO.input(LED)})

if __name__ == "__main__":
    # Chay Flask tren cong 5000, cho phep tat ca thiet bi cung mang ket noi qua IP cua Pi
    app.run(host="0.0.0.0", port=5000, debug=True)
