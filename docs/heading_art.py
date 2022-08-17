import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "!pip", "install", package])

def heading(text,my_color=False):
  if __name__ == '__main__':
    import pyfiglet
    import termcolor
    from random import choice

    if type(my_color) == int:
      raise TypeError('Please enter a valid color!')
    elif not my_color:
      color = choice(('red','green','yellow','blue','magenta','cyan','white')) 
    elif my_color not in ('red','green','yellow','blue','magenta','cyan','white'):
      raise ValueError('Color not in valid range')
    else:
      color = my_color
    rendered = pyfiglet.figlet_format(text, font='standard')
    colored_text = termcolor.colored(rendered,color)
    return  print(colored_text)

if __name__ == '__main__':
  install()
  heading()

