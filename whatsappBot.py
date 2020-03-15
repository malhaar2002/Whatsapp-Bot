from selenium import webdriver
from time import sleep
from datetime import datetime

chromedriver = r"C:\Users\Malhaar\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)

thumbs_up = """"░░░░░░░░░░░░▄▄░░░░░░░░░
░░░░░░░░░░░█░░█░░░░░░░░
░░░░░░░░░░░█░░█░░░░░░░░
░░░░░░░░░░█░░░█░░░░░░░░
░░░░░░░░░█░░░░█░░░░░░░░
███████▄▄█░░░░░██████▄░░
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
▓▓▓▓▓▓█████░░░░░░░░░█░░
██████▀░░░░▀▀██████▀░░░░"""

bruh = """

██████╗░██████╗░██╗░░░██╗██╗░░██╗
██╔══██╗██╔══██╗██║░░░██║██║░░██║
██████╦╝██████╔╝██║░░░██║███████║
██╔══██╗██╔══██╗██║░░░██║██╔══██║
██████╦╝██║░░██║╚██████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝"""

idk = """¯\_(ツ)_/¯"""

FuckYou = """┌∩┐(◣_◢)┌∩┐"""

What = """≧☉_☉≦"""

Marja = """█▬█ █ ▀█▀"""

Hmmm = """( ⚆ _ ⚆ )"""

I_See = """ಠ_ಠ"""

Crazy = """╚(ಠ_ಠ)=┐"""

Bc = """ლ(ಠ益ಠლ)"""

Abbe = """(─‿‿─)"""

Badiya = """☜(˚▽˚)☞"""

CoolBoi = """(▀̿Ĺ̯▀̿ ̿)"""

driver.get("https://web.whatsapp.com/")
sleep(5)

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").send_keys("bot")
sleep(1.5)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[2]").click()

def bot():
    list1 = []
    resultSet = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div")
    options = resultSet.find_elements_by_class_name("X7YrQ")

    for option in options:
        list1.append(option.text)
    print(list1)

    for item in list1:
        if "Best of luck" in item:
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(thumbs_up)
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]").click()

        if "Bruh" in item:
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(bruh)
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]").click()

        if "Idk" in item:
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(idk)
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]").click()

        if "Fuck you" in item:
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(FuckYou)
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]").click()

        if "What" in item:
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(What)
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]").click()

        if "Marja" in item:
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(Marja)
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]").click()

        if "Hmmm" in item:
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(Hmmm)
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]").click()

        if "I see" in item:
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(I_See)
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]").click()

        if "crazy" in item:
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(Crazy)
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]").click()

        if "Bc" in item:
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(Bc)
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]").click()

        if "Abbe" in item:
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(Abbe)
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]").click()

        if "Badiya" in item:
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(Badiya)
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]").click()

        if "Cool boi" in item:
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(CoolBoi)
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]").click()



while True:
    bot()
    sleep(2)
