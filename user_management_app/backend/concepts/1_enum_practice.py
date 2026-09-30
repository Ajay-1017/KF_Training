from enum import Enum , Flag , auto


#-------------------------------------------------------
# Enum 
#-------------------------------------------------------

# class Color(Enum):
#     RED : str = "R" 
#     BLUE : str = "B"
#     GREEN : str = "G"

# print(Color('R')) # color.RED
# print(Color.RED) # color.RED


# print(type(Color('R'))) # <enum 'color'>
# print(repr(Color.RED))# <color.RED: 'R'>


# print(Color.RED.name) # RED
# print(Color.RED.value) # R


#-------------------------------------------------------
# Flag
#-------------------------------------------------------

# class Color(Flag):
#     RED : int = 1
#     BLUE : int = 2
#     GREEN : int = 4
#     YELLOW : int = 8

# yellow_and_red : Color = Color.YELLOW | Color.RED 
# print(yellow_and_red)
# print(yellow_and_red.value) # 9

# for color in yellow_and_red:
#     print(color)


#----------------------------------------------------------------
# Flag , auto -> automatically set the above like integer value
#----------------------------------------------------------------

class Color(Flag):
    RED : int = auto()
    BLUE : int = auto()
    GREEN : int = auto()
    YELLOW : int = auto()

yellow_and_red : Color = Color.YELLOW | Color.RED 
print(yellow_and_red.value)
for color in yellow_and_red:
    print(color)

