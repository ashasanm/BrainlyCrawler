# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from time import sleep
import json
from .brainlyreformat import BrainlyReformat

class BrainlySpider(scrapy.Spider):
    name = 'brainly'
    allowed_domains = ['brainly.co.id']
    
    # insert url below
    start_urls = [
                'https://brainly.co.id/app/profile/1989491',
                "https://brainly.co.id/app/profile/3032811",
                "https://brainly.co.id/app/profile/109516",
                "https://brainly.co.id/app/profile/3997408",
                "https://brainly.co.id/app/profile/203667",
                "https://brainly.co.id/app/profile/6207235"
                ]

    user_datas = []

    # custom_settings = {
    #     'DOWNLOAD_TIMEOUT': 360,
    # }

    headers = {
        "authority": "api2.branch.io",
        "method": "GET",
        "Accept": "*/*",
        "scheme": "https",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "Host": "brainly.co.id",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
    }

    def start_requests(self):
        for u in BrainlySpider.start_urls:
            yield scrapy.Request(u, self.parseUser)
                
        
        

    def parseData(self, response):
        sleep(5)
        print("processing: "+ response.url)
        #loading Web Page
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = Chrome("G:\chromedriver.exe", chrome_options=chrome_options)
        driver.implicitly_wait(10)
        driver.get(response.url)
        driver.maximize_window()

        try:
            skillBtn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sg-button--transparent-light")))
            # skillBtn = driver.find_element_by_css_selector(".sg-button--transparent-light")
            skillBtn.click()

        except TimeoutException:
            pass


        sleep(5)

        sel = Selector(text=driver.page_source)
        user_name = sel.css("body > div.js-page-wrapper > div > div.js-react-single-page-entry > div > div.sg-layout__container.sg-layout__container--reversed-order.sg-layout__container--no-margin-top > div.sg-layout__aside-content.ProfilePage__asideContent--3nDME > div > div.sg-flex.sg-flex--full-width.sg-flex--align-items-center.sg-flex--column.sg-flex--margin-bottom-m > h1::text").get()
        titles = sel.css("body > div.js-page-wrapper > div > div.js-react-single-page-entry > div > div.sg-layout__container.sg-layout__container--reversed-order.sg-layout__container--no-margin-top > div.sg-layout__aside-content.ProfilePage__asideContent--3nDME > div > div.sg-flex.sg-flex--full-width.sg-flex--align-items-center.sg-flex--column.sg-flex--margin-bottom-m > div.sg-flex.sg-flex--justify-content-center.sg-flex--wrap.sg-flex--margin-top-m > div > div > div > div > div > span > div > h2::text").getall()
        total_answer = sel.css("body > div.js-page-wrapper > div > div.js-react-single-page-entry > div > div.sg-layout__container.sg-layout__container--reversed-order.sg-layout__container--no-margin-top > div.sg-layout__content.ProfilePage__container--LX_d7 > div > div.brn-fade-in-fast.UserActivity__tabsContainer--HyDe1 > div > h2.sg-text.sg-text--small.sg-text--bold.sg-text--capitalize.sg-text--no-wrap.UserActivity__tab--MjLkU.UserActivity__tabActive--cXBzw::text").getall()
        total_best = sel.css("body > div.js-page-wrapper > div > div.js-react-single-page-entry > div > div.sg-layout__container.sg-layout__container--reversed-order.sg-layout__container--no-margin-top > div.sg-layout__aside-content.ProfilePage__asideContent--3nDME > div > div.sg-flex.sg-flex--full-width.sg-flex--align-items-center.sg-flex--column.sg-flex--margin-bottom-m > div.sg-flex.sg-flex--full-width.sg-flex--justify-content-space-around.sg-flex--margin-top-m > div:nth-child(3) > div > div > div > div:nth-child(2) > div::text").getall()
        thanks = sel.css("body > div.js-page-wrapper > div > div.js-react-single-page-entry > div > div.sg-layout__container.sg-layout__container--reversed-order.sg-layout__container--no-margin-top > div.sg-layout__aside-content.ProfilePage__asideContent--3nDME > div > div.sg-flex.sg-flex--full-width.sg-flex--align-items-center.sg-flex--column.sg-flex--margin-bottom-m > div.sg-flex.sg-flex--full-width.sg-flex--justify-content-space-around.sg-flex--margin-top-m > div:nth-child(5) > div > div > div > div:nth-child(2) > div::text").getall()
        total_question = sel.css("body > div.js-page-wrapper > div > div.js-react-single-page-entry > div > div.sg-layout__container.sg-layout__container--reversed-order.sg-layout__container--no-margin-top > div.sg-layout__content.ProfilePage__container--LX_d7 > div > div.brn-fade-in-fast.UserActivity__tabsContainer--HyDe1 > div > h2:nth-child(2)::text").getall()
        total_friends = sel.css("body > div.js-page-wrapper > div > div.js-react-single-page-entry > div > div.sg-layout__container.sg-layout__container--reversed-order.sg-layout__container--no-margin-top > div.sg-layout__content.ProfilePage__container--LX_d7 > div > div.brn-fade-in-fast.UserActivity__tabsContainer--HyDe1 > div > h2:nth-child(3)::text").getall()
        subjects = sel.css("body > div.js-page-wrapper > div > div.js-react-single-page-entry > div > div.sg-layout__container.sg-layout__container--reversed-order.sg-layout__container--no-margin-top > div.sg-layout__aside-content.ProfilePage__asideContent--3nDME > div > div.sg-flex.sg-flex--full-width.sg-flex--column.sg-flex--margin-top-m > div > div > div > div > h3::text").getall()
        subject_answer = sel.css("body > div.js-page-wrapper > div > div.js-react-single-page-entry > div > div.sg-layout__container.sg-layout__container--reversed-order.sg-layout__container--no-margin-top > div.sg-layout__aside-content.ProfilePage__asideContent--3nDME > div > div.sg-flex.sg-flex--full-width.sg-flex--column.sg-flex--margin-top-m > div > div > div > div > div::text").getall()
        information_name = sel.css("body > div.js-page-wrapper > div > div.js-react-single-page-entry > div > div.sg-layout__container.sg-layout__container--reversed-order.sg-layout__container--no-margin-top > div.sg-layout__aside-content.ProfilePage__asideContent--3nDME > div > div.sg-flex.sg-flex--full-width.sg-flex--column.sg-flex--margin-top-m > div > h3 > span.sg-text.sg-text--xsmall.UserBasicInfo__userBasicText--2fC8U::text").getall()
        information_value = sel.css("body > div.js-page-wrapper > div > div.js-react-single-page-entry > div > div.sg-layout__container.sg-layout__container--reversed-order.sg-layout__container--no-margin-top > div.sg-layout__aside-content.ProfilePage__asideContent--3nDME > div > div.sg-flex.sg-flex--full-width.sg-flex--column.sg-flex--margin-top-m > div > h3 > span.sg-text.sg-text--xsmall.sg-text--bold::text").getall()
        
        sleep(10)
        

        subjects_data = dict(zip(subjects, subject_answer))
        
        information_data = dict(zip(information_name, information_value))
        reformat = BrainlyReformat()
        total_answer = reformat.transform_int(total_answer)
        total_best = reformat.transform_int(total_best)
        thanks = reformat.transform_int(thanks)
        total_question = reformat.transform_int(total_question)
        total_friends = reformat.transform_int(total_friends)
        subject_dict = reformat.subject_format(subjects_data)
        print(subject_dict)
        info_dict = reformat.information_format(information_data)

        
        scraped_info = {
            
            'url': response.url,
            'nama_pengguna': user_name,
            'title': titles,
            'pertanyaan': total_question,
            'teman': total_friends,
            'total_jawaban': total_answer,
            'total_tercerdas': total_best,
            'terima_kasih': thanks,
        }

        scraped_info.update(subject_dict)
        scraped_info.update(info_dict)

        print("\nSCRAPED INFO: ")
        yield scraped_info



        
    def parseUser(self, response):
        print("processing: "+ response.url)
        #loading Web Page
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = Chrome("G:\chromedriver.exe", chrome_options=chrome_options)
        driver.implicitly_wait(15)
        driver.get(response.url)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div[1]/div/div/h3")))
        skillBtn = driver.find_element_by_css_selector(".sg-button--transparent-light")
        skillBtn.click()

        sleep(5)
        
        friendBtn = driver.find_element_by_css_selector("h2.sg-text:nth-child(3)")
        friendBtn.click()
        
        sleep(5)
        
        moreBtn = driver.find_element_by_css_selector('.UserActivity__loadMoreButton--kYokf')
        while True:
            try:
                moreBtn.click()
                sleep(5)
            except:
                break
        
        #Extracting friend Data
        sel = Selector(text=driver.page_source)
        driver.close()
        userUrls= sel.css('body > div.js-page-wrapper > div > div.js-react-single-page-entry > div > div.sg-layout__container.sg-layout__container--reversed-order.sg-layout__container--no-margin-top > div.sg-layout__content.ProfilePage__container--LX_d7 > div > div.UserActivity__activityListContainer--7vHiZ > div.sg-flex.sg-flex--wrap.UserActivity__userFriends--igim7 > div > div > a::attr(href)').getall() 
        print("\nGETTING USER'S PROFILE !!!")
        sleep(5)
        user_names = sel.css("body > div.js-page-wrapper > div > div.js-react-single-page-entry > div > div.sg-layout__container.sg-layout__container--reversed-order.sg-layout__container--no-margin-top > div.sg-layout__content.ProfilePage__container--LX_d7 > div > div.UserActivity__activityListContainer--7vHiZ > div.sg-flex.sg-flex--wrap.UserActivity__userFriends--igim7 > div > div > a::text").getall()
        for userUrl in userUrls:
            for user_name in user_names:
                if user_name in userUrl:
                    href = userUrl.replace(user_name, '')
                    href = href.replace('-', '')
                    href = href.replace('profil', 'profile')
                    href = "/app"+ href
                    userProfile = response.urljoin(href)
                    yield response.follow(userProfile, callback=self.parseData)