from tkinter import Tk
def askCopyClip(nbt):
    if input('COPY TEXT TO CLIPBOARD? (Y\\N) >').lower() != 'n':
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(nbt)
        r.update()
        r.destroy()
patterns = {
    'Snout': 'pig',
    'Bordure Indenter': 'bfo',
    'Field Masoned': 'bri',
    'Thing': 'moj',
    'Flower Charge': 'flo',
    'Skull Charge': 'sku',
    'Creeper Charge': 'cre',
    'Bordure': 'bo',
    'Roundel': 'mc',
    'Saltire': 'cr',
    'Per Bend Inverted': 'ld',
    'Per Bend Sinister Inverted': 'rud',
    'Per Bend Sinister': 'lud',
    'Per Bend': 'rd',
    'Gradient': 'gra',
    'Base Gradient': 'gru',
    'Per Fess': 'hh',
    'Per Fess Inverted': 'hhb',
    'Per Pale': 'vh',
    'Per Pale Inverted': 'vhr',
    'Lozenge': 'mr',
    'Per Paly': 'ss',
    'Base Dexter Canton': 'bl',
    'Base Sinister Canton': 'br',
    'Chief Dexter Canton': 'tl',
    'Chief Sinister Canton': 'tr',
    'Cross': 'sc',
    'Base Fess': 'bs',
    'Pale': 'cs',
    'Bend Sinister': 'dls',
    'Bend': 'drs',
    'Pale Dexter': 'ls',
    'Fess': 'ms',
    'Pale Sinister': 'rs',
    'Chief Fess': 'ts',
    'Chevron': 'bt',
    'Inverted Chevron': 'tt',
    'Base Indented': 'bts',
    'Chief Indented': 'tts',
}
colors = {
    'Black': '0',
    'Red': '1',
    'Green': '2',
    'Brown': '3',
    'Blue': '4',
    'Purple': '5',
    'Cyan': '6',
    'Light Gray': '7',
    'Gray': '8',
    'Pink': '9',
    'Lime': '10',
    'Yellow': '11',
    'Light Blue': '12',
    'Magenta': '13',
    'Orange': '14',
    'White': '15',
}
if input('PRINT BANNER PATTERN CODES? (Y\\N) >').lower() != 'n':
    print ('NAME : CODE')
    for i in patterns:
        print (i + ' : ' + patterns[i])
if input('PRINT BANNER COLOR CODES? (Y\\N) >').lower() != 'n':
    print ('COLOR : CODE')
    for i in colors:
        print (i + ' : ' + colors[i])
def generate(color, pattern):
    return '{Color:'+color+',Pattern:"'+pattern+'"}'
def generate2(patterns):
    nbt = '{Patterns:['
    for i in patterns:
        nbt = nbt + i + ','
    nbt = nbt + ']}'
    return nbt
layer = 0
patterns = []
print ('PRESS CTRL+C WHEN YOU ARE DONE ENTERING PATTERNS')
while True:
    try:
        pattern = input('ENTER PATTERN ID FOR LAYER '+str(layer)+' >')
        color = input('ENTER COLOR OF PATTERN >')
        try:
            if int(color) > 15 or int(color) < 0:
                raise Exception
            patterns.append(generate(color, pattern))
            layer = layer + 1
        except:
            print ('INVALID BANNER COLOR SELECTED')
    except KeyboardInterrupt:
        break
nbt = generate2(patterns)
print ('USE [.nbt write] ON HELD BANNER TO APPLY PATTERN (THIS WILL DELETE ANY PATTERN ALREADY ON THE BANNER)')
print (nbt)
askCopyClip(nbt)
