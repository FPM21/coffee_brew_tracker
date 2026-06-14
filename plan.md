# coffee_brew_tracker project

## Goals:
Have an app that can store data about my brews

Can log data from phone

Running on my local PI - can be accessed via Tailscale

Some kind of automation? - NFC pads?

## Stack:
Pyhton

SQLLite3

Telegram_bot ??

## Database Scheme
Brews:

time, coffee (FK), doze, time_of_brewing, grinder_settings, ID (PK), water_volume, method

Grades:

brew_id (FK), taste, sweet, acid, bitter - all scaled 1-10

Coffees:

ID (PK), brand, name, description, comment, AI comment, roast level, origin