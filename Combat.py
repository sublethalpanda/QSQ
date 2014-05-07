import Globals

def combat(entities):
    sEntities = sortEntities(entities)
    combat = True
    while combat:
        for i in range(0, len(sEntities)):
            combat = sEntities[i].hitSomething(sEntities[:])
        for en in sEntities:
            if en.dead():
                sEntities.remove(en)
        if Globals.player not in sEntities or len(sEntities) <= 1:
            combat = False
        Globals.player.printCombat()
    if Globals.player.dead():
        print("You have been slain!")
        Globals.quitGame = True

def sortEntities(entities):
    orderedEntities = []
    orderedInitiative = []
    initiative = []
    neg = 0
    for i in range(0, len(entities)):
        initiative.append(entities[i].initiative())
        try:
            if int(initiative[i]) < neg:
                neg = initiative[i]
        except:
            pass
    for i in range(0, len(initiative)):
        initiative[i] = int(initiative[i]) + neg
    orderedInitiative = sorted(initiative)
    for i in range(len(orderedInitiative)-1, -1, -1):
        for j in range(len(initiative)-1, -1, -1):
            if orderedInitiative[i] == initiative[j]:
                orderedEntities.append(entities[j])
                break
    return orderedEntities