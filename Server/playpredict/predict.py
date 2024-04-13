from . import play as p, formation as f

# TODO: Actually predict.

# Your team is possessing the ball
# Suggest a list of offensive plays (based on game's situation, the other team's defense's formation, your current offensive formation, and previous plays)
def suggest_offense_plays(game_situation, their_defense_formation, your_offense_formation, previous_plays_with_situation) -> list[p.Play]:
    return []


# Suggest a list of offensive formations (based on game's situation, the other team's defense's formation, and previous plays)
def suggest_offense_formations(
    game_situation, their_defense_formation, previous_plays_with_situation
) -> list[f.Formation]:
    return []


# Your team is not possessing the ball
# Suggest a list of offensive plays that the other team is likely to run (based on game's situation, your team's current defense's formation, other team's current offensive formation, and previous plays)
def predict_offense_plays(
    game_situation,
    your_defense_formation,
    their_offense_formation,
    previous_plays_with_situation,
) -> list[p.Play]:
    return []


# Suggest a defensive formation (based on game's situation, the other team's offense's formation, and previous plays)
def suggest_defense_formations(
    game_situation, their_offense_formation, previous_plays_with_situation
) -> list[f.Formation]:
    return []
