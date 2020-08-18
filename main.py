import random
from colorama import Fore

def invitegen():
  invite = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

  char = random.choice((invite))
  char2 = random.choice((invite))
  char3 = random.choice((invite))
  char4 = random.choice((invite))
  char5 = random.choice((invite))
  char6 = random.choice((invite))

  print(f'{Fore.GREEN}https://discord.gg/{Fore.RESET}{Fore.RED}{char}{char2}{char3}{char4}{char5}{char6}{Fore.RESET}')

while True:
  invitegen()
