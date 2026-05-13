# 👗 날씨 기반 의상 추천 슬랙 봇

매일 아침 현재 날씨를 분석하여 체감온도와 날씨 상황에 맞는 최적의 코디를 추천해주는 슬랙 봇입니다.
친한 여자친구가 보내주는 듯한 귀여운 반말 톤으로 전송됩니다!

## 주요 기능
- **체감온도 기반 추천**: 9가지 온도 카테고리에 따른 세부 의상 추천
- **특수 상황 알림**: 강풍, 고습도, 비, 눈 발생 시 맞춤형 멘트 결합
- **랜덤 메시지**: 매일 조금씩 다른 말투로 전송 (카테고리별 3개 변형)
- **한 줄 요약**: 슬랙에서 보기 편하도록 깔끔하게 한 줄로 전송

## 기술 스택
- Python 3.10+
- OpenWeatherMap API (Current Weather)
- Slack Incoming Webhook
- GitHub Actions (Scheduling)

## 설치 및 로컬 실행 방법

### 1. 레포지토리 클론 및 이동
```bash
cd outfit_bot
```

### 2. 가상환경 설정 및 패키지 설치
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
# source venv/bin/activate    # Mac/Linux
pip install -r requirements.txt
```

### 3. 환경 변수 설정
`.env.example` 파일을 복사하여 `.env` 파일을 만들고 본인의 API 키와 웹훅 URL을 입력하세요.
```bash
cp .env.example .env
```

### 4. 실행
```bash
python main.py
```

## GitHub Actions 설정
GitHub 레포지토리의 `Settings > Secrets and variables > Actions` 메뉴에서 다음 값들을 등록해야 합니다.

- `OPENWEATHER_API_KEY`: OpenWeatherMap API 키
- `SLACK_WEBHOOK_URL`: Slack 웹훅 URL

## 파일 구조
- `main.py`: 메인 실행 로직
- `weather.py`: 날씨 API 호출 모듈
- `messages.py`: 추천 로직 및 멘트 템플릿
- `slack.py`: 슬랙 메시지 발송 모듈
