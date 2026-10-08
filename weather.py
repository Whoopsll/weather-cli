from request import req

cityUrl = "https://geocoding-api.open-meteo.com/v1/search"
cityParams = {"name":"","count":1}
cityTimeout = 10

weatherUrl= "https://api.open-meteo.com/v1/forecas"
weatherParams = {"latitude":0,"longitude":0,"current_weather":True}
weatherTimeout = 10

def get_coordinates(city):
    if not city:
        print("输入不可为空")
        return None
    cityParams["name"] = city
    resp = req(cityUrl,cityParams,cityTimeout)
    if resp is None:
        print("网络错误,请稍后重试")
        return None
    data = resp.json()
    try:
        result = data["results"][0]
    except KeyError:
        print("找不到该城市")
        return None
    latitude = result["latitude"]
    longitude = result["longitude"]
    return latitude,longitude

def get_weather(latitude, longitude):
    weatherParams["latitude"] = latitude
    weatherParams["longitude"] = longitude
    resp = req(weatherUrl,weatherParams,weatherTimeout)
    if resp is None:
        print("网络错误,请稍后重试")
        return None
    data = resp.json()
    try:
        result = data["current_weather"]["temperature"]
    except KeyError:
        print("找不到地区")
        return None
    return result


if __name__ == "__main__":

    lat,lon= get_coordinates("beijing")
    tem =  get_weather(lat,lon)    

    print(f"Beijing当前温度:{tem}摄氏度")
