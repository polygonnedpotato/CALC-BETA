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
elif other == "y -d":
    isofflineplatform = 0
    debug = 1
    print("Running with colors.")
elif other == "Y -d":
    isofflineplatform = 0
    debug = 1
    print("Running with colors.")
elif other == "n":
    isofflineplatform = 1
    print("Running without colors.")
elif other == "N":
    isofflineplatform = 1
    print("Running without colors.")
elif other == "n -d":
    isofflineplatform = 1
    debug = 1
    print("Running without colors.")
elif other == "N -d":
    isofflineplatform = 1
    debug = 1
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