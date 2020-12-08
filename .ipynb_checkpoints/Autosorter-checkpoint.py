from random import shuffle


# Import admin and participant data from txt file:
def among_us_lobby_sorter():
    '''
    admins must be included in the participants list
    the number of participants must be divisible by 10
    Have an even amount of admins in the list. A pair for each lobby is good.

    The auto-sorter will sort participants 
    into lobbies of 10 and standby.txt players will go 
    into a separate lobby.
    '''
    
    with open('uploads/participants.txt', 'r') as party, open('uploads/admins.txt', 'r') as adminlist,   open('uploads/standby.txt', 'r') as standby:
        participants = party.read().split('\n')
        admins = adminlist.read().split('\n')
        standby = standby.read().split('\n')
    
    # Make a copy of participant list for shuffling
    shuffled_participants = participants.copy()
    
    shuffle(admins)
    admins_copy = admins.copy()
    
    n = int(len(participants)/10)
    
    if n == 2:
        lobby1, lobby2, lobby3 = [], [], []
        lobbies = lobby1, lobby2, Standby
    elif n == 3:
        lobby1, lobby2, lobby3, lobby4 = [],[],[],[]
        lobbies = lobby1, lobby2, lobby3, Standby
    else:
        lobby1, lobby2, lobby3, lobby4, lobby5 = [],[],[],[],[]
        lobbies = lobby1, lobby2, lobby3, lobby4, Standby

        
    while len(admins_copy) > 0:
        for lobby in lobbies[:n]:
            lobby.append(admins_copy.pop())
            if len(admins_copy)>0:
                continue
            else:
                break
    
    for admin in admins:
        shuffled_participants.remove(admin)

    shuffle(shuffled_participants)
    
    while len(shuffled_participants) > 0:
        for lobby in lobbies[:n]:
            if len(lobby) <10:
                lobby.append(shuffled_participants.pop())
                if len(shuffled_participants)>0:
                    continue
                else:
                    break

    # standby participants:
    while len (standby)>0:
        lobbies[n].append(standby.pop())
        if len(standby)>0:
            continue
        else:
            break
    return lobbies
