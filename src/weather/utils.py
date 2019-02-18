import requests
import re


def get_img_code(img):
    img_url = f'http://openweathermap.org/img/w/{img}.png'
    respon_img = requests.get(img_url)
    print(respon_img.status_code)
    if respon_img.status_code == 200:
        return img_url
    return respon_img.status_code

def get_citys_weather(apikey,citys,units_format='metric',lang='en_us'):
    weather_data = []
    for city in citys:
        # search chinese
        zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')
        result = zh_pattern.search(city)
        if result: # is china weather 
            cn_url = f'https://www.tianqiapi.com/api/?version=v1&city={city}'   
            respon = requests.get(cn_url).json()
            icon = respon['data'][0]['wea_img']
            weather = {
            'name':respon['city'],
            'description':respon['data'][0]['wea'],
            'icon':f'weather/img/icon/{icon}.png',
            'temp':respon['data'][0]['tem'].replace('℃',''),
            'img_static':True
            }
        else:    
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units={units_format}&lang={lang}&appid={apikey}'
            respon = requests.get(url).json()
            if respon['cod'] == '404':
                continue
            weather = {
                'name':respon['name'],
                'description':respon['weather'][0]['description'],
                'icon':respon['weather'][0]['icon'],
                'temp':respon['main']['temp']
            }
        weather_data.append(weather)
    return weather_data