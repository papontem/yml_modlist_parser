# YAML Mod List Parse Version 0.2

my personal r2modman modlist.yml file parser

# How To Use

1. Make sure you have installed the requirements for your python library.

2. Make sure you have exported your mods.yml file from r2modman. Do this by opening the profile that has the mods you want to parse, head to settings, and select export as file. Rename the file extension to zip, extract it, and take the mods.yml file from your profile folder.

3. next head over to this projects parse_app.py file and change the path of the parser to the path of your mods.yml file.

```PY
from yml_modlist_parse import *

# Parser initializations
my_yml_parser = Yml_modlist_parser("path/to/my/file.yml") # change your file path

# my_yml_parser.print_data() # commented
```
4. Then go to the next line and uncomment the print_data() method

```PY
from yml_modlist_parse import *

# Parser initialization
my_yml_parser = Yml_modlist_parser("mods.yml") # example path if you put it in the same folder as the py file

my_yml_parser.print_data() # uncommented

```

5. Now run the parse_app.py file, the result will be printed right on the terminal with the mod author, name, and mod version in three seperate columns like so:

```
_____________________________________________________________________________________
|<------------------+----------------------------------------------------+--------->|
|        Mod        |                        Mod                         |   Mod    |
|       Author      |                        Name                        | Version  |
|<----------------->+<---------------------------------------------------+--------->|
|.. mods ... mods ... mods ... mods ... mods ... mods ... mods ... mods ... mods ...|
|+------------------V----------------------------------------------------V---------+|
[___________________________________________________________________________________]
```
---
# Tips
- you can change the width of each column by editing the print_data method over in the yml_modlist_parse.py file
```py
# dynamically editable column widths
author_c_w = 17
modname_c_w = 50
version_c_w = 8
```
---

# TODO 

some things id like to work on going foward.

- allowing for word wrap on the mod text that can get really long.
- allowing the table to change size dynamicly without user input if a mod name, author name or version number exceeds the pre-set editable dynamic values.
- create an actual application with interface that can have the user select their r2modman profile from the r2modman files, extract the mods.yml file from the profile and then have a button available to parse and present the text to the user.