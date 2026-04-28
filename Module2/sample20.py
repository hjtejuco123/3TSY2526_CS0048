# Game level unlock system Sample 20: Game level unlock system with nested if statements
current_level = 5
score = 2500
has_bonus = True

if current_level >= 1:
    print(f"Level {current_level} is unlocked")
    if score >= 2000:
        print("You've earned a gold medal!")
        if has_bonus:
            print("Bonus stage unlocked!")
        else:
            print("Complete all challenges for bonus content")
    elif score >= 1000:
        print("You've earned a silver medal")
    else:
        print("You've earned a bronze medal")
else:
    print("Complete previous levels to unlock this one")