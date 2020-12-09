# Among Us Tournament Autosorter
This Jupyter notebook, python app.py file and associated materials are designed to aid the Among Us tournament hoster in randomising teams of 10 players for matches.

### Version 0.1
Changelog - 20.11.2020
- Auto-sorter now automatically reads the length of the participants txt file to calibrate itself.
### Version 0.2
Changelog - 06.12.2020
- The Auto-sorter is now a Flask application that is hosted by Heroku at: https://among-us-tournament-randomiser.herokuapp.com/  
- The initial code has been modified to only add a participant to a lobby if the lobby is not already full.   
- The app has its own design and pages uses css styles and html to display the results of the randomiser.
### Version 0.3  
Changelog - 07.12.2020
- No. of lobbies created in Autosorter is now completely dependent on participants entering.
### Version 0.4
Changelog - 08.12.2020
- Equal lobby sorting when admins.txt contains no names, or odd number of names.
- admins.txt and standby.txt can be empty now.
### Version 0.5
Changelog - 08.12.2020
- Submit button now redirects to results.html for a better user experience.
- The reading of files is now more robust using .strip() and list comprehensions with .readlines() rather than .read().  
- Empty lines and whitepsaces will not cause issue to the auto-sorter now.
### Version 0.9
Changelog - 09.12.2020
- Uploads folder is cleared after showing results. People now no longer see other names from other uploads.
- Update Main.html instructions to explain how to select multiple files.
- Style code blocks on instructions page for .txt files
#### Version 1
Changelog - 09.12.2020
- Switch production web server to gunicorn

## Among Us tournaments
Among us tournament currently hold lobbies of 10 people and points are awarded as participants win lose gain kills or vote correctly/ incorrectly. The code in this notebook and script file is designed to randomly auto-sort a number of participants 20 - 40 into groups of 10 for tournament level games. The output will produce randomised teams of ten players labeled lobbies.

### Usage:

Visit the link: https://among-us-tournament-randomiser.herokuapp.com/ and feed the auto-sorter  
the three .txt files which should contain no whitespaces and no extra lines:
file 1: participants.txt (must have a number of participants divisible by 10)
file 2: admins.txt (should contain admins or moderators who are also in participants.txt - can be blank)
file 3: standby.txt (contains names of players who are standing by for participation - can be blank)

The code in the Jupyter notebook can be run to the same effect, if you prefer.

