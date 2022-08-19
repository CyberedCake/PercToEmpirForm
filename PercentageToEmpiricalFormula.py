# PercentageToEmpiricalFormula.py
#
# This file was created by and modified by CyberedCake
# Last Modified: November 9th, 2021 at 12:28PM ET
# Version: 1.0
#
# Please do not modify or distribute without first
# acknowledging you did not create this and including
# the github page for this project... which can be found
# here: https://github.com/CyberedCake/PercToEmpirForm
# (or you could just fork it on GitHub)
#
# I, the creator of this file, am aware the code is not
# the best and not quite as efficient as it could be, but
# oh well. This project isn't suppose to be maintained or
# made as efficient as possible as it's just a small script
# running on my school computer!
#
# Created by CyberedCake


import os, time, sys, math, subprocess
from os.path import exists
import urllib.request
# import things

# vvv Automatically installs PyAutoGui if not already installed
# Note: This requires "depends.py" in the parent directory because that is how it was programmed
import sys

import pyautogui, requests

def setup():
    global supportsColor
    def supportsColor(): # Checks if the current console supports color
        return True # Just going to make it return true until I can find an alternative
        
        #plat = sys.platform
        #supported_platform = plat != 'Pocket PC' and (plat != 'win32' or
                                                     # 'ANSICON' in os.environ)
        # isatty is not always implemented, #6223.
        #is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
        #return supported_platform and is_a_tty

    os.system("color") #makes console colory :D
    os.system("title Percentage to Empirical Formula") # yay titlebars

    # yes i know this function code sucks but oh well it works and
    # the main reason it exist is because i'm used3 to minecraft
    # color codes lol
    global printF
    def printF(string):
        if(supportsColor() == True):
            string = str(string)
            string = string.replace("&0", "\u001b[30m")
            string = string.replace("&1", "\u001b[34m")
            string = string.replace("&2", "\u001b[32m")
            string = string.replace("&3", "\u001b[36m")
            string = string.replace("&4", "\u001b[31m")
            string = string.replace("&5", "\u001b[35m")
            string = string.replace("&6", "\u001b[33m")
            string = string.replace("&7", "\u001b[37m")
            string = string.replace("&8", "\u001b[30;1m")
            string = string.replace("&9", "\u001b[34;1m")
            string = string.replace("&a", "\u001b[32;1m")
            string = string.replace("&b", "\u001b[36;1m")
            string = string.replace("&c", "\u001b[31;1m")
            string = string.replace("&d", "\u001b[35;1m")
            string = string.replace("&e", "\u001b[33;1m")
            string = string.replace("&f", "\u001b[37;1m")
            string = string.replace("&l", "\u001b[1m")
            string = string.replace("&n", "\u001b[4m")
            string = string.replace("&h", "\u001b[7m")
            string = string.replace("&r", "\u001b[0m")
            print(string + "\u001b[0m")
        else:
            string = string.replace("&0", "")
            string = string.replace("&1", "")
            string = string.replace("&2", "")
            string = string.replace("&3", "")
            string = string.replace("&4", "")
            string = string.replace("&5", "")
            string = string.replace("&6", "")
            string = string.replace("&7", "")
            string = string.replace("&8", "")
            string = string.replace("&9", "")
            string = string.replace("&a", "")
            string = string.replace("&b", "")
            string = string.replace("&c", "")
            string = string.replace("&d", "")
            string = string.replace("&e", "")
            string = string.replace("&f", "")
            string = string.replace("&l", "")
            string = string.replace("&n", "")
            string = string.replace("&h", "")
            string = string.replace("&r", "")
            print(string)

    alreadyHaveElements = exists('elements.txt')
    import webbrowser as browser
    def checkElements():
        if alreadyHaveElements == False:
            print("Downloading 'elements.txt' (required)...")
            url = "https://raw.githubusercontent.com/CyberedCake/PercToEmpirForm/main/elements.txt"
            try:
                request = requests.get(url)

                with open('elements.txt', 'wb') as file:
                    file.write(request.content)

                print("Successfully downloaded 'elements.txt'... launching program!")
                
            except Exception as err:
                exception = str(err)
                button = "Close program"
                if(pyautogui == True):
                    gui.alert("An error occurred: " + exception, "An exception occurred!", button)
                printF("&cAn exception occurred: &8" + exception)
                printF(" ")
                alert = pyautogui.confirm(str(exception) + "\n\nCheck your connection or try again later.\n\nSelect an option for what the program should do next:", "An exception occurred!", buttons=['Try again', 'Download manually', 'Restart program', 'Close program'])
                if(alert == "Try again"):
                    checkElements()
                    return
                elif(alert == "Restart program"):
                    printF(" ")
                    printF("&aRebooting program, please wait...")
                    os.system("title Rebooting program, please wait...")
                    os.startfile(__file__)
                elif(alert == "Download manually"):
                    browser.open("https://github.com/CyberedCake/PercToEmpirForm/tree/main/elements")
                    printF(" ")
                    printF("&aOpening web browser...")
                    time.sleep(5)
                    checkElements()
                    return
                exit()
    checkElements()
        
    printF("&6PERCENTAGE TO EMPIRICAL/MOLECULAR FORMULA")
    printF(" ")
    printF("Please enter the percentage &7(without the % sign) &falong with the chemical formula in the following format:")
    printF("&a%element%=%grams%, %element 2%=%grams%")
    printF("&eEX: carbon=50, oxygen=50")
    printF("&7OR &a%element=%grams%, %element 2%=%grams, |%molecular mass%")
    printF("&eEX 2: carbon=50, oxygen=50, |28")
    printF(" ")

