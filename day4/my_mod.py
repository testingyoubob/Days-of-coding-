import random 

random_integer = random.randint(1, 10)
random_number = random.random() * 10 
random_float = random.uniform(1, 10)

def head_tails():
    return random.randint(0,1)


fruitslist = ["apple", "organe", "banana", "pear",]
#give me a list of all of the states in the usa 
us_states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California",
    "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
    "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
    "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
    "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

game_text_image = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) ''', '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

 ''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) ''',
'''
          _   _
         ( \ / )
        __\ Y /,-')
       (__     .-'
          |   (
          [___]
          |oo |
        ,' \  |
       <___/  |
          |   |
          |   |
          |   |
          |   |
      _,-/_._  \,_
_.-"^`  //   \    `^"-.,__
\     ,//     \          /
 `\,-":;       ;  \-.,_/'
      ||       |   ;
      ||       ;   |
      :\      /    ;
       \`----'    /
        `._____.-'
          | | |
        __| | |__
  jgs  /    |    |
       `""""`""""` ''']
