#Group Charming P* - Exam Group with Peter, Marco, Rune and Myself- assignment FBI_Dataset - Arkadiusz

import matplotlib as mpl
mpl.use('TkAgg') #Code ran fine on my Windows pc but had to change framework settings to _macosx to run on my laptop
import pandas as pd
import webget as wg
import re
from collections import Counter


url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/twitter-ratio/realDonaldTrump.csv'
url1 = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/twitter-ratio/BarackObama.csv'
# Datasets start with the lines: created_at,text,url,replies,retweets,favorites,user.
# Not sure if these are meant to be columns or?
# Dataset columns used are 1 and 6. 1 being Text, 6 being Users.

response = wg.download(url)
response1 = wg.download(url1)
print(response + response1, "downloaded")


dataFrame = pd.read_csv('realDonaldTrump.csv', encoding='UTF-16')
dataFrame2 = pd.read_csv('BarackObama.csv', encoding='UTF-16')
obama_matrix = dataFrame2.as_matrix() #Converting frame to numpy-array using pandas.
donald_matrix = dataFrame.as_matrix()


def question_1():
    count = Counter(donald_matrix[:, 6])
    print("Question 1:")
    print(sum(count.values()))


def question_2():
    count = Counter(obama_matrix[:, 6])
    print("Question 2:")
    print(sum(count.values()))


def question_3():
    obama_text = ''.join(obama_matrix[:, 1]).lower()
    obama_count = [m.start() for m in re.finditer('yes we can', obama_text)]
    obama_count2 = [m.start() for m in re.finditer('yeswecan', obama_text)]
    # Assurring we get the correct count

    donald_text = ''.join(donald_matrix[:, 1]).lower()
    donald_count = [m.start() for m in re.finditer('makeamericagreatagain', donald_text)]
    donald_count2 = [m.start() for m in re.finditer('make america great again', donald_text)]
    # Assuring we get the correct count.
    print("Question 3:")
    print("Obama mentions his slogan: " + str(len(obama_count)+len(obama_count2))+" times")
    print("Donald mentions his slogan: " + str(len(donald_count)+len(donald_count2))+" times")


def question_4():
    obama_text = ''.join(obama_matrix[:, 1]).lower()
    obama_count = [m.start() for m in re.finditer('iran', obama_text)]

    donald_text = ''.join(donald_matrix[:, 1]).lower()
    donald_count = [m.start() for m in re.finditer('iran', donald_text)]
    print("Question 4:")
    print("Obama mentions Iran: " + str(len(obama_count)) + " times")
    print("Donald mentions Iran: " + str(len(donald_count)) + " times")


def question_5():
    obama_text = ''.join(obama_matrix[:, 1]).lower()
    obama_count = [m.start() for m in re.finditer('obamacare', obama_text)]
    # Assuring we get the correct count
    donald_text = ''.join(donald_matrix[:, 1]).lower()
    donald_count = [m.start() for m in re.finditer('obamacare', donald_text)]
    print("Question 5:")
    print("Obama mentions Obamacare: " + str(len(obama_count)) + " times")
    print("Donald mentions Obamacare: " + str(len(donald_count)) + " times")


question_1()
question_2()
question_3()
question_4()
question_5()