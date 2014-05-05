pos = [1,2]

#Test Input
userIn = input("\n>").lower()
userIn = userIn[0:1]
def room(x,y):
    pos = [x,y]
    if pos == [1,2]:
        print("entrance room")
    else:
        return False
    return True
def roomDesc(x,y):
    pass


blockFlag = False
if userIn == "n":
    if room(pos[0],pos[1]+1):
        print("Moving north")
    else:
        blockFlag = True
elif userIn =="s":
    if room(pos[0],pos[1]-1):
        print("Moving south")
    else:
        blockFlag = True
elif userIn =="e":
    if room(pos[0]+1,pos[1]):
        print("Moving east")
    else:
        blockFlag = True
elif userIn =="w":
    if room(pos[0]-1,pos[1]):
        print("Moving west")
    else:
        blockFlag = True
else:
    print("That is not a direction!")
if blockFlag == True:
    print("You can't go that way!")





# import wave
#
# def room(title, descrip):
#     print("\n\n"+title+"\n\n"+descrip)
#
# currentlocation = ""
#
# def x2y1():
#     direction = ""
#     location = False
#     room("x2 y1 Cave Entrance:", "The light from outside the cave lights up this first room.")
# ##    createEnemy(player.level)
# ##    foe.summary()
# ##    combat()
#     direction = input("\n\nYou have four options. Would you like to travel West, North, East, or exit the tunnel by going South?").lower()
#     while direction != "west" and direction != "north" and direction != "east" and direction != "south":
#         print("\n\nMaybe you didn't understand your options. Let's try again.")
#         direction = input("\n\nWould you like to travel West, North, East, or South?").lower()
#     if direction == "west":
#         currentlocation = "x1y1"
#         direction = ""
#         x1y1()
#     elif direction == "north":
#         currentlocation = "x2y2"
#         direction = ""
#         x2y2()
#     elif direction == "east":
#         currentlocation = "x3y1"
#         direction = ""
#         x3y1()
#     elif direction == "south":
#         print("\n\nYou exit the cave and feel the warm glow of the sun on your face.")
#         print("\n\nWell I guess that was enough of an adventure for one day.")
#
#
# def x2y2():
#     direction = ""
#     location = False
#     room("x2 y2 Cave Entrance:", "The light from outside the cave lights up this first room.")
# ##    createEnemy(player.level)
# ##    foe.summary()
# ##    combat()
#     direction = input("\n\nYou have three options. Would you like to travel West, North, or South?").lower()
#     while direction != "west" and direction != "north" and direction != "south":
#         print("\n\nMaybe you didn't understand your options. Let's try again.")
#         direction = input("\n\nWould you like to travel West, North, or South?").lower()
#     if direction == "west":
#         currentlocation = "x1y2"
#         direction = ""
#         x1y2()
#     elif direction == "north":
#         currentlocation = "x2y3"
#         direction = ""
#         x2y3()
#     elif direction == "south":
#         currentlocation = "x2y1"
#         direction = ""
#         x2y1()
#
#
# def x1y1():
#     direction = ""
#     location = False
#     room("x1 y1 :", "Tcave lights up this first room.")
# ##    createEnemy(player.level)
# ##    foe.summary()
# ##    combat()
#     direction = input("\n\nYou have three options. Would you like to travel West, North, or East?").lower()
#     while direction != "west" and direction != "north" and direction != "east":
#         print("\n\nMaybe you didn't understand your options. Let's try again.")
#         direction = input("\n\nWould you like to travel West, North, or East?").lower()
#     if direction == "west":
#         currentlocation = "x0y1"
#         direction = ""
#         x0y1()
#     elif direction == "north":
#         currentlocation = "x1y2"
#         direction = ""
#         x1y2()
#     elif direction == "east":
#         currentlocation = "x2y1"
#         direction = ""
#         x2y1()
#
# def x0y1():
#     direction = ""
#     location = False
#     room("x0 y1 ", " room.")
# ##    createEnemy(player.level)
# ##    foe.summary()
# ##    combat()
#     direction = input("\n\nYou've reached a dead-end. You can only travel East.").lower()
#     while direction != "east":
#         direction = input("\n\nJust go East!").lower()
#     if direction == "east":
#         currentlocation = "x1y1"
#         direction = ""
#         x1y1()
#
# def x1y2():
#     direction = ""
#     location = False
#     room("x1 y2 Cave Entrance:", "The light from outside the cave lights up this first room.")
# ##    createEnemy(player.level)
# ##    foe.summary()
# ##    combat()
#     direction = input("\n\nYou have three options. Would you like to travel North, East or South?").lower()
#     while direction != "south" and direction != "north" and direction != "east":
#         print("\n\nMaybe you didn't understand your options. Let's try again.")
#         direction = input("\n\nWould you like to travel North, East or South?").lower()
#     if direction == "south":
#         currentlocation = "x1y1"
#         direction = ""
#         x1y1()
#     elif direction == "north":
#         currentlocation = "x1y3"
#         direction = ""
#         x1y3()
#     elif direction == "east":
#         currentlocation = "x2y2"
#         direction = ""
#         x2y2()
#
#
# def x1y3():
#     direction = ""
#     location = False
#     room("x1 y3 Lair of the Cave Whale:", "The air around you smells of old sushi.")
# # awesome WHALE TRAP (First Entry)
#     direction = input("\n\nYou have three options. Would you like to travel West, North, or South?").lower()
#     while direction != "west" and direction != "north" and direction != "south":
#         print("\n\nMaybe you didn't understand your options. Let's try again.")
#         direction = input("\n\nWould you like to travel West, North, or South?").lower()
#     if direction == "south":
#         currentlocation = "x1y2"
#         direction = ""
#         x1y2()
#     elif direction == "north":
#         currentlocation = "x1y4"
#         direction = ""
#         x1y4()
#     elif direction == "west":
#         currentlocation = "x0y3"
#         direction = ""
#         x0y3()
#
# def x0y3():
#     direction = ""
#     location = False
#     room("x0 y3 Cave Entrance:", "The light from outside the cave lights up this first room.")
# ##    createEnemy(player.level)
# ##    foe.summary()
# ##    combat()
#     direction = input("\n\nYou've reached a dead-end. You can only travel East.").lower()
#     while direction != "east":
#         direction = input("\n\nJust go East!").lower()
#     if direction == "east":
#         currentlocation = "x1y3"
#         direction = ""
#         x1y3()
#
#
# def x1y4():
#     direction = ""
#     location = False
#     room("x1 y4 Mini Boss:", "Generic Description.")
# # Mini Boss
#     direction = input("\n\nYou have three options. Would you like to travel West, North, or South?").lower()
#     while direction != "west" and direction != "north" and direction != "south":
#         print("\n\nMaybe you didn't understand your options. Let's try again.")
#         direction = input("\n\nWould you like to travel West, North, or South?").lower()
#     if direction == "south":
#         currentlocation = "x1y3"
#         direction = ""
#         x1y3()
#     elif direction == "north":
#         currentlocation = "x1y5"
#         direction = ""
#         x1y5()
#     elif direction == "west":
#         currentlocation = "x0y4"
#         direction = ""
#         x0y4()
#
# def x0y4():
#     direction = ""
#     location = False
#     room("x0 y4 Something", "Keys. Lots of keys...")
# # Key room
#     direction = input("\n\nYou've reached a dead-end. You can only travel East.").lower()
#     while direction != "east":
#         direction = input("\n\nJust go East!").lower()
#     if direction == "east":
#         currentlocation = "x1y4"
#         direction = ""
#         x1y4()
#
#
# def x1y5():
#     direction = ""
#     location = False
#     room("x1 y5 Blank", "Generic Description.")
# # Gnoblin
#     direction = input("\n\nYou have two options. Would you like to travel South or East?").lower()
#     while direction != "east" and direction != "south":
#         print("\n\nMaybe you didn't understand your options. Let's try again.")
#         direction = input("\n\nWould you like to travel South or East?").lower()
#     if direction == "south":
#         currentlocation = "x1y4"
#         direction = ""
#         x1y4()
#     elif direction == "east":
#         currentlocation = "x2y5"
#         direction = ""
#         x2y5()
#
# def x2y5():
#     direction = ""
#     location = False
#     room("x2 y5 Somewhere else:", "The light from outside the cave lights up this first room.")
# ##    createEnemy(player.level)
# ##    foe.summary()
# ##    combat()
#     direction = input("\n\nYou have three options. Would you like to travel West, North, or East?").lower()
#     while direction != "west" and direction != "north" and direction != "east":
#         print("\n\nMaybe you didn't understand your options. Let's try again.")
#         direction = input("\n\nWould you like to travel West, North, or East?").lower()
#     if direction == "west":
#         currentlocation = "x1y5"
#         direction = ""
#         x1y5()
#     elif direction == "north":
#         currentlocation = "x2y6"
#         direction = ""
#         x2y6()
#     elif direction == "east":
#         currentlocation = "x3y5"
#         direction = ""
#         x3y5()
#
#
# def x2y6():
#     direction = ""
#     location = False
#     room("x2 y6 Something please", "Ehh.")
# # Gnoblin
#     direction = input("\n\nYou've reached a dead-end. You can only travel South.").lower()
#     while direction != "south":
#         direction = input("\n\nJust go South!").lower()
#     if direction == "south":
#         currentlocation = "x2y5"
#         direction = ""
#         x2y5()
#
#
# def x3y5():
#     direction = ""
#     location = False
#     room("x3 y5 Lair:", "The air around you smells of something or other.")
# # Gnoblin
#     direction = input("\n\nYou have two options. Would you like to travel West or South?").lower()
#     while direction != "west" and direction != "south":
#         print("\n\nMaybe you didn't understand your options. Let's try again.")
#         direction = input("\n\nWould you like to travel West or South?").lower()
#     if direction == "south":
#         currentlocation = "x3y4"
#         direction = ""
#         x3y4()
#     elif direction == "west":
#         currentlocation = "x2y5"
#         direction = ""
#         x2y5()
#
#
# def x3y4():
#     direction = ""
#     location = False
#     room("x3 y4 Lair # 2:", "The air around you smells of something else.")
# # Gnoblin
#     direction = input("\n\nYou have two options. Would you like to travel North or South?").lower()
#     while direction != "north" and direction != "south":
#         print("\n\nMaybe you didn't understand your options. Let's try again.")
#         direction = input("\n\nWould you like to travel North or South?").lower()
#     if direction == "south":
#         currentlocation = "x3y3"
#         direction = ""
#         x3y3()
#     elif direction == "north":
#         currentlocation = "x3y5"
#         direction = ""
#         x3y5()
#
# def x3y3():
#     direction = ""
#     location = False
#     room("x3 y3 Lair # 3:", "The air around you smells of something else.. again.")
# # Gnoblin
#     direction = input("\n\nYou have two options. Would you like to travel West or North?").lower()
#     while direction != "north" and direction != "west":
#         print("\n\nMaybe you didn't understand your options. Let's try again.")
#         direction = input("\n\nWould you like to travel West or North?").lower()
#     if direction == "west":
#         currentlocation = "x2y3"
#         direction = ""
#         x2y3()
#     elif direction == "north":
#         currentlocation = "x3y4"
#         direction = ""
#         x3y4()
#
#
# def x2y3():
#     direction = ""
#     location = False
#     room("x2 y3 Somewhere else again:", "Some description")
# ##    createEnemy(player.level)
# ##    foe.summary()
# ##    combat()
#     direction = input("\n\nYou have three options. Would you like to travel North, East, or South?").lower()
#     while direction != "south" and direction != "north" and direction != "east":
#         print("\n\nMaybe you didn't understand your options. Let's try again.")
#         direction = input("\n\nWould you like to travel North, East, or South?").lower()
#     if direction == "south":
#         currentlocation = "x2y2"
#         direction = ""
#         x2y2()
#     elif direction == "north":
#         currentlocation = "x2y4"
#         direction = ""
#         x2y4()
#     elif direction == "east":
#         currentlocation = "x3y3"
#         direction = ""
#         x3y3()
#
#
# def x2y4():
#     direction = ""
#     location = False
#     room("x2 y4 The Rest Room", "You dont want to know..")
# # Rest Room
#     direction = input("\n\nYou've reached a dead-end. You can only travel South.").lower()
#     while direction != "south":
#         direction = input("\n\nJust go South!").lower()
#     if direction == "south":
#         currentlocation = "x2y3"
#         direction = ""
#         x2y3()
#
#
# def x3y1():
#     direction = ""
#     location = False
#     room("x3 y1 Somewhere else again:", "Some description")
# ##    createEnemy(player.level)
# ##    foe.summary()
# ##    combat()
#     direction = input("\n\nYou have three options. Would you like to travel West, East, or South?").lower()
#     while direction != "south" and direction != "west" and direction != "east":
#         print("\n\nMaybe you didn't understand your options. Let's try again.")
#         direction = input("\n\nWould you like to travel West, East, or South?").lower()
#     if direction == "south":
#         currentlocation = "x3y0"
#         direction = ""
#         x3y0()
#     elif direction == "west":
#         currentlocation = "x2y1"
#         direction = ""
#         x2y1()
#     elif direction == "east":
#         currentlocation = "x4y1"
#         direction = ""
#         x4y1()
#
#
# def x3y0():
#     direction = ""
#     location = False
#     room("x3 y0", "You dont want to know..")
# # Gnoblin
#     direction = input("\n\nYou've reached a dead-end. You can only travel North.").lower()
#     while direction != "north":
#         direction = input("\n\nJust go North!").lower()
#     if direction == "north":
#         currentlocation = "x3y1"
#         direction = ""
#         x3y1()
#
#
# def x4y1():
#     direction = ""
#     location = False
#     room("x4 y1 Somewhere else again:", "Some description")
# ##    createEnemy(player.level)
# ##    foe.summary()
# ##    combat()
#     direction = input("\n\nYou have three options. Would you like to travel West, North, or East?").lower()
#     while direction != "north" and direction != "west" and direction != "east":
#         print("\n\nMaybe you didn't understand your options. Let's try again.")
#         direction = input("\n\nWould you like to travel West, North, or East?").lower()
#     if direction == "north":
#         currentlocation = "x4y2"
#         direction = ""
#         x4y2()
#     elif direction == "west":
#         currentlocation = "x3y1"
#         direction = ""
#         x3y1()
#     elif direction == "east":
#         currentlocation = "x5y1"
#         direction = ""
#         x5y1()
#
#
# def x4y2():
#     direction = ""
#     location = False
#     room("x4 y2 Somewhere else again:", "Some description")
# ##    createEnemy(player.level)
# ##    foe.summary()
# ##    combat()
#     direction = input("\n\nYou have two options. Would you like to travel North, or South?").lower()
#     while direction != "north" and direction != "south":
#         print("\n\nMaybe you didn't understand your options. Let's try again.")
#         direction = input("\n\nWould you like to travel North or South?").lower()
#     if direction == "north":
#         currentlocation = "x4y3"
#         direction = ""
#         x4y3()
#     elif direction == "south":
#         currentlocation = "x4y1"
#         direction = ""
#         x4y1()
#
# def x5y1():
#     direction = ""
#     location = False
#     room("x5 y1", "You dont want to know..")
# # gnoblin
#     direction = input("\n\nYou've reached a dead-end. You can only travel West.").lower()
#     while direction != "west":
#         direction = input("\n\nJust go West!").lower()
#     if direction == "west":
#         currentlocation = "x4y1"
#         direction = ""
#         x4y1()
#
# def x4y3():
#     direction = ""
#     location = False
#     room("x4 y3 Somewhere else again:", "Some description")
# ##    createEnemy(player.level)
# ##    foe.summary()
# ##    combat()
#     direction = input("\n\nYou have two options. Would you like to travel North, or South?").lower()
#     while direction != "north" and direction != "south":
#         print("\n\nMaybe you didn't understand your options. Let's try again.")
#         direction = input("\n\nWould you like to travel North or South?").lower()
#     if direction == "north":
#         currentlocation = "x4y4"
#         direction = ""
#         x4y4()
#     elif direction == "south":
#         currentlocation = "x4y2"
#         direction = ""
#         x4y2()
#
# def x4y4():
#     direction = ""
#     location = False
#     room("x4 y4 Somewhere else again:", "Some description")
# ##    createEnemy(player.level)
# ##    foe.summary()
# ##    combat()
#     direction = input("\n\nYou have two options. Would you like to travel North, or South?").lower()
#     while direction != "north" and direction != "south":
#         print("\n\nMaybe you didn't understand your options. Let's try again.")
#         direction = input("\n\nWould you like to travel North or South?").lower()
#     if direction == "north":
#         currentlocation = "x4y5"
#         direction = ""
#         x4y5()
#     elif direction == "south":
#         currentlocation = "x4y3"
#         direction = ""
#         x4y3()
#
#
# def x4y5():
#     direction = ""
#     location = False
#     room("x4 y5 Boss Door:", "Need a key")
# ##    Boss Door. Need a key
#     # this code will have to be altered to check whether the hero has a key or not. Maybe dictionary check for term "key"?
#     direction = input("\n\nYou have two options. Would you like to travel North, or South?").lower()
#     while direction != "north" and direction != "south":
#         print("\n\nMaybe you didn't understand your options. Let's try again.")
#         direction = input("\n\nWould you like to travel North or South?").lower()
#     if direction == "north": #again, would need key
#         currentlocation = "x4y6"
#         direction = ""
#         x4y6()
#     elif direction == "south":
#         currentlocation = "x4y4"
#         direction = ""
#         x4y4()
#
#
# def x4y6():
#     direction = ""
#     location = False
#     room("x4 y6.. This is the boss", "You probably won't it through this room alive...")
# # Boss Room
# ##    direction = input("\n\nYou've reached a dead-end. You can only travel West.").lower()
# ##    while direction != "west":
# ##        direction = input("\n\nJust go West!").lower()                        I DONT THINK DIRECTION MATTERS AT THIS POINT, unless you want to give the player the option to flee
# ##    if direction == "south":
# ##        currentlocation = "x4y5"
# ##        direction = ""
# ##        x4y5()
#
# endcave = False
# while endcave == False:
#     x2y1()
#     endcave = True
#
#
# print("\n\nYou have either beaten the boss by this point, or died embarrassingly. Or maybe you just ran away like a coward.")
# input("\n\nPress Enter to exit")
#
#
# ##
# ##Table I
# ##Dice: Result
# ##01-06 Accursed
# ##07-12 Ancient
# ##13-14 Baneful
# ##15-18 Batrachian
# ##19-25 Black
# ##26-28 Bloodstained
# ##29-30 Cold
# ##31-38 Dark
# ##39-40 Devouring
# ##41-42 Diabolical
# ##43-44 Ebon
# ##45-47 Eldritch
# ##48-51 Forbidden
# ##52-55 Forgotten
# ##56-57 Haunted
# ##58-61 Hidden
# ##62-63 Lonely
# ##64-67 Lost
# ##68-69 Malevolent
# ##70-71 Misplaced
# ##72-73 Nameless
# ##74-75 Ophidian
# ##76-77 Scarlet
# ##78-80 Secret
# ##81-82 Shrouded
# ##83-84 Squamous
# ##85-86 Strange
# ##87-88 Tenebrous
# ##89-90 Uncanny
# ##91-92 Unspeakable
# ##93-94 Unvanquishable
# ##95-96 Unwholesome
# ##97-98 Vanishing
# ##99-00 Weird
# ##
# ##
# ##Table II
# ##Dice: Result
# ##01-02 Abyss
# ##03-05 Catacombs
# ##06-10 Caverns
# ##11-13 Citadel
# ##14-15 City
# ##16-17 Cyst
# ##18-21 Depths
# ##22-26 Dungeons
# ##27-30 Fane
##31-33 Fortress
##34-36 Halls
##37-38 Haunts
##39-40 Isle
##41-43 Keep
##44-49 Labyrinth
##50-53 Manse
##54-60 Maze
##61-62 Milieu
##63-67 Mines
##68-71 Mountain
##72-74 Oubliette
##75-77 Panopticon
##78-81 Pits
##82-84 Ruins
##85-87 Sanctum
##88-89 Shambles
##90-93 Temple
##94-95 Tower
##96-00 Vault
##
##Table III
##Dice: Result
##01-00 of
##
##Table IV
##Dice: Result
##01-02 the Axolotl
##03-04 Blood
##05-06 Bones
##07-08 Chaos
##09-11 the (Table I) Cult
##12-13 Curses
##14-15 the Dead
##16-17 Death
##18-19 Demons
##20-21 Despair
##22-23 Deviltry
##24-25 Doom
##26-27 the Dweller(s) in [01-50] the (Table II) [51-00] (Table IV)
##28-29 (Table I) Dweomercraeft
##30-31 Evil
##32-33 Fire
##34-35 Frost
##36-37 the (3-13) Geases
##38-39 Gloom
##40-41 Hells
##42-43 Horrors
##44-45 Ichor
##46-47 Id Insinuation
##48-49 the (Table I) Idol
##50-51 Iron
##52-53 Madness
##54-55 Mirrors
##56-57 Mists
##58-59 Monsters
##60-61 Mystery
##62-63 Necromancy
##64-65 Oblivion
##66-68 the (Table I) One(s)
##69-70 Peril
##71-72 Phantasms
##73-74 Random Harlots
##75-76 Secrets
##77-78 Shadows
##79-80 Sigils
##81-82 Skulls
##83-84 Slaughter
##85-86 Sorcery
##87-88 Syzygy
##89-90 Terror
##91-92 Torment
##93-94 Treasure
##95-96 the Undercity
##97-98 the Underworld
##99-00 the Unknown
##
##
##http://www.basicfantasy.org/dungeoneer.html
##
