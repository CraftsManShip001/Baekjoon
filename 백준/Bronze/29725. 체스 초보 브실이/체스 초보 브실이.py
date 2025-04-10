chess={'P':1, 'p':-1, 'N':3, 'n':-3, 'B':3, 'b':-3, 'R':5, 'r':-5, 'Q':9, 'q':-9}
piece=[]
for _ in range(8):
    piece.extend(list(input()))
score=0
for idx,val in chess.items():
    score+=piece.count(idx)*val
print(score)