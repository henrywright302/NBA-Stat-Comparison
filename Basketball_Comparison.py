from bs4 import BeautifulSoup
import requests
import re
import sys

def remove_tags(text):
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', text)

#What to do next:
#Break main up into functions - Functional Decomposition
#Add different modes (ex. just get stats, stat compare, other stats besides points)

def main():
    print("- Player 1 - ")  
    firstName = input("Enter First Name: ").lower()
    lastName = input("Enter Last Name: ").lower()

    print("- Player 2 - ")
    firstName2 = input("Enter First Name: ").lower()
    lastName2 = input("Enter Last Name: ").lower()

    lastName_letter = lastName[0]
    lastName_5letter = lastName[:5]
    firstName_2letter = firstName[:2]

    lastName_letter2 = lastName2[0]
    lastName_5letter2 = lastName2[:5]
    firstName_2letter2 = firstName2[:2]

    test_name = str("[" + firstName + " " + lastName + "]")
    url = "https://www.basketball-reference.com/players/" + lastName_letter + "/" + lastName_5letter + firstName_2letter + "01.html"
  
    test_name2 = str("[" + firstName2 + " " + lastName2 + "]")
    url2 = "https://www.basketball-reference.com/players/" + lastName_letter2 + "/" + lastName_5letter2 + firstName_2letter2 + "01.html"
   
    



    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    name_soup = soup.find("h1")
    name_tag = str(name_soup.findAll('span'))
    name = remove_tags(name_tag).lower()

    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')
    name_soup2 = soup2.find("h1")
    name_tag2 = str(name_soup2.findAll('span'))
    name2 = remove_tags(name_tag2).lower()


    wrongName = 0
    while test_name != name:
        wrongName += 1
        if wrongName < 5:

            print("Given name doesn't match found name")
            print("Finding correct page...")
            count = 1
            count = count + 1
            count = str(count)
            url = "https://www.basketball-reference.com/players/" + lastName_letter + "/" + lastName_5letter + firstName_2letter + "0" + count +".html"
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            name_soup = soup.find("h1")
            name_tag = str(name_soup.findAll('span'))
            name = remove_tags(name_tag).lower()
            count = int(count)
        else:
            print("Given Name: " + firstName, lastName)
            catchInputError = input("Are you sure this is the right name? (y/n): ").lower()
            if catchInputError == 'y':
                wrongName = 0
            else:
                sys.exit("Wrong Input Name")

            
    wrongName = 0         

    while test_name2 != name2:
        wrongName += 1
        if wrongName < 5:
            
            print("Given name doesn't match found name")
            print("Finding correct page...")
            count = 1
 
            count = count + 1
            count = str(count)
            url2 = "https://www.basketball-reference.com/players/" + lastName_letter2 + "/" + lastName_5letter2 + firstName_2letter2 + "0" + count +".html"
      
            response2 = requests.get(url2)
            soup2 = BeautifulSoup(response2.content, 'html.parser')
            name_soup2 = soup2.find("h1")
            name_tag2 = str(name_soup2.findAll('span'))
            name2 = remove_tags(name_tag2).lower()
            count = int(count)
        else:
            print("Given Name: " + firstName2, lastName2)
            catchInputError2 = input("Are you sure this is the right name? (y/n): ").lower()
            if catchInputError2 == 'y':
                wrongName = 0
            else:
                sys.exit("Wrong Input Name")


    containers = soup.find("div", {"class":"stats_pullout"})
   
    containers2 = soup2.find("div", {"class":"stats_pullout"})
    

    career_ppg_tag = str(containers.findAll('p')[5])
    career_ppg_tag2 = str(containers2.findAll('p')[5])
    
    career_ppg = remove_tags(career_ppg_tag)
    career_ppg2 = remove_tags(career_ppg_tag2)
    
   
    print("Who do you think averaged more points?")
   
    userGuess = input("Enter 1 for " + firstName.title() + " " + lastName.title() + ", Enter 2 for " + firstName2.title() + " " + lastName2.title() + ": ")

    if int(userGuess) == 1 or int(userGuess) == 2:
        if int(userGuess) == 1 and float(career_ppg) > float(career_ppg2):
            print("Correct! " + firstName.title() + " " + lastName.title() + " averaged more points over his career than " + firstName2.title() + " " + lastName2.title() + ".")

        elif int(userGuess) == 2 and float(career_ppg2) > float(career_ppg):
            print("Correct! " + firstName2.title() + " " + lastName2.title() + " averaged more points over their career than " + firstName.title() + " " + lastName.title() + ".")

        else:
            print("Incorrect.")
    else:
        print("Please enter a valid input.")
        userGuess = input("Enter 1 for " + firstName.title() + " " + lastName.title() + ", Enter 2 for " + firstName2.title() + " " + lastName2.title() + ": ")



    print()
    print("------------------------")
    print("Player:",firstName.title(),lastName.title())
    print("Career PPG: " + career_ppg)
    print("------------------------")
    print("Player:",firstName2.title(),lastName2.title())
    print("Career PPG: " + career_ppg2)
    print("------------------------")

main()
