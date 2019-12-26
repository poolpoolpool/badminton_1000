#Byron Jones   bjone079@uottawa.ca
#This program is for organising badminton games.
#The badminton club I will use it for is doubles play, with 4 available courts.

import random
from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as tkscrolled


class Player:


    def __init__(self, name = 'Guest', group = 2, games = 0):        #rating currently not in use

        self.name = name

        self.group = group

        self.games = games
    
    def __repr__(self):
        
        return str(self.name)# + ":" + str(self.group) + ":" + str(self.games)

    def __eq__(self, o):
        
        return self.name == o.name and self.group == o.group
    

class Badminton:

    def __init__(self, master):
        
        mainframe = Frame(master)
        mainframe.grid(padx = 5, pady = 5)
        
        
        self.add_button = Button(mainframe, text = "Add Player", command=self.add_player)
        self.add_button.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = W)

        self.remove_button = Button(mainframe, text = "Remove Player", command = self.remove_player)
        self.remove_button.grid(row = 1, column = 1, padx = 5, pady = 5)

        self.new_game_button = Button(mainframe, text = "New Game", command = self.new_game)
        self.new_game_button.grid(row = 0, rowspan = 2, column = 2, columnspan = 2, padx = 5, pady = 5)

        self.new_game_button.focus()
        self.new_game_button.bind("<Return>", self.new_game)
        
        self.game_display = tkscrolled.ScrolledText(mainframe, undo = True, width = 40, height = 32)
        self.game_display.grid(row = 0, rowspan = 2, column = 4, columnspan = 2)


        add_frame = Frame(mainframe)
        add_frame.grid(row = 0, column = 0)
        
        self.add_listbox = Listbox(add_frame, height = 16)
        self.add_scrollbar = Scrollbar(add_frame, orient = VERTICAL)
        self.add_listbox.config(yscrollcommand = self.add_scrollbar.set)
        self.add_scrollbar.config(command = self.add_listbox.yview)

        self.add_listbox.bind("<Double-Button-1>", self.add_player)

        self.add_scrollbar.pack(side = RIGHT, fill = Y)
        self.add_listbox.pack()
        

        remove_frame = Frame(mainframe)
        remove_frame.grid(row = 1, column = 0)

        self.remove_listbox = Listbox(remove_frame, height=16)
        self.remove_scrollbar = Scrollbar(remove_frame, orient = VERTICAL)
        self.remove_listbox.config(yscrollcommand = self.remove_scrollbar.set)
        self.remove_scrollbar.config(command = self.remove_listbox.yview)

        self.remove_listbox.bind("<Double-Button-1>", self.remove_player)
        
        self.remove_scrollbar.pack(side = RIGHT, fill = Y)
        self.remove_listbox.pack()

        self.current = None

        for member in add_list:
            self.add_listbox.insert(END, member)

        for player in sorted(player_strlist):
            self.remove_listbox.insert(END, player)


        self.player_strlist = player_strlist

        self.member_strlist = member_strlist

        self.add_list = add_list

        self.member_list = member_list

        self.player_list = player_list
        
    def new_game(self, *args):

        random.shuffle(player_list)                         #shuffle list to randomise play
    
        player_list.sort(key=lambda x: x.games)             #sort from fewest games played to most
    
        orgfield = []                                       #temp list for new game
        total[0] += 1

        game_text = str('\nGames played = ' + str(total[0]) + '\n\n\n')
        
        #print('\n Games played = '+ str(total[0]))
        
        i = 0

        while i < 16:
        
            player_list[i].games = player_list[i].games + 1     #Increase the games played by those playing next round by 1
            orgfield.append(player_list[i])                     #Add those players to temp list for new game
            if i == len(player_list) -1:
                break
            i += 1

    
        orgfield.sort(key=lambda x: x.group)                #sort temp list by skill group

        b=0                                                 #index for courts
        print('')
    
        for i in orgfield:                                  #go through temp list of players and print names and court placement

            game_text = game_text + str(i) + '\n'
            b=b+1

            if (b % 4) == 0:                                #Court number

                game_text = game_text + '\nCOURT: ' + str(b // 4) + '\n\n'

        game_text = game_text + '----------------------------------------'
        self.game_display.insert(1.0, str(game_text))
        orgfield = []                                       #clear temp list

        self.new_game_button.focus()

    def remove_player(self, *args):

        player = self.remove_listbox.curselection()

        if player == ():
            return
        
        for person in player_list:
            if str(person.name) == str(self.player_strlist[player[0]]):
                player_list.remove(person)

        self.player_strlist = []

        for player in player_list:
            self.player_strlist.append(player.name)

        self.player_strlist = sorted(self.player_strlist)
        self.remove_listbox.delete('0', 'end')
        
        for player in sorted(self.player_strlist):
            self.remove_listbox.insert(END, player)

        self.add_list = []

        self.add_list = sorted(list(set(self.member_strlist).difference(set(self.player_strlist))))

        self.add_listbox.delete('0', 'end')

        for member in self.add_list:
            self.add_listbox.insert(END, member)

        self.new_game_button.focus()
            
    def add_player(self, *args):

        player = self.add_listbox.curselection()

        if player == ():
            return
        
        for person in member_list:
            if str(person.name) == str(self.add_list[player[0]]):
                person.games = self.player_list[len(player_list) // 2].games 
                player_list.append(person)
                break
        
        self.player_strlist = []

        for player in player_list:
            self.player_strlist.append(player.name)

        self.player_strlist = sorted(self.player_strlist)
        self.remove_listbox.delete('0', 'end')
        
        for player in sorted(self.player_strlist):
            self.remove_listbox.insert(END, player)

        self.add_list = []

        self.add_list = sorted(list(set(self.member_strlist).difference(set(self.player_strlist))))

        self.add_listbox.delete('0', 'end')

        for member in self.add_list:
            self.add_listbox.insert(END, member)

        self.new_game_button.focus()

        

   
"-------------------------------------------------------------------------------------------------------------------------"
#This area is for creating the player list, and member_list.
#The member list has all the members in the club, and drop-in slots
#The player list has all the players who will be selected in
#the new game. It might make sense to not append members to the player list
#if they rarely show up.


member_list = []

player_list = []

total = [0]


Byron_Jones = Player('Byron Jones', 3)
member_list.append(Byron_Jones)
player_list.append(Byron_Jones)

Angus_Young = Player('Angus Young', 2)
member_list.append(Angus_Young)
player_list.append(Angus_Young)

Nicholas_Lee = Player('Nicholas Lee', 2)
member_list.append(Nicholas_Lee)
player_list.append(Nicholas_Lee)

Justin_Micheals = Player('Justin Micheals', 2)
member_list.append(Justin_Micheals)
player_list.append(Justin_Micheals)

Phanisri_Mudunuri = Player('Phanisri Mudunuri', 3)
member_list.append(Phanisri_Mudunuri)
player_list.append(Phanisri_Mudunuri)

Cassandra_Cheng = Player('Cassandra Cheng', 2)
member_list.append(Cassandra_Cheng)
player_list.append(Cassandra_Cheng)

Prisha = Player('Prisha', 4)
member_list.append(Prisha)
player_list.append(Prisha)
    
Fiorelli_Lagdamen = Player('Fiorelli Lagdamen', 2)
member_list.append(Fiorelli_Lagdamen)
player_list.append(Fiorelli_Lagdamen)
    
Michael_Chainiere = Player('Micheal Chainiere', 3)
member_list.append(Michael_Chainiere)
player_list.append(Michael_Chainiere)
    
Danica_Plourde = Player('Danica Plourde', 3)
member_list.append(Danica_Plourde)
player_list.append(Danica_Plourde)
    
Tonia_Kong = Player('Tonia Kong', 3)
member_list.append(Tonia_Kong)
player_list.append(Tonia_Kong)
    
Sean_H = Player('Sean H', 3)
member_list.append(Sean_H)
player_list.append(Sean_H)
    
Natania_Ng = Player('Natania Ng', 2)
member_list.append(Natania_Ng)
player_list.append(Natania_Ng)
    
Josephine_Ng = Player('Josephine Ng', 2)
member_list.append(Josephine_Ng)
player_list.append(Josephine_Ng)
    
Kevin_Lu = Player('Kevin Lu', 4)
member_list.append(Kevin_Lu)
player_list.append(Kevin_Lu)
    
Yunji_Chung = Player('Yunji Chung', 1)
member_list.append(Yunji_Chung)
player_list.append(Yunji_Chung)
    
Chandler_Wong = Player('Chandler Wong', 2)
member_list.append(Chandler_Wong)
player_list.append(Chandler_Wong)
    
Enrick_Rainville = Player('Enrick Rainville', 3)
member_list.append(Enrick_Rainville)
player_list.append(Enrick_Rainville)

Francois_Rioux = Player('Francois Rioux', 3)
member_list.append(Francois_Rioux)
player_list.append(Francois_Rioux)

Melissa_Beland = Player('Melissa Beland', 3)
member_list.append(Melissa_Beland)
player_list.append(Melissa_Beland)

Fred_Zhang = Player('Fred Zhang', 3)
member_list.append(Fred_Zhang)
player_list.append(Fred_Zhang)

Ethan_Li = Player('Ethan Li', 3)
member_list.append(Ethan_Li)
player_list.append(Ethan_Li)

Andy_Lou = Player('Andy Lou', 2)
member_list.append(Andy_Lou)
player_list.append(Andy_Lou)

Emerald = Player('Emerald', 1)
member_list.append(Emerald)
player_list.append(Emerald)

Nicholas_Gauthier = Player('Nicholas Gauthier', 2)
member_list.append(Nicholas_Gauthier)
player_list.append(Nicholas_Gauthier)



drop_in_1 = Player('drop_in_1', 1)
member_list.append(drop_in_1)
#player_list.append(drop_in_1)

drop_in_2 = Player('drop_in_2', 1)
member_list.append(drop_in_2)
#player_list.append(drop_in_2)

drop_in_3 = Player('drop_in_3', 2)
member_list.append(drop_in_3)
#player_list.append(drop_in_3)

drop_in_4 = Player('drop_in_4', 2)
member_list.append(drop_in_4)
#player_list.append(drop_in_4)

drop_in_5 = Player('drop_in_5', 3)
member_list.append(drop_in_5)
#player_list.append(drop_in_5)

drop_in_6 = Player('drop_in_6', 3)
member_list.append(drop_in_6)
#player_list.append(drop_in_6)


"--------------------------------------------------------------------------------------------------------------------------"
member_strlist = []

player_strlist = []

for member in member_list:
    member_strlist.append(member.name)

for player in player_list:
    player_strlist.append(player.name)

#print(player_strlist)

add_list = sorted(list(set(member_strlist).difference(set(player_strlist))))

add_list = list(sorted(add_list))

player_strlist = sorted(player_strlist)

#print(player_strlist)
"-------------------------------------------------------------------------------------------"

root = Tk()
root.title("Badminton 1000")
b = Badminton(root)
root.mainloop
