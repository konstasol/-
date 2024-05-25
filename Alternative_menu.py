"""
Εναλλακτικό back up μενού για το τρέξιμο του γενετικού αλγόριθμου
σε παράθυρο idle (σε περίπτωση που δε θέλετε να χρησιμοποιήσετε το tkinter interface)
Τρέξτε το παρών αρχείο για να τρέξετε τον γενετικό αλγόριθμό σε περιβάλλον idle

"""
# Εισαγωγή της συνάρτησης γενετικός αλγόριθμος
from GENETIC_ALGORITHM_HOME_ import genetic_algortihm

print("Επιλέξτε αναπαράσταση 🧬 Δυαδική, Ακέραια ή Πραγματική")  # Επιλογές Χρήστη

# Αμυντικός για εισαγωγή αναπαράστασης
while True:
    try:
        variable_type = int(input("1(Δυαδική), 2(Ακέραια) ή 3(Πραγματική): "))  # Εισαγωγή επιλογής με αριθμούς 1,2,3
        if variable_type in [1, 2, 3]:
            break
        if variable_type < 1 or variable_type > 3:
            print("Εισάγετε 1,2, ή 3")  # Μήνυμα λάθους
    except:
        print("Λάθος τύπος δεδομένων! Ξαναπροσπαθήστε!")  # Μήνυμα λάθους

# Αμυντικός για ακρίβεια δεκαδικών
while True:
    try:
        if variable_type == 1 or variable_type == 3:  # Επιλογή ακρίβειας δεκαδικών [1-4]
            decimals = int(input("Ακρίβεια Δεκαδικών ♾️ από 1-4: "))
            if decimals == 1 or decimals == 2 or decimals == 3 or decimals == 4:
                break
            if decimals < 1 or decimals > 4:
                print("Δώστε ακέραιο στο διάστημα [1-4]")  # Μήνυμα λάθους
        else:  # default 0 για τους ακέραιους
            decimals = 0
            break
    except:
        print("Λάθος τύπος δεδομένων! Ξαναπροσπαθήστε!")  # Μήνυμα λάθους

# Αμυντικός για Πληθυσμό
while True:
    try:
        population_input = int(input("👨‍👩‍👧‍👧 Πληθυσμός: "))
        if population_input < 2:
            print("Δώστε ακέραιο μεγαλύτερο του 1!")  # Μήνυμα λάθους
        else:
            break
    except:
        print("Λάθος τύπος δεδομένων! Ξαναπροσπαθήστε!")  # Μήνυμα λάθους
# Αμυντικός για πιθανότητα διασταύρωσης
while True:
    try:
        mating_p = float(input("Δώστε πιθανότητα διαστάυρωσης 👩‍❤️‍👨 [0 - 1]: πχ 0.6: "))
        if mating_p > 1 or mating_p < 0:
            print("Δώστε πραγματικό αριθμό στο διάστημα [0-1]!")  # Μήνυμα λάθους
        else:
            break
    except:
        print("Λάθος τύπος δεδομένων! Ξαναπροσπαθήστε!")  # Μήνυμα λάθους
# Αμυντικός για πιθανότητα μετάλλαξης
while True:
    try:
        mutation_p = float(input("Δώστε πιθανότητα μετάλλαξης 👽 [0 - 0.1]- Βέλτιστες τιμες (0-0.05): "))
        if mutation_p > 0.1 or mating_p < 0:
            print("Δώστε πραγματικό αριθμό στο διάστημα [0-0.1]!")  # Μήνυμα λάθους
        else:
            break
    except:
        print("Λάθος τύπος δεδομένων! Ξαναπροσπαθήστε!")  # Μήνυμα λάθους

generations_in = genetic_algortihm(variable_type, decimals, population_input, mating_p, mutation_p)
# Κλήση της συνάρτησησς genetic_algorithm με ορίσματα τις επιλογές του χρήστη
# Αποθήκευση σε λίστα της επιστρεφόμενης λίστας με το βέλτιστο μέλος κάθε γενιάς

# Εκτύπωση των βέλτιστων μελών και του κορυφαίου σκορ κάθε γενιάς
print("ΑΠΟΤΕΛΕΣΜΑΤΑ: \n")
for gen in generations_in:
    print(f"ΓΕΝΙΑ {gen[0]} : ΚΑΛΥΤΕΡΟ ΑΠΟΤΕΛΕΣΜΑ: {gen[2]:.{decimals}f}, ΑΤΟΜΟ: {gen[1]}")

max_score = max(generations_in, key=lambda x: x[2])  # εύρεση του ολικού μέγιστου όλων των γενιών

# ψάχνουμε το πιο πρόσφατο max για να το τυπώσουμε, οποτε διατρέχουε τη γενιά αντίστροφα και βρίσκουμε το 1ο max
for gen, atom, score in reversed(
        generations_in):  # διαπέρασα ανα βέλτιστο άτομο για τα 3 χαρακτηριστικά (γενιά, άτομο, σκορ)
    if score == max_score[2]:
        best_generation = gen  # Αποθηκεύουμε αριθμό γενιάς σε μεταβλητή
        best_atom = atom       # ομοίως, το άτομο
        best_score = score     # ομοίως, το σκορ
        break
# Εκτύπωση ενός βέλτιστου ατόμου όλων των γενιών (τυπώνεται της πιο πρόσφατης γενιάς) με αριθμό γενιάς, άτομο και σκορ
print(f"\nΒέλτιστο όλων των γενεών  🏆\nΓΕΝΙΑ: {best_generation:2d} - ΑΤΟΜΟ: "
      f"{best_atom} - ΣΚΟΡ: {best_score:.{decimals}f}\n")
