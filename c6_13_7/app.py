from flask import Flask, render_template, jsonify
import mysql.connector
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

LED = 18
GPIO.setup(LED, GPIO.OUT)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="iot"
)

@app.route("/")
def home():

    cursor = db.cursor()

    cursor.execute("""
        SELECT time,temperature,humidity
        FROM sensor_data
        ORDER BY id DESC
        LIMIT 10
    """)

    data = cursor.fetchall()

    data.reverse()

    labels=[]
    temp=[]
    hum=[]

    for row in data:
        labels.append(str(row[0]))
        temp.append(row[1])
        hum.append(row[2])

    led=GPIO.input(LED)

    return render_template(
        "index.html",
        labels=labels,
        temp=temp,
        hum=hum,
        led=led
    )


@app.route("/toggle")
def toggle():

    if GPIO.input(LED):

        GPIO.output(LED,GPIO.LOW)

    else:

        GPIO.output(LED,GPIO.HIGH)

    return jsonify({"status":GPIO.input(LED)})


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
