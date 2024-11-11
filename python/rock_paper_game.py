import random
import json
import os

policy = {
    "rock": {"rock": "tie", "paper": "lose", "scissors": "win"},
    "paper": {"rock": "win", "paper": "tie", "scissors": "lose"},
    "scissors": {"rock": "lose", "paper": "win", "scissors": "tie"}
}

choices = list(policy.keys())
sc_f = "scores.json"

def cache():
    if os.path.exists(sc_f):
        with open(sc_f, "r") as ft:
            return json.load(ft)
    else:
        return {}


def record(results):
    with open(sc_f, "w") as f:
        json.dump(results, f, indent=4)

results = cache()

win_messages = ["You crushed it!", "Victory is yours!", "You're on fire! 🔥"]
lose_messages = ["Better luck next time!", "The computer got you this time!", "Ouch, close one!"]
tie_messages = ["It's a tie! Great minds think alike.", "Draw! Try again to break the tie.", "Stalemate! Go again!"]

def game(player):
    player_1, player_2 = results.get(player, {}).values()
    
    player_move = input("Choose rock, paper, or scissors: ").lower()
    if player_move not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return

    # Randomly select the computer's move
    computer_move = random.choice(choices)
    print(f"Computer chose: {computer_move}")

    # Determine the result
    result = policy[player_move][computer_move]
    if result == "win":
        player_1 += 1
        message = f"{random.choice(win_messages)}"
        print(message)
    elif result == "lose":
        player_2 += 1
        message = f"{random.choice(lose_messages)}"
        print(message)
    else:
        message = f"{random.choice(tie_messages)}"
        print(message)

    if player_1 != results[player]["score"] or player_2 != results[player]["games_played"]:
        results[player]["score"] = player_1
        results[player]["games_played"] = player_2
        
        print(f"\nScore: You {player_1} - Computer {player_2}\n")

def score_board():
    sorted_scores = sorted(results.items(), key=lambda x: x[1]["score"], reverse=True)
    print("\nLeaderboard ")
    for rank, (player, _) in enumerate(sorted_scores, start=1):
        print(f"{rank}. {player} - Score: {results[player]['score']}")

print("Welcome to Rock, Paper, Scissors! ")

def users(player):
    if player.lower() == 'exit':
        print("Goodbye!")
        exit()
    
    if player not in results:
        results[player] = {"score": 0, "games_played": 0}
        print(f"Hello, {player}! Good luck!")

while True:
    player = input("\nEnter your username to log in (or type 'exit' to quit): ").strip()
    users(player)
    round_counter = 0
    while True:
        game(player)
        round_counter += 1

        if round_counter % 5 == 0:
            record(results)
            resume = input("\nPlay again? (yes/no): ").lower() 
            if resume != "yes":
                break
        
        if player.lower() == 'exit':
            break

    print("\nThanks for playing! Final Score:")
    player_score = results[player]["score"]
    games_played = results[player]["games_played"]
    print(f"{player}: {player_score} - Computer: {games_played}")
    
    if player_score > games_played:
        print("You won overall! Amazing job!")
    elif games_played > player_score:
        print("The computer won overall. Better luck next time!")
    else:
        print("It was a tie overall! Well played!")

    score_board()
    record(results)
    print("\n\nYour scores have been saved.")
    #break
