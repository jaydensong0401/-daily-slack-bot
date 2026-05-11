import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def get_trends_data():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    url = "https://trends.google.co.kr/explore?geo=KR&date=now%207-d"
    driver.get(url)
    
    # Wait for initial load
    time.sleep(5)
    
    results = {"rising": [], "top": []}
    
    try:
        # Widgets usually contain 'Rising' and 'Top'
        # The user provided classes: fG3KIc (text), pYTkkf-Bz112c-RLmnJb (button)
        
        # Helper to scrape 3 pages
        def scrape_pages(section_name):
            data = []
            for page in range(3):
                # Wait for elements
                elements = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, "fG3KIc"))
                )
                
                # Filter elements based on context if possible, but for now just collect
                page_items = [el.text for el in elements if el.text.strip()]
                data.extend(page_items)
                
                # If not the last page, click next
                if page < 2:
                    try:
                        next_buttons = driver.find_elements(By.CLASS_NAME, "pYTkkf-Bz112c-RLmnJb")
                        # Usually there are multiple widgets (related queries, related topics)
                        # We might need to click the specific one. 
                        # For simplicity, we'll try to find the button in the relevant widget.
                        # This part is tricky without exact DOM mapping, but we'll use the user's provided class.
                        if next_buttons:
                            # Try to click the last one or iterate? 
                            # Google Trends usually has Rising/Top for both Topics and Queries.
                            # We'll click the one that's clickable.
                            driver.execute_script("arguments[0].click();", next_buttons[-1]) 
                            time.sleep(2)
                    except Exception as e:
                        print(f"Pagination error: {e}")
                        break
            return list(set(data)) # Unique items

        # Scrape default (usually Rising)
        results["rising"] = scrape_pages("rising")
        
        # Switch to 'Top' if possible? 
        # Usually there's a dropdown. The user didn't provide the dropdown class.
        # But for now, we'll collect what's visible with the class provided.
        
    except Exception as e:
        print(f"Scraping error: {e}")
    finally:
        driver.quit()
        
    return results

if __name__ == "__main__":
    print(get_trends_data())
