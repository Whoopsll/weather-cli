from weather import get_coordinates,get_weather
 
city = input("请输入要查询的城市英文名称:").strip()
latlon = get_coordinates(city)
if latlon is not None:
    result = get_weather(latlon[0],latlon[1])
    if result is not None:
        print(f"{city}当前温度:{result}°C")