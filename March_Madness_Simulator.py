import random
import numpy as np

def coinflip():
    odds = ["heads", "tails"] 
    return random.choice(odds)

def seeding(seed1, seed2):
    heads_count = 0
    tails_count = 0
    
    if seed1 > seed2:
        higher_seed = seed1
        lower_seed = seed2
    else:
        higher_seed = seed2
        lower_seed = seed1
    
    for _ in range(higher_seed + lower_seed):
        result = coinflip()
        if result == "heads":
            heads_count += 1
            # if random.randint(1, 100) < 10: 
            # # if np.random.randn() < -1 or np.random.randn() > 1:
            #     heads_count += 1
            if heads_count == higher_seed:
                return higher_seed
        else:
            tails_count += 1
            # if np.random.rand() < .1: 
            #     tails_count += 1
            if tails_count == lower_seed:
                if random.randint(1, 100) < 14: 
                    return higher_seed
                else:
                    return lower_seed

def round_64():
    next_round = []
    for i in range(8):
        winner_seed = seeding(i + 1, 16 - i)
        next_round.append(winner_seed)
        # print("Winner is the", winner_seed, "seed.")
    return next_round
print(round_64())

def final_4(seed1, seed2):
    heads_count = 0
    tails_count = 0
    
    if seed1 > seed2:
        higher_seed = seed1
        lower_seed = seed2

    if seed1 == seed2: 
        higher_seed = seed1
        lower_seed = seed2
       
    
    else:
        higher_seed = seed2
        lower_seed = seed1
        

    
    for _ in range(higher_seed + lower_seed):
        result = coinflip()
        if result == "heads":
            heads_count += 1
            # if random.randint(1, 100) < 10: 
            # # if np.random.randn() < -1 or np.random.randn() > 1:
            #     heads_count += 1
            if heads_count == higher_seed:
                if lower_seed == higher_seed :
                    print("Left side won ", seed1)
                    return higher_seed
                else:
                    return higher_seed
        else:
            tails_count += 1
            # if np.random.rand() < .1: 
            #     tails_count += 1
            if tails_count == lower_seed:
                  if tails_count == lower_seed:
                    if lower_seed == higher_seed :
                        print("Right side won ", seed1)
                        return lower_seed
                    elif random.randint(1, 100) < 14:
                        return higher_seed
                    else:
                        return lower_seed

def final_2(seed_l, seed_r):    
    result = coinflip()
    if result == "heads":
        # heads_count += 1
        # if random.randint(1, 100) < 10: 
        # # if np.random.randn() < -1 or np.random.randn() > 1:
        #     heads_count += 1
        # if heads_count == seed_l:
        print("Winner is right side: ", seed_r)
    else:
        # tails_count += 1
        # if np.random.rand() < .1: 
        #     tails_count += 1
        # if tails_count == seed_r:
        print("Winner is left side: ", seed_l)
        

# def round_32():
#     current_round = round_64()
#     next_round = []
#     for i in range(int(len(current_round) / 2)):
#         winner_seed = seeding(current_round[i], current_round[len(current_round) - i - 1])
#         next_round.append(winner_seed)
#         print("Winner is the", winner_seed, "seed.")
#     return next_round

def round(last_round):
    current_round = last_round
    next_round = []
    for i in range(int(len(current_round) / 2)):
        winner_seed = seeding(current_round[i], current_round[len(current_round) - i - 1])
        next_round.append(winner_seed)
        # print("Winner is the", winner_seed, "seed.")
    return next_round

def bracket():
    east = []
    south =[]
    west = []
    midwest = []

    east = round_64()
    south = round_64()
    west = round_64()
    midwest = round_64()

    print("Round of 64 results: ")
    print("East: ",east)
    print("South: ",south)
    print("West: ",west)
    print("Midwest: ",midwest)
    print("")

    east = round(east)
    south = round(south)
    west = round(west)
    midwest = round(midwest)

    print("Round of 32 results: ")
    print("East: ",east)
    print("South: ",south)
    print("West: ",west)
    print("Midwest: ",midwest)
    print("")

    east = round(east)
    south = round(south)
    west = round(west)
    midwest = round(midwest)
    
    print("Round of 16 results: ")
    print("East: ",east)
    print("South: ",south)
    print("West: ",west)
    print("Midwest: ",midwest)
    print("")

    east = round(east)
    south = round(south)
    west = round(west)
    midwest = round(midwest)

    print("Round of 8 results: ")
    print("East: ",east)
    print("South: ",south)
    print("West: ",west)
    print("Midwest: ",midwest)
    print("")

    # east = round(east)
    # south = round(south)
    # west = round(west)
    # midwest = round(midwest)

    print("Final 2: ")
    winner_l = final_4(east[0],west[0])
    winner_r = final_4(south[0],midwest[0])
    print("Winner of Left Side: ", winner_l)
    print("Winner of Right Side: ", winner_r)
    print("")

    print("National Champ: ")
    winner = final_4(winner_l,winner_r)
    print("The National Champ ", winner)



    # print("Final : ")
    # seeding(east[0],west[0])
    # seeding(south[0],midwest[0])

    # print("Round of 2 results: ")
    # print("East: ",east)
    # print("South: ",south)
    # print("West: ",west)
    # print("Midwest: ",midwest())

bracket()

# print("Round of 64 results: ")
# print("East: ",round_64())
# print("South: ",round_64())
# print("West: ",round_64())
# print("Midwest: ",round_64())

#Round of 64 results
# East =  [1, 2, 3, 4, 5, 11, 10, 8]
# South =  [1, 2, 3, 4, 5, 6, 7, 9]
# West =  [1, 2, 3, 4, 5, 6, 7, 8]
# Midwest =  [1, 2, 3, 4, 5, 6, 7, 8]

# #Round of 32 results
# East=  [1, 2, 3, 4]
# South= [1, 7, 3, 4]
# West=  [1, 2, 3, 5]
# Midwest=  [1, 2, 3, 5]

# #Round of 16 results
# East=  [1, 3]
# South=  [1, 3]
# West=  [1, 2]
# Midwest=  [1, 2]

# print("East: ",round(East))
# print("South: ",round(South))
# print("West: ",round(West))
# print("Midwest: ",round(Midwest))

