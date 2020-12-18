
def help():
  print("==CALC EMBEDDED HELP==")
  print("IMPORT: use the import command to add main.py to your project. It is recommened that you rename the file first before adding it. In this tutorial, it will be imported as CALC.")


def r():
    print("<<run_app>>")
    print("0) help()")
    print("1) calcbasic()")
    print("2) calcrand()")
    print("3) main()")
    print("4) err()")
    a = int(input("q:"))
    if a == 0:
        help()
    elif a == 1:
        calcbasic(10890, "+", 28753)
        calcbasic(10890, "-", 28753)
        calcbasic(10890, "*", 28753)
        calcbasic(10890, "/", 28753)
        calcbasic(10890, "/", 0)
    elif a == 2:
        calcrand(5475, -2300, 2354444)
    elif a == 3:
        main("pass", -1)
    elif a == 4:
        err(0x004, "SAMPLE_TEXT", "f")





def calcbasic(*arg):
    x = arg[0]
    y = arg[2]
    print("")
    if isofflineplatform == 1:
        if arg[1] == "+":
            result = str((x + y))
            if result == "inf":
              err("0x009", "main.py#def_calcbasic", "c")
            else:
              print("The Result is: " + result)
        if arg[1] == "-":
            result = str((x - y))
            if result == "inf":
              err("0x009", "main.py#def_calcbasic", "c")
            else:
              print("The Result is: " + result)
        if arg[1] == "*":
            result = str((x * y))
            if result == "inf":
              err("0x009", "main.py#def_calcbasic", "c")
            else:
              print("The Result is: " + result)
        if arg[1] == "/":
            if y == 0:
                err("0x001", "main.py#def_calcbasic", "f")
            else:
                result = str((x / y))
                if result == "inf":
                  err("0x009", "main.py#def_calcbasic", "c")
                else:
                  print("The Result is: " + result)
    else:
        if arg[1] == "+":
            result = str((x + y))
            print("The Result is: " + color.BOLD + result + color.END)
        if arg[1] == "-":
            result = str((x - y))
            print("The Result is: " + color.BOLD + result + color.END)
        if arg[1] == "*":
            result = str((x * y))
            print("The Result is: " + color.BOLD + result + color.END)
        if arg[1] == "/":
            if y == 0:
                err("0x001", "main.py#def_calcbasic", "f")
            else:
                result = str((x / y))
                print("The Result is: " + color.BOLD + result + color.END)


def calcrand(*arg):
    amt = arg[0]
    low = arg[1]
    high = arg[2]
    stop = 0
    temp = ""
    tempint = 0
    tempavg = 0
    tempset = []
    while stop == 0:
        tempset.clear()
        for x in range(amt):
            result = str(random.randint(low, high))
            tempset.append(result)
            print("Random integer number " + str(x) + " was returned as " +
                  result)
        print("all numbers calculated")
        tempint = min(tempset)
        print("The lowest number generated was " + tempint + ".")
        tempint = max(tempset)
        print("The highest number generated was " + tempint + ".")
        for x in tempset:
            tempavg += int(x)
        tempint = str(tempavg / amt)
        print("The average number that was generated was " + tempint + ".")

        temp = input("Repeat? [Y/N]?")
        if temp == "y":
            stop = 0
        elif temp == "Y":
            stop = 0
        elif temp == "n":
            stop = 1
        elif temp == "N":
            stop = 1
        else:
            pass