# >>>    THIS IS THE PART WHERE I KINDA WISH IT WAS MORE EFFICIENT   <<<
# >>> AND SOMETIMES I CAN'T EVEN UNDERSTAND MY OWN CODE, BUT OH WELL <<<
def main():
    printF(" ")
    ending = ""
    if(supportsColor() == True):
        ending = "\u001b[36;1m"
    format = input("Enter format: " + ending)
    timing = epoch()
    printF("&r")

    if (format.strip() == ""):
        throwParseException("INPUT_REQUIRED")
    if not("=" in format):
        throwParseException("NO_EQUALS_FOUND")
    if not(", " in format):
        throwParseException("NO_COMMAS_FOUND")

    file = open('elements.txt', 'r')

    elementsOnFile = []
    for line in file:
        elementsOnFile.append(line)

    file.close()

    molarMasses = {}

    elementsAndPercents, amount, alreadyUsed = format.split(", "), 0, []

    fourthStepInitiate, molecularMass = False, 0
    for elementAndPercent in elementsAndPercents: # detect if element starts with |
        if(elementAndPercent.startswith('|')):
            inputtedMolecFormMass = elementAndPercent.replace("|", "")
            if(isfloat(inputtedMolecFormMass) == False):
                throwParseException("MOLEC_MASS_NOT_A_FLOAT")
            inputMolFormMass = float(inputtedMolecFormMass)
            if(inputMolFormMass <= 0):
                throwParseException("MOLEC_MASS_TOO_SMALL")
            fourthStepInitiate, molecularMass = True, inputMolFormMass
            elementsAndPercents.remove(elementAndPercent)
            break
    for elementAndPercent in elementsAndPercents:
        if(len(elementAndPercent.split("=")) <= 1):
            throwParseException("MISSING_ELEMENT_PERCENT_DEFINITION")
        if(elementAndPercent.split("=")[1] == ""):
            throwParseException("MISSING_ELEMENT_PERCENT_DEFINITION_[1]")
        validElement = False
        inputtedElement = elementAndPercent.split("=")[0]
        for element in elementsOnFile:
            if(inputtedElement.lower() == element[0:element.find("(")-1].lower()):
                if(element in alreadyUsed):
                    throwParseException("FOUND_DUPLICATE_ELEMENTS")
                validElement = True
                start = element.find("(") + 1
                end = element.find(")")
                substring = element[start:end]
                molarMasses[inputtedElement] = substring
                alreadyUsed.append(element)
        if(validElement == False):
            throwParseException("INVALID_ELEMENT")
            main()
            return

        inputtedNumber = elementAndPercent.split("=")[1]
        if(isfloat(inputtedNumber) == False):
            throwParseException("INVALID_NUMBER_PERCENT")
        if(float(inputtedNumber) >= 100 or float(inputtedNumber) <= 0):
            throwParseException("NUMBERS_TOO_LARGE_OR_TOO_SMALL")
        amount = amount + float(inputtedNumber)
        
    # FIRST STEP
    firstStep = {}
    index = 0
    for element in molarMasses.keys():
        molarMass = float(molarMasses.get(element))
        originalPercent = float(elementsAndPercents[index].split("=")[1])

        firstStep[element] = round(originalPercent / molarMass, 3)

        index = index+1

    # SECOND STEP
    minimum = min(firstStep.values())
    secondStep = {}
    thirdStepInitiate = False
    for element in molarMasses.keys():
        firstStepOutput = firstStep.get(element)

        secondStep[element] = round(firstStepOutput / minimum, 1)

        fractional, whole = math.modf(round(firstStepOutput / minimum, 1))
        if(fractional > 0.0):
            thirdStepInitiate = True

    # THIRD (sometimes) STEP
    # (also referred to as the step I don't understand how this code works, but it does)
    thirdStep = {}
    if(thirdStepInitiate == True):
        minimumWorks = 0
        entered = False
        while(minimumWorks == 0):
            for integer in range(1, 10):
                allWork = True
                for element in molarMasses.keys():
                    secondStepOutput = secondStep.get(element)
                    fractional, whole = math.modf(secondStepOutput * integer)

                    if(fractional > 0.0):
                        allWork = False

                if(allWork == True):
                    minimumWorks = integer
                    entered = True
                    break
            break
        if(entered == True):
            for element in molarMasses.keys():
                secondStep[element] = secondStep.get(element) * minimumWorks
        if(fourthStepInitiate == False):
            printF("&fEmpirical Formula: " + formatDict(secondStep))
            if(entered == False):
                printF("&f                   &9[Number &dcould not &9be multiplied by numbers up to &ex9&9]")
            else:
                printF("&f                   &9[These numbers are all multiplied by &ex" + str(minimumWorks) + "&9]")
            timeDifference(timing)
            main()
    elif(fourthStepInitiate == False):
        printF("&fEmpirical Formula: " + formatDict(secondStep))
        timeDifference(timing)
        main()
        
    # FOURTH STEP
    fourthStep = {}
    if(fourthStepInitiate == True):
        total = 0.0
        for element in molarMasses.keys():
            total = total + (float(molarMasses.get(element))*float(secondStep.get(element)))

        multiplyBy = round(molecularMass/total)
        for element in molarMasses.keys():
            fourthStep[element] = multiplyBy * float(secondStep.get(element))

        printF("&fEmpirical Formula: " + formatDict(secondStep))
        printF("&fMolecular Formula: " + formatDict(fourthStep) + " &9x" + str(multiplyBy))
        timeDifference(timing)
        main()

    printF("&9The worst kind of exceptions... unknown ones :(")
    printF("&7Here may be some useful debug information and what we know:")
    debug = {
        "thirdStep": boolToString(thirdStepInitiate),
        "fourthStep": boolToString(fourthStepInitiate),
        "timeTakenMs": str(epoch() - timing)
        }
    printF(formatDict(debug))
    exception("An unknown exception occurred and we could not trace the cause for it. Try again later!", "Try again")

