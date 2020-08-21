from os import system
prog = ['chrome', 'notepad', 'wmplayer', 'vlc', 'anaconda', 'jupyter notebook', 'idle', 'teamviewer', "github"]
ignore, cont = ["not", 'terminate'], True
#trig = ["run", "launch", "execute", "load"]
print("Please, enter your name: ", end='')
name = input().capitalize()
print(f"Hello, {name}, greetings...\n", end='')
print('The list of programs: \n')
for i in prog:
     print(i, end=', ')
while cont:   
     print('\n\n############################################################################## \
     	    \n\nEnter your command: ', end='')
     command = input().lower()
     for i in ignore:
          if i in command.split():
               print('Command did not run')
               break   
          else:
               for k in prog:
                    if k in command:
                         choice = k
          if 'load' in command or 'run' in command or 'execute' in command or 'launch' in command:
               if system(choice) == 0:
                    print(f'{choice} executed')
                    break
               else:
                    print("ERROR!!!, \nUNABLE TO EXECUTE.")
                    break
          else:
               print('COMMAND NOT VALID.')
               break
     print('\n\n ############################################################################# \
     	    \n\nDo you wish to continue? (Y/N): ', end='')
     cont = input().lower()
     if cont == 'n':
          print('Thank You!')
          cont =False

