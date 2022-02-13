from bs4 import BeautifulSoup
import time
import re
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


def get_schedule(group):
    URL = f"https://education.khai.edu/union/schedule/group/{group}"

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver.get(URL)
    time.sleep(5)
    r = driver.page_source
    driver.close()
    # f = open('shed.html', 'r', encoding='UTF-8')
    # r = f.read()
    # f.close()

    soup = BeautifulSoup(r, 'html.parser')
    table = soup.find_all("table")[0]
    table_soup = BeautifulSoup(str(table), 'html.parser')
    tds = table_soup.find_all("td")

    schedule = {}

    day = ""
    couple_chisl = []
    couple_znam = []
    isTimeFor1 = False
    isTimeFor2 = False

    for i in tds:
        keys = i.attrs
        text = i.text

        if keys == {'class': ['py-3'], 'colspan': '3'}:
            # print("day of week")
            day = i.text

        if keys == {'class': [], 'colspan': ''}:
            # print("couple chisl")
            couple_chisl.append(i.text)

        if keys == {'class': ['x-blue'], 'colspan': ''}:
            # print("couple znam")
            couple_znam.append(i.text)
            isTimeFor2 = False

        if keys == {} and isTimeFor1 and i.text != "":
            couple_znam.append(i.text)
            couple_chisl.append(i.text)
            isTimeFor1 = False

        if keys == {'class': ['py-3'], 'colspan': '2'}:
            # print("empty couple")
            if isTimeFor1:
                couple_znam.append("empty")
                couple_chisl.append("empty")
                isTimeFor1 = False

            elif isTimeFor2:
                if len(couple_chisl) == len(couple_znam):
                    couple_chisl.append("empty")
                isTimeFor2 = False

        if keys == {'class': ['x-blue', 'py-3'], 'colspan': '2'}:
            # print("empty couple")
            couple_znam.append("empty")
            isTimeFor2 = False

        if re.fullmatch(r"\d\d:\d\d - \d\d:\d\d", text):  # 08:00 - 09:35
            if keys == {'rowspan': '2'}:
                # print("time for 2")
                isTimeFor2 = True
            else:
                # print("time")
                isTimeFor1 = True

        if len(couple_chisl) == 4 and len(couple_znam) == 4 and day != "":
            schedule[day] = {"numerator": couple_chisl, "denominator": couple_znam}
            couple_chisl = []
            couple_znam = []
            day = ""
            isTimeFor1 = False
            isTimeFor2 = False

    return schedule


if __name__ == "__main__":
    from colorama import init, Fore

    init(autoreset=True)

    schedule = get_schedule("345")
    for day in schedule.keys():
        print(day)
        for c in range(4):
            print(c + 1)
            print(schedule[day]["numerator"][c])
            print(Fore.BLUE + schedule[day]["denominator"][c])
#