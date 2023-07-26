import yaml

class Yml_modlist_parser:
    """
        This is a class which will hold instances of our parsing of yaml data from yml files.
    """
    
    # Factory/Constructor method (initialize object attributes) for our yaml parsers
    def __init__(self, filepath):
        self.file_path = filepath
        self.extracted_mods = self.get_safe_data()

    def __repr__(self) -> str:
        return f"< YAML Parser: file_path = {self.file_path} >"

    def get_safe_data(self):
        """ get data from yaml file safely making sure no one puts python commands into the yml file"""
        with open(self.file_path, "r") as file:
            mods = yaml.safe_load(file)
        return mods
    
    def print_data_items_nicely(self):
        """ prints data per key value pair onto the terminal """
        for key, value in self.extracted_mods.items():
            print(key + " : " + str(value))

    def print_data(self):
        """
            This funcion will try to print all of the mods that may be inside the extracted safe data in a tabular format
            LIKE SO: 
            currently VV
            __________________________________________________________________________
            |<----------------+------------------------------------------+-----------+
            |       Mod       |                   Mod                    |    Mod    |
            |      Author     V                   Name                   |  Version  |
            |<--------------->+<-----------------------------------------+-----------+
            | author name     |        display name of the mod           | v1.2.3    |
            |+----------------V------------------------------------------V-----------V
            [________________________________________________________________________]


            WIP WISH VV
            ______________________________________________________________________________________________________________
            |<----------------+------------------------------------------+-----------+---------+-------+---------------->|
            |       Mod       |                   Mod                    |    Mod    |  on - 1 |  Bug  |      Mod        |
            |      Author     V                   Name                   |  Version  | off - 0 | ?/X/! |     Source      |
            |<--------------->+<-----------------------------------------+-----------+---------+-------+---------------->|
            | author name     |        display name of the mod           | v1.2.3    |    0    |  ?    | Thunderstore    |
            |+----------------V------------------------------------------V-----------V---------V-------V----------------+|
            [____________________________________________________________________________________________________________]
        
            
        """
        # dynamically editable column widths
        author_c_w = 17
        modname_c_w = 50
        version_c_w = 8
        print("\n")
        # HEAD
        # self.print_header()
        print(f"""__{          "_"*author_c_w                 }___{           "_"*modname_c_w              }___{              "_"* version_c_w             }__""")
        print(f"""|<{          "-"*author_c_w                 }-+-{           "-"*modname_c_w              }-+-{              "-"* version_c_w             }>|""")
        print(f"""| {   self.center_justify("Mod", author_c_w)} | { self.center_justify("Mod", modname_c_w)} | {    self.center_justify("Mod", version_c_w)} |""")
        print(f"""| {self.center_justify("Author", author_c_w)} | {self.center_justify("Name", modname_c_w)} | {self.center_justify("Version", version_c_w)} |""")
        print(f"""|<{          "-"*author_c_w                 }>+<{           "-"*modname_c_w              }-+-{              "-"* version_c_w             }>|""")
        
        # BODY
        for mod in self.extracted_mods:
            mod_author = mod['authorName']
            mod_name = mod['displayName']
            version = f"{mod['versionNumber']['major']}.{mod['versionNumber']['minor']}.{mod['versionNumber']['patch']}"
            print(f"| { self.center_justify(mod_author, author_c_w)} | {self.center_justify(mod_name, modname_c_w)} | {self.center_justify(version, version_c_w)} |")
        
        # FOOTER
        # self.print_footer()
        # dynamicly editable
        print(f"""|+{          "-"*author_c_w                 }-V-{           "-"*modname_c_w              }-V-{              "-"* version_c_w             }+|""")
        print(f"""[_{          "_"*author_c_w                 }___{           "_"*modname_c_w              }___{              "_"* version_c_w             }_]""")

    #### formating helper
    def center_justify(self, text, width):
        # padding = (width - len(text)) // 2
        return text.center(width, ' ')
    
    
    