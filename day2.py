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

input_file = "./data/day2.txt"

class part1:
    @staticmethod
    def answer():
        sum_of_ids = 0
        total_cubes = {'red':12,
                       'green':13,
                       'blue':14}
        with open(input_file) as f:
            for line in f:
                good = True
                game_number = int(line.split(':')[0].split()[1])
                grab = [s.lstrip().rstrip() for s in line.split(':')[1].split(';')]
                for pull in grab:
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
    @staticmethod
    def answer():
        cv_sum = 0
        num_match = [('one', '1'),
                     ('two', '2'),
                     ('three', '3'),
                     ('four', '4'),
                     ('five', '5'),
                     ('six', '6'),
                     ('seven', '7'),
                     ('eight', '8'),
                     ('nine', '9')]
        with open('./data/day1.txt') as f:
            for line in f:
                for i in range(len(line)):
                    s = ''
                    if line[i].isdigit():
                        s = line[i]
                        break
                    else:
                        for num in num_match:
                            if line[i:i+len(num[0])] == num[0]:
                                s = num[1]
                                break
                        else:
                            continue
                        break

                for i, c in reversed(list(enumerate(line))):
                    if c.isdigit():
                        s += c
                        break
                    else:
                        for num in num_match:
                            if line[i-len(num[0]):i] == num[0]:
                                s += num[1]
                                break
                        else:
                            continue
                        break
                cv_sum += int(s)
            return cv_sum

def findnum(line):
    s = ""
    for _, c in enumerate(line):
        if c.isdigit():
            s = c
            break
    for _, c in reversed(list(enumerate(line))):
        if c.isdigit():
            s += c
            break
    return int(s)