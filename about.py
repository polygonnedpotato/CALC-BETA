appinfo = {
    "appname":"Command-Based mathematical processor",
    "appnameshort":"CALC-BETA",
    "version":"1.2-BETA03",
    "isdebugver":"true",
    "isbetaver":"true",
    "developer":"@elburg",
    "webversion?":"true",
    "weblink":"https://repl.it/@elburg/CALC-BETA?embed=1&output=1",
    "usesclasses":"true",
    "classcount":1,
    "classes":"color",
    "classes/color#subclasses":"PURPLE;CYAN;DARKCYAN;BLUE;GREEN;YELLOW;RED;BOLD;UNDERLINE;END",
    "usesstrings?":"false",
    "functioncount":6,
    "funtions":"help();calcbasic(*arg);main(source, srcver);err(code, source, c);calcrand(*arg);r()",
    "usesmodules?":"true",
    "modules":"os;sys;random;math;helpapp",
    "containshelp?":"true",
    "helpfunction":"calc.help()"
}
def main():
  print("not_implimented")
def full():
  for x, y in appinfo.items():
    print(x, ":", y)
