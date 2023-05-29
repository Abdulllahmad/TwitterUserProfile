#####YOU KNOW WHAT HAPPENS HERE####


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def get_twitter_profile_details(username):
    # Set up Selenium
    options = Options()
    options.headless = True  # Run Chrome in headless mode
    service = Service('path_to_chromedriver')  # Replace with the path to chromedriver executable
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Load the profile page
        driver.get(f"https://twitter.com/{username}")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "main")))

        # Extract the page source
        page_source = driver.page_source

        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(page_source, "html.parser")

        # Get the profile details
        username = soup.find("span", {"class": "css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"}).text
        
        num_tweets_element = soup.find("a", {"href": f"/{username}/tweets"})
        num_tweets = int(num_tweets_element.find("span", {"class": "css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"}).text.replace(",", "")) if num_tweets_element else None

        num_followers = int(soup.find("a", {"class": "css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-1wbh5a2 r-dnmrzs r-1ny4l3l"}).find_all("span")[0].text.replace(",", ""))
        join_date = soup.find("a", {"class": "css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-1wbh5a2 r-dnmrzs r-1ny4l3l"}).find_all("span")[1]["title"]

        return {
            "Username": username,
            "Number of Tweets": num_tweets,
            "Number of Followers": num_followers,
            "Join Date": join_date
        }

    finally:
        driver.quit()


# Example usage
username = input("Enter the Twitter username: ")
profile_details = get_twitter_profile_details(username)
print(profile_details)
