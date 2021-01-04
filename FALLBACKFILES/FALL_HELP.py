def help():
    os.system('cls')  # For Windows
    os.system('clear')  # For Linux/OS X
    print("")
    print("")
    print("")
    print("CALC 1.2 HELP")
    print("")
    print("")
    if isofflineplatform == 1:  # if the platform can't show colors, it will show only text without colors
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
        print(
            "err() -- error reporting application. DO NOT EXECUTE THIS FUNCTION."
        )
        print("")
        print("help() -- this function")
        print("")
        print("This application also uses 1 module.")
        print(
            "  os -- used normally for OS related actions, but in this case, clearing the screen."
        )
        print("")
        print("This application uses 1 special Python class.")
        print("")
        print(
            "  COLOR -- used to change the color, and or make the text printed in the shell bold and or underlined."
        )
        print(
            "Unfortinatly, this class is not supported on this platform. Please use a different version, or run online at https://CALC.elburg.repl.run"
        )
        print("")
        print("")
        print("NOTICE")
        print(
            "This app was built on Python 3.9. This means that some functions will not work with previous versions of Python. It should also be noted that this may not work with any desktop versions of Python, so it would be best to use an online IDE, such as Repl.it."
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
        print(color.BOLD + "help()" + color.END + " -- this function")
        print("")
        print("This application also uses " + color.BOLD + "1" + color.END +
              " module.")
        print(
            color.BOLD + "  os" + color.END +
            "-- used normally for OS related actions, but in this case, clearing the screen."
        )
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
    print("")
    print("")
    print("SPECIAL APP METADATA")
    print("")
    for x, y in appinfo.items():
        print(x, ":", y)