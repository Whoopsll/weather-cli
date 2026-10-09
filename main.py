from weather import get_coordinates,get_weather
from db import init_db,save_query,get_history

init_db()

def query_history():
    print("历史记录:")
    history = get_history()
    if not history:
        print("暂无查询记录")
        return
    for city,temp,queried_at in history:
        print(queried_at,city,temp)
    

def query_save_city_weather(city):
    coordinates = get_coordinates(city)
    if coordinates is not None:
        weather = get_weather(coordinates[0],coordinates[1])
        if weather is not None:
            print(f"{city}当前温度:{weather}°C")
            if not save_query(city,weather):
                print("系统故障,记录保存失败")
            else:
                print("查询已保存到历史记录中")
    
 
while True:
    city = input("请输入城市名(history 查看历史,q 退出):").strip()
    if not city:
        continue 
    if city == "history":
        query_history()
    elif city == "q":
        print("即将退出程序...")
        break
    else:
        query_save_city_weather(city)

        
