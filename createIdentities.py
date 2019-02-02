import pandas as pd
import random
import datetime

#get date
now = datetime.datetime.now()


#open csv set as df
df = pd.read_csv("namesSample.csv") 

def createMale():
    i = random.randint(1,100)
    j = random.randint(1,100)
    firstName = df.iloc[i]['MaleNames']
    lastName = df.iloc[j]['LastNames']
    age = random.randint(18,71)
    birthYear = now.year - age
    birthMonth = random.randint(1,13)
    return(firstName, lastName, age, birthMonth, birthYear)


def createFemale():
    i = random.randint(1,100)
    j = random.randint(1,100)
    firstName = df.iloc[i]['FemaleNames']
    lastName = df.iloc[j]['LastNames']
    age = random.randint(18,70)
    birthYear = now.year - age
    birthMonth = random.randint(1,13)
    return(firstName, lastName, age, birthMonth, birthYear)
