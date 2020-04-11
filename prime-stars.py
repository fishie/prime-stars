from math import pi, sqrt
from itertools import combinations
from collections import defaultdict
import matplotlib.pyplot as matplot

class Coordinates:
    def __init__(self, angles, lengths):
        self.angles = angles
        self.lengths = lengths

def complete_circle(*arguments):
    for argument in arguments:
        argument.append(argument[0])

def angles(n):
    return [x*2*pi/n for x in range(1 + int(n/4), 1 + int(n*5/4))]

def read_sequence(filename):
    sequence = []
    for line in open(filename):
        stripped = line.strip()
        if stripped != '':
            sequence.append(int(stripped))
    return sequence

def plot_duplicates(*arguments):
    duplicate_counts = defaultdict(int)

    for pair in combinations(arguments, 2):
        angles1 = [round(x, 10) for x in pair[0].angles]
        angles2 = [round(x, 10) for x in pair[1].angles]
        zip1 = zip(angles1, pair[0].lengths)
        zip2 = zip(angles2, pair[1].lengths)
        for duplicate in set(zip1).intersection(zip2):
            duplicate_counts[duplicate] += 1

    count_duplicates = defaultdict(list)
    for duplicate, count in duplicate_counts.items():
        count_duplicates[count].append(duplicate)

    for count, duplicates in count_duplicates.items():
        print(count, duplicates)
        matplot.polar([x[0] for x in duplicates], [x[1] for x in duplicates], 'ko', markersize=4+count)


one = Coordinates([pi/2], [1])
two = Coordinates([pi/2], [2]) # (2-1)
three = Coordinates([pi/2, -pi/2], [2, 4]) # (2-1)(3-1)

# (2-1)(3-1)(5-1)
five = Coordinates(angles(8), [6, 4, 2, 4, 2, 4, 6, 2])
complete_circle(five.angles, five.lengths)

# (2-1)(3-1)(5-1)(7-1)
seven = Coordinates(angles(48), [10, 2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6, 4, 2, 6, 4, 6, 8, 4, 2, 4, 2, 4, 8, 6, 4, 6, 2, 4, 6, 2, 6, 6, 4, 2, 4, 6, 2, 6, 4, 2, 4, 2, 10, 2])
complete_circle(seven.angles, seven.lengths)

# (2-1)(3-1)(5-1)(7-1)(11-1)
eleven = Coordinates(angles(480), [12, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6, 4, 2, 6, 4, 6, 8, 4, 2, 4, 2, 4, 14, 4, 6, 2, 10, 2, 6, 6, 4, 2, 4, 6, 2, 10, 2, 4, 2, 12, 10, 2, 4, 2, 4, 6, 2, 6, 4, 6, 6, 6, 2, 6, 4, 2, 6, 4, 6, 8, 4, 2, 4, 6, 8, 6, 10, 2, 4, 6, 2, 6, 6, 4, 2, 4, 6, 2, 6, 4, 2, 6, 10, 2, 10, 2, 4, 2, 4, 6, 8, 4, 2, 4, 12, 2, 6, 4, 2, 6, 4, 6, 12, 2, 4, 2, 4, 8, 6, 4, 6, 2, 4, 6, 2, 6, 10, 2, 4, 6, 2, 6, 4, 2, 4, 2, 10, 2, 10, 2, 4, 6, 6, 2, 6, 6, 4, 6, 6, 2, 6, 4, 2, 6, 4, 6, 8, 4, 2, 6, 4, 8, 6, 4, 6, 2, 4, 6, 8, 6, 4, 2, 10, 2, 6, 4, 2, 4, 2, 10, 2, 10, 2, 4, 2, 4, 8, 6, 4, 2, 4, 6, 6, 2, 6, 4, 8, 4, 6, 8, 4, 2, 4, 2, 4, 8, 6, 4, 6, 6, 6, 2, 6, 6, 4, 2, 4, 6, 2, 6, 4, 2, 4, 2, 10, 2, 10, 2, 6, 4, 6, 2, 6, 4, 2, 4, 6, 6, 8, 4, 2, 6, 10, 8, 4, 2, 4, 2, 4, 8, 10, 6, 2, 4, 8, 6, 6, 4, 2, 4, 6, 2, 6, 4, 6, 2, 10, 2, 10, 2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6, 6, 6, 4, 6, 8, 4, 2, 4, 2, 4, 8, 6, 4, 8, 4, 6, 2, 6, 6, 4, 2, 4, 6, 8, 4, 2, 4, 2, 10, 2, 10, 2, 4, 2, 4, 6, 2, 10, 2, 4, 6, 8, 6, 4, 2, 6, 4, 6, 8, 4, 6, 2, 4, 8, 6, 4, 6, 2, 4, 6, 2, 6, 6, 4, 6, 6, 2, 6, 6, 4, 2, 10, 2, 10, 2, 4, 2, 4, 6, 2, 6, 4, 2, 10, 6, 2, 6, 4, 2, 6, 4, 6, 8, 4, 2, 4, 2, 12, 6, 4, 6, 2, 4, 6, 2, 12, 4, 2, 4, 8, 6, 4, 2, 4, 2, 10, 2, 10, 6, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6, 4, 2, 10, 6, 8, 6, 4, 2, 4, 8, 6, 4, 6, 2, 4, 6, 2, 6, 6, 6, 4, 6, 2, 6, 4, 2, 4, 2, 10, 12, 2, 4, 2, 10, 2, 6, 4, 2, 4, 6, 6, 2, 10, 2, 6, 4, 14, 4, 2, 4, 2, 4, 8, 6, 4, 6, 2, 4, 6, 2, 6, 6, 4, 2, 4, 6, 2, 6, 4, 2, 4, 12, 2])
complete_circle(eleven.angles, eleven.lengths)

# (2-1)(3-1)(5-1)(7-1)(11-1)(13-1)
thirteen = Coordinates(angles(5760), read_sequence('13'))
complete_circle(thirteen.angles, thirteen.lengths)

matplot.polar(one.angles, one.lengths, 'ko', markersize=1, color='#888888')
matplot.polar(two.angles, two.lengths, 'ko', markersize=1, color='#888888')
matplot.polar(three.angles, three.lengths, 'ko', markersize=1, color='#888888')
matplot.polar(five.angles, five.lengths, 'ko', markersize=1, color='#888888')
matplot.polar(seven.angles, seven.lengths, 'ko', markersize=1, color='#888888')
matplot.polar(eleven.angles, eleven.lengths, 'ko', markersize=1, color='#888888')
matplot.polar(thirteen.angles, thirteen.lengths, 'ko', markersize=1, color='#888888')

plot_duplicates(one, two, three, five, seven, eleven, thirteen)

matplot.thetagrids([])
matplot.rgrids(())
matplot.gca(projection='polar').spines['polar'].set_visible(False)
matplot.subplots_adjust(bottom=0, top=1)
matplot.show()
