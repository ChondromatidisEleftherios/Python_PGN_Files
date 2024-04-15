import sys

import my_re_functions as rf

if __name__ == "__main__":
    text = []
    with open(sys.argv[1], "r") as my_file: #Ανοίγει το αρχείο που βρίσκετε στη 1η θέση της λίστας (μετράει το ίδιο το πρόγραμμα σαν 1 θεση)
        text = my_file.read() #Διάβασμα Αρχείου
        wins = []
        dates = []
        elo = []
        moves = []
        wins = rf.winner(text)
        dates = rf.date_of_game(text)
        elo = rf.diff_elo(text)
        moves = rf.moves(text)
        print(wins)
        print(dates)
        print(elo)
        print(moves)
    my_file.close() 
