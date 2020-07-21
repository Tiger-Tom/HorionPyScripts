from tkinter import Tk
def askCopyClip(nbt):
    if input('COPY TEXT TO CLIPBOARD? (Y\\N) >').lower() != 'n':
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(nbt)
        r.update()
        r.destroy()

x = input('ENTER X VALUE TO TP TO >')
y = input('ENTER Y VALUE TO TP TO >')
z = input('ENTER Z VALUE TO TP TO >')
print ('GENERATING NBT FOR END GATEWAY TO TP TO '+x+ ' ; '+y+ ' ; '+z)
print ('TO GET COMMAND, USE [.nbt write] WHILE HOLDING A STORAGE ITEM (CHEST, FURNACE, DISPENSER\\DROPPER, ETC. THEN TAKE OUT THE GATEWAY AND PLACE IT WHEREVER. YOU CAN USE THE INSTABREAK HACK TO REMOVE IT IF NEED BE.')
nbt = '{Items:[{Count:1b,Damage:0s,Name:"minecraft:end_gateway",Slot:0b,tag:{ExactTeleport:1b,ExitPortal:['+x+','+y+','+z+'],display:{Lore:["End Gateway to '+x+' ; '+y+' ; '+z+'"],Name:"End Gateway"}}}],display:{Lore:["Hacked"],Name:"Hacked"},ench:[{id:26s,lvl:1s}]}'
print (nbt)
askCopyClip(nbt)
