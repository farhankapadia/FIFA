import pandas as pd

fifa_15= pd.read_csv('players_15.csv')
fifa_16= pd.read_csv('players_16.csv')
fifa_17= pd.read_csv('players_17.csv')
fifa_18= pd.read_csv('players_18.csv')
fifa_19= pd.read_csv('players_19.csv')
fifa_20= pd.read_csv('players_20.csv')

cols= ['short_name', 'nationality', 'club', 'overall', 'player_positions']
#these are the columns I want to use out of the entire dataset 
combined= pd.concat([fifa_15, fifa_16, fifa_17, fifa_18, fifa_19, fifa_20])
rows= combined.shape[0]
columns= combined.shape[1]
combined.sort_values('overall', axis=0, ascending= False, inplace=True)
#for sorting dataset in decreasing order of ratings
#print(combined[cols].head(15))
l=[]
#for loop is for extracting the players' positions
#that are separated by commas
for i in combined['player_positions'].values:
    if ',' in i:
        index= i.index(',')
        i= i[0:index]
    l.append(i)
combined['player_positions']= l
print(combined[cols].head(10))
no_defend= int(input("Enter the number of defenders: "))
no_mid= int(input("Enter the number of midfielders: "))
no_forw= int(input("Enter the number of forwards: "))
nat=[]
club=[]
j=0
k=0
m=0
o=0
defend=[]
mid=[]
forw=[]
#in the dataset, all defenders have "B" as their last letter in their positions
#eg CB, LB, RB so I've looked for all players with "B" ending in their position
#same logic for choosing "M" for midfielders and "T"/"W"/"F" for strikers,
#wingers and forwards
#the if condition is the most important line of the entire code
#it tracks the different clubs a player has played for throughout his career
#(in this case from FIFA 15 -20 career) and only allows the player to enter 
#into the team if a player from those teams hasn't already been selected
#example Ibrahimovic has played for PSG, Man Utd and LA Galaxy in these games
#so if Ibra is selected then no other player from  Utd/PSG/LA can be selected
for i in range(len(combined['player_positions'].values)):
   while j != no_defend:
       if combined['player_positions'].values[i][len(combined['player_positions'].values[i])-1]=='B' and combined['nationality'].values[i] not in nat: 
           df= combined.loc[combined['long_name']==combined['long_name'].values[i]]
           if bool(set(club).intersection(df['club'].values)) == False: 
               club.extend(df['club'].values)
               defend.append(combined['short_name'].values[i])
               nat.append(combined['nationality'].values[i])
               j=j+1
               break
           else:
               break
       else:
           break
   while k != no_mid:
       if combined['player_positions'].values[i][len(combined['player_positions'].values[i])-1]=='M' and combined['nationality'].values[i] not in nat: 
           df= combined.loc[combined['long_name']==combined['long_name'].values[i]]
           if bool(set(club).intersection(df['club'].values)) == False:
               club.extend(df['club'].values)
               mid.append(combined['short_name'].values[i])
               nat.append(combined['nationality'].values[i])
               k= k+1
               break
           else:
               break
       else:
           break
   while m != no_forw:
       if (combined['player_positions'].values[i][len(combined['player_positions'].values[i])-1]=='W' or combined['player_positions'].values[i][len(combined['player_positions'].values[i])-1]=='F' or combined['player_positions'].values[i][len(combined['player_positions'].values[i])-1]=='T') and combined['nationality'].values[i] not in nat: 
           df= combined.loc[combined['long_name']==combined['long_name'].values[i]]
           if bool(set(club).intersection(df['club'].values)) == False:
               club.extend(df['club'].values)
               forw.append(combined['short_name'].values[i])
               nat.append(combined['nationality'].values[i])
               m= m+1
               break
           else:
               break
       else:
           break
   while o!= 1:
       if combined['player_positions'].values[i][len(combined['player_positions'].values[i])-1]=='K' and combined['nationality'].values[i] not in nat and combined['club'].values[i] not in club:
           gk= combined['short_name'].values[i]
           nat.append(combined['nationality'].values[i])
           club.append(combined['club'].values[i])
           o= o+1
           break
       else:
           break
       
print(gk)
print(defend)
print(mid)
print(forw)
               
            
               
           
            