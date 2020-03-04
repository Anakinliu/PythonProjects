"""
damage = 50 * (attack / defense) * effectiveness

attack = your attack power
defense = the opponent's defense
effectiveness = the effectiveness of the attack based on the matchup (see explanation below)

Attacks can be super effective, neutral, or not very effective depending on the matchup. For example, water would be super effective against fire, but not very effective against grass.

Super effective: 2x damage
Neutral: 1x damage
Not very effective: 0.5x damage

fire, water, grass, and electric

fire > grass
fire < water
fire = electric
water < grass
water < electric
grass = electric

any type against itself is not very effective

assume that the relationships between different types
are symmetric (if A is super effective against B, then B is not very effective against A).

"""
# damage = 50 * (attack / defense) * effectiveness
def calculate_damage(your_type, opponent_type, attack, defense):
    dicts = {
        'fire': {'water': 0.5,
                 'grass': 2,
                 'electric': 1},
        'water': {'fire': 2,
                  'grass': 0.5,
                  'electric': 0.5},
        'grass': {'fire': 0.5,
                  'water': 2,
                  'electric': 1},
        'electric': {'fire': 1,
                     'grass': 1,
                     'water': 2},
    }
    if your_type == opponent_type:
        return 50 * (attack / defense) * 0.5
    return 50 * (attack / defense) * dicts[your_type][opponent_type]


print(calculate_damage("fire", "water", 100, 100))