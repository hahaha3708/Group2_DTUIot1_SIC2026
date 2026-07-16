import time
import board
import adafruit_dht
from datetime import datetime

dht_sensor = adafruit_dht.DHT11(board.D4)

try:
    while True:
        try:
            nhiet_do = dht_sensor.temperature
            do_am = dht_sensor.humidity

            if nhiet_do is not None and do_am is not None:

                # Lấy thời gian hiện tại
                now = datetime.now()
                timestamp = now.strftime("%Y-%m-%d %H-%M-%S")

                # Chuỗi ghi file
                log_data = f"{timestamp} {nhiet_do:.1f}oC {do_am:.1f}%"

                # Hiển thị ra màn hình
                print(log_data)

                # Ghi vào file log.txt
                with open("log.txt", "a") as file:
                    file.write(log_data + "\n")

        except RuntimeError as error:
            print("Lỗi đọc DHT11:", error)

        time.sleep(2)

except KeyboardInterrupt:
    print("\nĐã dừng chương trình")

finally:
    dht_sensor.exit()
