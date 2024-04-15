import re
import string


def winner(a_pgn_game):
    p = []
    ap = re.findall(
        r'\[Result "(?P<result>.+)"', a_pgn_game
    )  # Βρίσκει και βάζει σε λίστα όλα τα αποτελέσματα από τους αγώνες
    for x in range(len(ap)):
        if ap[x] == "1/2-1/2":
            p.append("ΙΣΟΠΑΛΙΑ")
        elif ap[x] == "0-1":
            p.append("ΜΑΥΡΑ")
        elif ap[x] == "1-0":
            p.append("ΛΕΥΚΑ")
    if len(p) == 1:  # Αν η λίστα έχει μόνο ένα στοιχείο μέσα
        win = p[0]
        return win  # Επέστρεψε το κατευθείαν (για να φαίνεται πιο καθαρό αν το κάνουμε print)
    else:
        return p


def date_of_game(a_pgn_game):
    p = []
    parts = []
    ap = re.findall(
        r'\[Date "(?P<result>.+)"', a_pgn_game
    )  # Βρίσκει και βάζει σε λίστα ολες τις ημερομηνίες των αγώνων
    for x in range(len(ap)):
        parts = ap[x].split(".")  # Σπάει σε κομμάτια την ημερομηνία όποτε συναντάει .
        f = (
            parts[2] + "-" + parts[1] + "-" + parts[0]
        )  # Αλλάζω τη σειρά της ημερομηνίας
        p.append(f)
    if len(p) == 1:
        date = p[0]
        return date
    else:
        return p


def diff_elo(a_pgn_game):
    p = []
    ap1 = re.findall(
        r'\[WhiteElo "(?P<result>.+)"', a_pgn_game
    )  # Βρίσκει και βάζει σε λίστα όλα τα Elo ranks των λευκών
    ap2 = re.findall(
        r'\[BlackElo "(?P<result>.+)"', a_pgn_game
    )  # Βρίσκει και βάζει σε λίστα όλα τα Elo ranks των μαύρων
    for x in range(len(ap1)):
        p.append(
            abs(int(ap1[x]) - int(ap2[x]))
        )  # Αφαίρεση της δυναμικότητας του λευκού από του μαύρου σε απόλυτη τιμή
    if len(p) == 1:
        elo = p[0]
        return elo
    else:
        return p


def moves(a_pgn_game):
    p = []
    pl = 0
    ap = re.findall(
        r"\d+\.\D", a_pgn_game
    )  # Βρίσκει και βάζει σε λίστα τη κάθε κίνηση του κάθε παιχνιδιού
    for x in range(len(ap)):
        if ( # Aυτό που συμβαίνει είναι πως κάθε φορά που πάμε από το ένα παιχνιδι στο άλλο ο αριθμός των κινήσεων πέφτει απο n σε 1. Άρα, θέλουμε το πλήθος των κινήσεων πριν γίνει αυτό το reset
            ap[x].startswith("1.") and x != 0
        ):  # Αν η κίνηση ξεκινάει με 1. και δεν είναι η πρώτη που εντοπίστηκε σε όλο το pgn αρχείο
            p.append(pl)
            pl = 1  # Το πλήθος γίνεται 1 αντί για 0 διότι θέλουμε να μετρήσουμε και τη πρώτη κίνηση. Αν ήταν 0, θα εμφάνιζε κάθε φορά μια κίνηση λιγότερο από το κανονικό
        else:
            pl = pl + 1
    p.append(
        pl
    )  # Αφού κάποτε το αρχείο θα τελειώσει και δε θα έχουμε ξανά reset του αριθμού κίνησης από n σε 1, βάζει στη λίστα το τελευταίο πλήθος που υπολογίστηκε
    if len(p) == 1:
        m = p[0]
        return m
    else:
        return p
