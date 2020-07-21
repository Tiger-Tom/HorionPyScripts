from tkinter import Tk
def askCopyClip(nbt):
    if input('COPY TEXT TO CLIPBOARD? (Y\\N) >').lower() != 'n':
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(nbt)
        r.update()
        r.destroy()
damage = input('ENTER DAMAGE VALUE TO SET >')
nbt = '{Damage:'+damage+'}'
print ('USE [.nbt write] WHILE HOLDING ANY ITEM TO SET THE DAMAGE VALUE')
print (nbt)
askCopyClip(nbt)
