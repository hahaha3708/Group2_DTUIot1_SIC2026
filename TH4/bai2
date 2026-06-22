import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

# Khởi tạo các danh sách để lưu dữ liệu bóc tách được
timestamps = []
temperatures = []
humidities = []

# Đọc file log.txt tạo ra từ Bài 1
try:
    with open("log.txt", "r") as file:
        for line in file:
            # Tách dòng thành các phần tử dựa vào khoảng trắng
            parts = line.strip().split()
            
            # Kiểm tra dòng hợp lệ (phải có đủ ít nhất 4 phần tử)
            if len(parts) >= 4:
                try:
                    # 1. Xử lý Thời gian (Ghép ngày và giờ)
                    time_str = f"{parts[0]} {parts[1]}"
                    time_obj = datetime.strptime(time_str, "%Y-%m-%d %H-%M-%S")
                    
                    # 2. Xử lý Nhiệt độ (Bỏ chữ 'oC' và chuyển sang số thực)
                    temp_val = float(parts[2].replace("oC", ""))
                    
                    # 3. Xử lý Độ ẩm (Bỏ dấu '%' và chuyển sang số thực)
                    hum_val = float(parts[3].replace("%", ""))
                    
                    # Nếu không có lỗi gì, thêm dữ liệu vào danh sách
                    timestamps.append(time_obj)
                    temperatures.append(temp_val)
                    humidities.append(hum_val)
                except ValueError:
                    # Bỏ qua những dòng bị lỗi định dạng hoặc lỗi cảm biến đọc sai chữ
                    continue

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'log.txt'. Hãy chạy Bài 1 trước để sinh dữ liệu!")
    exit()

# Kiểm tra nếu file có dữ liệu nhưng không bóc tách được gì
if not timestamps:
    print("File log.txt trống hoặc dữ liệu bên trong không hợp lệ.")
    exit()

# --- TIẾN HÀNH VẼ ĐỒ THỊ ---
plt.figure(figsize=(12, 6))

# Vẽ đường Nhiệt độ (Màu đỏ, nét liền, có chấm tròn tại các điểm dữ liệu)
plt.plot(timestamps, temperatures, label="Nhiệt độ (°C)", color="red", marker="o", linestyle="-")

# Vẽ đường Độ ẩm (Màu xanh dương, nét liền, có hình vuông tại các điểm dữ liệu)
plt.plot(timestamps, humidities, label="Độ ẩm (%)", color="blue", marker="s", linestyle="-")

# Cấu hình tiêu đề và nhãn các trục
plt.title("ĐỒ THỊ BIẾN THIÊN NHIỆT ĐỘ & ĐỘ ẨM THEO THỜI GIAN", fontsize=14, fontweight="bold")
plt.xlabel("Thời gian (Giờ:Phút:Giây)", fontsize=11)
plt.ylabel("Giá trị đo được", fontsize=11)

# Định dạng hiển thị trục X (Thời gian) cho đẹp và không bị chồng chữ
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
plt.gcf().autofmt_xdate() # Tự động xoay nghiêng ngày tháng/giờ giấc

# Bật lưới tọa độ và chú thích (Legend)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(loc="upper right")

# Hiển thị đồ thị lên màn hình
plt.tight_layout()
plt.show()
