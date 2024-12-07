import random
import json

def get_player_name():
    return input("ENTER PLAYER NAME: ").strip()

def get_match_type():
    print("\nCHOOSE MATCH TYPE:")
    print("1. T20 (20 Overs)")
    print("2. ODI (50 Overs)")
    print("3. Test Match (Unlimited Overs)")
    while True:
        try:
            choice = int(input("ENTER YOUR CHOICE (1-3): "))
            if choice in [1, 2, 3]:
                return [120, 300, float('inf')][choice - 1]
            else:
                print("Please choose a valid match type.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

def get_pitch_condition():
    print("\nSELECT PITCH CONDITION:")
    print("1. Flat (High Scoring)")
    print("2. Green (Balanced)")
    print("3. Dry (Low Scoring)")
    while True:
        try:
            choice = int(input("ENTER YOUR CHOICE (1-3): "))
            if choice in [1, 2, 3]:
                return ["Flat", "Green", "Dry"][choice - 1]
            else:
                print("Please choose a valid pitch condition.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

def scoring_weights(pitch, match_overs):
    if match_overs == 120:
        if pitch == "Flat":
            return [20, 30, 35, 25, 30, 15, 10]
        elif pitch == "Green":
            return [25, 35, 30, 30, 25, 15, 12]
        else:
            return [30, 40, 35, 25, 20, 10, 8]
    elif match_overs == 300:
        if pitch == "Flat":
            return [15, 25, 30, 20, 25, 10, 5]
        elif pitch == "Green":
            return [20, 30, 25, 25, 20, 10, 12]
        else:
            return [25, 35, 30, 20, 15, 5, 12]
    else:
        if pitch == "Flat":
            return [10, 20, 25, 15, 20, 5, 5]
        elif pitch == "Green":
            return [15, 25, 20, 20, 15, 5, 5]
        else:
            return [20, 30, 25, 15, 10, 0, 5]

def cricket_game():
    match_overs = get_match_type()
    pitch = get_pitch_condition()

    if match_overs == 120:
        target = random.randint(50, 200)
    elif match_overs == 300:
        target = random.randint(75, 425)
    else:
        target = random.randint(100, 500)

    print(f"\nTARGET SET: {target} RUNS")
    print(f"MATCH TYPE: {'Unlimited Overs' if match_overs == float('inf') else match_overs // 6} OVERS")
    print(f"PITCH CONDITION: {pitch}\n")
    player_name = get_player_name()

    total_score = 0
    balls_played = 0
    wickets = 0
    max_wickets = 10

    scoring_probs = scoring_weights(pitch, match_overs)

    player_data = {
        player_name: {
            "runs": 0,
            "dots": 0,
            "singles": 0,
            "twos": 0,
            "threes": 0,
            "fours": 0,
            "sixes": 0,
            "balls": 0
        }
    }

    commentary = {
        0: ["Dot ball! Excellent delivery.", "No runs scored.", "Defended well."],
        1: ["Quick single!", "Good running between the wickets.", "One run taken."],
        2: ["Nicely placed for two.", "Great running! Two runs added.", "Well played, two runs."],
        3: ["Brilliant running! Three runs.", "Fielders under pressure, it's three runs."],
        4: ["That's a boundary!", "Crisp shot, four runs!", "What a shot, it's a four!"],
        6: ["SIX! That's massive!", "Out of the park, six runs!", "Huge hit for a six!"],
        "OUT": ["That's a wicket!", "Caught! The batsman is out.", "Bowled! Cleaned up."]
    }

    while wickets < max_wickets and balls_played < match_overs:
        outcome = random.choices([0, 1, 2, 3, 4, 6, "OUT"], weights=scoring_probs)[0]
        balls_played += 1

        player_data[player_name]["balls"] += 1

        if outcome == "OUT":
            wickets += 1
            print(random.choice(commentary["OUT"]))
            if wickets < max_wickets:
                new_player = get_player_name()
                player_data[new_player] = {
                    "runs": 0,
                    "dots": 0,
                    "singles": 0,
                    "twos": 0,
                    "threes": 0,
                    "fours": 0,
                    "sixes": 0,
                    "balls": 0
                }
                player_name = new_player
        else:
            player_data[player_name]["runs"] += outcome
            total_score += outcome
            print(random.choice(commentary[outcome]))
            if outcome == 0:
                player_data[player_name]["dots"] += 1
            elif outcome == 1:
                player_data[player_name]["singles"] += 1
            elif outcome == 2:
                player_data[player_name]["twos"] += 1
            elif outcome == 3:
                player_data[player_name]["threes"] += 1
            elif outcome == 4:
                player_data[player_name]["fours"] += 1
            elif outcome == 6:
                player_data[player_name]["sixes"] += 1

        if total_score >= target:
            print("\nYOU WON THE GAME!")
            break

    overs_played = balls_played // 6
    balls_in_current_over = balls_played % 6
    print("\nMATCH SUMMARY:")
    print(f"TARGET: {target} RUNS")
    print(f"FINAL SCORE: {total_score}/{wickets}")
    print(f"OVERS PLAYED: {overs_played}.{balls_in_current_over}")
    
    overall_summary = {
        "dots": 0,
        "singles": 0,
        "twos": 0,
        "threes": 0,
        "fours": 0,
        "sixes": 0
    }
    
    print("\nINDIVIDUAL PLAYER SCORES:")
    for player, stats in player_data.items():
        print(f"{player}: {stats['runs']} runs ({stats['balls']} balls)")
        print(f"Dots: {stats['dots']}, Singles: {stats['singles']}, Twos: {stats['twos']}, Threes: {stats['threes']}, Fours: {stats['fours']}, Sixes: {stats['sixes']}")
        for key in overall_summary:
            overall_summary[key] += stats[key]
    
    print("\nOVERALL SUMMARY:")
    print(f"Total Dots: {overall_summary['dots']}")
    print(f"Total Singles: {overall_summary['singles']}")
    print(f"Total Twos: {overall_summary['twos']}")
    print(f"Total Threes: {overall_summary['threes']}")
    print(f"Total Fours: {overall_summary['fours']}")
    print(f"Total Sixes: {overall_summary['sixes']}")

    if total_score < target:
        print(f"YOU LOST THE GAME BY {target - total_score} RUNS.")
    elif total_score == target-1:
        print("THE MATCH ENDED IN A TIE!")
    
    game_data = {
        "target": target,
        "score": total_score,
        "wickets": wickets,
        "overs_played": f"{overs_played}.{balls_in_current_over}",
        "result": "WON" if total_score >= target else "LOST" if total_score < target else "TIED",
        "player_data": player_data,
        "overall_summary": overall_summary
    }

    with open("advanced_game_state.json", "w") as file:
        json.dump(game_data, file, indent=4)
    
    print("\nGAME DATA SAVED TO 'advanced_game_state.json'")

# Run the game
cricket_game()
