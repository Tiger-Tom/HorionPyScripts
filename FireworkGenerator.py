from tkinter import Tk
def askCopyClip(nbt):
    if input('COPY TEXT TO CLIPBOARD? (Y\\N) >').lower() != 'n':
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(nbt)
        r.update()
        r.destroy()
explosions = []
flightDur = input('ENTER FLIGHT DURATION (DEFAULT: 1) >')
try:
    int(flightDur)
except:
    print ('INCORRECT FLIGHT DURATION. SETTING TO 1')
    flightDur = '1'
print ('PRESS CTRL+C ONCE YOU HAVE FINISHED INPUTTING THE EXPLOSIONS')
while True:
    try:
        twinkle = input('DOES CURRENT EXPLOSION HAVE TWINKLE? (Y\\N) >')
        if twinkle.lower() != 'y':
            twinkle = '0'
        else:
            twinkle = '1'
        trail = input('DOES CURRENT EXPLOSION HAVE TRAIL? (Y\\N) >')
        if trail.lower() != 'y':
            trail = '0'
        else:
            trail = '1'
        #colors = []#'BCC458'#input('ENTER FIREWORK COLOR (YOU CAN GET THE DECIMAL COLORS FROM https://www.mathsisfun.com/hexadecimal-decimal-colors.html) >')
        #print ('PRESS CTRL+C WHEN YOU ARE DONE INPUTTING THE DYE COLORS. THE DYE VALUES CAN BE FOUND AT https://minecraft.gamepedia.com/Dye#Item_data , IN THE "DEC" COLUMN UNDERNEATH THE "DATA" COLUMN')
        #while True:
        #    try:
        #        color = input('ENTER DYE VALUE >')
        #        try:
        #            int(color)
        #            colors.append(color)
        #        except:
        #            print ('INCORRECT COLOR')
        #    except KeyboardInterrupt:
        #        break
        #colorNBT = str(colors)
        #colorNBT = colorNBT.replace(' ', '').replace('\'', '')
        #print (colors)
        #print (colorNBT)
        print ('DUE TO A LIMIT IN NBT DATA EDITING, ADDING CUSTOM COLORS ISN\'T POSSIBLE. SORRY FOR ANY INCONVINIENCE.')
        print ('FIREWORK TYPES:\n- 0 : SMALL BALL\n- 1 : LARGE BALL\n- 2 : STAR SHAPED\n- 3 : CREEPER SHAPED\n- 4 : BURST')
        type_ = input('SELECT A FIREWORK TYPE >')
        explosion = '{FireworkFade:,FireworkFlicker:'+twinkle+'b,FireworkTrail:'+trail+'b,FireworkType:'+type_+'b}'
        explosions.append(explosion)
    except KeyboardInterrupt:
        break
nbt = '{Fireworks:{Explosions:['
for i in explosions:
    nbt = nbt + i + ','
nbt = nbt + '],Flight:'+flightDur+'b}}'
print ('USE [.nbt write] WHILE HOLDING A FIREWORK ROCKET TO APPLY EFFECTS')
print (nbt)
askCopyClip(nbt)
