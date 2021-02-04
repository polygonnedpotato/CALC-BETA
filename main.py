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
debug = 0
appinfo = {
  "appname":
    "Command-Based mathematical processor",
  "appnameshort":
    "CALC-BETA",
  "version":
    "1.2-BETA04",
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
  hlp.help(isofflineplatform, debug)

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
              if noreplit == 0:
                d["ans"] = result
              else:
                pass
        if arg[1] == "-":
            result = str((x - y))
            if result == "inf":
              err("0x009", "main.py#def_calcbasic", "c")
            else:
              print("The Result is: " + result)
              if noreplit == 0:
                d["ans"] = result
              else:
                pass
        if arg[1] == "*":
            result = str((x * y))
            if result == "inf":
              err("0x009", "main.py#def_calcbasic", "c")
            else:
              print("The Result is: " + result)
              if noreplit == 0:
                d["ans"] = result
              else:
                pass
        if arg[1] == "/":
            if y == 0:
                err("0x001", "main.py#def_calcbasic", "f")
            else:
                result = str((x / y))
                if result == "inf":
                  err("0x009", "main.py#def_calcbasic", "c")
                else:
                  print("The Result is: " + result)
                  if noreplit == 0:
                    d["ans"] = result
                  else:
                    pass
    else:
      if arg[1] == "+":
        result = str((x + y))
        print("The Result is: " + color.BOLD + result + color.END)
        if noreplit == 0:
          d["ans"] = result
        else:
          pass
      if arg[1] == "-":
        result = str((x - y))
        print("The Result is: " + color.BOLD + result + color.END)
        if noreplit == 0:
          d["ans"] = result
        else:
          pass
      if arg[1] == "*":
        result = str((x * y))
        print("The Result is: " + color.BOLD + result + color.END)
        if noreplit == 0:
          d["ans"] = result
        else:
          pass
      if arg[1] == "/":
        if y == 0:
          err("0x001", "main.py#def_calcbasic", "f")
        else:
          result = str((x / y))
          print("The Result is: " + color.BOLD + result + color.END)
          if noreplit == 0:
            d["ans"] = result
          else:
            pass


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
def calcint(*arg):
  inpu = arg[0]
  if int(inpu) < 0:
    print(inpu + " is negative.")
  elif int(inpu) > 0:
    print(inpu + " is positive.")
  else:
    print(inpu + " is not negative nor positive.")


#main function.
def main():
    print("")
    print("")
    print("")
    if isofflineplatform == 1:
        print("        CALC 1.2 [BETA]")
        print("          by  @elburg")
    else:
        print(color.BOLD + color.DARKCYAN + "        CALC 1.2 [BETA]" +
              color.END)
        print("          by  " + color.RED + "@" + color.YELLOW + "e" +
              color.GREEN + "l" + color.CYAN + "b" + color.DARKCYAN + "u" +
              color.BLUE + "r" + color.PURPLE + "g" + color.END)
    print("")
    if debug == 1:
      print('DEBUG MODE')
    else:
      pass
    print("VERSION:" + appinfo["version"])
    print("")
    print("")
    loop = 0
    while loop == 0:
        print(
          "Please enter the type of calculations you want to do. (For Help, type \"help\" or \"exit\" to exit) "
          "AVAILABLE:BASIC,RAND,INT "
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
            if temp == "ans":
              if noreplit == 0:
                d0 = int(d["ans"])
              else:
                err("1x000", "main.py#def_main", "f")
            else:
              d0 = int(temp)
            temp = input("Enter your second digit:")
            if temp == "ans":
              if noreplit == 0:
                d1 = int(d["ans"])
              else:
                err("1x000", "main.py#def_main", "f")
            else:
              d1 = int(temp)
            temp = input(
              "Enter which operation you want to execute. (Types Available: +, -, *, /):"
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
        elif typeofmath == "Int" or typeofmath == "int" or typeofmath == "INT":
          stop = 0
          while stop == 0:
            inp = input("Enter Integer (Enter STOP to end): ")
            if inp == "STOP":
              break
            else:
              calcint(inp)
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
  er.err(code, source, c, isofflineplatform , debug)

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
      hlp.help(isofflineplatform, debug)
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
noreplit = 0
import platform as p
if p.system() == "Linux":
  isofflineplatform = 0
  te = input("CALC has detected that the platform is Linux. This means Colors will be used. Press ENTER to start.")
  if te == " -d":
    debug = 1
  elif te == " -b":
    import subprocess

    subprocess.call("build.sh")
  elif te == " -noreplit":
    noreplit = 1
  elif te == " -d -noreplit":
    debug = 1
    noreplit = 1
  else:
    pass
elif p.system() == "Windows":
  isofflineplatform = 1
  noreplit = 1
  te = input(
    "CALC has detected that the platform is Windows. This means Colors will not be used. Press ENTER to start.")
  if te == " -d":
    debug = 1
  else:
    pass
elif p.system() == "Darwin":
  isofflineplatform = 0
  noreplit = 1
  te = input("WARNING! CALC CANNOT RUN ON DARWIN AS THE PYTHON VERSION INSTALLED IS 2.7. PRESS ENTER TO CONTINUE "
             "ANYWAYS.")
  if te == " -d":
    debug = 1
  else:
    pass
print("Initializing...")
print("Importing \"error\"  [0/7]")
import error as er

print("Importing \"sys\"    [1/7]")
print("Importing \"os\"     [2/7]")
import os as o

print("Importing \"random\" [3/7]")
import random as r

print("Importing \"math\"   [4/7]")
print("Importing \"helpapp\"[5/7]")
import helpapp as hlp

if noreplit == 0:
  print("Importing \"db\"     [6/7]")
  from replit import db as d
else:
  print("Platform is not Repl.it. Skipping \"db\"")
  pass
print("Finalizing...      [7/7]")
a = er.ready()
if noreplit == 0:
  d["ans"] = "nan"
  d["starttime"] = ""
else:
  pass
if debug == 1:
  pass
else:
  o.system('clear')
  o.system('cls')
print("Import Complete! Initializing CALC")
main()