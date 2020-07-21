from tkinter import Tk
def getMob(entId):
    entId = str(entId)
    mobs = '''64	40	item	Dropped item\n69	45	xp_orb	Experience Orb\n65	41	tnt	Primed TNT\n66	42	falling_block	Falling block\n67	43	moving_block	Moving Block\n61	3D	armor_stand	Armor stand\n68	44	xp_bottle	Thrown Bottle o' Enchanting\n70	46	eye_of_ender_signal	Eye of Ender\n71	47	ender_crystal	Ender Crystal\n72	48	fireworks_rocket	Firework rocket\n73	49	thrown_trident	Trident\n76	4C	shulker_bullet	Shulker bullet\n77	4D	fishing_hook	Fishing Rod hook\n79	4F	dragon_fireball	Dragon fireball\n80	50	arrow	Shot arrow\n81	51	snowball	Thrown snowball\n82	52	egg	Thrown egg\n83	53	painting	Painting\n84	54	minecart	Minecart\n85	55	fireball	Ghast fireball\n86	56	splash_potion	Thrown splash potion\n87	57	ender_pearl	Thrown Ender Pearl\n88	58	leash_knot	Leash knot\n89	59	wither_skull	Wither skull\n90	5A	boat	Boat\n91	5B	wither_skull_dangerous	Blue wither skull\n93	5D	lightning_bolt	Lightning Bolt\n94	5E	small_fireball	Blaze fireball\n95	5F	area_effect_cloud	Area Effect Cloud\n96	60	hopper_minecart	Minecart with Hopper\n97	61	tnt_minecart	Minecart with TNT\n98	62	chest_minecart	Minecart with Chest\n100	64	command_block_minecart	Minecart with Command Block\n101	65	lingering_potion	Thrown lingering potion\n102	66	llama_spit	Llama spit\n103	67	evocation_fang	Evocation fangs\n106	6A	ice_bomb	Ice Bomb\n107	6B	balloon	Balloon\n32	20	zombie	Zombie\n33	21	creeper	Creeper\n34	22	skeleton	Skeleton\n35	23	spider	Spider\n36	24	zombified_piglin	Zombified Piglin\n37	25	slime	Slime\n38	26	enderman	Enderman\n39	27	silverfish	Silverfish\n40	28	cave_spider	Cave Spider\n41	29	ghast	Ghast\n42	2A	magma_cube	Magma Cube\n43	2B	blaze	Blaze\n44	2C	zombie_villager	Zombie Villager\n45	2D	witch	Witch\n46	2E	stray	Stray\n47	2F	husk	Husk\n48	30	wither_skeleton	Wither Skeleton\n49	31	guardian	Guardian\n50	32	elder_guardian	Elder Guardian\n52	34	wither	Wither\n53	35	ender_dragon	Ender Dragon\n54	36	shulker	Shulker\n55	37	endermite	Endermite\n57	39	vindicator	Vindicator\n58	3A	phantom	Phantom\n59	3B	ravager	Ravager\n104	68	evocation_illager	Evoker\n105	69	vex	Vex\n110	6E	drowned	Drowned\n114	72	pillager	Pillager\n116	74	zombie_villager_v2	Zombie Villager\n123	7B	piglin	Piglin\n124	7C	hoglin	Hoglin\n126	7E	zoglin	Zoglin\n10	A	chicken	Chicken\n11	B	cow	Cow\n12	C	pig	Pig\n13	D	sheep	Sheep\n14	E	wolf	Wolf\n15	F	villager	Villager\n16	10	mooshroom	Mooshroom\n17	11	squid	Squid\n18	12	rabbit	Rabbit\n19	13	bat	Bat\n20	14	iron_golem	Iron Golem\n21	15	snow_golem	Snow Golem\n22	16	ocelot	Ocelot\n23	17	horse	Horse\n24	18	donkey	Donkey\n25	19	mule	Mule\n26	1A	skeleton_horse	Skeleton Horse\n27	1B	zombie_horse	Zombie Horse\n28	1C	polar_bear	Polar Bear\n29	1D	llama	Llama\n30	1E	parrot	Parrot\n31	1F	dolphin	Dolphin\n74	4A	turtle	Turtle\n75	4B	cat	Cat\n108	6C	pufferfish	Pufferfish\n109	6D	salmon	Salmon\n111	6F	tropicalfish	Tropical Fish\n112	70	cod	Cod\n113	71	panda	Panda\n115	73	villager_v2	Villager\n118	76	wandering_trader	Wandering Trader\n121	79	fox	Fox\n122	7A	bee	Bee\n125	7D	strider	Strider\n63	3F	player	Player\n117	75	shield	Shield\n120	78	elder_guardian_ghost	Elder Guardian Ghost\n51	33	npc	NPC\n56	38	agent	Agent\n62	3E	tripod_camera	Camera\n78	4E	chalkboard	Chalkboard'''
    decs = []
    hexs = []
    ids = []
    nams = []
    for i in mobs.split('\n'):
        mbs = i.split('\t')
        decs.append(mbs[0])
        hexs.append(mbs[1])
        ids.append(mbs[2])
        nams.append(mbs[3])
    pairHexs = dict()
    num = 0
    while num < len(decs):
        pairHexs[decs[num]] = hexs[num]
        num = num + 1
    pairIds = dict()
    num = 0
    while num < len(decs):
        pairIds[decs[num]] = ids[num]
        num = num + 1
    pairNams = dict()
    num = 0
    while num < len(decs):
        pairNams[decs[num]] = nams[num]
        num = num + 1
    return [entId, pairHexs[entId], pairIds[entId], pairNams[entId]]
def askCopyClip(nbt):
    if input('COPY TEXT TO CLIPBOARD? (Y\\N) >').lower() != 'n':
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(nbt)
        r.update()
        r.destroy()

entID = input('ENTER ENTITY ID (CAN BE FOUND AT [minecraft.gamepedia.com/Bedrock_Edition_data_value#Entity_IDs]) >')
mob = getMob(entID)
dec = mob[0]
hex_ = mob[1]
id_ = mob[2]
name = mob[3]
nbt = '{Items:[{Block:{name:"minecraft:lever",states:{lever_direction:"down_east_west",open_bit:0b},version:17760256},Count:64b,Damage:0s,Name:"minecraft:lever",Slot:1b},{Count:1b,Damage:5s,Name:"minecraft:bucket",Slot:2b,tag:{EntityType:'+entID+',display:{Lore:["ID_DEC:'+dec+'", "ID_HEX:'+hex_+'", "ID_STRING:'+id_+'"],Name:"Bucket Of '+name+'"}}}]}'
print ('TO GET COMMAND, USE [.nbt write] WHILE HOLDING A STORAGE ITEM (CHEST, FURNACE, DISPENSER\\DROPPER, ETC. THEN TAKE OUT THE PUFFERFISH FROM THE BLOCK AND PLACE IT DOWN TO SPAWN THE MOB\\ENTITY.')
print (nbt)
askCopyClip(nbt)
