import random
from game import Player, Enemy, MAX_HEALTH, HEAL_AMOUNT
ROUND_RECOVERY = 30
def start_game():
    round_number = 1
    player1 = Player("David", 0, 100)
    player1.add_score(100)
    score_tracker = {
        "attack": 0,
        "critical_hits": 0,
        "victory_bonus": 0
    }
    enemy1 = Enemy("Goliath",100)
    shadow_beast = Enemy ("Shadow Beast",150)
    lucifer = Enemy ("LUCIFER😈",200)
    player1_heal = True
    print("==========🎮WELCOME TO BATTLE OF SIGNAL🎮==========")
    print(f"========== Round {round_number} ==========")
    while player1.health > 0:
        current_enemy = get_current_enemy(round_number, enemy1, shadow_beast, lucifer)
        while player1.health>0 and current_enemy.health>0:
          player1_heal = player_turn(player1, current_enemy,player1_heal,score_tracker)
          if current_enemy.health>0:
             enemy_turn(current_enemy, player1, round_number)
          display_status(player1,current_enemy)
        if current_enemy.health <= 0:
           if current_enemy == lucifer:
               handle_victory(player1,current_enemy, score_tracker)
               break
           recover_after_round(player1)
           round_number += 1
        else:
            print("Ouch David lost!")
def player_attack(player1,current_enemy,score_tracker):
    choice = random.choice(["Normal","Normal","Normal","critical","Normal","Normal","critical","Normal"])
    if choice == "Normal":
     player1.attack_enemy(current_enemy, 20)
     player1.add_score(10)
     score_tracker["attack"] += 10
     print(f"⚔️ David attacked {current_enemy.name}!")
     print(f"🔥 {current_enemy.name} lost 20 health!")
    else:
        player1.attack_enemy(current_enemy, 40)
        player1.add_score(25)
        score_tracker["critical_hits"] += 25
        print(f"⚔️ David attacked {current_enemy.name}!")
        print("⚔️ Critical hit!")
        print(f"🔥 {current_enemy.name} lost 40 health!")
def get_choice(valid_choices):
    while True:
     choice = input("Enter your choice: ")
     if choice in valid_choices:
        return choice
     print("Invalid choice. try again!")
def player_action(player1,current_enemy,choice,score_tracker):
    if choice == "1":
        player_attack(player1, current_enemy,score_tracker)
    elif choice == "2":
        print("You Snooze 😂😂😂😂")
def player_heal(player1,player1_heal):
    if player1_heal:
       if player1.health < MAX_HEALTH:
          if player1.health <= MAX_HEALTH - HEAL_AMOUNT:
             player1.health += HEAL_AMOUNT
          else:
              player1.health = MAX_HEALTH
          print("David healed!")
          player1_heal = False
       else:
        print("Can't heal up right now, try again later!")
    else:
        print("David had already used his heal!")
    return player1_heal
def player_turn(player1, current_enemy, player1_heal, score_tracker):
    while True:
       print("===David's turn===")
       print(f"1.Attack {current_enemy.name}")
       print("2.Do Nothing")
       print("3.Heal !")
       print("4.Use Health Potion!")
       print("5.Show Inventory🎒")
       print("6.Use Shield🛡️")
       choice = get_choice(["1","2","3","4","5","6"])
       if choice == "3":
          player1_heal = player_heal(player1,player1_heal)
          continue
       if choice == "1" or choice == "2":
          player_action(player1, current_enemy, choice, score_tracker)
          break
       elif choice == "5":
            player1.show_inventory()
       elif choice == "6":
           player1.use_shield()
       elif choice == "4":
           player1.use_health_potion()
    return player1_heal
def enemy_turn(current_enemy, player1, round_number):
    print("===Enemy's turn===")
    print("1.Attack David")
    print("2.Do Nothing")
    print("3.Heavy attack")
    if round_number == 3:
     print("4.Hellfire")
    if player1.health > 50:
       if round_number == 3:
          choice = random.choice(["1","1","2","1","4","3","2","4","1","2","3","4"])
       else:
         choice = random.choice(["1","1","1","3","1","1","1","2","2","3","2","1","3","2","3","1","3","1","3","1","2","3"])
    else:
       choice = random.choice(["1", "3", "1", "2", "1", "3", "3", "1"])
    if choice == "1":
       damage = 20
       blocked = current_enemy.attack_player(player1,20)
       if blocked:
           print(f"Shield🛡️ Blocked {damage} Damage!")
       else:
           print(f"😈 {current_enemy.name} attacked David!")
           print(f"🔥 David lost {damage} health!")
    elif choice == "3":
        damage = 40
        blocked = current_enemy.attack_player(player1,40)
        if blocked:
            print(f"Shield🛡️ Blocked {damage} Damage!")
        else:
           print(f"⚔️ {current_enemy.name} attacked David heavily!")
           print(f"🔥 David lost {damage} health!")
    elif choice == "2":
        print("Stop Snoozing 😂😂")
    elif choice == "4":
        damage = 60
        blocked = current_enemy.attack_player(player1, 60)
        if blocked:
            print(f"Shield🛡️ Blocked {damage} Damage!")
        else:
            print(f"😈 {current_enemy.name} unleashed Hellfire!")
            print(f"🔥 David lost {damage} health!")
def get_current_enemy(round_number, enemy1, shadow_beast, lucifer):
    if round_number == 1:
        current_enemy = enemy1
    elif round_number == 2:
        current_enemy = shadow_beast
    elif round_number == 3:
        current_enemy = lucifer
    return current_enemy
def recover_after_round(player1):
    if player1.health < MAX_HEALTH:
        player1.health += ROUND_RECOVERY
        if player1.health > MAX_HEALTH:
            player1.health = MAX_HEALTH
        print(f"❤️ David recovered {ROUND_RECOVERY} health!")
def handle_victory(player1, current_enemy, score_tracker):
    player1.add_score(100)
    score_tracker["victory_bonus"] += 100
    print("David Won!")
    display_status(player1, current_enemy)
    print("========== 📊 SCORE BREAKDOWN 📊 ==========")
    print(f"Normal Attack Points: {score_tracker['attack']} ⭐")
    print(f"Critical Hit Points: {score_tracker['critical_hits']} ⭐")
    print(f"Victory Bonus: {score_tracker['victory_bonus']} ⭐")
    print("============================================")
    print(f"Final Score: {player1.score} ⭐")
    print(f"Final Health: {player1.health}️️️❤️")
    print(f"Lucifer Health: {current_enemy.health}❤️")
    print("========== 🏆 BATTLE OF SIGNAL COMPLETE 🏆 ==========")
def display_status(player1,current_enemy):
    print("⚔️ BATTLE STATUS")
    print(f"Player:{player1.name}")
    print(f"Score:{player1.score} ⭐")
    print(f"Health:{player1.health} ❤️")
    print(f"Enemy:{current_enemy.name}")
    print(f"Health:{current_enemy.health} ❤️")
start_game()