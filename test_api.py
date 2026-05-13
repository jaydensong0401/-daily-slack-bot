import requests

def test_weather_api():
    print("=== OpenWeatherMap API 디버깅 ===")
    api_key = input("발급받으신 OpenWeatherMap API 키를 붙여넣어 주세요 (숨김처리 안됨): ").strip()
    
    if not api_key:
        print("API 키가 입력되지 않았습니다.")
        return

    lat = 37.4654
    lon = 126.9436
    
    # 1. 예전 2.5 일반 날씨 API 테스트
    print("\n[테스트 1] 일반 Current Weather API (무료 기본 제공)")
    url_current = f"https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid={api_key}"
    res_current = requests.get(url_current)
    print(f"상태 코드: {res_current.status_code}")
    print(f"응답 결과: {res_current.text}")
    
    # 2. One Call 3.0 API 테스트
    print("\n[테스트 2] One Call API 3.0 (결제 구독 필요)")
    url_onecall = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}"
    res_onecall = requests.get(url_onecall)
    print(f"상태 코드: {res_onecall.status_code}")
    print(f"응답 결과: {res_onecall.text}")
    
    print("\n=== 분석 가이드 ===")
    if res_onecall.status_code == 200:
        print("✅ API 키가 정상적으로 3.0 버전을 지원합니다! (이 경우 깃허브 Secrets에 키가 잘못 입력되었을 확률이 높습니다.)")
    elif res_current.status_code == 200 and res_onecall.status_code == 401:
        print("⚠️ 일반 날씨 API는 되지만, One Call 3.0은 막혀있습니다.")
        print("이 경우, OpenWeatherMap 홈페이지에서 [Billing plans] -> [One Call by Call] 메뉴의 'Subscribe' 버튼을 누르셨는지 확인해주세요. (결제 카드만 등록하고 구독 버튼을 안 누르면 이 에러가 납니다.)")
    else:
        print("❌ 둘 다 안 된다면, API 키 복사가 잘못되었거나 아직 키가 활성화되지 않은 것입니다. (가입/발급 후 최대 2시간 소요)")

if __name__ == "__main__":
    test_weather_api()
