# pengage
Waddle you do to boost your school spirit?  Look no further than Pengage, the quintessential tool for student involvement! With intuitive event promotion tools and a seamless attendance system, organizing and participating in school events has never been easier - and more fun!
Pengage also features a point-scoring system with a leaderboard, where you can earn amazing prizes, challenges, and badges. By competing with your fellow penguins, you'll be motivated to get involved and showcase your school pride.
So dive right in. Join the flock and become a school spirit sensation with Pengage! You'll be a "beak"-on of leadership and inspiration to all your peers.

## about
Pengage was made using Django with SQLite for a database. 

## features

**main features:**
- easy keeep track and know what is upcoming events (ill try to make it filterable with tags, but tags is a selling point because ani doesnt have that) 
- points/leaderboard system
- cool attendance system for our events
- inceentivized with prizes and rewards
- cool side quests/challenges/badges (kinda scuffed rn hopefully i fix in time LMAO)
+ and a cool dashboard having all of the above visible at a glance

**minor features:**
- events catered to you! - you are able to set interested tags, so events with the tags you added will be recommended to you on your dashboard
- seamless attendance system - uses qr codes to easily scan attendees into events with just a staff member...
- interest/rsvp system
- 

## installation
Firstly, have python installed, make sure to install the requirements, prepare the database, and lastly, run the server.
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
