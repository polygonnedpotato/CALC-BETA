class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


appinfo = {
    "appname":
    "Command-Based mathematical processor",
    "appnameshort":
    "CALC",
    "version":
    "1.1",
    "isdebugver":
    "false",
    "isbetaver":
    "false",
    "developer":
    "@elburg",
    "webversion?":
    "true",
    "weblink":
    "https://repl.it/@elburg/CALC-BETA?embed=1&output=1",
    "usesclasses":
    "true",
    "classcount":
    1,
    "classes":
    "color",
    "classes/color#subclasses":
    "PURPLE;CYAN;DARKCYAN;BLUE;GREEN;YELLOW;RED;BOLD;UNDERLINE;END",
    "usesstrings?":
    "false",
    "functioncount":
    6,
    "funtions":
    "help();calcbasic(*arg);main(source, srcver);err(code, source, c);calcrand(*arg);r()",
    "usesmodules?":
    "true",
    "modules":
    "os;sys;random;math;helpapp",
    "containshelp?":
    "true",
    "helpfunction":
    "calc.help()"
}
errcodes = {
    "0x000": "INVALID_INPUT",
    "0x001": "CANNOT_DIVIDE_BY_ZERO",
    "0x002": "FS_ACCESS_DENIED",
    "0x003": "APPLICATION_IS_CORRUPTED",
    "0x004": "SAMPLE_ERROR",
    "0x005": "SAMPLE_ERROR_CRITICAL",
    "0x006": "UNKNOWN_ERROR",
    "0x007": "UNIMPLEMENTED_FUNCTION",
    "0x008": "DEV_ONLY",
    "0x009": "OUT_OF_RANGE",
}
errdef = {
    "0x000":
    "The input recived was in an invalid format, or was not an input the program was looking for.",
    "0x001":
    "It is impossible to divide any number by Zero(0).",
    "0x002":
    "The file system cannot be accessed.",
    "0x003":
    "The application is corrupted.",
    "0x004":
    "This is a sample error.",
    "0x005":
    "This is a sample critical error.",
    "0x006":
    "There was an unknown error. Try running the app again and try to find out where it occured",
    "0x007":
    "This function is not implemented",
    "0x008":
    "This function can only be accessed by the developer",
    "0x009":
    "The number is out of the 64-bit range and was returned as infinity",
}
romannum = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def help():
  helpapp.help(isofflineplatform)

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
        print("           CALC 1.1")
        print("          by @elburg")
    else:
        print(color.BOLD + color.DARKCYAN + "           CALC 1.1 " +
              color.END)
        print("          by " + color.RED + "@" + color.YELLOW + "e" +
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
