from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

#Clicker that gives 1 gold per click
#Buy Gold Gen
#Automatic Gold Gen

gold=0
size=.1
clicker = Button(scale=.15, texture='pickaxe', color=color.white)
gold_text = Text(text="0", y=.25, origin=(0,0), scale=2, padding=size)
#gold_text.create_background(padding=size, radius=size, color=color.black66)   

def onClick():
    global gold
    gold += 1
    gold_text.text = str(gold)

clicker.on_click = onClick

gold_miner = Button(text='Miner', color=color.gray, x=.2, scale=.15, cost=10)
gold_miner.tooltip = Tooltip(f'<gold>Gold Generator\n<default>Earn 1 gold every second.\nCosts {gold_miner.cost} gold.')

def buy_auto_mine():
    global gold
    if gold >= gold_miner.cost:
        gold -= gold_miner.cost
        gold_text.text = str(gold)
        invoke(auto_miner, 1, 1)

gold_miner.on_click = buy_auto_mine
def auto_miner(value=1, interval=1):
    global gold
    gold += 1
    gold_text.text = str(gold)
    invoke(auto_miner, value, delay=interval)

app.run()
