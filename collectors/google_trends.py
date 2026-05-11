import requests
import xml.etree.ElementTree as ET

def get_trends_data():
    # 구글 트렌드 한국 지역 공식 RSS 피드 주소
    url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=KR"
    
    # 봇 차단을 막기 위한 브라우저 위장 헤더
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/rss+xml, application/xml, text/xml"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        # 만약 XML이 아니라 차단 페이지(HTML)가 떴을 경우를 확인
        if response.status_code != 200:
            print(f"❌ 접속 실패: 상태 코드 {response.status_code}")
            return {"rising": []}
            
        # XML(RSS) 데이터 파싱
        root = ET.fromstring(response.text)
        
        trends_list = []
        # 각 트렌드 항목(item)에서 제목(title)만 추출
        for item in root.findall('.//item'):
            title = item.find('title').text
            if title:
                trends_list.append(title)
                
        results = {"rising": trends_list}
        return results
        
    except Exception as e:
        print(f"❌ RSS 수집 실패: {e}")
        return {"rising": []}
