# pengage
Waddle you do to boost your school spirit?  Look no further than Pengage, the quintessential tool for student involvement! With intuitive event promotion tools and a seamless attendance system, organizing and participating in school events has never been easier - and more fun!
Pengage also features a point-scoring system with a leaderboard, where you can earn amazing prizes, challenges, and badges. By competing with your fellow penguins, you'll be motivated to get involved and showcase your school pride.
So dive right in. Join the flock and become a school spirit sensation with Pengage! You'll be a "beak"-on of leadership and inspiration to all your peers.

## about
Pengage was made using Django with SQLite for a database. 

## links
[pitch](https://docs.google.com/presentation/d/1Nc6a9CO1Aj1EU6Mz8Gz6ZClQFrDZ2XJ5YG4dfSwtZNE/edit?usp=sharing), 
[documentation](https://docs.google.com/document/d/1JW6pNKZsZqvjWx-2vuyOSG4unTPhoZtNSQzdP2LoL5g/edit?usp=sharing)

## features

**main features:**
- events system to easily keep track of and be aware of upcoming events
- points/leaderboard system for the competitive spirit
- cool attendance system for our events 
- incentivized with prizes and rewards
- motivating side quests/challenges/badges
+ and a cool dashboard having all of the above visible at a glance

**minor features:**
- events catered to you! - you are able to set interested tags, so events with the tags you added will be recommended to you on your dashboard
- seamless attendance system - uses qr codes to easily scan attendees into events
- interest/rsvp system - for organizers to gauge how many people will attend (serves as a sign up as well to display the qr-code)
- private accounts - for user privacy
- is a progressive web app - can work just like an app

## installation
After cloning this repository, make sure you have Python installed. Then, install the requirements, prepare the database, and lastly, run the server.
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