#main function.
def main():
    print("Done. Intializing App...")
    print("")
    print("")
    print("")
    if isofflineplatform == 1:
        print("        CALC 1.1 [BETA]")
        print("          by  @elburg")
    else:
        print(color.BOLD + color.DARKCYAN + "        CALC 1.1 [BETA]" +
              color.END)
        print("          by  " + color.RED + "@" + color.YELLOW + "e" +
              color.GREEN + "l" + color.CYAN + "b" + color.DARKCYAN + "u" +
              color.BLUE + "r" + color.PURPLE + "g" + color.END)
    print("")
    print("VERSION:" + appinfo["version"])
    print("")
    print("")
    loop = 0
    while loop == 0:
        print(
            "Please enter the type of calculations you want to do. (For Help, type \"help\" or \"exit\" to exit) AVALIABLE:BASIC,RAND"
        )
        temp = input()
        typeofmath = temp
        if typeofmath == "help":
            help()
        elif typeofmath == "BASIC" or typeofmath == "basic" or typeofmath == "Basic":
            print("")
            print("Basic")
            print("")
            temp = input("Enter your first digit:")
            d0 = int(temp)
            temp = input("Enter your second digit:")
            d1 = int(temp)
            temp = input(
                "Enter which operation you want to execute. (Types Avaliable: +, -, *, /):"
            )
            ty = temp
            calcbasic(d0, ty, d1)
        elif typeofmath == "Rand" or typeofmath == "rand" or typeofmath == "RAND":
            temp = input("Enter how many random numbers you want:")
            a = int(temp)
            temp = input("Enter the lowest possible number you want:")
            l = int(temp)
            temp = input("Enter the highest possible number you want:")
            h = int(temp)
            calcrand(a, l, h)
        elif typeofmath == "exit" or typeofmath == "cancel" or typeofmath == "pass" or typeofmath == "quit":
            break
        elif typeofmath == "help":
            help()
        else:
            err("0x000", "main.py#def_main", "f")


# error reporter
def err(code, source, c):
    if code in errcodes:
        errcodedef = errcodes[code]
    else:
        errcodedef = errcodes["0x006"]
    define = errdef[code]
    if c == "f":
        if isofflineplatform == 1:
            print("===FATAL_ERROR===============")
            print(
                "A component has caused the application to close unexpectedly")
            print("Here is data linked to this crash.")
            print("CODE:" + code)
            print(errcodedef)
            print(define)
            print("SOURCE:" + source)
            print("TYPE:FATAL")
        else:
            print(color.RED + color.BOLD + "===FATAL_ERROR===============")
            print(
                "A component has caused the application to close unexpectedly")
            print("Here is data linked to this crash.")
            print("CODE:" + code)
            print(errcodedef)
            print(define)
            print("SOURCE:" + source)
            print("TYPE:FATAL" + color.END)
        sys.exit()
    elif c == "c":
        if isofflineplatform == 1:
            print("===CRITICAL_ERROR===============")
            print(
                "A component has ran into an error.")
            print("Here is data linked to this error.")
            print("CODE:" + code)
            print(errcodedef)
            print(define)
            print("SOURCE:" + source)
            print("TYPE:CRITICAL")
        else:
            print(color.RED + color.BOLD + "===CRITICAL_ERROR===============")
            print(
                "A component has ran into an error.")
            print("Here is data linked to this error.")
            print("CODE:" + code)
            print(errcodedef)
            print(define)
            print("SOURCE:" + source)
            print("TYPE:FATAL" + color.END)


#os is used to clear the screen

print(
    "CALC uses a color class, which is used to display text with colors, bold fonts, and underlined fonts. While this is fully functional, some shells cannot view these fonts. Do you want to run with colors? [Y/N]"
)
other = input()
if other == "y":
    isofflineplatform = 0
    print("Running with colors.")
elif other == "Y":
    isofflineplatform = 0
    print("Running with colors.")
elif other == "n":
    isofflineplatform = 1
    print("Running without colors.")
elif other == "N":
    isofflineplatform = 1
    print("Running without colors.")
else:
    isofflineplatform = 1
    print("No input or unknown input. Running without colors.")
# starts application

print("Initializing...")
print("Importing \"sys\"    [0/5]")
import sys
print("Importing \"os\"     [1/5]")
import os
print("Importing \"random\" [2/5]")
import random
print("Importing \"math\"   [3/5]")
import math
print("Importing \"helpapp\"[4/5]")
import helpapp
print("Finalizing...      [5/5]")
print("Import Complete!")
main()
