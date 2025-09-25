'''
Serena Williams 	Tennis 	23 Grand Slams
Lionel Messi 	Soccer 	7 Ballon d'Ors
Michael Phelps 	Swimming 	23 Gold Medals
Usain Bolt 	Athletics 	8 Gold Medals
Roger Federer 	Tennis 	20 Grand Slams
Cristiano Ronaldo 	Soccer 	5 Ballon d'Ors
'''
player_dict={"player":["Serena Williams","Lionel Messi","Michael Phelps","Usain Bolt","Roger Federer","Cristiano Ronaldo"] ,
             "sport":["Tennis","Soccer","Swimming","Athletics","Tennis","Soccer"],
             "achiements":["23 Grand Slams","7 Ballon d'Ors","23 Gold Medals","8 Gold Medals","20 Grand Slams","5 Ballon d'Ors"]}
#print(player_dict)
sports=[]
sports=player_dict.get("sport")
sp_ind=[]
print(len(sports))
for i in range(len(sports)):
    if sports[i]=="Tennis":
        sp_ind.append(i)
    else:
        continue
print(sp_ind)
x=None
ach=player_dict.get("achiements")
for i in len(ach):
    if int(ach[sp_ind[i]].split()[0]) == 20:
        x=
print(int(ach[sp_ind[0]].split()[0]))
print(int(ach[sp_ind[1]].split()[0]))
#print(f"Sport={player_dict.get("sport")}={player_dict.get("sport").index}")
""" print(if "Tennis" in player_dict.get("sport"))
for i in player_dict.get("sport").index:
    if i=="Tennis":
        sports
    sports
if "Tennis" in sports: """
