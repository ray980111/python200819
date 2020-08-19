score = []
maxscore = 0
minscore = 100
toal = 0

for i in range(5):
    n = int(input(score))
    score.append(n)
    if n > maxscore:
        maxscore = n
    if n > minscore:
        minscore = n
    total = total + n
        
s = total/len(score)
print('total',total)
print('even',s
print('hiest',maxscore)
print('loest',minscore)