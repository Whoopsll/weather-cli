from weather import get_coordinates,get_weather
from db import init_db,save_query,get_history

init_db()
 
while True:
    city = input("请输入城市名(history 查看历史,q 退出):").strip().split()
    if not city:
        continue 
    if city[0] == "history":
        print("历史记录:")
        history = get_history()
        if not history:
            print("暂无查询记录")
            continue 
        for history in get_history():
            print(history)
    elif city[0] == "q":
        print("即将退出程序...")
        break
    else:
        coordinates = get_coordinates(city)
        if coordinates is not None:
            weather = get_weather(coordinates[0],coordinates[1])
            if weather is not None:
                print(f"{city[0]}当前温度:{weather}°C")
                if not save_query(city[0],weather):
                    print("系统故障,记录保存失败")
                    continue
                print("查询已保存到历史记录中")
