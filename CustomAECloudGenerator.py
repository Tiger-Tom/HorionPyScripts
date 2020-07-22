from tkinter import Tk
def askCopyClip(nbt):
    if input('COPY TEXT TO CLIPBOARD? (Y\\N) >').lower() != 'n':
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(nbt)
        r.update()
        r.destroy()
def generateEffect(effectID, level, displayAnim, duration, showParticles):
    effect = '{Ambient:0b,Amplifier:'+level+'b,DisplayOnScreenTextureAnimation:'+displayAnim+'b,Duration:'+duration+',DurationEasy:'+duration+',DurationHard:'+duration+',DurationNormal:'+duration+',Id:'+effectID+'b,ShowParticles:'+showParticles+'b}'
    return effect
def generateEffects(effects):
    nbt = ''
    for i in effects:
        nbt = nbt + i + ','
    return nbt
#{Ambient:0b,Amplifier:6b,DisplayOnScreenTextureAnimation:0b,Duration:9999999,DurationEasy:9999999,DurationHard:9999999,DurationNormal:9999999,Id:27b,ShowParticles:0b}
#{Ambient:0b,Amplifier:0b,DisplayOnScreenTextureAnimation:1b,Duration:100,DurationEasy:100,DurationHard:100,DurationNormal:100,Id:1,ShowParticles:1b}]
radius = input('ENTER RADIUS (IN METERS\\BLOCKS) (DAFAULT:3) >')
try:
    int(radius)
except:
    print ('INVALID RADIUS. SETTING TO DEFAULT OF 3')
    radius = '3'
radius = radius + 'f'
particleID = input('ENTER PARTICLE ID (DEFAULT:55) >')
try:
    int(particleID)
except:
    print ('INVALID PARTICLE ID. SETTING TO DEFAULT OF 55')
    particleID = '55'
particleColor = input('ENTER PARTICLE COLOR (DEFAULT:65520) >')
try:
    int(particleColor)
except:
    print ('INVALID PARTICLE COLOR. SETTING TO DEFAULT OF 65520')
    particleColor = '65520'
duration = input('ENTER DURATION (IN TICKS [20TICKS = 1SECOND]) (DEFAULT:600 TICKS [30SECONDS]) >')
try:
    int(duration)
except:
    print ('INVALID DURATION. SETTING TO DEFAULT OF 600')
    duration = '600'

fxs = []
lores = []
print ('PRESS CTRL+C WHEN YOU ARE DONE ENTERING EFFECTS')
while True:
    try:
        effectId = input('ENTER EFFECT ID (CAN BE FOUND AT https://minecraft.gamepedia.com/Bedrock_Edition_data_value#Effect_IDs) >')
        level = input('ENTER LEVEL OF EFFECT (STARTS AT 0) >')
        #displayAnim = input('DISPLAY ON SCREEN TEXTURE ANIMATION? (Y\\N) >')
        #if displayAnim.lower() != 'n':
        #    displayAnim = '1'
        #else:
        #    displayAnim = '0'
        displayAnim = '0'
        duration = input('ENTER EFFECT DURATION IN TICKS >')
        showParticles = input('SHOW PARTICLES? (Y\\N) >')
        if showParticles.lower() != 'n':
            showParticles = '1'
        else:
            showParticles = '0'
        effect = generateEffect(effectId, level, displayAnim, duration, showParticles)
        fxs.append(effect)
        lores.append(effectId+':'+level+':'+duration)
    except KeyboardInterrupt:
        break
name = 'Custom Potion Generator'
lore = ''
for i in lores:
    lore = lore + '"' + i + '",'
effects = generateEffects(fxs)
nbt = '{Items:[{Count:1b,Damage:5s,Name:"minecraft:bucket",Slot:2b,tag:{EntityType:95,Duration:'+duration+',DurationOnUse:'+duration+',InitialRadius:'+radius+'f,Invulnerable:1b,ParticleColor:'+particleColor+',ParticleId:'+particleID+',Pos:[6.5f,4.5f,8.5f],PotionId:11s,Radius:'+radius+'f,Persistant:1b,RadiusChangeOnPickup:0f,RadiusOnUse:0f,RadiusPerTick:0f,ReapplicationDelay:40,Rotation:[19.8044f,0f],Variant:0,definitions:["+minecraft:area_effect_cloud"],mobEffects:['+effects+'],display:{Lore:['+lore+'],Name:"Custom Potion Generator"}}}],display:{Lore:['+lore+'],Name:"'+name+'"}}'
print ('USE [.nbt write] ON A STORAGE BLOCK (CHEST, SHULKER, FURNACE, DISPENSER\\DROPPER) AND TAKE PUFFERFISH BUCKET OUT AND PLACE BUCKET DOWN TO USE')
print (nbt)
askCopyClip(nbt)






#Duration:9999999,DurationOnUse:9999999,InitialRadius:3f,Invulnerable:1b,ParticleColor:65520,ParticleId:55,Pos:[6.5f,4.5f,8.5f],PotionId:11s,Radius:8f,Persistant:1b,RadiusChangeOnPickup:0f,RadiusOnUse:0f,RadiusPerTick:0f,ReapplicationDelay:40,Rotation:[19.8044f,0f],Variant:0,definitions:["+minecraft:area_effect_cloud"],
