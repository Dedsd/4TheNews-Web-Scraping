import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.common import exceptions as selenium_err
from selenium.webdriver.firefox.options import Options
import discord
from discord.ext import commands
from threading import Thread
import os
import csv
import random

token = "YOUR_TOKEN"

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    Thread(name="webdriver", target=web).run()
    print(f"{client.user} is in the server!")


driver = None

# You have to modify this according to your webdriver
def web():
    global driver
    options = webdriver.ChromeOptions()
    driver = webdriver.Firefox()
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome("", chrome_options=Options)
    driver.set_window_position(-10000, 0)
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "none"
    print('WebBrowser is ready!')

# First news
def get_first_news():
    driver.maximize_window()
    driver.get("https://www.cnnbrasil.com.br/")
    firstimage = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/main/div/div/div[1]/section/div/a/article/div/picture/img")
    firstimage40 = (firstimage.get_attribute('src'))
    first = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/main/div/div/div[1]/section/div/a/article/h2')
    title = first.text
    first.click()
    firstsubtitle = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div[1]/main/article/header/h2').text
    firsturl = driver.current_url
    return {
        "title": title,
        "firstsubtitle": firstsubtitle,
        "firstimage": firstimage40,
        "firsturl": firsturl,
    }

print("----------------------------------- SECOND NEWS -----------------------------------")

# Second news
def get_second_news():
    driver.maximize_window()
    driver.get("https://www.bbc.com/portuguese")
    element = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/header/div[1]/div/div/ul/li[1]")))
    cookies = driver.find_element_by_xpath("/html/body/div[2]/div/header/div[1]/div/div/ul/li[1]")
    cookies.click()
    second = driver.find_element_by_xpath("/html/body/div[2]/div/div/main/div/section[1]/div[2]/ul/li[1]/div/div[2]/h3/a")
    secondtitle = second.text
    print(secondtitle)
    secondsubtitle = driver.find_element_by_xpath("/html/body/div[2]/div/div/main/div/section[1]/div[2]/ul/li[1]/div/div[2]/p").text
    print(secondsubtitle)
    second.click()
    element19 = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[1]/main/div[3]/figure/div/div[1]/div/img")))
    secondimage = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/main/div[3]/figure/div/div[1]/div/img")
    secondimage40 = (secondimage.get_attribute('src'))
    secondurl = driver.current_url
    return {
        "secondtitle": secondtitle,
        "secondsubtitle": secondsubtitle,
        "secondimage40": secondimage40,
        "secondurl": secondurl,
    }

print("----------------------------------- THIRD NEWS -----------------------------------")

# Third news
def get_third_news():
    driver.maximize_window()
    driver.get("https://www.cnnbrasil.com.br/tecnologia")
    element = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/main/div/div/div[2]/section/div/a/article/div[2]/h2")))
    time.sleep(1)
    third = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/main/div/div/div[2]/section/div/a/article/div[2]/h2")
    thirdtitle = third.text
    thirdimage = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/main/div/div/div[2]/section/div/a/article/div[1]/picture/img")
    print(thirdtitle)
    thirdimg1 = thirdimage.get_attribute("src")
    print(thirdimg1)
    thirdimage.click()
    time.sleep(2)
    element = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[3]/div[1]/main/article/header/h2")))
    thirdsubtitle = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div[1]/main/article/header/h2').text
    print(thirdsubtitle)
    thirdurl = driver.current_url
    return {
        "thirdtitle": thirdtitle,
        "thirdsubtitle": thirdsubtitle,
        "thirdimage": thirdimg1,
        "thirdurl": thirdurl,
    }

print("----------------------------------- FOURTH NEWS -----------------------------------")

# Fourth news
def get_fourth_news():
    driver.maximize_window()
    driver.get("https://www.bbc.com/portuguese/topics/c404v027pd4t")
    element4 = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[9]/div[2]/div[2]/div/div/div/div/div[1]/ol/li[1]/article/header/div/h3/a/span")))
    fourth = driver.find_element_by_xpath("/html/body/div[2]/div[9]/div[2]/div[2]/div/div/div/div/div[1]/ol/li[1]/article/header/div/h3/a/span")
    fourthtitle = fourth.text
    print(fourthtitle)
    element4 = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[9]/div[2]/div[2]/div/div/div/div/div[1]/ol/li[1]/article/div[2]/div/div[2]/p")))
    fourthsubtitle = driver.find_element_by_xpath("/html/body/div[2]/div[9]/div[2]/div[2]/div/div/div/div/div[1]/ol/li[1]/article/div[2]/div/div[2]/p").text
    print(fourthsubtitle)
    fourth.click()
    element4 = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/header/div[1]/div/div/ul/li[1]")))
    cookies4 = driver.find_element_by_xpath("/html/body/div[2]/div/header/div[1]/div/div/ul/li[1]")
    cookies4.click()
    element20 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[1]/main/div[3]/figure/div/div[1]/div/img")))
    fourthimage = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/main/div[3]/figure/div/div[1]/div/img")
    fourthimage3 = (fourthimage.get_attribute('src'))
    print(fourthimage3)
    fourthurl = driver.current_url
    print(fourthurl)
    return {
        "fourthtitle": fourthtitle,
        "fourthsubtitle": fourthsubtitle,
        "fourthimage3": fourthimage3,
        "fourthurl": fourthurl,
    }

