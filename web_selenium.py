#! /usr/bin/python3
#scrape_git.py - Web scrape git repository Pannkaksgruppen

import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initiate start url
browser = webdriver.Chrome()
start_url = "https://github.com/onselius"

browser.get(start_url)
browser.set_window_position(0, 0)

browser.find_element_by_link_text("Hemme02/Pannkaksgruppen").click()
WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "src")))

browser.find_element_by_link_text("src").click()
WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Pannkaksgruppen")))

browser.find_element_by_link_text("Pannkaksgruppen").click()
WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'commits')]")))

browser.find_element_by_xpath("//*[contains(@class, 'commits')]//a").click()

# Generate a report textfile for git repo
def remove_empty(elements):
    new_list = []
    for e in elements:
        if e.text and e.text != "..":
            new_list.append(e.text)
    return new_list

def test_list(elements):
    for i in range(len(elements)):
        print(str(i) + " " + elements[i].text)

def fix_list(elements):
    new_list = []
    for e in elements:
        new_list.append(e.text)
    return new_list

# Initiate start url
start_url = "https://github.com/Hemme02/Pannkaksgruppen"

browser.get(start_url)

# Get repo title
try:
    title = browser.title.split("/")
    title = title[-1]
except Exception as e:
    print(e)
    print("No title found")

# Initiate report file
report_file = open("report.txt", "w")
report_file.write("Selenium report for repository \"" + title + "\"\n")

# Brief info for repo
try:
    base_info = browser.find_elements_by_class_name("text-emphasized")
    base_info = fix_list(base_info)

    commits = base_info[0] + " commits\n"
    branches = base_info[1] + " branch(es)\n"
    releases = base_info[2] + " releases\n"
    contributors = base_info[3] + " contributors\n"
    header = "\nBase info:\n"
    
    print(header + commits + branches + releases + contributors)
    report_file.write(header + commits + branches + releases + contributors)

except Exception as e:
    print(e)
    print("No elements found")

# Inspect files in /src/
browser.find_element_by_link_text("src").click()
element = WebDriverWait(browser, 10).until(EC.title_contains("src"))
try:
    files = browser.find_elements_by_css_selector("span > a[class=js-navigation-open]")
    files = fix_list(files)
    comments = browser.find_elements_by_css_selector("span > a[class=message]")
    comments = fix_list(comments)
    age = browser.find_elements_by_class_name("age")
    age = fix_list(age)
    col_widths = []
    col_widths.append(len(max(files, key=len)) + 2)
    col_widths.append(len(max(comments, key=len)) + 2)
    col_widths.append(len(max(age, key=len)) + 2)

    header = "\nFiles in /src/"
    print(header)
    report_file.write(header + "\n")
    for i in range(len(files)): 
        line = files[i].ljust(col_widths[0]) + " " + comments[i].ljust(col_widths[1]) + " " + age[i]
        print(line)
        report_file.write(line + "\n")
except Exception as e:
    print(e)
    print("No elements found")

browser.close()
report_file.close()
