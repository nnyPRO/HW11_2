#!/usr/bin/env python3
# เมษนี ลายเฮือง (แนน)
# 650510676
# HW11_2
# 204203 Sec 002

# # Ecommerce Purchases Exercise


# 0) ** Import pandas
import pandas as pd
# 0) read in the "Ecommerce.Purchases.csv" file and set it to a DataFrame called ecom. **
ecom = pd.read_csv('EcommercePurchases.csv')
# display the correct output in each function

# 1) **Check the head of the DataFrame.**

def q01():
    print("\nQ01")
    result = ecom.head()
    print(result)

# 2) ** How many rows and columns are there? **

def q02():
    print("\nQ02")
    rows = len(ecom.axes[0])
    cols = len(ecom.axes[1])
    print(rows,"rows" ,cols,"columns")

# 3) ** What is the average Purchase Price? **

def q03():
    print("\nQ03")
    print(ecom['Purchase Price'].mean())

# 4) ** What were the highest and lowest purchase prices? **


def q04():
    print("\nQ04")
    print("highest:", ecom['Purchase Price'].max())
    print("lowest:", ecom['Purchase Price'].min())


# 5) ** How many people have English 'en' as their Language of choice on the website? **

def q05():
    print("\nQ05")
    print(count_en())

def count_en():
    num = 0
    for i in ecom['Language']:
        if i == 'en':
            num+=1
    return num



# 6) ** How many people have the job title of "Lawyer" ? **
#

def q06():
    print("\nQ06")
    print(count_job_lawyer())

def count_job_lawyer():
    num = 0
    for i in ecom['Job']:
        if i == 'Lawyer':
            num+=1
    return num


# 7) ** How many people made the purchase during the AM and how many people made the purchase during PM ? **
#
# **(Hint: Check out [value_counts()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html) ) **

def q07():
    print("\nQ07")
    print(ecom['AM or PM'].value_counts())

# 8) ** What are the 5 most common Job Titles? **

def q08():
    print("\nQ08")
    print(ecom['Job'].value_counts().head())

# 9) ** Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction? **

def q09():
    print("\nQ09")
    print(ecom[ecom['Lot'] == '90 WT']['Purchase Price'])


# 10) ** What is the email of the person with the following Credit Card Number: 4926535242672853 **

def q10():
    print("\nQ10")
    print(ecom[ecom['Credit Card'] == 4926535242672853]['Email'])


# 11) ** How many people have American Express as their Credit Card Provider *and* made a purchase above $95 ?**

def q11():
    print("\nQ11")
    print(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count()['Address'])


# 12) ** Hard: How many people have a credit card that expires in 2025? **

def q12():
    print("\nQ12")
    num = 0
    for i in ecom['CC Exp Date']:
        if '/25' in i:
            num+=1
    print(num)



# 13) ** Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...) **

def substring(email):
    ad = email.index('@')
    new_str = email[ad+1:]
    return new_str

def q13():
    print("\nQ13")
    ecom['email provider'] = ecom['Email'].apply(substring)
    print(ecom['email provider'].value_counts().head())


if __name__ == '__main__':
    # q01()
    # q02()
    # q03()
    # q04()
    # q05()
    # q06()
    # q07()
    # q08()
    # q09()
    # q10()
    # q11()
    # q12()
    q13()
