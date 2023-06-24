import requests
from bs4 import BeautifulSoup
import datetime

WHITE = "\033[0;37m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
ORANGE = "\033[0;33m"
PINK = "\033[1;31m"
BLUE = "\033[0;34m"
PURPLE = '\033[95m'
DARKCYAN = '\033[36m'
YELLOW = '\033[93m'
RED = '\033[91m'
BLACK = "\033[0;30m"
MAGENTA = "\033[0;35m"
BRIGHT_BLACK = "\033[0;90m"
BRIGHT_RED = "\033[0;91m"
BRIGHT_GREEN = "\033[0;92m"
BRIGHT_YELLOW = "\033[0;93m"
BRIGHT_BLUE = "\033[0;94m"
BRIGHT_MAGENTA = "\033[0;95m"
BRIGHT_CYAN = "\033[0;96m"
BRIGHT_WHITE = "\033[0;97m"
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

# print(BOLD + 'This text is bold!' + END)
# print(PINK + "Hello World" + END)

print(ORANGE + BOLD + "\nHello 👋\n" + END)

# Current Month Name

month = datetime.datetime.now().strftime('%B')
# print (month)

# Today's date
today = int(datetime.datetime.now().strftime('%d'))

today1 = today
today2 = today + 1
today3 = today + 2
today4 = today + 3
today5 = today + 4
today6 = today + 5
today7 = today + 6
today8 = today + 7
today9 = today + 8
today10 = today + 9
today11 = today + 10
today12 = today - 20
today13 = today - 19
today14 = today - 18
# print(today14)

# BBC Riyadh import
Riyadh_page = requests.get('https://www.bbc.com/weather/108410')
soup1 = BeautifulSoup(Riyadh_page.content, 'html.parser')
week1 = soup1.find(class_='wr-day-carousel__list wr-js-day-carousel-list clearfix')
# day1 = week1.find_all(class_= 'wr-day wr-day--0 wr-js-day  wr-day--active')
tempmax1 = [item.find(class_='wr-value--temperature--c').get_text() for item in week1]
tempmin1 = [item1.find(class_='wr-day-temperature__low-value').get_text() for item1 in week1]
desc1 = [item.find(
    class_='wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque').get_text()
         for item in week1]

# BBC Los Angeles weather import
Los_Angeles_page = requests.get('https://www.bbc.com/weather/5368361')
soup2 = BeautifulSoup(Los_Angeles_page.content, 'html.parser')
week2 = soup2.find(class_='wr-day-carousel__list wr-js-day-carousel-list clearfix')
# day1 = week1.find_all(class_= 'wr-day wr-day--0 wr-js-day  wr-day--active')
tempmax2 = [item2.find(class_='wr-value--temperature--c').get_text() for item2 in week2]
tempmin2 = [item2.find(class_='wr-day-temperature__low-value').get_text() for item2 in week2]
desc2 = [item2.find(
    class_='wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque').get_text()
         for item2 in week2]

# BBC Hyderabad weather import
Hyderabad_page = requests.get('https://www.bbc.com/weather/1269843')
soup3 = BeautifulSoup(Hyderabad_page.content, 'html.parser')
week3 = soup3.find(class_='wr-day-carousel__list wr-js-day-carousel-list clearfix')
# day3 = week1.find_all(class_= 'wr-day wr-day--0 wr-js-day  wr-day--active')
tempmax3 = [item3.find(class_='wr-value--temperature--c').get_text() for item3 in week3]
tempmin3 = [item3.find(class_='wr-day-temperature__low-value').get_text() for item3 in week3]
desc3 = [item3.find(
    class_='wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque').get_text()
         for item3 in week3]
#print(tempmin3[1])

# BBC Dubai weather import
Dubai_page = requests.get('https://www.bbc.com/weather/292223')
soup4 = BeautifulSoup(Dubai_page.content, 'html.parser')
week4 = soup4.find(class_='wr-day-carousel__list wr-js-day-carousel-list clearfix')
# day4 = week1.find_all(class_= 'wr-day wr-day--0 wr-js-day  wr-day--active')
tempmax4 = [item4.find(class_='wr-value--temperature--c').get_text() for item4 in week4]
tempmin4 = [item4.find(class_='wr-day-temperature__low-value').get_text() for item4 in week4]
desc4 = [item4.find(
    class_='wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque').get_text()
         for item4 in week4]

