#     _       _                 _            __
#    / \   __| |_   _____ _ __ | |_    ___  / _|
#   / _ \ / _` \ \ / / _ \ '_ \| __|  / _ \| |_
#  / ___ \ (_| |\ V /  __/ | | | |_  | (_) |  _|
# /_/___\_\__,_| \_/ \___|_|_|_|\__|  \___/|_|___
#  / ___|___   __| | ___  |  _ \  __ _ _   _|___ \
# | |   / _ \ / _` |/ _ \ | | | |/ _` | | | | __) |
# | |__| (_) | (_| |  __/ | |_| | (_| | |_| |/ __/
#  \____\___/ \__,_|\___| |____/ \__,_|\__, |_____|
#                                      |___/

#  ____            _     _
# |  _ \ __ _ _ __| |_  / |
# | |_) / _` | '__| __| | |
# |  __/ (_| | |  | |_  | |
# |_|   \__,_|_|   \__| |_|



class part1:
    input_file = "./data/day2.txt"

    @staticmethod
    def answer():
        sum_of_ids = 0
        total_cubes = {'red':12,
                       'green':13,
                       'blue':14}
        with open(part1.input_file) as f:
            for line in f:
                game_number = int(line.split(':')[0].split()[1])
                game = [s.lstrip().rstrip() for s in line.split(':')[1].split(';')]
                for pull in game:
                    # go over each pull and make sure all the colors don't
                    # contain too many balls of any color
                    pull = [x.lstrip() for x in list(pull.split(','))]
                    for ind in pull:
                        val, key = ind.split()
                        val = int(val)
                        if val > total_cubes[key]:
                            break;
                    else:
                        continue
                    break
                else:
                    sum_of_ids += game_number
                    continue
        return sum_of_ids


#  ____            _     ____
# |  _ \ __ _ _ __| |_  |___ \
# | |_) / _` | '__| __|   __) |
# |  __/ (_| | |  | |_   / __/
# |_|   \__,_|_|   \__| |_____|
class part2:
    input_file = "./data/day2.txt"

    @staticmethod
    def answer():
        sum_of_powers = 0
        with open(part2.input_file) as f:
            for line in f:
                # Each line is a "game"
                # game_number = int(line.split(':')[0].split()[1])
                max = {}
                game = [s.lstrip().rstrip() for s in line.split(':')[1].split(';')]
                for pull in game:
                    # for each pull in a game keep track of the maximum of each
                    # color ball
                    pull = [x.lstrip() for x in list(pull.split(','))]
                    for ind in pull:
                        val, key = ind.split()
                        val = int(val)
                        if key not in max:
                            max[key] = val
                        elif max[key] < val:
                            max[key] = val
                power = 1
                for key in max.keys():
                    power *= max[key]
                sum_of_powers += power
        return sum_of_powers
