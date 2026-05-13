import random

# 카테고리별 멘트 템플릿
MESSAGES = {
    "EXTREMELY_COLD": [ # -10 이하
        "🧊 오늘 진짜 냉동고 수준이야!! 롱패딩, 목도리, 장갑 무조건 다 챙겨!! 히트텍 안 입으면 후회한다ㅠ",
        "❄️ 와.. 진짜 역대급 추위야!! 롱패딩 필수고 얼굴까지 다 꽁꽁 싸매고 나가!! 알겠지??",
        "🧣 오늘 밖에 나가면 얼어 죽을지도 몰라.. 패딩 중에 제일 두꺼운 거 입고 장갑도 꼭 챙겨!!"
    ],
    "COLD": [ # -10 ~ 0
        "🧊 오늘 패딩 입어 감기 걸려!! 체감 온도가 너무 낮아ㅠ 목도리랑 장갑도 다 챙겨!!",
        "❄️ 날씨 실화야? 너무 춥다!! 두꺼운 코트나 패딩 꼭 입고 따뜻하게 입고 나가!!",
        "🧣 오늘은 진짜 겨울 느낌!! 따뜻한 외투 챙기고 감기 조심해야 돼!!"
    ],
    "CHILLY": [ # 0 ~ 9
        "🍂 오늘 쌀쌀해!! 코트 입고 나가야 할걸? 니트까지 받쳐 입으면 딱 좋을 것 같아!!",
        "🧥 꽤 쌀쌀하니까 도톰한 자켓이나 코트 챙겨!! 멋 부리다 얼어 죽어!!",
        "🧣 오늘은 코트 각이다!! 따뜻한 니트랑 같이 매치해서 입고 나가자!!"
    ],
    "SLIGHTLY_CHILLY": [ # 9 ~ 12
        "🧥 오늘은 트렌치코트나 가디건 입기 딱 좋아!! 살짝 쌀쌀하니까 겉옷 꼭 챙겨!!",
        "🧣 가디건 하나 걸치고 나가!! 아침저녁으론 꽤 쌀쌀하니까 방심 금물!!",
        "🍂 트렌치코트 꺼낼 시간이야!! 분위기 있게 입고 나가보자!!"
    ],
    "COOL": [ # 12 ~ 17
        "🍃 가디건이나 얇은 자켓 하나 걸쳐!! 낮엔 더울 수도 있으니까 벗기 편한 거로!!",
        "🧥 오늘 날씨 선선하고 좋다!! 얇은 겉옷 하나만 챙기면 완벽할 듯!!",
        "🎀 얇은 자켓이나 가디건 챙겨 나가!! 일교차 조심하고!!"
    ],
    "MODERATE": [ # 17 ~ 20
        "✨ 오늘 날씨 너무 좋아!! 얇은 가디건에 긴팔이나 반팔 매치해서 입어봐!!",
        "🌸 딱 기분 좋은 날씨야!! 가벼운 가디건 하나면 충분할 것 같아!!",
        "🎀 오늘 코디는 가볍게!! 얇은 겉옷 하나만 가방에 쏙 넣어 가!!"
    ],
    "WARM": [ # 20 ~ 23
        "🌸 오늘 반팔 입어도 될 것 같아!! 얇은 가디건 하나만 가방에 챙겨!!",
        "✨ 날씨가 따뜻해졌어!! 가벼운 반팔 차림에 혹시 모르니 얇은 셔츠 하나 어때??",
        "☀️ 기분 좋게 따뜻한 날씨!! 오늘은 시원하게 입고 나가도 좋아!!"
    ],
    "HOT": [ # 23 ~ 27
        "☀️ 오늘 좀 덥다!! 반팔 반바지 입어도 충분해!! 시원하게 입고 나가!!",
        "🔥 벌써 더워지네ㅠ 오늘은 통기성 좋은 옷으로 입고 나가는 거 추천!!",
        "🩳 오늘 코디는 반팔로!! 가볍고 시원하게 입고 하루 시작하자!!"
    ],
    "EXTREMELY_HOT": [ # 27 이상
        "☀️ 오늘 반팔 반바지 입어!! 겉옷은 무거우니 두고 가!! 진짜 덥다ㅠ",
        "🔥 와.. 오늘 찜통이야!! 제일 시원한 옷 골라 입고 물 많이 마셔!!",
        "🥵 오늘 진짜 더워!! 무조건 반팔 반바지!! 통기성 좋은 옷이 최고야!!"
    ]
}

