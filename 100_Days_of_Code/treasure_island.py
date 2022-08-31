print('''
      . . .                                                             
,      ` ` ---. ___. .-._                                            
             `      ,   , ` -_.                                      
.   .      ,  ,    a.aaaaa.__a8                                      
, .   ,   ...--,a8P"  "Y888888a                                      
 ,   .a8a'/    `  \_       _ 8|                                     >
   .a88P    .       \ -' .a8|/                                       
.aa8P"     a         \aaP'  '\                                       
 \   \    a8   '      \.  -' /                                       
      \  / Y         ,a8   _/  _____                                 
 \__   `X   \  ___/  `Y8  a8\      ---__________                     
    \_       \        a \/  |   _________       __________           
     a  ._  _/_      a8a   /;                      _____             
  __/P8    \  "8a. ./Y"8-__a:.    |.                                 
 /a"" \.   a.    a88a'    88:     |                                  
      /8a  Y8a    8P_  _  a8.:    |                                  
--., / `878/88a._./�:\____a;; .   |                                  
   a__   \:::.::.::.::.;;'.''     |                          ____    
-_  `'\__/:.: ,:." .    .   .     |                                  
 a.   /:.:. . .                   | =>.-.                            
  \_ /::. ,                     .-|| |]- )                           
    |:.                      .-\ a8"-'.-'/___                        
.   \:  .                  .'\ '   .-'  /                            
\.   /.                    (_/\_.-'  _:'   .aaaa.                    
 \:_/.  .              ___ \ (  _..:='  .a:8888P                     
  \:.                    ---\| /:='___-.88888P'                      
   |: .                      `"'  ...:88888P'                        
   /. .       ___                 888888P' . .                       
 ----_                            `8P"'                        ___   
   _  \                                                              
  /   /                       ___                                    
     a:                                                              
    .' \_                                                            
   <     \ -.                                 ______                 
__/ Y     a`   \      ___                                            
  __/\  \/   `  `                     ,O                             
           `  `                  __- .//`-  __                       
               `           _o_      < )  .a                          
     `      `             `/   --    '  a8'                        __
                `         ' aP                                       
  `               `                                                  
      .////oO       `                          __                    
     ////'<>          `                                              
                   `    `                                            
         `  _.,             `                                        
           ()() ,        `       `                                   
  `   (_);     ;                   `                                 
     (_){        `.                    `                             
_ . '           .-              `        `                           
            , '                            `       .====_            
-  _     ` (               `         `     _`    _/      \------.    
     - .     .  `                      _--/  \__/      x         \a:f
         -. .          `          _---\                   ,          
\__    __          _.       ` ___/                 \ /               
   \__/  \    ___,/  \_______/             \J,                       
          \__/                                                       
''')                                                  	     

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
crossroads = input("Your at a crossroads and you can only go left or right, what will you chose????  ")
if crossroads == "left":
    print("You are safe for now!")
else:
    print("Fall in to a hole.\n Game over!")
waiting = input("You have approached treasure bay, will you swim or wait? ")
if waiting == "wait":
    print("Enjoy, your boat ride!!! But remember, I am the captain of this ship. ")
else:
    print("Once you learn patiences, then you will master Treasure Island")
door = input("Which door would you like to choose\n blue, red or yellow? Choose wisely...  ")
if door == "yellow":
    print("Well done, YOU WIN!")
elif door == "blue":
    print("Eaten by beasts.\n Game Over!! ")
elif door == "red":
    print("Burned by fire.\n Gave Over!! ")
else:
    print("Game Over!!!")
