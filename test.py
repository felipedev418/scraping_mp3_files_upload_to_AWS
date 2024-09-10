import requests
import json

# url = "http://54.190.160.237/process_audio"
# url ="http://144.202.89.110:5000/process_audio"
url = "http://192.168.123.8:5000/process_audio"
payload = {
    "url": "https://app.inquirly.com/download.php?action=iprFile&string=vqGO0qEkLqsXstEOsCXy0qE_BCE6zZ-_QZXyQ7QOwDoXLq6AzZXOzxcucZtusm4a0DGKDCF8zqeEBm8AzZ4OcZQdzmeE1RgaGPgi1ugAelejvutXGP-8GPclGCQ8vut8vRvxHY1iQqQR1qtWQme9vWF5BP1ZBC4uBCXAzXEdQP6PMq16QR4XvRbFvZI6QPsl1PIjvR161RI61RcRQRljGu8lcZjXvq-c-POiGPbaGu1x1aQyQqtl4pX9QeXILYlT"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(payload), headers=headers)
print(response.text)