# 추가 상황 멘트
EXTRA_MESSAGES = {
    "WIND_STRONG": "💨 오늘 바람 개-강함!! 겉옷 꼭 챙겨 기온보다 훨씬 춥게 느껴질 거야!!",
    "WIND_MODERATE": "💨 오늘 바람 좀 부니까 조심해!! 머리 다 망가질 수도ㅠ",
    "HUMID_HOT": "💦 오늘 습해서 더 덥게 느껴질 거야.. 땀 잘 흡수되는 시원한 옷 입어!!",
    "RAIN": "☔ 우산!! 오늘 비 와!! 우산 챙겨 또 편의점 가서 우산 사기 싫으면!!",
    "SNOW": "❄️ 눈 온다고!! 롱패딩 입고 굽 있는 신발은 오늘 패스해 미끄러져!!"
}

def get_outfit_recommendation(weather_data):
    feels_like = weather_data["feels_like"]
    temp = weather_data["temp"]
    wind_speed = weather_data["wind_speed"]
    humidity = weather_data["humidity"]
    weather_main = weather_data["weather_main"]
    
    # 1. 체감온도 기반 카테고리 결정
    if feels_like <= -10:
        category = "EXTREMELY_COLD"
    elif -10 < feels_like <= 0:
        category = "COLD"
    elif 0 < feels_like <= 9:
        category = "CHILLY"
    elif 9 < feels_like <= 12:
        category = "SLIGHTLY_CHILLY"
    elif 12 < feels_like <= 17:
        category = "COOL"
    elif 17 < feels_like <= 20:
        category = "MODERATE"
    elif 20 < feels_like <= 23:
        category = "WARM"
    elif 23 < feels_like <= 27:
        category = "HOT"
    else:
        category = "EXTREMELY_HOT"
        
    # 2. 메인 멘트 선택
    main_msg = random.choice(MESSAGES[category])
    
    # 3. 추가 상황 결합
    extras = []
    
    # 비/눈 (메인 대체 또는 결합 - 여기서는 결합으로 처리)
    if weather_main == "Rain" or weather_main == "Drizzle" or weather_main == "Thunderstorm":
        extras.append(EXTRA_MESSAGES["RAIN"])
    elif weather_main == "Snow":
        extras.append(EXTRA_MESSAGES["SNOW"])
        
    # 바람
    if wind_speed >= 10:
        extras.append(EXTRA_MESSAGES["WIND_STRONG"])
    elif wind_speed >= 5:
        extras.append(EXTRA_MESSAGES["WIND_MODERATE"])
        
    # 습도 + 더위
    if humidity >= 80 and temp >= 23:
        extras.append(EXTRA_MESSAGES["HUMID_HOT"])
        
    # 모든 멘트 합치기
    final_msg = main_msg
    if extras:
        final_msg = f"{main_msg} {' '.join(extras)}"
        
    # 한 줄로 정리 (모든 개행 제거)
    final_msg = final_msg.replace("\n", " ").strip()
    
    # 핵심 수치 및 마무리 이모지
    # 예: [메인멘트] — 서울 16°C 🎀
    # 바람이나 비 정보도 포함하면 좋음
    city = weather_data["city"]
    final_output = f"{final_msg} — {city} {round(temp, 1)}°C {get_footer_emoji(category)}"
    
    return final_output

def get_footer_emoji(category):
    emojis = {
        "EXTREMELY_COLD": "❄️",
        "COLD": "❄️",
        "CHILLY": "🧣",
        "SLIGHTLY_CHILLY": "🧥",
        "COOL": "🎀",
        "MODERATE": "✨",
        "WARM": "🌸",
        "HOT": "🩳",
        "EXTREMELY_HOT": "🔥"
    }
    return emojis.get(category, "✨")
