from tkinter import Tk
def askCopyClip(nbt):
    if input('COPY TEXT TO CLIPBOARD? (Y\\N) >').lower() != 'n':
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(nbt)
        r.update()
        r.destroy()

#Offers:{Recipes:[{buyA:{Count:1b,Damage:0s,Name:"minecraft:dirt"},buyCountA:0,buyCountB:0,demand:0,maxUses:999999,priceMultiplierA:0.05f,priceMultiplierB:0f,rewardExp:1b,sell:{Count:1b,Damage:0s,Name:"minecraft:arrow"},tier:0,traderExp:1,uses:0},{buyA:{Count:1b,Damage:0s,Name:"minecraft:dirt"},buyCountA:0,buyCountB:0,demand:0,maxUses:999999,priceMultiplierA:0.05f,priceMultiplierB:0f,rewardExp:1b,sell:{Count:64b,Damage:0s,Name:"minecraft:cooked_beef"},tier:0,traderExp:1,uses:0}]
def generateTrade(item1, item1Amount, sell, sellAmount):
    if not 'minecraft:' in item1:
        item1 = 'minecraft:'+item1
    if not 'minecraft:' in sell:
        sell = 'minecraft:'+sell
    trade = '{buyA:{Count:'+item1Amount+'b,Damage:0s,Name:"'+sell+'",WasPickedUp:0b},buyCountA:'+item1Amount+',buyCountB:0,demand:0,maxUses:4500,priceMultiplierA:0f,priceMultiplierB:0f,rewardExp:1b,sell:{Count:'+sellAmount+'b,Damage:0s,Name:"'+sell+'",WasPickedUp:0b},tier:0,traderExp:2,uses:0}'
    #'{buyA:{Count:6b,Damage:32767s,Name:"minecraft:leather",WasPickedUp:0b},buyCountA:6,buyCountB:0,demand:0,maxUses:16,priceMultiplierA:0.05f,priceMultiplierB:0f,rewardExp:1b,sell:{Count:1b,Damage:0s,Name:"minecraft:emerald",WasPickedUp:0b},tier:0,traderExp:2,uses:10}'
    return trade
def generateTrades(trades):
    nbt = 'Offers:{Recipes:['
    for i in trades:
        nbt = nbt + i + ','
    nbt = nbt.split(',')
    del(nbt[-1])
    nbt = ','.join(nbt)
    nbt = nbt + ']}'
    return nbt
#def generateVillager(tradeNBT):
#    nbt = 'Armor:[{Count:0b,Damage:0s,Name:"",WasPickedUp:0b},{Count:0b,Damage:0s,Name:"",WasPickedUp:0b},{Count:0b,Damage:0s,Name:"",WasPickedUp:0b},{Count:0b,Damage:0s,Name:"",WasPickedUp:0b}],AttackTime:0s,Attributes:[{Base:0f,Current:0f,Max:1024f,Name:"minecraft:luck"},{Base:20f,Current:20f,Max:20f,Name:"minecraft:health"},{Base:0f,Current:0f,Max:16f,Name:"minecraft:absorption"},{Base:0f,Current:0f,Max:1f,Name:"minecraft:knockback_resistance"},{Base:0.5f,Current:0.5f,Max:3.40282e+38f,Name:"minecraft:movement"},{Base:0.02f,Current:0.02f,Max:3.40282e+38f,Name:"minecraft:underwater_movement"},{Base:0.02f,Current:0.02f,Max:3.40282e+38f,Name:"minecraft:lava_movement"},{Base:16f,Current:16f,Max:2048f,Name:"minecraft:follow_range"}],BodyRot:71.7188f,Chested:0b,Color:0b,Color2:0b,Dead:0b,DeathTime:0s,FallDistance:1.27849f,Fire:0s,HighTierCuredDiscount:0,HurtTime:0s,Invulnerable:0b,IsAngry:0b,IsAutonomous:0b,IsBaby:0b,IsEating:0b,IsGliding:0b,IsGlobal:0b,IsIllagerCaptain:0b,IsOrphaned:0b,IsPregnant:0b,IsRoaring:0b,IsScared:0b,IsStunned:0b,IsSwimming:0b,IsTamed:0b,IsTrusting:0b,LastDimensionId:0,LeasherID:-1l,LootDropped:0b,LowTierCuredDiscount:0,Mainhand:[{Count:0b,Damage:0s,Name:"",WasPickedUp:0b}],MarkVariant:0,NaturalSpawn:0b,NearbyCuredDiscount:0,NearbyCuredDiscountTimeStamp:0,' + tradeNBT + ',TierExpRequirements:[{0:0}]},Offhand:[{Count:0b,Damage:0s,Name:"",WasPickedUp:0b}],OnGround:1b,OwnerNew:0l,Persistent:1b,PortalCooldown:0,Pos:[-10.6076f,3f,16.7f],Riches:0,Rotation:[47.8125f,-35.1563f],Saddled:0b,Sheared:0b,ShowBottom:0b,Sitting:0b,SkinID:0,Strength:0,StrengthMax:0,Surface:0b,TargetID:-1l,TradeExperience:256,TradeTier:4,UniqueID:-249108103135l,Variant:0,Willing:0b,boundX:0,boundY:0,boundZ:0,canPickupItems:1b,definitions:["+minecraft:villager_v2"],hasBoundOrigin:0b,hasSetCanPickupItems:1b,identifier:"minecraft:villager_v2",limitedLife:-1'
#    return nbt
name = input('ENTER VILLAGER NAME >')
trades = []
print ('PRESS CTRL+C ONCE YOU ARE DONE INPUTTING TRADE')
while True:
    try:
        buy = input('ENTER ITEM TO GIVE TO VILLAGER >')
        buyA = input('ENTER AMOUNT >')
        try:
            int(buyA)
        except:
            print ('INCORRECT AMOUNT. SETTING TO 1')
            buyA = '1'
        sell = input('ENTER ITEM TO RECIEVE FROM VILLAGER >')
        sellA = input('ENTER AMOUNT >')
        try:
            int(sellA)
        except:
            print ('INCORRECT AMOUNT. SETTING TO 1')
            sellA = '1'
        trades.append(generateTrade(buy, buyA, sell, sellA))
    except KeyboardInterrupt:
        break
