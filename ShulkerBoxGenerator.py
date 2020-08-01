import tkinter
import json
class Shulker():
    def __init__(self, color=None, name='', lore=[]):
        self.color = color
        self.name = name
        self.lore = lore
        self.inventory = []
        self.emptyAllSlots()
    def emptyAllSlots(self, num=27):
        i = 0
        while i < num:
            try:
                self.inventory[i] = []
            except:
                self.inventory.append([])
            i = i + 1
    def findFirstEmptySlot(self):
        slotNum = -1
        i = 0
        while i < len(self.inventory):
            if self.inventory[i] == []:
                slotNum = i
                break
            i = i + 1
        return slotNum
    def addItem(self, item, slot=None):
        if slot == None:
            slot = self.findFirstEmptySlot()
        if slot == -1:
            print ('SHULKER BOX IS FULL') ########### CHANGE TO TKINTER OUTPUT
            return False
        else:
            self.inventory[slot] = item
            return True


def makeItem(itemName, amount, damage, slot, custom_name, lore, enchantments, unbreakable, nbt):
    #ITEMNAME:STRING  AMOUNT:INT  SLOT:INT  CUSTOM_NAME:STRING  LORE:LIST OF STRINGS  ENCHANTMENTS:DICTIONARY  UNBREAKABLE:BOOLEAN  NBT:DICTIONARY
    item = {}
    tag = {}
    #ITEM ID
    item['Name'] = itemName
    #AMOUNT
    item['Count'] = amount
    #DAMAGE
    item['Damage'] = damage
    #NAME ; LORE
    item['Display'] = {'Name': custom_name, 'lore': lore}
    #ENCHANTMENTS
    item['ench'] = enchantments
    #UNBREAKABLE
    item['Unbreakable'] = unbreakable
    #NBT
    for i in nbt:
        item[i] = nbt[i]
    return item
