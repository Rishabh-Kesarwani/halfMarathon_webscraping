from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# define the website to scrape and path where the chromediver is located
website = 'https://alpharacingsolution.com/event/result/232f9d60-fae8-4a4a-a96c-384b0cc2e387?noheader=true#nav-result'
# path = '/Users/frankandrade/Downloads/chromedriver'  # write your path here
# service = Service(executable_path=path)  # selenium 4
# driver = webdriver.Chrome(service=service)  # define 'driver' variable
# open Google Chrome with chromedriver
driver.get(website)
driver.maximize_window()

# locate and click on a button
# all_matches_button = driver.find_element(by='xpath', value='//label[@analytics-event="All matches"]')
# all_matches_button.click()

# # select dropdown and select element inside by visible text
dropdown = Select(driver.find_element(by='id', value='RaceCats'))
dropdown.select_by_visible_text('10 KM')
dropdown = Select(driver.find_element(by='id', value='AgeCategory'))
dropdown.select_by_visible_text('All')
time.sleep(1)
dropdown = Select(driver.find_element(by='name', value='tblResult_length'))
dropdown.select_by_visible_text('100')
# # implicit wait (useful in JavaScript driven websites when elements need seconds to load and avoid error "ElementNotVisibleException")
time.sleep(1)



# Pagination 1
pagination = driver.find_element(by='xpath',value='//ul[contains(@class, "pagination")]')  # locating pagination bar
pages = pagination.find_elements(by='tag name',value='li')  # locating each page displayed in the pagination bar
last_page = int(pages[-2].text)  # getting the last page with negative indexing (starts from where the array ends)

current_page = 1

# storage data in lists
bib_no = []
name = []
category = []
gun_time = []
category_rank=[]
gender_rank=[]
overall_rank=[]
status=[]
certificate=[]
race_category=[]

while current_page <= last_page:
    time.sleep(1)
    print(current_page)

    # select elements in the table
    rows = driver.find_elements(by='xpath', value='//*[@id="tblResult"]/tbody/tr')
    
    # looping through the matches list
    for row in rows:
        bib_no.append(int((row.find_element(by='xpath', value='./td[1]/a')).text))
        # element = row.find_element('xpath',value='./td[1]/a')
        # text = element.text
        # print(text)
        Name = row.find_element(by='xpath', value='./td[2]').text
        name.append(Name)
        # print(Name)
        category.append(row.find_element(by='xpath', value='./td[3]').text)
        gun_time.append(row.find_element(by='xpath', value='./td[4]').text)
        category_rank.append(row.find_element(by='xpath', value='./td[5]').text)
        gender_rank.append(row.find_element(by='xpath', value='./td[6]').text)
        overall_rank.append(row.find_element(by='xpath', value='./td[7]').text)
        status.append(row.find_element(by='xpath', value='./td[8]').text)
        race_category.append(10)
    # certificate.append((row.find_element(by='xpath', value='./td[9]//text()')).text)
    current_page = current_page + 1  # increment the current_page by 1 after the data is extracted
    # Locating the next_page button and clicking on it. If the element isn't on the website, pass to the next iteration
    try:
        next_page = driver.find_element(by='xpath',value=".//li[contains(@class,'paginate_button page-item next')]")
        next_page.click()
    except:
        pass

driver.quit()


# Create Dataframe in Pandas and export to CSV (Excel)
df = pd.DataFrame({'bib_no': bib_no, 'name': name, 'category': category, 'gun_time': gun_time,'category_rank':category_rank,'gender_rank': gender_rank, 'name': name, 'overall_rank': overall_rank, 'status': status,'race_category':race_category})
# df = pd.DataFrame({'bib_no': bib_no, 'name': name, 'category': category, 'gun_time': gun_time,'category_rank':category_rank,'gender_rank': gender_rank, 'name': name, 'overall_rank': overall_rank, 'status': status})
# df = pd.DataFrame({ 'name': name, 'category': category, 'gun_time': gun_time,'category_rank':category_rank,'gender_rank': gender_rank, 'name': name, 'overall_rank': overall_rank, 'status': status})
df.to_csv('10Km_data.csv', index=False)

# select elements in the table
# rows = driver.find_elements(by='xpath', value='//*[@id="tblResult"]/tbody/tr')


# # storage data in lists
# bib_no = []
# name = []
# category = []
# gun_time = []
# category_rank=[]
# gender_rank=[]
# overall_rank=[]
# status=[]
# certificate=[]

# # looping through the matches list
# for row in rows:
#     bib_no.append(int((row.find_element(by='xpath', value='./td[1]/a')).text))
#     # element = row.find_element('xpath',value='./td[1]/a')
#     # text = element.text
#     # print(text)
#     Name = row.find_element(by='xpath', value='./td[2]').text
#     name.append(Name)
#     # print(Name)
#     category.append(row.find_element(by='xpath', value='./td[3]').text)
#     gun_time.append(row.find_element(by='xpath', value='./td[4]').text)
#     category_rank.append(row.find_element(by='xpath', value='./td[5]').text)
#     gender_rank.append(row.find_element(by='xpath', value='./td[6]').text)
#     overall_rank.append(row.find_element(by='xpath', value='./td[7]').text)
#     status.append(row.find_element(by='xpath', value='./td[8]').text)
#     # certificate.append((row.find_element(by='xpath', value='./td[9]//text()')).text)

# # # quit drive we opened at the beginning
# driver.quit()
# # print(bib_no)
# # Create Dataframe in Pandas and export to CSV (Excel)
# df = pd.DataFrame({'bib_no': bib_no, 'name': name, 'category': category, 'gun_time': gun_time,'category_rank':category_rank,'gender_rank': gender_rank, 'name': name, 'overall_rank': overall_rank, 'status': status})
# # df = pd.DataFrame({ 'name': name, 'category': category, 'gun_time': gun_time,'category_rank':category_rank,'gender_rank': gender_rank, 'name': name, 'overall_rank': overall_rank, 'status': status})
# # # df.to_csv('football_data.csv', index=False)
# print(df)
    