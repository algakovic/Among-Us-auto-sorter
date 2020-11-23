# tournament-simulations
This notebook and script is designed to simulate various tournaments points systems, participant teams etc.

### Version 0.1
Changelog -   
Auto-sorter now automatically reads the length of the participants txt file to calibrate itself.


## Among Us tournaments
Among us tournament currently hold lobbies of 10 people and points are awarded as participants win lose gain kills or vote correctly/ incorrectly. The code in this notebook and script file is designed to randomly auto-sort a large number of participants e.g. 20, 30 or 40 into groups of 10 for fair tournament level games. The output will produce txt files with designated assortments of players called lobbies.

### Usage:

Simply have the script read called autosorter imported into a notebook and read 3 txt files 
file 1: participants.txt (should have a number of participants divisble by 10)
file 2: admins.txt (should contain admins or moderators who are also in participants.txt - Not necessary)
file 3: standby.txt (contains names of players who are standing by for participation)

run the code in the notebook and use results or saved outputs as you like. 

