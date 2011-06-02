'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
'''
import string
def read_file(name='./names.txt'):
    f = open(name)
    return f.readline()

def get_scoring_table():
    score = 1
    score_dict = {}
    for letter in string.uppercase:
        score_dict[letter] = score
        score += 1
    
    return score_dict
if __name__ =="__main__":

    score_table = get_scoring_table()
    names = map(lambda x: x[1:-1], read_file().split(','))
    names.sort()
    scores = []
    for i in range(len(names)):
        scores.append(sum([score_table[c] for c in names[i]]) * (i+1))
    print sum(scores)
