import mysql.connector

""" Description of the application: 
The menu allows the user to select several options: Show the games with the most global score 
for a specific console, show the ratings for the games in a saga, show how many times games
have been played in a console, show all games, in every console, with a specific global score, 
add a new game and to all the required tables, and finally, exit the application.  """

config = {
  'user':'test',    # could be root, or a user you created, I created 'testuser'
  'password':'none',  # the password for that use
  'database':'games',   # the database to connect to
  'host':'192.168.1.128',   # localhost
  'allow_local_infile':True  # needed so can load local files
  }

def print_menu():
  print("\n"*10)
  print("Choose the action to take")
  print("1. Show a number of top games from a game system")
  print("2. Show game ratings of game collections")
  print("3. Show times played in a game system")
  print("4. Show all games with a specific rating")
  print("5. Add a new game")
  print("6. Exit")

if __name__ == "__main__":
  mydb = mysql.connector.connect(**config)
  myc = mydb.cursor()
  while True:
    query = ""
    print_menu()
    x = int(input("Select your option\n"))
    match x:
      case 1:
        num_games = int(input("How many games do you want to see?\n"))
        game_system = str(input("From which system do you want to see the games?\n"))
        query = """select distinct g.title, e.global_score from games g, game_system gs, 
        availability a, partof po, enjoyment e where gs.sName = a.SystemName and 
        g.title = po.title and e.game = g.title and gs.sName = \"{}\" 
        order by e.global_score desc limit {}""".format(game_system,num_games)
      case 2:
        saga_like = str(input("Wildcard for the sagas to show\n"))
        query = """with games as (select s.members from saga s where s.saga 
        like \"%{}%\") select g.members, e.global_score from games g, enjoyment e 
        where g.members = e.game""".format(saga_like)
      case 3:
        game_system = str(input("From which system do you want to see the games?\n"))
        query = """with playedtimes as (select distinct g.title, p.played_times from games g, 
        game_system gs, availability a, partof po, enjoyment e, played p
        where gs.sName = a.SystemName and g.title = po.title and e.game = g.title 
        and e.game = p.title and gs.sName = \"{}\") select sum(played_times) from playedtimes""".format(game_system)
      case 4:
        expected_score = int(input("What is the exact score to show the games?\n"))
        query = """select game from enjoyment where global_score = {}
        """.format(expected_score)
      case 5:
        title = str(input("Title: \n"))
        systemname = str(input("System in which you can play it: \n"))
        music_score = int(input("Music Score: \n"))
        graphics_score = int(input("Graphics Score: \n"))
        gameplay_score = int(input("Gameplay Score: \n"))
        story_score = int(input("Story Score: \n"))
        global_score = (music_score + graphics_score + gameplay_score + story_score)/4
        release_date = str(input("Release Date: \n"))
        developer = str(input("Developer: \n"))
        classification = str(input("Classification: \n"))
        Genre = str(input("Genre: \n")) 
        saga = str(input("Saga: \n"))
        played_times = int(input("Played items: \n"))
        try:
          insert_statement = "insert into games values (\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".format(title, release_date, developer, classification, Genre)
          myc.execute(insert_statement)
        except Exception as e:
          print(e)
          print("That game appears to be already in the database")
        try:
          
          insert_statement = "insert into saga values (\"{}\",1,\"{}\")".format(saga, title)
          myc.execute(insert_statement)
        except Exception as e:
          print(e)
          print("Either the saga already exists, or the game does not exist")
        try: 
          insert_statement = "insert into availability values (\"{}\",\"{}\")".format(systemname, saga)
          myc.execute(insert_statement)
          insert_statement = "insert into enjoyment values (\"{}\",{},{},{},{},{})".format(title, music_score, graphics_score, gameplay_score, story_score, global_score)
          myc.execute(insert_statement)
          insert_statement = "insert into ownedon values (\"{}\",\"{}\")".format(title, systemname)
          myc.execute(insert_statement)
          insert_statement = "insert into partof values (\"{}\",\"{}\")".format(saga, title)
          myc.execute(insert_statement)
          query = "select * from games where title = \"{}\"".format(title)
        except Exception as e:
          print(e)
        mydb.commit()
      case 6:
        break
      case _:
        pass
    print(query)
    myc.execute(query)
    for x in myc:
      print(x)
  mydb.close()