print("welcome to calc!")
print("please choose an option")
print("[1] use normal main funtion")
print("[2] try new main funtion")
a = input()
if a == 1:
  import os
  os.system("main.py")
elif a == 2:
  import newmain
  newmain.start("null")