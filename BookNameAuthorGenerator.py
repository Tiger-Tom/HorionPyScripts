from tkinter import Tk
def askCopyClip(nbt):
    if input('COPY TEXT TO CLIPBOARD? (Y\\N) >').lower() != 'n':
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(nbt)
        r.update()
        r.destroy()
author = input('ENTER AUTHOR NAME TO WRITE >')
title = input('ENTER BOOK TITLE TO WRITE >')
print ('BOOK GENERATION IDS: \n0 : ORIGINAL\n1 : COPY OF ORIGINAL\n2 : COPY OF COPY\n3 : TATTERED\n(ANYTHING ELSE WILL BE [book.generation.GEN])')
gen = input('ENTER BOOK GENERATION >')
nbt = '{author:"'+author+'",generation:'+gen+',title:"'+title+'"}'
print ('USE [.nbt write] ON A WRITTEN BOOK TO USE')
print (nbt)
askCopyClip(nbt)
