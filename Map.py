pos = [2,1]

#Test Input

def main():
    global flag
    userIn = input("\n>").lower()
    if userIn == "exit":
        print("closing...")
        flag = True
    userIn = userIn[0:1]
    checkDirect(userIn)
    roomDesc(pos[0],pos[1])
    print(pos)

def room(x,y,dir):
    global flag
    pos = [x,y]
    if pos == [2,0]:
        #Exit
        print("You exit the cave")
        flag = True
        return True
    elif pos == [2,1]:
        #Entrance room, N E W, S exits.
        return True
    elif pos == [3,0]:
        #Offshoot
        return True
    elif pos == [0,1]:
        #Offshoot
        return True
    elif pos == [1,1]:
        #NEW Junction
        return True
    elif pos == [3,1]:
        #SEW Junction
        return True
    elif pos == [4,1]:
        #NEW Junction
        return True
    elif pos == [5,1]:
        #Offshoot
        return True
    elif pos == [1,2]:
        #NSE Junction
        return True
    elif pos == [2,2]:
        #NSW Junction
        return True
    elif pos == [4,2]:
        #NS Hall
        return True
    elif pos == [0,3]:
        #Offshoot
        if dir !="w":
            return False
        else:
            return True
    elif pos == [1,3]:
        if dir == "w":
            return False
        else:
            return True
    elif pos == [2,3]:
        if dir == "e":
            return False
        else:
            return True
    elif pos == [3,3]:
        if dir == "w":
            return False
        else:
            return True
    elif pos == [4,3]:
        if dir == "e":
            return False
        else:
            return True
    elif pos ==[0,4]:
        #Key Room
        if dir == "n":
            return False
        else:
            return True
    elif pos == [1,4]:
        if dir == "w":
            return False
        else:
            return True
    elif pos == [2,4]:
        #Rest area
        if dir == "n":
            return True
        else:
            return False
    elif pos == [3,4]:
        if dir == "e" or dir == "w":
            return False
        else:
            return True
    elif pos == [4,4]:
        if dir == "e":
            return False
        else:
            return True
    elif pos == [1,5]:
        return True
    elif pos == [2,5]:
        if dir == "n":
            return False
        else:
            return True
    elif pos == [3,5]:
        if dir == "w":
            return False
    elif pos == [4,5]:
        if dir == "e":
            return False
        else:
            return True
    elif pos == [2,6]:
        return True
    elif pos == [4,6]:
        return True
    else:
        return False
    return True

def roomDesc(x,y):
    pos = [x,y]
#         if pos == [2,0]:
#         #Exit
#
#     elif pos == [2,1]:
#         #Entrance room, N E W, S exits.
#
#     elif pos == [3,0]:
#         #Offshoot
#
#     elif pos == [0,1]:
#         #Offshoot
#
#     elif pos == [1,1]:
#         #NEW Junction
#
#     elif pos == [3,1]:
#         #SEW Junction
#
#     elif pos == [4,1]:
#         #NEW Junction
#
#     elif pos == [5,1]:
#         #Offshoot
#
#     elif pos == [1,2]:
#         #NSE Junction
#
#     elif pos == [2,2]:
#         #NSW Junction
#
#     elif pos == [4,2]:
#         #NS Hall
#
#     elif pos == [0,3]:
#         #Offshoot
#
#     elif pos == [1,3]:
#
#     elif pos == [2,3]:
#
#     elif pos == [3,3]:
#
#     elif pos == [4,3]:
#
#     elif pos ==[0,4]:
#         #Key Room
#
#     elif pos == [1,4]:
#
#     elif pos == [2,4]:
#         #Rest area
#
#     elif pos == [3,4]:
#
#     elif pos == [4,4]:
#
#     elif pos == [1,5]:
#
#     elif pos == [2,5]:
#
#     elif pos == [3,5]:
#
#     elif pos == [4,5]:
#
#     elif pos == [2,6]:
#
#     elif pos == [4,6]:


def checkDirect(userIn):
    global pos
    blockFlag = False
    if userIn == "n":
        if room(pos[0],pos[1]+1,userIn):
            print("Moving north")
            pos[1] += 1
        else:
            blockFlag = True
    elif userIn =="s":
        if room(pos[0],pos[1]-1,userIn):
            print("Moving south")
            pos[1] -= 1
        else:
            blockFlag = True
    elif userIn =="e":
        if room(pos[0]+1,pos[1],userIn):
            print("Moving east")
            pos[0] += 1
        else:
            blockFlag = True
    elif userIn =="w":
        if room(pos[0]-1,pos[1],userIn):
            print("Moving west")
            pos[0] -= 1
        else:
            blockFlag = True
    else:
        print("That is not a direction!")
    if blockFlag == True:
        print("You can't go that way!")

flag = False
print("Pick a direction. type 'exit' to leave.")
while flag == False:
    main()




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
