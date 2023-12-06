class part1:
    @staticmethod
    def answer():
        cv_sum = 0
        with open('./data/day1.txt') as f:
            for line in f:
                cv = findnum(line) #calibration value
                cv_sum += cv
        return cv_sum

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