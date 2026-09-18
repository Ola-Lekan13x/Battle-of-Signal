MAX_HEALTH = 150
HEAL_AMOUNT = 50
class Player:
    def __init__(self, name, score, health,):
        self.name = name
        self.score = score
        self.health = health
        self.inventory = {
            "Health Potion🧪": 3,
            "Shield🛡️": 1       }
        self.shield_active= False
    def lose_health(self,health_rank):
        if self.health - health_rank < 0:
            self.health = 0
        else:
            self.health -= health_rank
    def add_score(self,amount):
        self.score += amount
    def lose_score(self,amount):
        if amount <= self.score:
         self.score -= amount
        else:
            self.score = 0
    def attack_enemy(self, enemy, damage):
        enemy.lose_health(damage)
    def show_inventory(self):
        for key,value in self.inventory.items():
            print(key, value)
    def use_health_potion(self):
        if self.inventory["Health Potion🧪"] <= 0:
            print("❌ Sorry! You are out of Health Potions.")
        elif self.health == MAX_HEALTH:
            print("❌ Can't use Health Potion, try again later!")
        else:
            old_health = self.health
            self.health += HEAL_AMOUNT
            if self.health > MAX_HEALTH:
               self.health = MAX_HEALTH
            recovered = self.health - old_health
            print("David Used a health Potion🧪!")
            print(f"❤️ David recovered {recovered} health!")
            self.inventory["Health Potion🧪"] -= 1
    def use_shield(self):
        if self.inventory["Shield🛡️"] > 0:
           print("David activated Shield!")
           self.inventory["Shield🛡️"] -=1
           self.shield_active = True
        else:
            print("David is out of Shield!")
class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def lose_health(self,health_rank):
        if self.health - health_rank < 0:
            self.health = 0
        else:
            self.health -= health_rank
    def attack_player(self, player, damage ):
        blocked = player.shield_active
        if player.shield_active:
            player.shield_active = False
            return blocked
        else:
         player.lose_health(damage)
         return blocked