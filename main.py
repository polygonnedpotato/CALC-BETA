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
isofflineplatform = 1

appinfo = {
    "appname":
    "Command-Based mathematical processor",
    "appnameshort":
    "CALC-BETA",
    "version":
    "1.1-BETA06",
    "isdebugver":
    "true",
    "isbetaver":
    "true",
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

romannum = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def help():
  hlp.help(isofflineplatform)

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
            result = str(r.randint(low, high))
            tempset.append(result)
            print("Random integer number " + str(x) + " was returned as " +
                  result)
        print("All numbers calculated")
        tempint = min(tempset)
        if tempint == "inf":
          err("0x009", "main.py#def_calcrand", "c")
        else:
          print("The lowest number generated was " + tempint + ".")
        print("The lowest number generated was " + tempint + ".")
        tempint = max(tempset)
        if tempint == "inf":
          err("0x009", "main.py#def_calcrand", "c")
        else:
          print("The highest number generated was " + tempint + ".")
        for x in tempset:
            tempavg += int(x)
        tempint = str(tempavg / amt)
        if tempint == "inf":
          err("0x009", "main.py#def_calcrand", "c")
        else:
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
        elif typeofmath == "ferr":
          err("0x004", "main.py#def_main", "f")
        elif typeofmath == "cerr":
          err("0x005", "main.py#def_main", "c")
        else:
            err("0x000", "main.py#def_main", "f")


# error reporter
def err(code, source, c):
  er.err(code, source, c, isofflineplatform)

def r():
    print("<<run_app>>")
    print("0) help()")
    print("1) calcbasic()")
    print("2) calcrand()")
    print("3) main()")
    print("4) err()")
    print("5) err()_alt")
    print("6) quit")
    import helpapp as hlp
    import error as er
    import sys as s
    isofflineplatform = 1
    a = int(input("q:"))
    if a == 0:
        hlp.help(isofflineplatform)
    elif a == 1:
        calcbasic(10890, "+", 28753)
        calcbasic(10890, "-", 28753)
        calcbasic(10890, "*", 28753)
        calcbasic(10890, "/", 28753)
        calcbasic(10890, "/", 0)
    elif a == 2:
        calcrand(5475, -2300, 2354444)
    elif a == 3:
        main()
    elif a == 4:
        er.err("0x004", "SAMPLE_TEXT", "f", 1)
    elif a == 5:
        er.err("0x004", "SAMPLE_TEXT", "c", 1)
    elif a == 6:
      s.exit()
    s.exit()
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
elif other == "ab":
  import about
  about.full()
  import sys as s
  s.exit()
elif other == "git":
  import error as er
  print("Clearing Error data")
  er.ready()
  print("Ready for GitHub! Now Closing...")
  import sys as s
  s.exit()
elif other == "r":
  r()
else:
    isofflineplatform = 1
    print("No input or unknown input. Running without colors.")
# starts application

print("Initializing...")
print("Importing \"error\"  [0/6]")
import error as er
print("Importing \"sys\"    [1/6]")
import sys as s
print("Importing \"os\"     [2/6]")
import os as o
print("Importing \"random\" [3/6]")
import random as r
print("Importing \"math\"   [4/6]")
import math as m
print("Importing \"helpapp\"[5/6]")
import helpapp as hlp
print("Finalizing...      [6/6]")
a = er.ready()
o.system('clear')
o.system('cls')
print("Import Complete!")
main()
