# Among Us Tournament Autosorter
This Jupyter notebook, python app.py file and associated materials are designed to aid the Among Us tournament hoster in randomising teams of 10 players for matches.

### Version 0.1
Changelog -   
- Auto-sorter now automatically reads the length of the participants txt file to calibrate itself.
### Version 0.2
Changelog - 
- The Auto-sorter is now a Flask application that is hosted by Heroku at: http://among-us-tournament-randomiser.herokuapp.com/randomise  
- The initial code has been modified to only add a participant to a lobby if the lobby is not already full.   
- The app has its own design and pages uses css styles and html to display the results of the randomiser.


## Among Us tournaments
Among us tournament currently hold lobbies of 10 people and points are awarded as participants win lose gain kills or vote correctly/ incorrectly. The code in this notebook and script file is designed to randomly auto-sort a number of participants 10 - 40 into groups of 10 for tournament level games. The output will produce randomised teams of ten players called lobbies.

### Usage:

Simply visit the link: http://among-us-tournament-randomiser.herokuapp.com/randomise  
and feed the auto-sorter the three .txt files which should contain no whitespaces and no extra lines:
file 1: participants.txt (should have a number of participants divisble by 10)
file 2: admins.txt (should contain admins or moderators who are also in participants.txt - Not necessary)
file 3: standby.txt (contains names of players who are standing by for participation - Not necessary)

The code in the Jupyter notebook can be run to the same effect, if you prefer.

