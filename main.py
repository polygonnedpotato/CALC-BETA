import random as r
def help():
  print("==CALC EMBEDDED HELP==")
  print("IMPORT: use the import command to add main.py to your project. It is recommened that you rename the file first before adding it. In this tutorial, it will be imported as calc.")
  print("")
  print(" import main as calc ")
  print("")
  print("calc.calcbasic() -- basic ops. empty command returns nothing. the wildcards used here are integers for the op. decimals will not work.")
  print("calc.calcbasic(\"*\" , \"+\" , \"*\") -- basic addition ops.")
  print("calc.calcbasic(\"*\" , \"-\" , \"*\") -- basic subtraction ops.")
  print("calc.calcbasic(\"*\" , \"*\" , \"*\") -- basic multiplication ops. note: * in middle is required in execution.")
  print("calc.calcbasic(\"*\" , \"/\" , \"*\") -- basic division ops.")
  print("calc.calcrand() -- random number ops. empty command returns nothing. the wildcards used here are integers for the op but are harder to understand. the first wildcard is the amount of numbers to generate. the second wildcard is the lowest number to generate. the third wildcard is the highest number to generate. decimals will not work.")
  print("calc.calcrand(\"*\" , \"*\" , \"*\" , \"0\") -- random number ops. returns lowest number")
  print("calc.calcrand(\"*\" , \"*\" , \"*\" , \"1\") -- random number ops. returns highest number")
  print("calc.calcrand(\"*\" , \"*\" , \"*\" , \"2\") -- random number ops. returns average number")
def calcbasic(*a):
    x = int(a[0])
    y = int(a[2])
    if a[1] == "+":
      result = str((x + y))
      if result == "inf":
        return "inferror"
      else:
        return result
    if a[1] == "-":
      result = str((x - y))
      if result == "inf":
        return "inferror"
      else:
        return result
    if a[1] == "*":
      result = str((x * y))
      if result == "inf":
        return "inferror"
      else:
        return result
    if a[1] == "/":
      if y == 0:
        return "dividebyzeroerror"
      else:
        result = str((x / y))
        if result == "inf":
          return "inferror"
        else:
          return result
def calcrand(*a):
    amt = int(a[0])
    low = int(a[1])
    high = int(a[2])
    stop = 0
    tempint = 0
    tempavg = 0
    tempset = []
    while stop == 0:
        tempset.clear()
        for x in range(amt):
            result = str(r.randint(low, high))
            tempset.append(result)
        if a[3] == 0:
          tempint = min(tempset)
          if tempint == "inf":
            return "inferror"
          else:
            return tempint
        elif a[3] == 1:
          tempint = max(tempset)
          if tempint == "inf":
            return "inferror"
          else:
            return tempint
        elif a[3] == 2:
          for x in tempset:
            tempavg += int(x)
          tempint = str(tempavg / amt)
          if tempint == "inf":
            return "inferror"
          else:
            return tempint 