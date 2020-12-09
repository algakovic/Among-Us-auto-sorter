from random import shuffle


# Import admin and participant data from txt file:
def among_us_lobby_sorter():
    '''
    * Admins must be included in the participants list. Their names must match like for like.
    Having even number of admins is not necessary but a pair for each lobby at least is good.

    The auto-sorter will sort participants 
    into lobbies of 10 and remaining players will go into a standby lobby
    '''
    
    with open('uploads/participants.txt', 'r') as party, open('uploads/admins.txt', 'r') as adminlist:
        participants = [s.strip() for s in party.readlines()]
        admins = [s.strip() for s in adminlist.readlines()]    
    
    standby_index = len(participants)%10
    if standby_index:
        #slice the last x participants where x is the modulo result above and place in standby list:
        standby = participants[-standby_index:]
        #remove standby from participants list:
        del participants[-standby_index:]
        print(len(standby))
    
    # Make a copy of admin and participants list and shuffle
    shuffled_participants = participants.copy()
    shuffle(shuffled_participants)
    
    shuffle(admins)
    admins_copy = admins.copy()
    
    # Create magic variable based on participant number:
    n = int(len(participants)/10)
    
    # No. of lobbies created depends on participants:
    index = list(range(n+1))    
    lobbies = [[] for i in index]
    
    # seed admins to lobbies:
    while len(admins_copy) > 0:
        for lobby in lobbies[:n]:
            lobby.append(admins_copy.pop())
            if len(admins_copy)>0:
                continue
            else:
                break
  
    for admin in admins:  
        shuffled_participants.remove(admin)

    # add remaining participants to lobbies:
    full = []
    while len(shuffled_participants) > 0:
        for lobby in lobbies[:n]:
            if lobby not in full:
                lobby.append(shuffled_participants.pop())
                if len(lobby) == 10:
                    full.append(lobby)
                else: 
                    continue

        if len(shuffled_participants) > 0:
            continue
        else:
            break
            
    if standby_index:
        # add standby participants:
        while len (standby)>0:
            lobbies[n].append(standby.pop())
            if len(standby)>0:
                continue
            else:
                break

    return lobbies
