## GW2TeamGenerator
 Creates sPvP teams of any size, given a template, their ranked ratings and the roles they play. The main purpose of GW2TG is helping sPvP guilds create events (like in-houses and tournaments) easily while being fair to all players. GW2TG **doesn't** take build strength into consideration as that would be impossible.

v2.1

![GW2TG GUI](https://i.imgur.com/oO9dG25.png)

## How to use
### Installing:
1. Download the lastest release.
2. Extract the .rar file to somewhere you can reach easily.

### Preparation:
1. Use a form with exactly the same layout as [Sample form style](https://docs.google.com/forms/d/e/1FAIpQLScUDl_ECvYax1dhXi13cHridjF3wl4U2-fbC9Iq4fAWXI0wUw/viewform).
2. You can customize roles, but you will need to customize style text files (you probably want to do that anyway).
3. After players are done filling the form, send it to Google Sheets.
4. Export the answers sheet as a *tab-seperated values file (.tsv)*. 
5. Optional: Change its name to *players.tsv* and put it next to the executable.

### Usage:
1. **Input file**: Browse and choose a .tsv file
2. **Output folder**: Browse and choose a folder to save the output
3. **Style**: In the folder you extracted the .rar file, there is a Styles file. 
4. Create a new .txt file with a name you can understand later.
5. Create a custom team composition, one role for each line. For example, you can add "support, support, support" if you want teams consising of 3 supports.
6. You can also use the *Default values*.
7. **Reroll count**: Enter a positive number. I wouldn't go over 5000 for less than 20 players. If you go too high, the program will stop working.

### Default values
1. **Input file**: Defaults to *players.tsv* next to the executable.
2. **Output file**: Defaults to *output.txt* next to the executable.
3. **Style**: There are three default team compositions. See *Usage*.
4. **Reroll count**: Defaults to 2000 rerolls.

## Additional
 Guild Wars 2 is a property of ArenaNet. I am not affiliated with ArenaNet.
