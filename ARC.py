Team1=input("enter a team name : ")
Team2=input("enter 2 team name : ")
Team1_member1,Team1_member2,Team2_member1,Team2_member2=input('first team enter first member name : '),input('first team enter second member name : '),input('second team enter first member name : '),input('second team enter second member name : ')
team1_score=team2_score=a1=b1=a2=b2=0
score={'a':5,'b':4,'c':3,'d':2,'e':1,'f':0}
for i in range(1,4):
    s1,s2,s3,s4=input('team 1 player 1 score : '),input('team 1 player 2 score : '),input('team 2 player 1 scored : '),input('team 2 player 2 scored : ')
    if s1==s2 and s1!='f':
        team1_score=team1_score+2
    if s3==s4 and s3!='f':
        team2_score=team2_score+2
    team1_score=score[s1]+score[s2]+team1_score
    team2_score=score[s3]+score[s4]+team2_score
    a1+=score[s1]
    b1+=score[s2]
    a2+=score[s3]
    b2+=score[s4]
    print(i,'is over')
    print('the first team scored',team1_score)
    print('the second team scored',team2_score)
if team1_score>team2_score:
    print(Team1,'is the winner')
elif team1_score==team2_score:
    print('The game is tied')
else:
    print(Team2,'is the winner')
print('The scores are\n',Team1,'scored',team1_score,'\n',Team1_member1,'scored',a1,'\n',Team1_member2,'scored',b1,'\n',Team2,'scored',team2_score,'\n',Team2_member1,'scored',a2,'\n',Team2_member2,'scored',b2)