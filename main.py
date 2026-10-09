from weather import get_coordinates,get_weather
from db import init_db

init_db()
 
while True:
    city = input("请输入城市名(history 查看历史,q 退出):").strip().split()
    if not city:
        continue 
    if city[0] == "history":
        print("历史记录:")

    elif city[0] == "q":
        print("即将退出程序...")
        break
    else:
        coordinates = get_coordinates(city)
        if coordinates is not None:
            weather = get_weather(coordinates[0],coordinates[1])
            if weather is not None:
                print(f"{city[0]}当前温度:{weather}°C")


# latlon = get_coordinates(city)
# if latlon is not None:
#     result = get_weather(latlon[0],latlon[1])
#     if result is not None:
#         print(f"{city}当前温度:{result}°C")