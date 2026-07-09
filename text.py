sudo apt install build-essential ruby-dev -y
sudo gem install mqtt
require 'mqtt'

# Cau hinh ket noi toi Broker cuc bo tren Raspberry Pi
BROKER_HOST = '127.0.0.1'
TOPIC = 'pbl/chat_room'

puts "--- CHUONG TRINH CHAT MQTT ---"
print "Nhap ten cua ban: "
username = gets.chomp

# Luong 1: LANG NGHE tin nhan moi tu Broker
Thread.new do
  MQTT::Client.connect(BROKER_HOST) do |client|
    client.get(TOPIC) do |topic, message|
      # Chi in tin nhan neu no khong phai do chinh minh gui
      if !message.start_with?("[#{username}]")
        puts "\n#{message}"
        print "[#{username}]: " # Giu lai prompt nhap lieu
      end
    end
  end
end

# Luong 2: GUI tin nhan tu ban phim len Broker
MQTT::Client.connect(BROKER_HOST) do |client|
  loop do
    print "[#{username}]: "
    msg = gets.chomp
    next if msg.empty?
    
    break if msg.downcase == 'exit'
    
    client.publish(TOPIC, "[#{username}]: #{msg}")
  end
end