tradeNBT = generateTrades(trades)
nbt = '{Air:300s,Armor:[{Count:0b,Damage:0s,Name:""},{Count:0b,Damage:0s,Name:""},{Count:0b,Damage:0s,Name:""},{Count:0b,Damage:0s,Name:""}],AttackTime:0s,Attributes:[{Base:20f,Current:20f,Max:20f,Name:"minecraft:health"},{Base:0f,Current:0f,Max:16f,Name:"minecraft:absorption"},{Base:0f,Current:0f,Max:1f,Name:"minecraft:knockback_resistance"},{Base:0.5f,Current:0.5f,Max:3.40282e+38f,Name:"minecraft:movement"},{Base:0.02f,Current:0.02f,Max:3.40282e+38f,Name:"minecraft:underwater_movement"},{Base:0f,Current:0f,Max:1024f,Name:"minecraft:luck"},{Base:16f,Current:16f,Max:2048f,Name:"minecraft:follow_range"}],BodyRot:74.6875f,Chested:0b,Color:0b,Color2:0b,CustomName:"'+name+'",CustomNameVisible:1b,Dead:0b,DeathTime:0s,EntityType:115,FallDistance:1.04735f,Fire:0s,HurtTime:0s,Invulnerable:0b,IsAngry:0b,IsAu0tonomous:0b,IsBaby:0b,IsEating:0b,IsGliding:0b,IsGlobal:0b,IsIllagerCaptain:0b,IsOrphaned:0b,IsPregnant:0b,IsRoaring:0b,IsScared:0b,IsStunned:0b,IsSwimming:0b,IsTamed:0b,IsTrusting:0b,LastDimensionId:0,LeasherID:-1l,LootDropped:0b,Mainhand:[{Count:0b,Damage:0s,Name:""}],MarkVariant:0,NaturalSpawn:0b,'+tradeNBT+',TierExpRequirements:[{0:0}]},Offhand:[{Count:1b,Damage:0s,Name:""}],OnGround:1b,OwnerNew:-1l,Persistent:1b,PortalCooldown:0,Pos:[13.2312f,4.5625f,-11.7f],Riches:0,Rotation:[60.4688f,-42.3438f],Saddled:0b,Sheared:0b,ShowBottom:0b,Sitting:0b,SkinID:2,Strength:0,StrengthMax:0,Surface:0b,TargetID:-1l,TradeExperience:310,TradeTier:4,UniqueID:-30064771065l,Variant:8,Willing:0b,boundX:0,boundY:0,boundZ:0,definitions:0,hasBoundOrigin:0b,identifier:"minecraft:villager_v2",limitedLife:-1}'
print ('TO GET COMMAND, USE [.nbt write] WHILE HOLDING ANY FISH IN A BUCKET AND PLACE IT DOWN TO SUMMON THE VILLAGER.')
print (nbt)
askCopyClip(nbt)
