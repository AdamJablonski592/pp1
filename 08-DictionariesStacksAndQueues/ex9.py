mobile_phone = {
    "manufacturer": "Nokia",
    "on_sale": True,
    "price": 245,
    "availability": ["Walmart", "BestBuy"],
    "size": {"big": "9", "small": "7"},
    "serial_number": 151353165
}

for item in mobile_phone.items():
    print(item[0].capitalize(), ":", item[1])