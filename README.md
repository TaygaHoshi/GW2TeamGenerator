## GW2TeamGenerator
 Creates sPvP teams of any size, given a template, their ranked ratings and the roles they play. The main purpose of GW2TG is helping sPvP guilds create events (like in-houses and tournaments) easily while being fair to all players. GW2TG **doesn't** take build strength into consideration as that would be impossible.

Version 2.0
![GW2TG GUI](https://i.imgur.com/KHEwN1H.png)

## How to use
### Preparation:
* Use a form with exactly the same layout as [Sample form style](https://docs.google.com/forms/d/e/1FAIpQLScUDl_ECvYax1dhXi13cHridjF3wl4U2-fbC9Iq4fAWXI0wUw/viewform).
* After players fill it, send it to Google Sheets.
* Export the answers sheet as a *tab-seperated values file (.tsv)*. Optional: Change its name to *players.tsv* and put it next to the executable.

### Usage:
* Input file: Browse and choose a .tsv file
* Output folder: Browse and choose a folder to save the output
* Style: Enter roles a team can have, seperated by a comma (,) and without any spaces. See the default value for an example.
* Reroll count: Enter a positive number. I wouldn't go over 5000 for less than 20 players. If you go too high, the program will stop working.

### Default values
* Input file: Defaults to *players.tsv* next to the executable.
* Output file: Defaults to *output.txt* next to the executable.
* Style: Defaults to "support,damage,random".
* Reroll count: Defaults to 2000 rerolls.

## Additional
 Guild Wars 2 is a property of ArenaNet. I am not affiliated with ArenaNet.
