from random import choice

name_1 = ["", "", "", "", "Maneater ", "Paladin ", "Sir ", "Knight ", "Dark ", "Lady ", "Lord ", "Saint "]
name_2 = ["Ashelyn", "Donnal", "Baren", "Krista", "Avri", "Venmoor", "Creighton", "Sylvia", "Gotthard", "Yura", "Annalise", "Sina"]
name_3 = ["", "", " the Bloody", " the Sorcerer", " of Cardor", " of Carina", " of Everill", " of Ashesh", " of the Reedlands", " of Venheim", " the Lost", " the Wanderer"]

abiltiies = [
    ("Toughened", "Your maximum health increases by 3."),
    ("Fast", "Your speed increases by 1."),
    ("Sprinter", "The first time you take the move action each round you may move +2 spaces."),
    ("Superior Swordsman", "You have +1 to hit on all melee weapon attacks."),
    ("Superior Marksman", "You have +1 to hit on all ranged weapon attacks."),
    ("Vanguard", "You can make ranged attacks against characters adjacent to you but those attacks have -2 to hit."),
    ("Headshot", "You may spend an action on your turn to steady your aim. When you do so you gain +2 to hit and +3 damage on all ranged weapon attacks you make this turn."),
    ("Heavy Attack", "When you take the attack action and attack with a melee weapon you can spend one of your actions (spending 2 actions in total on the attack). The attack takes -1 to hit but on a hit its damage is doubled and ignores resist. If the weapon you attack with is heavy you can also choose to push the target 1 space directly away from you on a hit."),
    ("Charger", "Whenever you take the move action your next melee weapon attack this turn deals +2 damage on a hit."),
    ("Blade Dancer", "Your dual wielding attacks have +1 to hit."),
    ("Defender", "As a reaction when an ally adjacent to you is hit by an attack you can choose to be hit by that attack instead."),
    ("Adaptability", "Attacks you dodge against take a -1 penalty to the hit roll."),
    ("Assassin", "Your knives ignore piercing damage resist."),
    ("Duelist", "When you hit with an attack from a sword your next melee attack this combat has +1 to hit."),
    ("Mercenary", "The first time you hit with a hand weapon each turn its damage ignores resist."),
    ("Tower Guard", "You gain +1 to hit when you counter with a polearm."),
    ("Warrior", "Your great weapons deal +1 damage."),
    ("Bestial Soul", "The third time you hit with a melee attack in a single round you regain 4 health."),
    ("Kick", "Use an action to make a melee weapon attack against an adjacent character. On a hit they are pushed 1 space directly away from you and the next attack made against them until the start of their next turn has +3 to hit."),
    ("Attuned", "You gain 1 spell slot."),
    ("Demontouched", "Increase the fire damage dealt by your spells by 2."),
    ("Astrology adept", "Ranged attacks you make with sorceries have +1 to hit."),
    ("Faithful", "When you use a spell to restore health to a character that character regains +1 health."),
    ("Sweeping Attack", "Once per turn when you take the attack action with a melee weapon you may pick another target within your weapon’s range and adjacent to your original target. Make attacks against both characters, the second attack has -1 to hit and deals only half damage (halved before other modifiers).")
]

common_equipment_one = [
    "Dagger",
    "Shortsword",
    "Blue Bug Pellets",
    "Soldier's Armor",
    "Wooden Shield",
    "Broken Sword",
    "Short Spear",
    "Mace",
    "Buckler",
    "Handaxe",
    "Firebomb",
    "Charcoal Pine Resin",
    "Wood Arrows",
    "Shortbow",
    "Shard of Fading Soul",
    "Red Bug Pellets",
    "Wood Bolts",
    "Club",
    "Fletched Arrows",
    "Minor Heal Scroll"
]

common_equipment_two = [
    "Halberd",
    "Questing Knight Armor",
    "Scimitar",
    "Soldier's Crossbow",
    "Black Firebomb",
    "Longsword",
    "Starlight Pellet Scroll",
    "Greataxe",
    "Throwing knife",
    "Yellow Bug Pellets",
    "Iron Round Shield",
    "Red and Blue Kite Shield",
    "Pilgrim's Talisman",
    "Knight Armour",
    "Winged Spear",
    "Battleaxe",
    "Scholar's Staff",
    "Iron Helm",
    "Longbow",
    "Barrior of Faith Scroll"
]

common_rings = [
    "Rusted Iron Ring",
    "Wood Grain Ring",
    "Life Ring",
    "Red Stoneplate Ring",
    "Golden Sword Ring",
    "Golden Shield Ring",
    "Blue Stoneplate Ring",
    "Hawk Ring"
]


def make_character() -> str:
    return f'Name: {choice(name_1)+choice(name_2)+choice(name_3)}\nEquipment:{choice(common_equipment_one)+", "+choice(common_equipment_one)+", "+choice(common_equipment_one)+","+choice(common_equipment_two)+", "+choice(common_rings)}\nAbility:{choice(abiltiies)}'