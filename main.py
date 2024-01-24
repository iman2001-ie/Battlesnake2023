
# Welcome to
# __________         __    __  .__                               __
# \______   \_____ _/  |__/  |_|  |   ____   ______ ____ _____  |  | __ ____
#  |    |  _/\__  \\   __\   __\  | _/ __ \ /  ___//    \\__  \ |  |/ // __ \
#  |    |   \ / __ \|  |  |  | |  |_\  ___/ \___ \|   |  \/ __ \|    <\  ___/
#  |________/(______/__|  |__| |____/\_____>______>___|__(______/__|__\\_____>
#
# This file can be a nice home for your Battlesnake logic and helper functions.
#
# To get you started we've included code to prevent your Battlesnake from moving backwards.
# For more info see docs.battlesnake.com

import random
import typing
import math


# info is called when you create your Battlesnake on play.battlesnake.com
# and controls your Battlesnake's appearance
# TIP: If you open your Battlesnake URL in a browser you should see this data
def info() -> typing.Dict:
    print("INFO")

    return {
        "apiversion": "1",
        "author": "iman2001_ie",  # TODO: Your Battlesnake Username
        "color": "#990505",  # TODO: Choose color
        "head": "evil",  # TODO: Choose head
        "tail": "nr-booster",  # TODO: Choose tail
    }


# start is called when your Battlesnake begins a game
def start(game_state: typing.Dict):
    print("GAME START")


# end is called when your Battlesnake finishes a game
def end(game_state: typing.Dict):
    print("GAME OVER\n")

def get_distance_between_two(a, b) -> int:
        distance = math.sqrt((a["x"]-b["x"])**2 + (a["y"] - b["y"])**2)
        return distance

