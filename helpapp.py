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



def help(a):
    os.system('cls')  # For Windows
    os.system('clear')  # For Linux/OS X
    print("")
    print("")
    print("")
    print("CALC 1.0 HELP")
    print("")
    print("")
    if a == 1:  # if the platform can't show colors, it will show only text without colors
        print(
            "main() -- executes main program. to manually execute this, type: 'main(\"pass\", -1)'"
        )
        print("")
        print(
            "calcbasic() -- basic calculation function. this only supports 2 digits and 4 different operations. used in form of 'calcbasic(digit0, operationtype, digit1'."
        )
        print("")
        print("  digit0 - first digit")
        print(
            "  operationtype - type of mathematical operation to execute. '+' is for addition, '-' for subtraction, '*' for multipication, and '/' for division."
        )
        print("  digit1 - second digit")
        print("")
        print("calcrand() -- random number generator")
        print("")
        print(
            "err() -- error reporting application. DO NOT EXECUTE THIS FUNCTION."
        )
        print("")
        print("help() -- this function")
        print("")
        print("This application also uses 5 modules.")
        print(
            "  os -- used normally for OS related actions, but in this case, clearing the screen."
        )
        print("  sys -- used to halt app in case of fatal error.")
        print("  random -- used to randomize numbers.")
        print("  math -- unused.")
        print("  helpapp -- used for help")
        print("")
        print("This application uses 1 special Python class.")
        print("")
        print(
            "  COLOR -- used to change the color, and or make the text printed in the shell bold and or underlined."
        )
        print(
            "Unfortinatly, this class is not supported on this platform. Please use a different version, or run online at https://repl.it/@elburg/CALC-BETA?embed=1&output=1"
        )
        print("")
        print("")
        print("NOTICE")
        print(
            "This app was built on Python 3.8.6. This means that some functions will not work with previous versions of Python. It should also be noted that this may not work with any desktop versions of Python, so it would be best to use an online IDE, such as Repl.it."
        )
    else:
        print(
            color.BOLD + "main()" + color.END +
            " -- executes main program. to manually execute this, type: 'main()'"
        )
        print("")
        print(
            color.BOLD + "calcbasic()" + color.END +
            " -- basic calculation function. this only supports 2 digits and 4 different operations. used in form of 'calcbasic(digit0, operationtype, digit1'."
        )
        print("")
        print("  " + color.BOLD + "digit0" + color.END + " - first digit")
        print(
            "  " + color.BOLD + "operationtype" + color.END +
            " - type of mathematical operation to execute. '+' is for addition, '-' for subtraction, '*' for multipication, and '/' for division."
        )
        print("  " + color.BOLD + "digit1" + color.END + " - second digit")
        print("")
        print(color.BOLD + "err()" + color.END +
              " -- error reporting application." + color.RED + color.BOLD +
              " DO NOT EXECUTE THIS FUNCTION." + color.END)
        print("")
        print(color.BOLD + "calcrand()" + color.END + " -- random number generator")
        print("")
        print(color.BOLD + "help()" + color.END + " -- this function")
        print("")
        print("This application also uses " + color.BOLD + "5" + color.END +
              " modules.")
        print(
            color.BOLD + "  os" + color.END +
            "-- used normally for OS related actions, but in this case, clearing the screen."
        )
        print(color.BOLD + "  sys" + color.END + " -- used to halt app in case of fatal error.")
        print(color.BOLD + "  random" + color.END + " -- used to randomize numbers.")
        print(color.BOLD + "  math" + color.END + " -- unused.")
        print(color.BOLD + "  helpapp" + color.END + " -- used for help")
        print("")
        print("This application uses " + color.BOLD + "1" + color.END +
              " special Python class.")
        print("")
        print(
            color.BOLD + "  COLOR " + color.END +
            "-- used to change the color, and or make the text printed in the shell bold and or underlined. Here are examples of the class in use."
        )
        print("")
        print(color.PURPLE + "    color.PURPLE")
        print(color.CYAN + "    color.CYAN")
        print(color.DARKCYAN + "    color.DARKCYAN")
        print(color.BLUE + "    color.BLUE")
        print(color.GREEN + "    color.GREEN")
        print(color.YELLOW + "    color.YELLOW")
        print(color.RED + "    color.RED")
        print(
            color.END + color.BOLD +
            "    color.BOLD -- can be combined with other colors and or color.UNDERLINE"
        )
        print(
            color.END + color.UNDERLINE +
            "    color.UNDERLINE -- can be combined with other colors and or color.BOLD"
        )
        print(
            color.END +
            "    color.END -- resets all color settings and shows default text"
        )
        print("")
        print("")
        print(color.BOLD + "NOTICE")
        print(
            "This app was built on Python 3.8.6. This means that some functions will not work with previous versions of Python. It should also be noted that this may not work with any desktop versions of Python, so it would be best to use an online IDE, such as Repl.it."
            + color.END)
import os