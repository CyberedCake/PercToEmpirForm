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


import os, time, sys, math, subprocess # import things

# vvv Automatically installs PyAutoGui if not already installed
pyautogui = False
try:
    import pyautogui as gui
    pyautogui = True
except:
    os.system("title Downloading 'pyautogui'")
    downloadDependencies = input("You need to download some OPTIONAL dependencies, would you like to download them? Y/N: ")
    if(downloadDependencies.lower() == "n" or downloadDependencies.lower() == "no"):
        print("Skipping installation of soft-dependent library...")
    else:
        print("Downloading and installing a soft-dependent library...")
        print(" ")
        print("Installing library: 'pyautogui'")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'pyautogui'])
        try:
            import pyautogui as gui
            print("pyautogui library import success! starting main program...")
            pyautogui = True
        except:
            print(" ")
            print("System failed to download soft-dependent libraries. Continuing without...")
        
        os.system("cls")
        if(pyautogui == "true"):
            print("System console cleared: Installed PYAUTOGUI")
            print(" ")

os.system("color") #makes console colory :D

# yes i know this function code sucks but oh well it works and
# the main reason it exist is because i'm used to minecraft
# color codes lol
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
        string = string.replace("&r", "")
        print(string)

def supportsColor(): # Checks if the current console supports color
    return True # Just going to make it return true until I can find an alternative
    
    #plat = sys.platform
    #supported_platform = plat != 'Pocket PC' and (plat != 'win32' or
                                                 # 'ANSICON' in os.environ)
    # isatty is not always implemented, #6223.
    #is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
    #return supported_platform and is_a_tty

os.system("title Percentage to Empirical Formula") # yay titlebars
    
printF("&6PERCENTAGE TO EMPIRICAL FORMULA")
printF(" ")
printF("Please enter the percentage &7(without the % sign) &falong with the chemical formula in the following format:")
printF("&a%element%=%percentage%, %element 2%=%percentage 2%")
printF("&eEX: (carbon=50, oxygen=50)")
printF(" ")

# >>>    THIS IS THE PART WHERE I KINDA WISH IT WAS MORE EFFICIENT   <<<
# >>> AND SOMETIMES I CAN'T EVEN UNDERSTAND MY OWN CODE, BUT OH WELL <<<
def main():
    ending = ""
    if(supportsColor() == True):
        ending = "\u001b[36;1m"
    format = input("Enter format: " + ending)
    printF("&r")

    if (format.strip() == ""):
        throwParseException("INPUT_REQUIRED")
    if not("=" in format):
        throwParseException("NO_EQUALS_FOUND")
    if not(", " in format):
        throwParseException("NO_COMMAS_FOUND")
        

    try:
        file = open(os.path.dirname(sys.argv[0]) + "\elements.txt", mode='r+')
    except Exception as err:
        exception("File 'elements.txt' not present in current python script directory", "Restart program")

    elementsOnFile = file.readlines()
    file.close()

    molarMasses = {}

    elementsAndPercents = format.split(", ")
    amount = 0
    alreadyUsed = []
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

    if not(amount == 100):
        throwParseException("NUMBER_DOES_NOT_ADD_TO_100")
        
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
            for integer in range(1, 11):
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
                thirdStep[element] = secondStep.get(element) * minimumWorks
        formatDict(thirdStep)
        if(entered == False):
            printF("&9[Number could not be multiplied by numbers up to 10]")
        else:
            printF("&9[These numbers are all multiplied by &ex" + str(minimumWorks) + "&9]")
        printF(" ")
        main()
    elif(thirdStepInitiate == False):
        formatDict(secondStep)
        printF(" ")
        main()

    exception("Something went wrong, we could not determine the cause!", "Attempt to run program again")

def exception(exception, button):
    if(pyautogui == True):
        gui.alert(exception, "An exception occurred!", button)
    printF("&cAn exception occurred: &8" + exception)
    printF(" ")
    main()

def throwParseException(why):
    exception("Could not parse your format correctly!\n(" + why + ")", "Restart program")

def formatDict(item): # (this could be done better, please message me if you find a way)
    textFirst = "&c"
    integerLast = "&e"
    
    item = str(item)
    split = item.split("'")
    active = False
    added = []
    for substring in split:
        if(active == True):
            active = False
            added.append(substring + "&r")
        elif(active == False):
            active = True
            added.append(substring + textFirst)

    joined = ''.join(added)
    ints = [int(s) for s in joined if s.isdigit()]
    for integer in ints:
        joined = joined.replace(str(integer), integerLast + str(integer) + "&r")
    
    printF(joined)
    #start = element.find("'") + 1
    #end = element.find("'")
    #substring = element[start:end]

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

main() # init
