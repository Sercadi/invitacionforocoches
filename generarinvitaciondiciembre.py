import webbrowser
import pyperclip

print('Introduce código :')
invitacion = input()
invitacionmayuscula=invitacion.swapcase()
    
pyperclip.copy(str(''.join(invitacionmayuscula)))

webbrowser.open("https://www.forocoches.com/codigo/", new=2, autoraise=True)
