heighest_score = 100

def update_highscore(scores):
    global heighest_score
    s = sum(scores)
    if s > heighest_score:
        heighest_score = s

update_highscore([50,100,150])
assert heighest_score == 300