#  Asking yes or no
yesno = input(CYAN + BOLD + "\nDo you want the weather of the world 🌞  ⛱️  🌩️  (y/n)? : " + END)
yesno = yesno.lower()

# Riyadh

if yesno == "y":
    city = input(WHITE + BOLD + UNDERLINE + "\nWhich city of the world do you want get the weather (Riyadh, Los Angeles(LA), Hyderabad, Dubai)?: \n" + END)
    city = city.lower()
    if city == "riyadh":
        day1r = input(BLUE + BOLD + "\nPlease type date of the day that you wanted to get the weather 🗓️  (Ex: " + str(
            today1) + "): \n" + END)
        short_desc = input(BLUE + BOLD + '\nDo you need the Short Description of this day? 📙  (y/n): ' + END)
        short_desc = short_desc.lower()
        if day1r == str(today1):
            if short_desc == 'y':
                print(PINK + BOLD + (desc1[0]) + END)
            elif short_desc == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁 ' + END)
            minmax1 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            minmax1 = minmax1.lower()
            if minmax1 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1r + ' ' + month + " = " + tempmax1[
                        0] + " Celsius." + END)
            elif minmax1 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1r + month + " = " + (
                tempmin1[0][0:3]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1r == str(today2):
            if short_desc == 'y':
                print(PINK + BOLD + (desc1[1]) + END)
            elif short_desc == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax1 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax1 == "max":
                print(PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1r + ' ' + month + " = " + tempmax1[
                        1] + " Celsius." + END)
            elif minmax1 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1r + ' ' + month + " = " + (
                tempmin1[1][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1r == str(today3):
            if short_desc == 'y':
                print(PINK + BOLD + (desc1[2]) + END)
            elif short_desc == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax1 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax1 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1r + ' ' + month + " = " + tempmax1[
                        2] + " Celsius." + END)
            elif minmax1 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1r + ' ' + month + " = " + (
                tempmin1[2][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1r == str(today4):
            if short_desc == 'y':
                print(PINK + BOLD + (desc1[3]) + END)
            elif short_desc == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax1 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax1 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1r + ' ' + month + " = " + tempmax1[
                        3] + " Celsius." + END)
            elif minmax1 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1r + + ' ' + month + " = " + (
                tempmin1[3][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1r == str(today5):
            if short_desc == 'y':
                print(PINK + BOLD + (desc1[4]) + END)
            elif short_desc == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax1 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈   or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax1 == "max":
                print(PINK + BOLD + "\nHere is the maximum 📈  temperature of " + day1r + ' ' + month + " = " + tempmax1[
                        4] + " Celsius." + END)
            elif minmax1 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1r + ' ' + month + " = " + (
                tempmin1[4][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1r == str(today6):
            if short_desc == 'y':
                print(PINK + BOLD + (desc1[5]) + END)
            elif short_desc == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax1 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax1 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1r + ' ' + month + " = " + tempmax1[
                        5] + " Celsius." + END)
            elif minmax1 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1r + ' ' + month + " = " + (
                tempmin1[5][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min or max  📈. " + END)

        elif day1r == str(today7):
            if short_desc == 'y':
                print(PINK + BOLD + (desc1[6]) + END)
            elif short_desc == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax1 = input(PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax1 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1r + ' ' + month + " = " + " Celsius." + END)
            elif minmax1 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1r + ' ' + month + " = " + (
                tempmin1[6][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1r == str(today8):
            if short_desc == 'y':
                print(PINK + BOLD + (desc1[7]) + END)
            elif short_desc == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax1 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax1 == "max":
                print(PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1r + ' ' + month + " = " + tempmax1[
                        7] + " Celsius." + END)
            elif minmax1 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1r + ' ' + month + " = " + (
                tempmin1[7][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1r == str(today9):
            if short_desc == 'y':
                print(PINK + BOLD + (desc1[8]) + END)
            elif short_desc == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax1 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax1 == "max":
                print(PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1r + ' ' + month + " = " + tempmax1[
                        8] + " Celsius." + END)
            elif minmax1 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1r + ' ' + month + " = " + (
                tempmin1[8][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈." + END)

        elif day1r == str(today10):
            if short_desc == 'y':
                print(PINK + BOLD + (desc1[9]) + END)
            elif short_desc == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax1 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax1 == "max":
                print(PINK + BOLD + "\nHere is the maximum temperature 📈   of " + day1r + ' ' + month + " = " + tempmax1[
                        9] + " Celsius." + END)
            elif minmax1 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1r + ' ' + month + " = " + (
                tempmin1[9][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + " \nPlease type min 📉  or max 📈." + END)

        elif day1r == str(today11):
            if short_desc == 'y':
                print(PINK + BOLD + (desc1[10]) + END)
            elif short_desc == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax1 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax1 == "max":
                print(PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1r + ' ' + month + " = " + tempmax1[
                        10] + " Celsius." + END)
            elif minmax1 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1r + ' ' + month + " = " + (
                tempmin1[10][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈" + END)

        elif day1r == str(today12):
            if short_desc == 'y':
                print(PINK + BOLD + (desc1[11]) + END)
            elif short_desc == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax1 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax1 == "max":
                print(PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1r + ' ' + month + " = " + tempmax1[
                        11] + " Celsius." + END)
            elif minmax1 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1r + ' ' + month + " = " + (
                tempmin1[11][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1r == str(today13):
            if short_desc == 'y':
                print(PINK + BOLD + (desc1[12]) + END)
            elif short_desc == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax1 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax1 == "max":
                print(PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1r + ' ' + month + " = " + tempmax1[
                        12] + " Celsius." + END)
            elif minmax1 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1r + ' ' + month + " = " + (
                tempmin1[12][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1r == str(today14):
            if short_desc == 'y':
                print(PINK + BOLD + (desc1[13]) + END)
            elif short_desc == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax1 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax1 == "max":
                print(PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1r + ' ' + month + " = " + tempmax1[
                        13] + " Celsius." + END)
            elif minmax1 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1r + ' ' + month + " = " + (
                tempmin1[13][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        else:
            print(RED + BOLD + "\nOnly type in the date! (ex: 19). " + END)

    # Dubai

    elif city == "dubai":
        day1d = input(BLUE + BOLD + "\nPlease type date of the day that you wanted to get the weather 🗓️  (Ex: " + str(
            today1) + "): \n" + END)
        short_desc4 = input(BLUE + BOLD + '\nDo you need the Short Description of this day? 📙  (y/n): ' + END)
        short_desc4 = short_desc4.lower()
        if day1d == str(today1):
            if short_desc4 == 'y':
                print(PINK + BOLD + (desc4[0]) + END)
            elif short_desc4 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁 ' + END)
            minmax4 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            minmax4 = minmax4.lower()
            if minmax4 == "max":
                print(PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1d + ' ' + month + " = " + tempmax4[
                        0] + " Celsius." + END)
            elif minmax4 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + + day1d + ' ' + month + " = " + (
                tempmin4[0][0:3]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1d == str(today2):
            if short_desc4 == 'y':
                print(PINK + BOLD + (desc4[1]) + END)
            elif short_desc4 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax4 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax4 == "max":
                print(PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1d + ' ' + month + " = " + tempmax4[
                        1] + " Celsius." + END)
            elif minmax4 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1d + ' ' + month + " = " + (
                tempmin4[1][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1d == str(today3):
            if short_desc4 == 'y':
                print(PINK + BOLD + (desc4[2]) + END)
            elif short_desc4 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax4 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax4 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1d + ' ' + month + " = " + tempmax4[
                        2] + " Celsius." + END)
            elif minmax4 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1d + ' ' + month + " = " + (
                tempmin4[2][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1d == str(today4):
            if short_desc4 == 'y':
                print(PINK + BOLD + (desc4[3]) + END)
            elif short_desc4 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax4 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax4 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1d + ' ' + month + " = " + tempmax4[
                        3] + " Celsius." + END)
            elif minmax4 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1d + ' ' + month + " = " + (
                tempmin4[3][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1d == str(today5):
            if short_desc4 == 'y':
                print(PINK + BOLD + (desc4[4]) + END)
            elif short_desc4 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax4 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈   or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax4 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum 📈  temperature of " + day1d + ' ' + month + " = " + tempmax4[
                        4] + " Celsius." + END)
            elif minmax4 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1d + ' ' + month + " = " + (
                tempmin4[4][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1d == str(today6):
            if short_desc4 == 'y':
                print(PINK + BOLD + (desc4[5]) + END)
            elif short_desc4 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax4 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax4 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1d + ' ' + month + " = " + tempmax4[
                        5] + " Celsius." + END)
            elif minmax4 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1d + ' ' + month + " = " + (
                tempmin4[5][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min or max  📈. " + END)

        elif day1d == str(today7):
            if short_desc4 == 'y':
                print(PINK + BOLD + (desc4[6]) + END)
            elif short_desc4 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax4 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax4 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1d + ' ' + month + " = " + tempmax4[
                        6] + " Celsius." + END)
            elif minmax4 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1d + ' ' + month + " = " + (
                tempmin4[6][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1d == str(today8):
            if short_desc4 == 'y':
                print(PINK + BOLD + (desc4[7]) + END)
            elif short_desc4 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax4 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax4 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1d + ' ' + month + " = " + tempmax4[
                        7] + " Celsius." + END)
            elif minmax4 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + + day1d + ' ' + month + " = " + (
                tempmin4[7][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1d == str(today9):
            if short_desc4 == 'y':
                print(PINK + BOLD + (desc4[8]) + END)
            elif short_desc4 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax4 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax4 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1d + ' ' + month + " = " + tempmax4[
                        8] + " Celsius." + END)
            elif minmax4 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1d + ' ' + month + " = " + (
                tempmin4[8][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈." + END)

        elif day1d == str(today10):
            if short_desc4 == 'y':
                print(PINK + BOLD + (desc4[9]) + END)
            elif short_desc4 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax4 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax4 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈   of " + day1d + ' ' + month + " = " + tempmax4[
                        9] + " Celsius." + END)
            elif minmax4 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1d + ' ' + month + " = " + (
                tempmin4[9][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + " \nPlease type min 📉  or max 📈." + END)

        elif day1d == str(today11):
            if short_desc4 == 'y':
                print(PINK + BOLD + (desc4[10]) + END)
            elif short_desc4 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax4 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax4 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1d + ' ' + month + " = " + tempmax4[
                        10] + " Celsius." + END)
            elif minmax4 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1d + ' ' + month + " = " + (
                tempmin4[10][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈" + END)

        elif day1d == str(today12):
            if short_desc4 == 'y':
                print(PINK + BOLD + (desc1[11]) + END)
            elif short_desc4 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax4 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax4 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1d + ' ' + month + " = " + tempmax4[
                        11] + " Celsius." + END)
            elif minmax4 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1d + ' ' + month + " = " + (
                tempmin4[11][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1d == str(today13):
            if short_desc4 == 'y':
                print(PINK + BOLD + (desc4[12]) + END)
            elif short_desc4 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax4 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax4 == "max":
                print(PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1d + ' ' + month + " = " + tempmax4[
                        12] + " Celsius." + END)
            elif minmax4 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1d + ' ' + month + " = " + (
                tempmin4[12][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1d == str(today14):
            if short_desc4 == 'y':
                print(PINK + BOLD + (desc4[13]) + END)
            elif short_desc4 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax4 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            if minmax4 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1d + ' ' + month + " = " + tempmax4[
                        13] + " Celsius." + END)
            elif minmax4 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1d + ' ' + month + " = " + (
                tempmin4[13][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)
        else:
            print(RED + BOLD + "\nOnly type in the valid date in less than two weeks from present!  (Example-" + str(
                today1) + ")" + END)

    # Los Angeles

    elif city == "la":
        day1L = input(BLUE + BOLD + "\nPlease type date of the day that you wanted to get the weather 🗓️  (Ex: " + str(
            today1) + "): \n" + END)
        short_desc2 = input(BLUE + BOLD + '\nDo you need the Short Description of this day? 📙  (y/n): ' + END)
        short_desc2 = short_desc2.lower()
        if day1L == str(today1):
            if short_desc2 == 'y':
                print(PINK + BOLD + (desc2[0]) + END)
            elif short_desc2 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁 ' + END)
            minmax2 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            minmax2 = minmax2.lower()
            if minmax2 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1L + ' ' + month + " = " + tempmax2[
                        0] + " Celsius." + END)
            elif minmax2 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + + day1L + ' ' + month + " = " + (
                tempmin2[0][0:3]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1L == str(today2):
            if short_desc2 == 'y':
                print(PINK + BOLD + (desc2[1]) + END)
            elif short_desc2 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax2 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax2 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1L + ' ' + month + " = " + tempmax2[
                        1] + " Celsius." + END)
            elif minmax2 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1L + ' ' + month + " = " + (
                tempmin2[1][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1L == str(today3):
            if short_desc2 == 'y':
                print(PINK + BOLD + (desc2[2]) + END)
            elif short_desc2 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax2 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax2 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1L + ' ' + month + " = " + tempmax2[
                        2] + " Celsius." + END)
            elif minmax2 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1L + ' ' + month + " = " + (
                tempmin2[2][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1L == str(today4):
            if short_desc2 == 'y':
                print(PINK + BOLD + (desc2[1]) + END)
            elif short_desc2 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax2 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax2 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1L + ' ' + month + " = " + tempmax2[
                        3] + " Celsius." + END)
            elif minmax2 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1L + ' ' + month + " = " + (
                tempmin2[3][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1L == str(today5):
            if short_desc2 == 'y':
                print(PINK + BOLD + (desc2[4]) + END)
            elif short_desc2 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax2 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax2 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1L + ' ' + month + " = " + tempmax2[
                        4] + " Celsius." + END)
            elif minmax2 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1L + ' ' + month + " = " + (
                tempmin2[4][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1L == str(today6):
            if short_desc2 == 'y':
                print(PINK + BOLD + (desc2[5]) + END)
            elif short_desc2 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax2 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax2 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1L + ' ' + month + " = " + tempmax2[
                        5] + " Celsius." + END)
            elif minmax2 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1L + ' ' + month + " = " + (
                tempmin2[5][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1L == str(today7):
            if short_desc2 == 'y':
                print(PINK + BOLD + (desc2[6]) + END)
            elif short_desc2 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax2 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax2 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1L + ' ' + month + " = " + tempmax2[
                        6] + " Celsius." + END)
            elif minmax2 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1L + ' ' + month + " = " + (
                tempmin2[6][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1L == str(today8):
            if short_desc2 == 'y':
                print(PINK + BOLD + (desc2[7]) + END)
            elif short_desc2 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax2 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax2 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1L + ' ' + month + " = " + tempmax2[
                        7] + " Celsius." + END)
            elif minmax2 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1L + ' ' + month + " = " + (
                tempmin2[7][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1L == str(today9):
            if short_desc2 == 'y':
                print(PINK + BOLD + (desc2[8]) + END)
            elif short_desc2 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax2 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax2 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1L + ' ' + month + " = " + tempmax2[
                        8] + " Celsius." + END)
            elif minmax2 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1L + ' ' + month + " = " + (
                tempmin2[8][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1L == str(today10):
            if short_desc2 == 'y':
                print(PINK + BOLD + (desc2[9]) + END)
            elif short_desc2 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax2 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax2 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1L + ' ' + month + " = " + tempmax2[
                        9] + " Celsius." + END)
            elif minmax2 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1L + ' ' + month + " = " + (
                tempmin2[9][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1L == str(today11):
            if short_desc2 == 'y':
                print(PINK + BOLD + (desc2[10]) + END)
            elif short_desc2 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax2 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax2 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1L + ' ' + month + " = " + tempmax2[
                        10] + " Celsius." + END)
            elif minmax2 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1L + ' ' + month + " = " + (
                tempmin2[10][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1L == str(today12):
            if short_desc2 == 'y':
                print(PINK + BOLD + (desc2[11]) + END)
            elif short_desc2 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax2 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax2 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1L + ' ' + month + " = " + tempmax2[
                        11] + " Celsius." + END)
            elif minmax2 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1L + ' ' + month + " = " + (
                tempmin2[11][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1L == str(today13):
            if short_desc2 == 'y':
                print(PINK + BOLD + (desc2[12]) + END)
            elif short_desc2 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax2 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax2 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1L + ' ' + month + " = " + tempmax2[
                        12] + " Celsius." + END)
            elif minmax2 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1L + ' ' + month + " = " + (
                tempmin2[12][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1L == str(today14):
            if short_desc2 == 'y':
                print(PINK + BOLD + (desc2[13]) + END)
            elif short_desc2 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax2 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax2 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1L + ' ' + month + " = " + tempmax2[
                        13] + " Celsius." + END)
            elif minmax2 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1L + ' ' + month + " = " + (
                tempmin2[13][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)
        else:
            print(RED + BOLD + "\nOnly type in the valid date in less than two weeks from present!  (Example-" + str(
                today1) + ")" + END)

    # Hyderabad

    elif city == "hyderabad":
        day1h = input(BLUE + BOLD + "\nPlease type date of the day that you wanted to get the weather 🗓️  (Ex: " + str(
            today1) + "): \n" + END)
        short_desc3 = input(BLUE + BOLD + '\nDo you need the Short Description of this day? 📙  (y/n): ' + END)
        short_desc3 = short_desc3.lower()
        if day1h == str(today1):
            if short_desc3 == 'y':
                print(PINK + BOLD + (desc3[0]) + END)
            elif short_desc3 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁 ' + END)
            minmax3 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉  temperature of the day? (min/max): \n" + END)
            minmax3 = minmax3.lower()
            if minmax3 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1h + ' ' + month + " = " + tempmax3[
                        0] + " Celsius." + END)
            elif minmax3 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉  of " + day1h + ' ' + month + " = " + (
                tempmin3[0][0:3]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1h == str(today2):
            if short_desc3 == 'y':
                print(PINK + BOLD + (desc3[1]) + END)
            elif short_desc3 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax3 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax3 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1h + ' ' + month + " = " + tempmax3[
                        1] + " Celsius." + END)
            elif minmax3 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1h + ' ' + month + " = " + (
                tempmin3[1][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1h == str(today3):
            if short_desc3 == 'y':
                print(PINK + BOLD + (desc3[2]) + END)
            elif short_desc3 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax3 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax3 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1h + ' ' + month + " = " + tempmax3[
                        2] + " Celsius." + END)
            elif minmax3 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1h + ' ' + month + " = " + (
                tempmin3[2][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1h == str(today4):
            if short_desc3 == 'y':
                print(PINK + BOLD + (desc3[3]) + END)
            elif short_desc3 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax3 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax3 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1h + ' ' + month + " = " + tempmax3[
                        3] + " Celsius." + END)
            elif minmax3 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1h + ' ' + month + " = " + (
                tempmin3[3][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1h == str(today5):
            if short_desc3 == 'y':
                print(PINK + BOLD + (desc3[4]) + END)
            elif short_desc3 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax3 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax3 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1h + ' ' + month + " = " + tempmax3[
                        4] + " Celsius." + END)
            elif minmax3 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1h + ' ' + month + " = " + (
                tempmin3[4][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1h == str(today6):
            if short_desc3 == 'y':
                print(PINK + BOLD + (desc3[5]) + END)
            elif short_desc3 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax3 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax3 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1h + ' ' + month + " = " + tempmax3[
                        5] + " Celsius." + END)
            elif minmax3 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1h + ' ' + month + " = " + (
                tempmin3[5][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1h == str(today7):
            if short_desc3 == 'y':
                print(PINK + BOLD + (desc3[6]) + END)
            elif short_desc3 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax3 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax3 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1h + ' ' + month + " = " + tempmax3[
                        6] + " Celsius." + END)
            elif minmax3 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1h + ' ' + month + " = " + (
                tempmin3[6][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1h == str(today8):
            if short_desc3 == 'y':
                print(PINK + BOLD + (desc3[7]) + END)
            elif short_desc3 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax3 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax3 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1h + ' ' + month + " = " + tempmax3[
                        7] + " Celsius." + END)
            elif minmax3 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1h + ' ' + month + " = " + (
                tempmin3[7][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1h == str(today9):
            if short_desc3 == 'y':
                print(PINK + BOLD + (desc3[8]) + END)
            elif short_desc3 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax3 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax3 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1h + ' ' + month + " = " + tempmax3[
                        8] + " Celsius." + END)
            elif minmax3 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1h + ' ' + month + " = " + (
                tempmin3[8][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1h == str(today10):
            if short_desc3 == 'y':
                print(PINK + BOLD + (desc3[9]) + END)
            elif short_desc3 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax3 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax3 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1h + ' ' + month + " = " + tempmax3[
                        9] + " Celsius." + END)
            elif minmax3 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1h + ' ' + month + " = " + (
                tempmin3[9][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1h == str(today11):
            if short_desc3 == 'y':
                print(PINK + BOLD + (desc3[10]) + END)
            elif short_desc3 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax3 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax3 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1h + ' ' + month + " = " + tempmax3[
                        10] + " Celsius." + END)
            elif minmax3 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1h + ' ' + month + " = " + (
                tempmin3[10][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1h == str(today12):
            if short_desc3 == 'y':
                print(PINK + BOLD + (desc3[11]) + END)
            elif short_desc3 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax3 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax3 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1h + ' ' + month + " = " + tempmax3[
                        1] + " Celsius." + END)
            elif minmax3 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1h + ' ' + month + " = " + (
                tempmin3[11][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1h == str(today13):
            if short_desc3 == 'y':
                print(PINK + BOLD + (desc3[12]) + END)
            elif short_desc3 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax3 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax3 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1h + ' ' + month + " = " + tempmax3[
                        12] + " Celsius." + END)
            elif minmax3 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1h + ' ' + month + " = " + (
                tempmin3[12][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        elif day1h == str(today14):
            if short_desc3 == 'y':
                print(PINK + BOLD + (desc3[13]) + END)
            elif short_desc3 == 'n':
                print(GREEN + BOLD + 'Ok, Let\'s continue with the weather! 🔁' + END)
            minmax3 = input(
                PURPLE + BOLD + "\nDo you want the maximum 📈  or minimum 📉   temperature of the day? (min/max): \n" + END)
            if minmax3 == "max":
                print(
                    PINK + BOLD + "\nHere is the maximum temperature 📈  of " + day1h + ' ' + month + " = " + tempmax3[
                        13] + " Celsius." + END)
            elif minmax3 == "min":
                print(PINK + BOLD + "\nHere is minimum temperature 📉   of " + day1h + ' ' + month + " = " + (
                tempmin3[13][0:4]) + " Celsius." + END)
            else:
                print(RED + BOLD + "\nPlease type min 📉  or max 📈. " + END)

        else:
            print(RED + BOLD + "\nOnly type in the valid date in less than two weeks from present!  (Example-" + str(
                today1) + ")" + END)

    else:
        print(RED + BOLD + "Please type the country's name as given." + END)

elif yesno == "n":
    print(CYAN + BOLD + UNDERLINE + "Fine, Will see you next time! 🙂" + END)