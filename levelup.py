import random

def get_level_up_die(career, checks, current_level):
    # Special rule for 75+
    if current_level >= 75:
        return 4
    if career:
        return 12 if checks == 2 else 6
    else:
        return 8 if checks == 2 else 4

def roll_advancement(skill, current_level, career, checks):
    roll_1d100 = random.randint(1, 100)
    passed = roll_1d100 > current_level
    die = get_level_up_die(career, checks, current_level)
    # Special rule for <25: min 1d4
    if current_level < 25:
        die = max(die, 4)
    if passed:
        adv_roll = random.randint(1, die)
        new_level = current_level + adv_roll
    else:
        adv_roll = 0
        new_level = current_level
    return {
        'skill': skill,
        'current_level': current_level,
        'career': career,
        'checks': checks,
        'roll_1d100': roll_1d100,
        'passed': passed,
        'die': die,
        'adv_roll': adv_roll if passed else None,
        'new_level': new_level
    }

def batch_level_up(skills_data):
    results = []
    for entry in skills_data:
        result = roll_advancement(
            entry['skill'],
            entry['current_level'],
            entry['career'],
            entry['checks']
        )
        results.append(result)
    return results