def timeDifference(time):
    printF("&fIt took &b" + str(epoch() - time) + "&bms &fto complete the operation!")

def epoch():
    return round(time.time() * 1000)
    
def exception(exception, button):
    if(pyautogui == True):
        gui.alert(exception, "An exception occurred!", button)
    printF("&cAn exception occurred: &8" + exception)
    printF(" ")
    main()

def throwParseException(why):
    exception("Could not parse your format correctly!\n(" + why + ")", "Restart program")

def boolToString(boolean):
    return "True" if boolean == True else "False"

def formatDict(item): # (this could be done better, please message me if you find a way)
    primary = "&c"
    secondary = "&e"
    
    item = "&r" + str(item)
    split = item.split("'")
    active = False
    added = []
    for substring in split:
        if(active == True):
            active = False
            added.append(substring + "&r")
        elif(active == False):
            active = True
            added.append(substring + primary)

    joined = ''.join(added)
    ints = [int(s) for s in joined if s.isdigit()]
    for integer in ints:
        joined = joined.replace(str(integer), secondary + str(integer) + "&r")
    joined = joined.lower().replace("true", secondary + "True")
    joined = joined.lower().replace("false", secondary + "False")
    
    return joined
    #start = element.find("'") + 1
    #end = element.find("'")
    #substring = element[start:end]

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    def execute():
        try:
            setup() # setup
            main() # init
        except Exception as err:
            printF("&b---------------------------------------------------------")
            printF("&cA fatal exception occurred within the program, going to restart!")
            printF("&8" + str(err))
            printF("&7Please contact a developer if this error persists.")
            printF("&b---------------------------------------------------------")
            execute()
    execute()