# Discord bot
@client.event
async def on_message(message):
    msgcnt = message.content
    print(message.content)
    cmmnd = msgcnt.startswith("!4news")
    if cmmnd:
        await message.channel.send("**Aguarde um pouco, até as notícias serem computadas.**")
        first_news = get_first_news()
        print("yes------------------------------------------------------------")
        second_news = get_second_news()
        print("yes-------------------------------------------------------------")
        third_news = get_third_news()
        print("yes------------------------------------------------------------")
        fourth_news = get_fourth_news()
        print("yes------------------------------------------------------------")
        driver.delete_all_cookies()
        embedfirstnews = discord.Embed( 
            title=f'**{first_news["title"]}**',
            description=f'{first_news["firstsubtitle"]}',
            colour=discord.Colour.dark_blue()
            )
        embedfirstnews.set_footer(text=' https://github.com/Dedsd/4TheNews-Web-Scraping ')
        embedfirstnews.set_image(url=f'{first_news["firstimage"]}')
        embedfirstnews.set_thumbnail(url='https://www.sferalabs.cc/wp-content/uploads/github-logo-white.png')
        embedfirstnews.set_author(name="Feito por Dedsd")
        embedfirstnews.add_field(name=f'**Veja a notícia: {first_news["firsturl"]}**', value=f'-', inline=True)
        await message.channel.send(embed=embedfirstnews)
        embedsecondnews = discord.Embed( 
            title=f'**{second_news["secondtitle"]}**',
            description=f'{second_news["secondsubtitle"]}',
            colour=discord.Colour.dark_blue()
            )
        embedsecondnews.set_footer(text=' https://github.com/Dedsd/4TheNews-Web-Scraping ')
        embedsecondnews.set_image(url=f'{second_news["secondimage40"]}')
        embedsecondnews.set_thumbnail(url='https://www.sferalabs.cc/wp-content/uploads/github-logo-white.png')
        embedsecondnews.set_author(name="Feito por Dedsd")
        embedsecondnews.add_field(name=f'**Veja a notícia: {second_news["secondurl"]}**', value=f'-', inline=True)
        await message.channel.send(embed=embedsecondnews)
        embedthirdnews = discord.Embed( 
            title=f'**{third_news["thirdtitle"]}**',
            description=f'{third_news["thirdsubtitle"]}',
            colour=discord.Colour.dark_blue()
            )
        embedthirdnews.set_footer(text=' https://github.com/Dedsd/4TheNews-Web-Scraping ')
        embedthirdnews.set_image(url=f'{third_news["thirdimage"]}')
        embedthirdnews.set_thumbnail(url='https://www.sferalabs.cc/wp-content/uploads/github-logo-white.png')
        embedthirdnews.set_author(name="Feito por Dedsd")
        embedthirdnews.add_field(name=f'**Veja a notícia: {third_news["thirdurl"]}**', value=f'-', inline=True)
        await message.channel.send(embed=embedthirdnews)
        embedfourthnews = discord.Embed( 
            title=f'**{fourth_news["fourthtitle"]}**',
            description=f'{fourth_news["fourthsubtitle"]}',
            colour=discord.Colour.dark_blue()
            )
        embedfourthnews.set_footer(text=' https://github.com/Dedsd/4TheNews-Web-Scraping ')
        embedfourthnews.set_image(url=f'{fourth_news["fourthimage3"]}')
        embedfourthnews.set_thumbnail(url='https://www.sferalabs.cc/wp-content/uploads/github-logo-white.png')
        embedfourthnews.set_author(name="Feito por Dedsd")
        embedfourthnews.add_field(name=f'**Veja a notícia: {fourth_news["fourthurl"]}**', value=f'-', inline=True)
        await message.channel.send(embed=embedfourthnews)
client.run(token)