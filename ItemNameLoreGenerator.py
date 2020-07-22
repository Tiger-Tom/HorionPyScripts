from tkinter import Tk
def askCopyClip(nbt):
    if input('COPY TEXT TO CLIPBOARD? (Y\\N) >').lower() != 'n':
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(nbt)
        r.update()
        r.destroy()

codes = {
    'color:dark_red': 'Â§4',
    'color:red': 'Â§c',
    'color:gold': 'Â§6',
    'color:yellow': 'Â§e',
    'color:dark_green': 'Â§2',
    'color:green': 'Â§a',
    'color:aqua': 'Â§b',
    'color:dark_aqua': 'Â§3',
    'color:dark_blue': 'Â§1',
    'color:blue': 'Â§9',
    'color:light_purple': 'Â§d',
    'color:dark_purple': 'Â§5',
    'color:white': 'Â§f',
    'color:gray': 'Â§7',
    'color:dark_gray': 'Â§8',
    'color:black': 'Â§0',
    'format:obfuscated': 'Â§k',
    'format:bold': 'Â§l',
    'format:strikethrough': 'Â§m',
    'format:underline': 'Â§n',
    'format:italic': 'Â§o',
    'code:reset': 'Â§r',
}
codesInternal = {
    '\\cdr\\': 'color:dark_red',
    '\\cr\\': 'color:red',
    '\\cg\\': 'color:gold',
    '\\cy\\': 'color:yellow',
    '\\cdg\\': 'color:dark_green',
    '\\cg\\': 'color:green',
    '\\ca\\': 'color:aqua',
    '\\cda\\': 'color:dark_aqua',
    '\\cdb\\': 'color:dark_blue',
    '\\cb\\': 'color:blue',
    '\\clp\\': 'color:light_purple',
    '\\cdp\\': 'color:dark_purple',
    '\\cw\\': 'color:white',
    '\\cg\\': 'color:gray',
    '\\cdg\\': 'color:dark_gray',
    '\\cb\\': 'color:black',
    '\\fo\\': 'format:obfuscated',
    '\\fb\\': 'format:bold',
    '\\fs\\': 'format:strikethrough',
    '\\fu\\': 'format:underline',
    '\\fi\\': 'format:italic',
    '\\rst\\': 'code:reset',
}
def generate(name, lores):
    nbt = 'display:{Lore:['
    for i in lores:
        nbt = nbt + '"' + i + '",'
    #nbt = nbt.split(',')
    #del(nbt[-1])
    #nbt = ','.join(nbt)
    nbt = nbt + '],Name:"'+name+'"}'
    nbt = '{' + nbt + '}'
    return nbt
if input('PRINT CUSTOM CODES (COLOR \\ FORMAT)? (Y\\N) >').lower() == 'y':
    print ('JUST TYPE IN THE CODE TO APPLY THE FORMATTING')
    print ('CODE : FORMAT')
    for i in codesInternal:
        print (i + ' : ' + codesInternal[i])
name = input('ENTER CUSTOM NAME >')
for i in codesInternal:
    name = name.replace(i, codesInternal[i])
for i in codes:
    name = name.replace(i, codes[i])
lores = []
print ('PRESS CTRL+C WHEN YOU ARE DONE ENTERING LORES')
while True:
    try:
        lore = input('ENTER LORE >')
        for i in codesInternal:
            lore = lore.replace(i, codesInternal[i])
        for i in codes:
            lore = lore.replace(i, codes[i])
    except KeyboardInterrupt:
        break
nbt = generate(name, lores)
print ('TO SET NAME & LORE OF ITEM, USE [.nbt write] ON THE ITEM YOU WANT TO NAME & LORE')
print (nbt)
askCopyClip(nbt)
