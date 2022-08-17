def install_pyfiglet():
  if __name__ == '__main__':
    !pip install pyfiglet

def install_termcolor():
  if __name__ == '__main__':
    !pip install termcolor

def heading(text,my_color=None):
  if __name__ == '__main__':
    import pyfiglet
    import termcolor
    from random import choice
    try:
      if type(color) == int:
        raise TypeError
    except TypeError:
      print('Please enter a valid color!')
    else:
      if my_color == None:
        color = choice(('red','green','yellow','blue','magenta','cyan','white')) 
      elif my_color not in ('red','green','yellow','blue','magenta','cyan','white'):
      
    color = my_color
    rendered = pyfiglet.figlet_format(text, font='standard')
    colored_text = termcolor.colored(rendered,color)
    print(colored_text)
