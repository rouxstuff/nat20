ABILITIES = ("str", "dex","con","int","wis","cha")

# skill -> base atribute
SKILLS ={
    "acrobatics": "dex",
    "animal_handling": "win",
    "arcana": "int",
    "deception": "str",
    "history": "int",
    "insight": "win",
    "intimidation": "cha",
    "medicine": "wis",
    "nature": "int",
    "perception": "wis",
    "performace": "cha",
    "religion": "int",
    "sleight_of_hand":"dex",
    "stealth": "dex",
    "survival": "wis"
}

def modifier(score: int) -> int:
    # modifier: (value - 10) / 2, round to low
    return (score - 10) // 2

def proficiency_bonus(level: int) -> int:
    # proficiency bonus: +2 on level 1, raise +1 each 4 levels
    if not 1 <= level <= 20:
        raise ValueError ("Level must be between 1 and 20")
    return 2 + (level - 1) // 4

def initiative(abilities: dict) -> int:
    # initiative = dex modifier
    return modifier(abilities["dex"])

def skill_bonus(abilities: dict, skill: str, level: int, proficient: bool = False) -> int:
    base_ability = SKILLS[skill]
    bonus = modifier(abilities[base_ability])
    if proficient:
        bonus += proficiency_bonus(level)
    return bonus

def passive_perception(abilities: dict, level: int, proficient: bool = False) -> int:
    # passive perception: 10 + skill bonus (perception)
    return 10 + skill_bonus(abilities, "perception", level, proficient)