# move is called on every turn and returns your next move
# Valid moves are "up", "down", "left", or "right"
# See https://docs.battlesnake.com/api/example-move for available data
def move(game_state: typing.Dict) -> typing.Dict:

    is_move_safe = {
      "up": True, 
      "down": True, 
      "left": True, 
      "right": True
    }

    # We've included code to prevent your Battlesnake from moving backwards
    my_head = game_state["you"]["body"][0]  # Coordinates of your head
    my_neck = game_state["you"]["body"][1]  # Coordinates of your "neck"
    print (game_state)
    #print(game_state["you"]["body"])

    if my_neck["x"] < my_head["x"]:  # Neck is left of head, don't move left
        is_move_safe["left"] = False

    elif my_neck["x"] > my_head["x"]:  # Neck is right of head, don't move right
        is_move_safe["right"] = False

    elif my_neck["y"] < my_head["y"]:  # Neck is below head, don't move down
        is_move_safe["down"] = False

    elif my_neck["y"] > my_head["y"]:  # Neck is above head, don't move up
        is_move_safe["up"] = False

    # TODO: Step 1 - Prevent your Battlesnake from moving out of bounds
    board_width = game_state['board']['width']
    board_height = game_state['board']['height']
  
    if my_head["x"] == 0:
      is_move_safe["left"] = False
    elif my_head["x"] == board_width - 1:
      is_move_safe["right"] = False
    if my_head["y"] == 0:
      is_move_safe["down"] = False
    elif my_head["y"] == board_height - 1:
      is_move_safe["up"] = False
      

    #TODO: Step 2 - Prevent your Battlesnake from colliding with itself
    my_body = game_state['you']['body']
    # print(my_body)
  
    for body_part in my_body:
      body_part_x = body_part["x"]
      body_part_y = body_part["y"]
      if my_head["x"] == body_part_x + 1 and my_head["y"] == body_part_y:  
        is_move_safe["left"] = False

      elif my_head["x"] == body_part_x - 1 and my_head["y"] == body_part_y: 
        is_move_safe["right"] = False

      elif my_head["x"] == body_part_x and my_head["y"] == body_part_y + 1:  
        is_move_safe["down"] = False

      elif my_head["x"] == body_part_x and my_head["y"] == body_part_y - 1:  
        is_move_safe["up"] = False

      
        
      
      

    # TODO: Step 3 - Prevent your Battlesnake from colliding with other Battlesnakes
    # Are there any safe moves left?
    safe_moves = []
    for move, isSafe in is_move_safe.items():
        if isSafe:
            safe_moves.append(move)
          
    opponents = game_state['board']['snakes']
    for snake in opponents:
      snake_head = snake["body"][0]
      if get_distance_between_two(snake_head, my_head) <= 2.5 and len(snake["body"]) >=len(my_body):
        if my_head["x"] == snake_head["x"] + 2 and my_head["y"] == snake_head["y"]:  
          is_move_safe["left"] = False
        
        elif my_head["x"] == snake_head["x"] - 2 and my_head["y"] == snake_head["y"]: 
          is_move_safe["right"] = False
        
        elif my_head["x"] == snake_head["x"] and my_head["y"] == snake_head["y"] + 2:  
          is_move_safe["down"] = False
        
        elif my_head["x"] == snake_head["x"] and my_head["y"] == snake_head["y"] - 2:  
          is_move_safe["up"] = False
            
        elif my_head["x"] == snake_head["x"]+1 and my_head["y"] == snake_head["y"] -1:
          is_move_safe["up"] = False
          if len(safe_moves) >= 3:
            is_move_safe["left"] = False

        elif my_head["x"] == snake_head["x"] - 1 and my_head["y"] == snake_head["y"] -1:
          is_move_safe["up"] = False
          if len(safe_moves) >= 3:
            is_move_safe["right"] = False
            
        elif my_head["x"] == snake_head["x"] + 1 and my_head["y"] == snake_head["y"] + 1:
          is_move_safe["down"] = False
          if len(safe_moves) >= 3:
            is_move_safe["left"] = False
            
        elif my_head["x"] == snake_head["x"] - 1 and my_head["y"] == snake_head["y"] + 1:
          is_move_safe["down"] = False
          if len(safe_moves) >= 3:
            is_move_safe["right"] = False
          
      for body_part in snake["body"]:
        body_part_x = body_part["x"]
        body_part_y = body_part["y"]
          
        if my_head["x"] == body_part_x + 1 and my_head["y"] == body_part_y:  
          is_move_safe["left"] = False
        
        elif my_head["x"] == body_part_x - 1 and my_head["y"] == body_part_y: 
          is_move_safe["right"] = False
        
        elif my_head["x"] == body_part_x and my_head["y"] == body_part_y + 1:  
          is_move_safe["down"] = False
        
        elif my_head["x"] == body_part_x and my_head["y"] == body_part_y - 1:  
          is_move_safe["up"] = False
       
          

    # Are there any safe moves left?
    safe_moves = []
    for move, isSafe in is_move_safe.items():
        if isSafe:
            safe_moves.append(move)

    if len(safe_moves) == 0:
        print(f"MOVE {game_state['turn']}: No safe moves detected! Moving down")
        return {"move": "down"}
    else:
      i = 2
      while i < len(my_body):
        body_part = my_body[i]
        body_part_x = body_part["x"]
        body_part_y = body_part["y"]
        if len(safe_moves) >= 2:
          if "right" in safe_moves and my_head["x"] == body_part_x - 2  and my_head["y"] == body_part_y:
              safe_moves.remove("right")
              print("right removed")
          elif "left" in safe_moves and my_head["x"] == body_part_x + 2  and my_head["y"] == body_part_y:
              safe_moves.remove("left") 
              print("left removed")
          elif "down" in safe_moves and my_head["x"] == body_part_x and my_head["y"] == body_part_y + 2:
              safe_moves.remove("down")
              print("down removed")
          elif "up" in safe_moves and  my_head["x"] == body_part_x and my_head["y"]  == body_part_y - 2 :
            safe_moves.remove("up")
            print("up removed")
            
          elif "right" in safe_moves and my_head["y"] == board_height-1 and body_part_y == board_height-2 and my_head["x"] < body_part_x:
            safe_moves.remove("right")
            print("right removed")
            
          elif "left" in safe_moves and my_head["y"] == board_height-1 and body_part_y == board_height-2 and my_head["x"] > body_part_x:
            safe_moves.remove("left")
            print("left removed")
            
          elif "right" in safe_moves and my_head["y"] == 0 and body_part_y == 1 and my_head["x"] < body_part_x:
            safe_moves.remove("right")
            print("right removed")
            
          elif "left" in safe_moves and my_head["y"] == 0 and body_part_y == 1 and my_head["x"] > body_part_x:
            safe_moves.remove("left")
            print("left removed")

          elif "up" in safe_moves and my_head["x"] == board_width-1 and body_part_x == board_width-2 and my_head["y"] < body_part_y:
            safe_moves.remove("up")
            print("up removed")

          elif "down" in safe_moves and my_head["x"] == board_width-1 and body_part_x == board_width-2 and my_head["y"] > body_part_y:
            safe_moves.remove("down")
            print("down removed")

          elif "up" in safe_moves and my_head["x"] == 0 and body_part_x == 1 and my_head["y"] < body_part_y:
            safe_moves.remove("up")
            print("up removed")

          elif "down" in safe_moves and my_head["x"] == 0 and body_part_x == 1 and my_head["y"] > body_part_y:
            safe_moves.remove("down")
            print("down removed")
          
        i += 1
        

    # Choose a random move from the safe ones
    next_move = random.choice(safe_moves)
      

    # TODO: Step 4 - Move towards food instead of random, to regain health and survive longer

      
    def get_distance(f) -> int:
      distance = math.sqrt((my_head["x"]-f["x"])**2 + (my_head["y"] - f["y"])**2)
      return distance
       
    food = game_state['board']['food']
    if len(food) > 0:
      closest = food[0]
      i = 1
      while i < len(food):
        if get_distance(food[i]) < get_distance(closest):
          closest = food[i]
        i += 1
    if len(my_body) < 10 or game_state["you"]["health"] < 50:
      if my_head["x"] < closest["x"] and ("right" in safe_moves):
        next_move = "right"
        print("Going for food")
        
      elif my_head["x"] > closest["x"] and ("left" in safe_moves):
        next_move = "left"
        print("Going for food")
        
      elif my_head["y"] > closest["y"] and ("down" in safe_moves):
        next_move = "down"
        print("Going for food")
        
      elif my_head["y"] < closest["y"] and ("up" in safe_moves):
        next_move = "up"
        print("Going for food")
        
      
     


          
         
    for snake in opponents:
      snake_head = snake["body"][0]
      if len(my_body) > 8 and len(snake["body"]) < len(my_body):
        if my_head["x"] < snake_head["x"] and snake_head["x"] > board_width-1 and ("right" in safe_moves):
          next_move = "right"
          print("Going for enemy")
          
        elif my_head["x"] > snake_head["x"] and snake_head["x"] > 0 and ("left" in safe_moves):
          next_move = "left"
          print("Going for enemy")
          
        elif my_head["y"] > snake_head["y"] and snake_head["y"] > 0 and ("down" in safe_moves):
          next_move = "down"
          print("Going for enemy")
          
        elif my_head["y"] < snake_head["y"] and snake_head["y"] > board_height-1 and ("up" in safe_moves):
          next_move = "up"
          print("Going for enemy")
          
        
    
    
    
    
    print("safe moves:", safe_moves)
    print(f"MOVE {game_state['turn']}: {next_move}")
    return {"move": next_move}



#Start server when `python main.py` is run
if __name__ == "__main__":
    from server import run_server

    run_server({
        "info": info, 
        "start": start, 
         "move": move, 
        "end": end
    })
