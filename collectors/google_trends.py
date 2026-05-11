from pytrends.request import TrendReq

def get_trends_data():
    try:
        # pytrends 설정 (한국 지역: KR, 시간대: 540은 KST)
        pytrends = TrendReq(hl='ko-KR', tz=540)
        
        # 실시간 인기 검색어(Trending Searches) 가져오기
        # 'south_korea' 지역 설정
        df = pytrends.trending_searches(pn='south_korea')
        
        # 리스트로 변환
        results = {"rising": df[0].tolist()}
        
        print(f"✅ pytrends 수집 완료: {len(results['rising'])}개 항목")
        return results
        
    except Exception as e:
        print(f"❌ pytrends 에러 발생: {e}")
        return {"rising": []}
