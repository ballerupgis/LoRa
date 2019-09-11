from selenium import webdriver
import time
import pandas as pd



print("Kører...")
# LOGIN SITE

#Angiv ID på applikation

user = input("Indtast brugernavn: ")
dit_pass = input("Dit password: ")
applikation = input("Hvad er ID på applikationen? (Kig under 'Applications'.: https://iotnet.teracom.dk/application/<ID>):" )


if len(applikation) < 7:
    print("Synes ikke at være korrekt ID. Prøv igen")
    breakpoint(quit())
else:
    pass


driver = webdriver.Chrome()
driver.get("https://iotnet.teracom.dk/login")

# user
form = driver.find_element_by_xpath("/html/body/lrt-masterpage/div/lrt-login/body/div/div[2]/form/div[1]/input")
form.send_keys(str(user))

# pass
form = driver.find_element_by_xpath("/html/body/lrt-masterpage/div/lrt-login/body/div/div[2]/form/div[2]/input")
form.send_keys(str(dit_pass))
form.submit()
print("Logget ind")
time.sleep(1)

# cookies
form = driver.find_element_by_css_selector("body > lrt-masterpage > div > div > div > button").click()

# APPLICATION
#Test
driver.get("https://iotnet.teracom.dk/application/" + str(applikation))

#Som de står i dit excel
kolonne = ("DevEUI", "AppEUI", "AppKey", "DevAddr", "NwkSKey", "AppSKey")

#Læs lokal fil
df = pd.read_excel('test_keys.xlsx')
count = df['DevEUI'].count()
my_json = df.to_dict()



class sendIotKeys(object):


    try:


        def __init__(self):
            pass


        def parseFile(self):
            try:
                print(count[i])
            except:
                pass






        def enrollment(self):

           time.sleep(1)

           #Enroll device
           #parameter defineret i toppen
           driver.get("https://iotnet.teracom.dk/application/" + str(applikation)+ "/enrolldevice")
           time.sleep(1)

           #Enrollment proces
           driver.find_element_by_xpath("/html/body/lrt-masterpage/div/nsw-device-enrollment-guided/div/section/lrt-box/div/div[2]/div[1]/div/div[2]/select").click()

           #Title
           form = driver.find_element_by_name("title")
           title = my_json["DevEUI"][i]

           form.send_keys('-'.join([title[index:index+2] for index in range(0, len(title), 2)]))

           #form.send_keys((my_json["DevEUI"][i]))


           time.sleep(2)

           #DevAddr
           form = driver.find_element_by_name("devaddr")
           form.send_keys((my_json["DevAddr"][i]))

           #DevEUI
           form = driver.find_element_by_name("deveui")
           form.send_keys(my_json["DevEUI"][i])

           #Description
           form = driver.find_element_by_name("description")
           form.send_keys('-'.join([title[index:index+2] for index in range(0, len(title), 2)]))


           #Uplink
           form = driver.find_element_by_name("seqno")
           form.send_keys('1')

           #Downlink
           form = driver.find_element_by_name("seqdn")
           form.send_keys('0')
           time.sleep(1)

           #NWSKKEY
           form = driver.find_element_by_name("nwkskey")
           form.send_keys(str(my_json["NwkSKey"][i]))
           time.sleep(1)

           #APPSKEY
           form = driver.find_element_by_name("appskey")
           form.send_keys(str(my_json["AppSKey"][i]))

           #Enroll another
           driver.find_element_by_xpath("/html/body/lrt-masterpage/div/nsw-device-enrollment-guided/div/section/lrt-box/div/div[2]/div[3]/div/lrt-abp/form/div[2]/div[5]/div/div[3]/div/label").click()

           time.sleep(1)

           #ENROLL THE SUCKER
           driver.find_element_by_xpath("/html/body/lrt-masterpage/div/nsw-device-enrollment-guided/div/section/lrt-box/div/div[2]/div[3]/div/lrt-abp/form/div[2]/div[5]/div/div[2]/button").click()

           time.sleep(1)






    except:
        pass


for i in range(count):

    row = (my_json["DevEUI"][i], my_json["AppEUI"][i], my_json["AppKey"][i], my_json["DevAddr"][i], my_json["NwkSKey"][i],  my_json["AppSKey"][i])
    print(row)

    length = str(my_json["DevEUI"][i]), len(my_json["DevEUI"][i]), len(my_json["AppEUI"][i]), len(my_json["AppKey"][i]), len(my_json["DevAddr"][i]), len(my_json["NwkSKey"][i]), len(my_json["AppSKey"])
    #Tjekker om længde på tegn overholdes. Brug det til at finde fejl.
    print(length)

    iot = sendIotKeys()
    iot.parseFile()
    iot.enrollment()


#"ENROLL"
form = driver.find_element_by_css_selector("body > lrt-masterpage > div > nsw-device-enrollment-guided > div > section > lrt-box > div > div.box-body > div:nth-child(3) > div > lrt-abp > form > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(2) > button").click()
time.sleep(1)
driver.get("https://iotnet.teracom.dk/application/" + str(applikation) + "/devices")
print('Færdig')

