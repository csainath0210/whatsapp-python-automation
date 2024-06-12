from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

xl_file = pd.read_excel(
    'contactAndMessage.xlsx', 
    sheet_name=None,
    usecols=['Contact Number', 'Message']
    )

data = []
for index in xl_file:
    df = xl_file[index]
    for i in df.index:
        data.append([str(df['Contact Number'][i]),str(df['Message'][i])])

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')
input("Press ENTER after login into Whatsapp Web and your chats are visiable.")
for item in data:
    contact = item[0]
    message = item[1]
    try:
        url = 'https://web.whatsapp.com/send?phone={}&text={}'.format(contact, message)

        sent = False
        driver.get(url)
        try:
            click_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']")))
        except Exception as e:
            print("Sorry message could not sent to " + str(contact))
        else:
            sleep(2)
            # Moves the cursor the the message bar in Whatsapp
            click_btn.click()
            sent = True
            sleep(5)
            print('Message sent to: ' + str(contact))

    except Exception as e:
        print('Failed to send message to ' + str(contact) + str(e))

print("The script executed successfully.")