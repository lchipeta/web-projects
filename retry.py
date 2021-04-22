import sys, msvcrt
from read_text import read_letters
import motel_navigation
def retry():
  read_letters("Would you like to try again? Y/N\n\033[1;37;40m")
  reset = msvcrt.getch().decode().lower()
  if reset == "y":
    motel_navigation.enter_corridor()
  elif reset == "n":
    read_letters("Thank you for playing!")
    sys.exit()
  else:
    read_letters("Please enter Y/N\n")
    retry()