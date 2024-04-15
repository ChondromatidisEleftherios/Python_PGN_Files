mport datetime
import re

import matplotlib.pyplot as ptl
import numpy as np


def count_games_in_pgn_file(file_path):
    gamecount = 0

    with open(file_path, "r") as file:  # Άνοιγμα αρχείου για ανάγνωση
        gamestarted = False
        for line in file:
            if line.strip() == "":
                if gamestarted == True:
                    gamecount += 1
                    gamestarted = False  # False μέχρι να βρεί το επόμενο [Event
            elif line.startswith(
                "[Event"
            ):  # Αν αρχίζει με [Event, σημαίνει πως έχουμε νέο παιχνίδι
                gamestarted = True

    return gamecount


def read_pgn_file(file_path):
    pgnc = ""
    with open(file_path, "r") as file:
        pgnc = file.read()
    games = count_games_in_pgn_file(file_path)  # Για να μετρήσει τα συνολικά παιχνίδια
    return games, pgnc


if __name__ == "__main__":
    plm = 0  # Τα αρχικοποιώ όλα με 0 ώστε να μην εμφανίσει κάποιο σφάλμα κατά την εκτέλεση
    plt = 0
    plw = 0
    plT = 0
    plf = 0
    pls = 0
    plS = 0
    apf = []
    games, pgnc = read_pgn_file("RetiKIA.pgn")
    ap = re.findall(
        r'\[Date "(?P<result>.+)"', pgnc
    )  # Κανονική Έκφραση για να βρεθούν όλες οι ημερομηνίες του αρχείου
    for x in range(games):
        if not (
            ("?" in ap[x])  # Αν βρεί ερωτηματικό στην ημερομηνία
            or ("1999.09.31" in ap[x])  # Λάθος ημερομηνία
            or ("2000.02.31" in ap[x])  # Λάθος ημερομηνία
            or ("2011.19.11" in ap[x])  # Λάθος ημερομηνία
            or ("`" in ap[x])  # Μια ημερομηνία είχε τον χαρακτήρα ` μέσα της#
        ):
            apf.insert(x, ap[x])
    for x in range(len(apf)):
        a = datetime.datetime.strptime(str(apf[x]), "%Y.%m.%d").strftime(
            "%A"
        )  # %Y = Χρονολογία με 4 ψηφια, %m= μήνας με 2 ψηφία, %d= ημέρα με 2 ψηφία, %A= ημέρα ολογράφος
        if a == "Monday":
            plm = plm + 1
        if a == "Tuesday":
            plt = plt + 1
        if a == "Wednesday":
            plw = plw + 1
        if a == "Thursday":
            plT = plT + 1
        if a == "Friday":
            plf = plf + 1
        if a == "Saturday":
            pls = pls + 1
        if a == "Sunday":
            plS = plS + 1
    ptl.style.use(
        "fivethirtyeight"
    )  # Ρύθμιση στυλ για ευκολότερη ανάγνωση του γραφήματος
    games = [plm, plt, plw, plT, plf, pls, plS]
    day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    ptl.bar(day, games, color="black", label="All Games Played")
    ptl.legend()
    ptl.xlabel("Days")
    ptl.ylabel("Games")
    ptl.title("Chess Games Played Throughout The Week")
    ptl.show()
