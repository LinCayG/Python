print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print('Welcome to Treasure Island! \n Your goal is to find the treasure!')
Start = input('You are at a crossroad.  Where do you want to go?  Type "left" or "right": ').lower()
if Start == "left":
    print('''

     /"""""/""""""".
    /     /         \             __
   /     /           \            ||
  /____ /             \           ||
 |     |  In Loving    |          ||
 |     |   Memory      |          ||
 |     |               |          ||
 |     |               |          ||
 |     |     * *   * * |         _||_
 |     |     *\/* *\/* |        | TT |
 |     |     *_\_  /   ...""""""| || |.""...."""""""".""
 |     |         \/.."""""..."""\ || /.""".......""""...
 |     |...."""""""........""""""^^^^"......."""""""".."
 |......"""""""""""""""........"""""....""""".."" ''')
    print('You stepped into quicksand and cannot get out.  You slowly start to sink.  It takes a while, but you eventually die.')
elif Start == "right":
    print("""
  ~         ~~          __
       _T      .,,.    ~--~ ^^
 ^^   // \                    ~
      ][O]    ^^      ,-~ ~
   /''-I_I         _II____
__/_  /   \ ______/ ''   /'\_,__
  | II--'''' \,--:--..,_/,.-{ },
; '/__\,.--';|   |[] .-.| O{ _ }
:' |  | []  -|   ''--:.;[,.'\,/
'  |[]|,.--'' '',   ''-,.    |
  ..    ..-''    ;       ''. '    """)
    print('You arrive at a town.')
    town = input('Do you want to go into the inn or continue on down the path and leave? Type "inn" or "leave": ').lower()
    if town == "inn":
        print('\n \n \n')
        print('''
      .======================================.
      | ___ ___ ___               _   _   _  |
      | \_/ \_/ \_/ C|||C|||C||| |-| |-| |-| |
      | _|_ _|_ _|_  ||| ||| ||| |_| |_| |_| |
      '===================================== ,sSSSs
                The Old Town Inn and Bar    SSSS "(
           .:.                              SSS@ =/  \~/
          C|||'                             SSSS_(_  _Y_
        ___|||______________________________SS/ _)_) /.-
       [____________________________________] \   /\//
        |   ____    ____    ____    ____   | \|==(\_/
        |  (____)  (____)  (____)  (____)  | (/   ;
        |  |    |  |    |  |    |  |    |  | |____|
        |  |    |  |    |  |    |  |    |  |  \  |\
        |  |    |  |    |  |    |  |    |  |   ) ) )
        |  |____|  |____|  |____|  |____|  |  (  |/
        |  I====I  I====I  I====I  I====I  |  /\ |
           |    |  |    |  |    |  |    |  | /.(=\
                                                ''')
        print('You talk to the waitress at the bar inside the inn and order a beer.\nWhile waiting for your beer, a fight breaks out and you get caught in the middle of it.  You get stabbed and die.')
        print('\n \n')
        print('''

     /"""""/""""""".
    /     /         \             __
   /     /           \            ||
  /____ /             \           ||
 |     |  In Loving    |          ||
 |     |   Memory      |          ||
 |     |               |          ||
 |     |               |          ||
 |     |     * *   * * |         _||_
 |     |     *\/* *\/* |        | TT |
 |     |     *_\_  /   ...""""""| || |.""...."""""""".""
 |     |         \/.."""""..."""\ || /.""".......""""...
 |     |...."""""""........""""""^^^^"......."""""""".."
 |......"""""""""""""""........"""""....""""".."" ''')
    elif town == "leave":
      print('You walk quickly out of the town, which was a good idea because as you get back on the road, \nyou hear shouting and screaming from the inn.')
      print('You continue walking for a short while and eventually get to a river with a dock.  The sign on the dock reads: "River Boat Crossing: ever hour, on the hour".')
      river = input('You wish to cross the river.  You have 30 minutes until the boat arrives at the dock.  \nDo you wait for the boat or do you swim across?  Type "wait" or "swim": ').lower()
      if river == "wait":
        print('''
                 ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----.....___
           \               ""/
      ~^~^~^~^~^`~^~^`^~^~^`^~^~^
       ~^~^~`~~^~^`~^~^~`~~^~^~
       ''')
        input('The boat arrives at the dock.  Press enter to continue.')
        print('''
            {)
           //\
   _-~~/-._|_|
  /'_,/,   //'~~~\;;,
  `~  _( _||_..\ | ';;
    /'~|/ ~' `\<\>  ;
    "  |      /  |
       "      "  "
       ''')
        input('As you begin to board, you see a man riding a horse racing towards the boat.  Press enter to continue.')
        print('The man leaps off the horse and he is covered in blood.  You hear shouting behind the man as more men on horses come up from behind. \nOne of the other men starts shooting and you are caught in the middle of a shootout.  You die.')
        print('''

     /"""""/""""""".
    /     /         \             __
   /     /           \            ||
  /____ /             \           ||
 |     |  In Loving    |          ||
 |     |   Memory      |          ||
 |     |               |          ||
 |     |               |          ||
 |     |     * *   * * |         _||_
 |     |     *\/* *\/* |        | TT |
 |     |     *_\_  /   ...""""""| || |.""...."""""""".""
 |     |         \/.."""""..."""\ || /.""".......""""...
 |     |...."""""""........""""""^^^^"......."""""""".."
 |......"""""""""""""""........"""""....""""".."" ''')

      elif river == "swim":
        print('''

                                           ^.     ^.    ^.
                                           ) '.   ) '.  ) '.   ^.
                                     ^.   / _..;--"""""---..;  ) '.
                                )\   ) ';-""                 "-""--.._
                            )\_/..'-""                                ".
                   __...---"""                                     ()   "
        ___...---""                                        .             )
 .--""""                      .     ,                       )       _..-"
(_______________________."".  "-.     _________..--".      /___r".""______
                        `,  \  .    '               L     (   '  ;
                          ,  \/   .'                 '.    '."  ,'
                          .      /                     `,      <_
                       _-'      <_                     "         '-_
                    .-'   .       '-_                   '     _.._  )
                  .'  _.-";   *-.._  )                 ' .\   \   ""
                   '-'    '  '     ""                .'  , `
                        .' .'                        ; .'   '  '.
                       '_.'                           "      '._'
       ''')
        input('You start swimming across the river.  A river monster appears.  Press enter to continue.')
        print('You start swimming faster but notice the river monster ignores you and keeps swimming along.')
        box = input('You reach the other side of the river.  You notice a road a bit of a distance away and also notice a telephone booth off to the right of the docks.  Do you go inside or continue towards the road? Type "inside" or "road": ').lower()
        if box == "inside":
            print('''
                     ___
           | |
           | |
   -------------------
   -------------------
    |  ___  |  ___  |
    | | | | | | | | |
    | |-+-| | |-+-| |
    | |_|_| | |_|_| |
    |  ___  |  ___  |
    | |   | | |   | |
    | |   | | |   | |
    | |___| | |___| |
    |  ___  |  ___  |
    | |   | | |   | |
    | |   | | |   | |
    | |___| | |___| |
    |       |       |
   ===================
   ''')
            input('You go inside the telephone booth.  It is bigger on the inside!  Press enter to continue.')
            print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
            print('You found the treasure! You win!')
        elif box == "road":
            print( '''
            Exterminate!
                   /
              ___
      D>=G==='   '.
            |======|
            |======|
        )--/]IIIIII]
           |_______|
           C O O O D
          C O  O  O D
         C  O  O  O  D
         C__O__O__O__D
        [_____________]
        ''')
            input('As you approach the road, you start hearing something yell "EXTERMINATE!".  Press enter to continue.')
            print('''

     /"""""/""""""".
    /     /         \             __
   /     /           \            ||
  /____ /             \           ||
 |     |  In Loving    |          ||
 |     |   Memory      |          ||
 |     |               |          ||
 |     |               |          ||
 |     |     * *   * * |         _||_
 |     |     *\/* *\/* |        | TT |
 |     |     *_\_  /   ...""""""| || |.""...."""""""".""
 |     |         \/.."""""..."""\ || /.""".......""""...
 |     |...."""""""........""""""^^^^"......."""""""".."
 |......"""""""""""""""........"""""....""""".."" ''')
            print('The dalek shoots you.  You die.')
        else:
          print('You choose neither direction and sit there and die.')
      else:
        print('''
                 ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----.....___
           \               ""/
      ~^~^~^~^~^`~^~^`^~^~^`^~^~^
       ~^~^~`~~^~^`~^~^~`~~^~^~
       ''')
        input('While trying to decide, 30 minutes pass and the boat arrives at the dock.  Press enter to continue.')
        print('''
            {)
           //\
   _-~~/-._|_|
  /'_,/,   //'~~~\;;,
  `~  _( _||_..\ | ';;
    /'~|/ ~' `\<\>  ;
    "  |      /  |
       "      "  "
       ''')
        input('You see a man riding a horse racing towards the boat.  Press enter to continue.')
        print('The man leaps off the horse and he is covered in blood.  You hear shouting behind the man as more men on horses come up from behind. \nOne of the other men starts shooting and you are caught in the middle of a shootout.  You die.')
        print('''

     /"""""/""""""".
    /     /         \             __
   /     /           \            ||
  /____ /             \           ||
 |     |  In Loving    |          ||
 |     |   Memory      |          ||
 |     |               |          ||
 |     |               |          ||
 |     |     * *   * * |         _||_
 |     |     *\/* *\/* |        | TT |
 |     |     *_\_  /   ...""""""| || |.""...."""""""".""
 |     |         \/.."""""..."""\ || /.""".......""""...
 |     |...."""""""........""""""^^^^"......."""""""".."
 |......"""""""""""""""........"""""....""""".."" ''')
    else:
        print('You choose neither direction and sit there and die.')
else:
   print('You choose neither direction and sit there and die.')
