import qrcode

ssid = "Nama_WiFi_Kamu"
password = "Password_WiFi_Kamu"
auth_type = "WPA"  # WPA, WEP, atau nopass

# Format protokol standar Wi-Fi QR
payload = f"WIFI:T:{auth_type};S:{ssid};P:{password};;"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)
qr.add_data(payload)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("wifi_access.png")
print("QR Code tersimpan sebagai 'wifi_access.png'. Scan menggunakan kamera HP!")