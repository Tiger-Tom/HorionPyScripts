from tkinter import Tk
def askCopyClip(nbt):
    if input('COPY TEXT TO CLIPBOARD? (Y\\N) >').lower() != 'n':
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(nbt)
        r.update()
        r.destroy()
def generateEnch(id_, lvl):
    return '{id:'+id_+'s,lvl:'+lvl+'s}'
def generateEnchs(enchs):
    ench = '{ench:['
    for i in enchs:
        ench = ench + i + ','
    ench = ench.split(',')
    del(ench[-1])
    ench = ','.join(ench)
    ench = ench + ']}'
    return ench

print ('PRESS CTRL+C WHEN YOU ARE FINISHED ENTERING ENCHANTMENTS. ENCHANTING AN ITEM WITH THIS WILL DELETE EVERY OTHER ITEM.')
print ('YOU CAN FIND A LIST OF ENCHANTMENT IDS AT https://minecraftbedrock.fandom.com/wiki/Enchanting/List_of_Enchantments')
enchs = []
while True:
    try:
        id_ = input('ENTER ENCHANTMENT ID >')
        lvl = input('ENTER ENCHANTMENT LEVEL >')
        try:
            int(lvl)
        except:
            print ('INCORRECT VALUE FOR LEVEL. SETTING TO 1')
            lvl = '1'
        enchs.append(generateEnch(id_, lvl))
    except KeyboardInterrupt:
        break
nbt = generateEnchs(enchs)
print ('TO ENCHANT AN ITEM, USE [.nbt write] WHILE HOLDING ANY ITEM')
print (nbt)
askCopyClip(nbt)
