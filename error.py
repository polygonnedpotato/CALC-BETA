import datetime as dt
import sys as s

from about import appinfo as mtdt


class color:
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'
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
  "1x000": "NOT_REPLIT"
}
errdef = {
  "0x000": "The input received was in an invalid format, or was not an input the program was looking for.",
  "0x001": "It is impossible to divide any number by Zero(0).",
  "0x002": "The file system cannot be accessed.",
  "0x003": "The application is corrupted.",
  "0x004": "This is a sample error.",
  "0x005": "This is a sample critical error.",
  "0x006": "There was an unknown error. Try running the app again and try to find out where it occurred",
  "0x007": "This function is not implemented",
  "0x008": "This function can only be accessed by the developer",
  "0x009": "The number is out of the 64-bit range and was returned as infinity",
  "1x000": "This command is not available. the platform this command can b used is on Repl.it"
}
def err(code, source, c, i, d):
    if code in errcodes:
        errcodedef = errcodes[code]
    else:
        errcodedef = errcodes["0x006"]
    define = errdef[code]
    if c == "f":
        if i == 1:
            print("===FATAL_ERROR==================")
            print(
                "A component has caused the application to close unexpectedly")
            print("Here is data linked to this crash.")
            print("CODE:" + code)
            print(errcodedef)
            print(define)
            print("SOURCE:" + source)
            print("TYPE:FATAL")
        else:
            print(color.RED + color.BOLD + "===FATAL_ERROR==================")
            print(
                "A component has caused the application to close unexpectedly")
            print("Here is data linked to this crash.")
            print("CODE:" + code)
            print(errcodedef)
            print(define)
            print("SOURCE:" + source)
            print("TYPE:FATAL" + color.END)
        print("Collecting Data... Please wait...")
        f = open("errinf.md", "wt")
        f.write("")
        f.close()
        d = dt.datetime.now()
        f = open("errinf.md", "at")
        f.write("# Error details")
        f.write("\nA fatal error had occurred while CALC was in use so CALC had to be stopped. Below are details about the said crash.")
        f.write("\n")
        f.write("\nApp Name and version: " + mtdt["appnameshort"] + "" + mtdt["version"])
        if d == 1:
          f.write(" [DEBUG-MODE]")
        else:
          pass
        f.write("\nDeveloper: " + mtdt["developer"])
        f.write("\nDate and Time of Error: " + d.strftime("%c"))
        f.write("\nError code returned: " + code)
        f.write("\nError Name: " + errcodedef)
        f.write("\nDefinition: " + define)
        f.write("\nSource: " + source)
        f.write("\nComments: Replace this part with your comments including what had happened.")
        f.write("\n")
        f.write("\nExtra Metadata for developer:")
        f.write("\n")
        f.write("\n")
        for x, y in mtdt.items():
          f.write("\n" + x)
          f.write(" : ")
          f.write(str(y))
        f.close()
        a = input("Hey! Before you restart this, Please open the \"errinf.md\" file. It contains error data on what just happened. Download it and use it to write an issue in the project's GitHub")
        if a == "failsafe":
          print("manual error details")
          print("")
          print("")
          print("")
          print("# Error details")
          print("A fatal error had occurred while CALC was in use so CALC had to be stopped. Below are details about the said crash.")
          print("")
          
          if d == 1:
            print("App Name and version: " + mtdt["appnameshort"] + "" + mtdt["version"] + "[DEBUG-MODE]")
          else:
            print("App Name and version: " + mtdt["appnameshort"] + "" + mtdt["version"])
          print("Developer: " + mtdt["developer"])
          print("Date and Time of Error: " + d.strftime("%c"))
          print("Error code returned: " + code)
          print("Error Name: " + errcodedef)
          print("Definition: " + define)
          print("Source: " + source)
          print("Comments: Replace this part with your comments including what had happened.")
          print("")
          print("Extra Metadata for developer:")
          print("")
          print("")
          for x, y in mtdt.items():
            print(x, ":", y)
          print("")
          se = input("copy the above lines and add it to a text document. then go to \"github.com\polygonnedpotato\calc-beta\", click on issues, click new issue, and click \"Get started\"")
        s.exit()
    elif c == "c":
        if i == 1:
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
            print(color.YELLOW + color.BOLD + "===CRITICAL_ERROR===============")
            print(
                "A component has ran into an error.")
            print("Here is data linked to this error.")
            print("CODE:" + code)
            print(errcodedef)
            print(define)
            print("SOURCE:" + source)
            print("TYPE:CRITICAL" + color.END)

def ready():
  f = open("errinf.md", "wt")
  f.write("No error here, move along...")
  f.close()