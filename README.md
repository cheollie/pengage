# pengage
Waddle you do to boost your school spirit?  Look no further than Pengage, the quintessential tool for student involvement! With intuitive event promotion tools and a seamless attendance system, organizing and participating in school events has never been easier - and more fun!
Pengage also features a point-scoring system with a leaderboard, where you can earn amazing prizes, challenges, and badges. By competing with your fellow penguins, you'll be motivated to get involved and showcase your school pride.
So dive right in. Join the flock and become a school spirit sensation with Pengage! You'll be a "beak"-on of leadership and inspiration to all your peers.

## about
Pengage was made using Django with SQLite for a database. 

## links
[pitch](https://docs.google.com/presentation/d/1Nc6a9CO1Aj1EU6Mz8Gz6ZClQFrDZ2XJ5YG4dfSwtZNE/edit?usp=sharing)
[documentation](https://docs.google.com/document/d/1JW6pNKZsZqvjWx-2vuyOSG4unTPhoZtNSQzdP2LoL5g/edit?usp=sharing)

## features

**main features:**
- easy to keep track of and know what are the upcoming events
- points/leaderboard system
- cool attendance system for our events
- incentivized with prizes and rewards
- cool side quests/challenges/badges
+ and a cool dashboard having all of the above visible at a glance

**minor features:**
- events catered to you! - you are able to set interested tags, so events with the tags you added will be recommended to you on your dashboard
- seamless attendance system - uses qr codes to easily scan attendees into events with just a staff member...
- interest/rsvp system
- private accounts
- is a progressive web app - can work just like an app
- event approval (coming soon)
- proximity attendance system (coming soon)
- filter, sort, search for events (coming soon)
- notifs (coming soon)
- referral (coming soon)
- markdown support (coming soon)
- themes (coming soon)
- private leaderboard (coming soon)
- partnership with local business for prizes (especially food - coming soon)

## installation
Firstly, have python installed, make sure to install the requirements, prepare the database, and lastly, run the server.
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
