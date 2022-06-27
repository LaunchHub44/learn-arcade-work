import random


def main():
    canteen_fill = 100
    thirst = 0
    camel_stamina = 0
    total_distance = 0
    travel_dist = 0
    dist_from_natives = -20
    player_min_speed = 0
    player_max_speed = 0
    native_min_speed = 0
    native_max_speed = 0
    thirst_limit = 0
    stamina_limit = 0
    prompt = None
    done = False

    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back, and are chasing you down!")
    print("Survive your desert trek, and outrun the natives.")
    print()

    print("Difficulty explanations are at the end of the game's code.")
    difficulty = input("Play on Easy (Easy/E), Normal (Normal/N), or Hard (Hard/H)? ")

    if difficulty == "Easy" or difficulty == "easy" or difficulty == "E" or difficulty == "e":
        player_min_speed = 10
        player_max_speed = 16
        native_min_speed = 4
        native_max_speed = 8
        thirst_limit = 10
        stamina_limit = 20
        camel_stamina = stamina_limit
    elif difficulty == "Normal" or difficulty == "normal" or difficulty == "N" or difficulty == "n":
        player_min_speed = 8
        player_max_speed = 14
        native_min_speed = 5
        native_max_speed = 11
        thirst_limit = 7
        stamina_limit = 15
        camel_stamina = stamina_limit
    elif difficulty == "Hard" or difficulty == "hard" or difficulty == "H" or difficulty == "h":
        player_min_speed = 7
        player_max_speed = 14
        native_min_speed = player_min_speed
        native_max_speed = player_max_speed
        thirst_limit = 5
        stamina_limit = 10
        camel_stamina = stamina_limit

    while not done:
        print()
        print("A: Drink from your canteen.")
        print("B: Ahead moderate speed.")
        print("C: Ahead full speed.")
        print("D: Stop for the night.")
        print("E: Status check.")
        print("Q: Quit.")
        prompt = input("What is your choice? ")

        if prompt == "A" or prompt == "a":
            print()
            if thirst == 0:
                print("You are not thirsty right now.")
                continue
            elif thirst > 0:
                if canteen_fill == 0:
                    print("Your canteen is empty! 0%")
                elif canteen_fill > 0:
                    print("You drink from your canteen.")

                if canteen_fill - (thirst * 10) // 2 < 0:
                    thirst = 0
                    canteen_fill = 0
                else:
                    canteen_fill -= (thirst * 10) // 2
                    thirst = 0

                if difficulty == "Hard" or difficulty == "hard" or difficulty == "H" or difficulty == "h":
                    dist_from_natives += random.randint(native_min_speed, native_max_speed)

        elif prompt == "B" or prompt == "b":
            print()
            travel_dist = random.randint(player_min_speed, player_max_speed)
            total_distance += travel_dist
            dist_from_natives -= travel_dist
            print(f"You traveled {travel_dist} miles.")
            thirst += 1
            camel_stamina -= 1
            dist_from_natives += random.randint(native_min_speed, native_max_speed)

            if random.randint(1, 21) == 10:
                print("There was an oasis with fresh water!")
                print("You refill your canteen.")
                canteen_fill = 100

        elif prompt == "C" or prompt == "c":
            print()
            travel_dist = random.randint(player_min_speed + 3, player_max_speed + 5)
            total_distance += travel_dist
            dist_from_natives -= travel_dist
            print(f"You traveled {travel_dist} miles.")
            thirst += 1
            camel_stamina -= random.randint(1, 3)
            dist_from_natives += random.randint(native_min_speed, native_max_speed)

            if random.randint(1, 21) == 10:
                print("There was an oasis with fresh water!")
                print("You refill your canteen.")
                canteen_fill = 100

        elif prompt == "D" or prompt == "d":
            print()
            print("You stop to rest that night.")
            if camel_stamina < 4:
                print("Your camel lets you rest your head on its side as thanks.")
            camel_stamina = stamina_limit
            dist_from_natives += random.randint(native_min_speed, native_max_speed)

        elif prompt == "E" or prompt == "e":
            print()
            print(f"Distance traveled: {total_distance} miles")
            print(f"Water left: {canteen_fill}%")
            print(f"Camel's stamina: {camel_stamina}/{stamina_limit}")
            print(f"The natives are {-dist_from_natives} miles behind you.")

        elif prompt == "Q" or prompt == "q":
            done = True

        else:
            print()
            print("That is not a valid option.")

        if thirst > thirst_limit:
            print("You died of dehydration!")
            done = True
        elif thirst > thirst_limit - 2:
            print("You're getting thirsty.")

        if camel_stamina < 0:
            print("Your camel died of exhaustion!")
            done = True
        elif camel_stamina < 4:
            print("Your camel is tired.")

        if dist_from_natives > -1:
            print("Oh no! The natives got you!")
            done = True
        elif dist_from_natives > -11:
            print("The natives are getting close!")

        if total_distance >= 200:
            print("You made it to the end! You win!")
            done = True

    if total_distance < 200:
        print()
        print(f"Game over! The goal was {200 - total_distance} miles away!")


main()

"""
Difficulty explanations

Easy:
- You can easily outrun the natives.
- You and your camel rarely need to replenish.
- The natives are WAY slower than you.
- The natives cannot move if you're drinking.

Normal:
- You move slightly slower than you would in Easy mode.
- You and your camel need to replenish occasionally.
- The natives have are slightly slower than you.
- The natives cannot move if you're drinking.

Hard:
- You and the natives move at the same speed as each other.
- You and your camel need to replenish frequently.
- The natives can move even while you drink.
"""