from collectors.google_trends import get_trends_data
from notifier.slack import send_slack_message
from datetime import datetime

def main():
    print(f"🚀 Bot started at {datetime.now()}")
    
    # 1. Collect Data
    trends = get_trends_data()
    
    # 2. Format Message
    message = "📢 *오늘의 구글 트렌드 리포트 (최근 7일)*\n\n"
    
    if trends["rising"]:
        message += "🔥 *급상승/상위 검색어 (3페이지 합계):*\n"
        # Display top 15 unique items for brevity
        for i, item in enumerate(trends["rising"][:15], 1):
            message += f"{i}. {item}\n"
    else:
        message += "데이터를 불러오지 못했습니다.\n"
        
    message += f"\n⏰ 수집 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    # 3. Send to Slack
    send_slack_message(message)

if __name__ == "__main__":
    main()
