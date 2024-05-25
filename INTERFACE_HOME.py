# Αρχείο InterFace. Από εδώ τρέχει ο αλγόριθμος σε παράθυρο διεπαφής χρήστη
# Εναλλακτικά για να τρέξετε τον αλγόριθμο σε περιβάλλον idle, ανοίγουμε και τρέχουμε το alternative_menu.py


# Εισαγωγή βιβλιοθήκης και κύριας συνάρτησης Γενετικού αλγόριθμου
from tkinter import *
from tkinter import messagebox
from GENETIC_ALGORITHM_HOME_ import genetic_algortihm


# Κύρια συνάρτηση εκτέλεσης του γενετικού αλγορίθμου
def execute_algorithm():
    # Αποθήκευση των τιμών από τα πεδία εισαγωγής σε μεταβλητές
    population_value = population_entry.get()  # Μέγεθος πληθυσμού
    variable_type = representation_var.get()  # Τύπος μεταβλητής
    variable_type = int(variable_type)  # Μετατροπή σε ακέραιο
    decimal_prec = precision_var.get()  # Ακρίβεια δεκαδικών
    crossover_value = crossover_entry.get()  # πιθανότητα αναπαραγωγής
    mutation_value = mutation_entry.get()  # πιθανότητα μετάλλαξης

    # αμυντικός, αν ο χρήστης προσπαθήσει να βάλει δεκαδικά στην ακέραια αναπαράσταση
    if representation_var.get() == "2" and precision_var.get() != 0:
        messagebox.showerror("Σφάλμα", "Για ακέραια αναπαράσταση, επιλέξτε ακέραιος στην ακρίβεια δεκαδικών.")
        return
    # αμυντικός για τον πληθυσμό, να είναι αριθμός μεγαλύτερος από το 0
    if population_value.isdigit() and int(population_value) > 0:
        population_value = int(population_value)  # αποθήκευση τιμής στην αντίστοιχη μεταβλητή
    else:
        messagebox.showerror("Σφάλμα", "Ο πληθυσμός πρέπει να είναι θετικός ακέραιος αριθμός.")
        # μήνυμα λάθους
        return
    # Αμυντικός Πιθανότητας διασταύρωσης (απο 0.1 εως 1)
    if crossover_value.replace('.', '', 1).isdigit() and 0.1 <= float(crossover_value) <= 1.0:
        crossover_value = float(crossover_value)  # αποθήκευση στην αντίστοιχη μεταβλητή
    else:
        messagebox.showerror("Σφάλμα",
                             "Η πιθανότητα διασταύρωσης πρέπει να είναι πραγματικός αριθμός μεταξύ 0.1 - 1 "
                             "\nΘυμηθείτε να χωρίσετε τα δεκαδικά με τελεία [ . ] και όχι με κόμμα [ , ]")
        return
    # Αμυντικός για πιθανότητα μετάλλαξης (από 0-0.1)
    if mutation_value.replace('.', '', 1).isdigit() and 0 <= float(mutation_value) <= 0.8:
        mutation_value = float(mutation_value)
    else:
        messagebox.showerror("Σφάλμα",
                             "Η πιθανότητα μετάλλαξης πρέπει να είναι πραγματικός αριθμός μεταξύ 0.01 - 0.1 "
                             "\nΘυμηθείτε να χωρίσετε τα δεκαδικά με τελεία [ . ] και όχι με κόμμα [ , ]")
        return

    # Κλήση της κύρια συνάρτησης του Γενετικού αλγόριθμου με ορίσματα τις εισαγωγές του χρήστη
    # Αποθήκευση σε λίστα του βέλτιστου μέλους κάθε γενιάς
    toppers = genetic_algortihm(variable_type, decimal_prec, population_value, crossover_value, mutation_value)
    # Μορφοποιημένη Εκτύπωση αποτελεσμάτων για κάθε γενιά
    result_text = ""
    for gen in toppers:
        result_text += f"ΓΕΝΙΑ {gen[0]:2}  : ΚΑΛΥΤΕΡΟ ΑΠΟΤΕΛΕΣΜΑ: {gen[2]:.{decimal_prec}f}, ΑΤΟΜΟ: {gen[1]}\n"

    # Επιπλεόν εκτύπωση, του βέλτιστου μέλους όλων των γενιών, επειδή μπορεί να έχει εμφανιστεί σε πολλές γενιές
    # Τυπώνουμε το βέλτιστο της πιο πρόσφατης γενιάς
    # Βρίσκουμε το μέγιστο
    max_score = max(toppers, key=lambda x: x[2])
    for gen, atom, score in (toppers):
        if score == max_score[2]:
            best_generation1 = gen
            best_atom1 = atom
            best_score1 = score
            break

    # Διατρέχουμε τη λίστα με τα βέλτιστα μέλη αντίστροφα και όταν βρούμε το πρώτο max (το πιο πρόσφατο)
    # αποθηκεύουμε σε αντίστοιχες μεταβλητές τα στοιχεία του (γενιά, άτομο, σκορ)
    for gen, atom, score in reversed(toppers):
        if score == max_score[2]:
            best_generation = gen
            best_atom = atom
            best_score = score
            break


    # Διαμορφώνουμε το κέιμενο του αποτελέσματος του βέλτιστου όλων των γενιών
    # Aν το βέλτιστο άτομο εμφνιστεί μια φορά, το τυπώνουμε 1 φορά
    if (best_generation1==best_generation) :
        result_text += (f"\nΚαλύτερος όλων των γενεών 🏆\n"
        f"ΓΕΝΙΑ : {best_generation1:2d} - ΑΤΟΜΟ: {best_atom1} - ΣΚΟΡ: {best_score1:.{decimal_prec}f}\n" )
    else:  # εναλλακτικά τυπώνουμε την πρώτη και τελευταία εμφάνιση του
        result_text += (f"\nΚαλύτερος όλων των γενεών 🏆\n"
        f"Πρώτη Εμφάνιση       ΓΕΝΙΑ : {best_generation1:2d} - ΑΤΟΜΟ: {best_atom1} - ΣΚΟΡ: {best_score1:.{decimal_prec}f}\n"
        f"Τελευταία Εμφάνιση   ΓΕΝΙΑ : {best_generation:2d} - ΑΤΟΜΟ: {best_atom} - ΣΚΟΡ: {best_score:.{decimal_prec}f}\n" )




    # ενεργοποίση του πλαισίου κειμένου
    result_text_widget.config(state=NORMAL)
    # Διαγραφή του περιεχόμενου του πλαισίου κειμένου
    result_text_widget.delete(1.0, END)
    # Εισαγωγή του νέου κειμένου στο πλαίσιο κειμένου
    result_text_widget.insert(END, result_text)
    # Απενεργοποίηση του πλαισίου κειμένου για αποφυγή επεξεργασίας από τον χρήστη
    result_text_widget.config(state=DISABLED)


# Συνάρτηση που καλείται από το κουμπί reset και διαγράφει τις εισαγωγές του χρήστη και τις εκτυπώσεις, επαναφέροντας
# όλα τα πεδία
def reset_fields():
    population_entry.delete(0, END)
    crossover_entry.delete(0, END)
    mutation_entry.delete(0, END)
    result_text_widget.config(state=NORMAL)
    result_text_widget.delete(1.0, END)
    result_text_widget.config(state=DISABLED)


root = Tk()  # Δημιουργία νέου παραθύρου interface
root.title("ΓΕΝΕΤΙΚΟΣ ΑΛΓΟΡΙΘΜΟΣ v 3.0")  # Τίτλος κορδέλας παραθύρου
root.geometry("1620x900")  # Διαστάσεις παραθύρου
root.configure(bg="#728FCE")  # Χρώμα background παραθύρου, ανοικτό μωβ

# Εικόνα
image = PhotoImage(file="gen.png")  # φορτώνουμε την εικόνα που βρίσκεται στον ίδιο φάκελο με το αρχείο py
image = image.subsample(8)  # μικραίνουμε την εικόνα
image_label = Label(root, image=image, bg="#728FCE")  # δημιούργια label (χώρου για την εικόνα)

image_label.pack(side=LEFT, padx=20, pady=20, anchor='nw')
# Τοποθέτηση της εικόνας αριστερά στο παράθυρο με περιθώρια 20 και με επιλογή αριστερά πάνω (nw)
font_style = ("Arial", 14)  # Επιλογή γραμματοσειράς και μεγέθους γραμματοσειράς

# Εκτύπωση Κειμένων Τίτλος και κείμενα περιγραφή εφαρμογής
title_label = Label(root, text="Γενετικός Αλγόριθμος ", font=("Arial", 24), fg="navy", bg="#728FCE")
title_label.pack(side=TOP, pady=10, anchor=W)
# επιλογές τίτλου, χρώματα, περιθώρια και anchor (θέση στο παράθυρο)

# Κέιμενο που περιγράφει τι κάνει η εφαρμογή, με παραμέτρους (χρώμα και γραμματοσειρά)
text_label = Label(root, text="Μεγιστοποίηση συνάρτησης f(x, y, z) = x**2 + y**3 + z**4 + x ∙ y ∙ z",
                   font=font_style, bg="#728FCE")
text_label.pack(side=TOP, pady=10, anchor=W)
# επιλογές θέσης και περιθωρίων

# Τίτλος για επιλογές χρήστη
text_label = Label(root, text="Επιλέξτε παραμέτρους:", font=font_style, bg="#728FCE")
text_label.pack(side=TOP, pady=10, anchor=W)
# επιλογές θέσης και περιθωρίων

# Πεδία για επιλογή αναπαράστασης (1 -δυαδική, 2 -ακέραια, 3- πραγματική)
representation_var = StringVar()
representation_var.set(1)  # προεπιλογή της αναπαράστασης σε 1 (δυαδικό)
representation_frame = Frame(root, bg="#728FCE")
representation_frame.pack(side=TOP, pady=5, padx=10, anchor=W)
# παράμετροι του block αναπαράσταση (χρωμα, θεση, αποστάσεις)

# Τίτλος "αναπαράσταση" για τα radio buttons
representation_label = Label(representation_frame, text="Aναπαράσταση 🔢  ", font=font_style, bg="#728FCE")
representation_label.grid(row=0, column=0, padx=(10, 5), pady=5, sticky=W)

# Πρώτο radio button για δυαδική αναπαράσταση
# Επιστρέφει την τιμή 1 που αποθηκεύουμε σε μεταβλητή για πέρασμα στη συνάρτηση Γ.Α.
binary_radio = Radiobutton(representation_frame, text="Δυαδική", variable=representation_var, value=1,
                           font=font_style, bg="#728FCE")
binary_radio.grid(row=0, column=1, padx=(0, 10), pady=5, sticky=W)

# 2ο radio button για Ακέραια αναπαράσταση
# Επιστρέφει την τιμή 2 που αποθηκεύουμε σε μεταβλητή για πέρασμα στη συνάρτηση Γ.Α.
integer_radio = Radiobutton(representation_frame, text="Ακέραια", variable=representation_var, value=2,
                            font=font_style, bg="#728FCE")
integer_radio.grid(row=0, column=2, padx=(0, 10), pady=5, sticky=W)

# 3ο radio button για δυαδική αναπαράσταση
# Επιστρέφει την τιμή 3 που αποθηκεύουμε σε μεταβλητή για πέρασμα στη συνάρτηση Γ.Α.
decimal_radio = Radiobutton(representation_frame, text="Πραγματική", variable=representation_var, value=3,
                            font=font_style, bg="#728FCE")
decimal_radio.grid(row=0, column=3, pady=5, sticky=W)

# BLOCK κώδικα για τα radio buttons ακρίβειας δεκαδικών
# Δημιουργία frame με χρώμα ίδιο με του background
precision_frame = Frame(root, bg="#728FCE")
precision_frame.pack(side=TOP, pady=5, padx=10, anchor=W)
# παράμετροι θέσης και padding

# Τίτλος Radio buttons
precision_label = Label(precision_frame, text="Ακρίβεια δεκαδικών", font=font_style, bg="#728FCE")
precision_label.grid(row=0, column=0, padx=(10, 5), pady=5, sticky=W)

# Μεταβλητή IntVar που χρησιμοποιείται για να αποθηκεύει την επιλεγμένη ακρίβεια από τα Radio Buttons
precision_var = IntVar()
precision_var.set(1)  # προεπιλεγμένη τιμή 1 ( Ακρίβεια ενός δεκαδικού)

# 1η επιλογή για 0 δεκαδικά
precision_radio0 = Radiobutton(precision_frame, text="Ακέραιος", variable=precision_var, value=0,
                               font=font_style, bg="#728FCE")
precision_radio0.grid(row=0, column=1, padx=(0, 10), pady=5, sticky=W)

# 2η επιλογή για 1 δεκαδικό
precision_radio1 = Radiobutton(precision_frame, text="1", variable=precision_var, value=1,
                               font=font_style, bg="#728FCE")
precision_radio1.grid(row=0, column=2, padx=(0, 10), pady=5, sticky=W)

# 3η επιλογή για 2 δεκαδικά
precision_radio2 = Radiobutton(precision_frame, text="2", variable=precision_var, value=2,
                               font=font_style, bg="#728FCE")
precision_radio2.grid(row=0, column=3, padx=(0, 10), pady=5, sticky=W)

# 4η επιλογή για 3 δεκαδικά
precision_radio3 = Radiobutton(precision_frame, text="3", variable=precision_var, value=3,
                               font=font_style, bg="#728FCE")
precision_radio3.grid(row=0, column=4, padx=(0, 10), pady=5, sticky=W)

# 5η επιλογή για 4 δεκαδικά
precision_radio4 = Radiobutton(precision_frame, text="4", variable=precision_var, value=4,
                               font=font_style, bg="#728FCE")
precision_radio4.grid(row=0, column=5, padx=(0, 10), pady=5, sticky=W)


# Block κώδικα για την εισαγωγή πληθυσμου
# Δημιουργία frame
population_frame = Frame(root, bg="#728FCE")
population_frame.pack(side=TOP, pady=5, padx=10, anchor=W) #θέση και padding
#Label και τίτλος
population_label = Label(population_frame, text="Πληθυσμός 👫🏽👫🏽👫🏽👫🏽👫🏽👫🏽     ", font=font_style, bg="#728FCE")
population_label.grid(row=0, column=0, padx=(10, 5), pady=5, sticky=W)
# πεδίο εισαγωγής
population_entry = Entry(population_frame, font=font_style)
population_entry.grid(row=0, column=1, padx=(0, 10), pady=5, sticky=W)
population_entry.insert(0, "π.χ. 10")  # Υποδειγματικό κείμενο για τον πληθυσμό
# Υποδείξεις δεξιά του πλαισίου εισαγωγής, για συμπλήρωση
population_placeholder_label = Label(population_frame, text="Θετικός ακέραιος            💡Προτείνεται: [40 - 100]",
                                     font=("Arial", 12), fg="#1f1061", bg="#728FCE")
population_placeholder_label.grid(row=0, column=2, padx=(5, 10), pady=5, sticky=W)


# Block κώδικα για την εισαγωγή πιθανότητας διασταύρωσης (όμοια με του πληθυσμού)
crossover_frame = Frame(root, bg="#728FCE")
crossover_frame.pack(side=TOP, pady=5, padx=10, anchor=W)

crossover_label = Label(crossover_frame, text="Πιθανότητα Διασταύρωσης 🤍", font=font_style, bg="#728FCE")
crossover_label.grid(row=0, column=0, padx=(10, 5), pady=5, sticky=W)
crossover_entry = Entry(crossover_frame, font=font_style)
crossover_entry.grid(row=0, column=1, padx=(0, 10), pady=5, sticky=W)
crossover_entry.insert(0, "π.χ. 0.5") # Υποδειγματικό κείμενο
crossover_entry_placeholder_label = Label(crossover_frame, text="Πραγματικός [0.0-1.0]     💡Προτείνεται: [0.4 - 0.9]",
                                          font=("Arial", 12), fg="#1f1061", bg="#728FCE")
crossover_entry_placeholder_label.grid(row=0, column=2, padx=(5, 10), pady=5, sticky=W)

# Block κώδικαι για την εισαγωγή πιθανότητας μετάλλαξης -όμοιες λειτουργίες με του πληθυσμού
mutation_frame = Frame(root, bg="#728FCE")
mutation_frame.pack(side=TOP, pady=5, padx=10, anchor=W)

mutation_label = Label(mutation_frame, text="Πιθανότητα Μετάλλαξης 👽     ", font=font_style, bg="#728FCE")
mutation_label.grid(row=0, column=0, padx=(10, 5), pady=5, sticky=W)

mutation_entry = Entry(mutation_frame, font=font_style)
mutation_entry.grid(row=0, column=1, padx=(0, 10), pady=5, sticky=W)
mutation_entry.insert(0, "π.χ. 0.03")
mutation_entry_placeholder_label = Label(mutation_frame, text="Πραγματικός [0.01-0.10]  💡Προτείνεται: [0.01 - 0.05]",
                                         font=("Arial", 12), fg="#1f1061", bg="#728FCE")
mutation_entry_placeholder_label.grid(row=0, column=2, padx=(5, 10), pady=5, sticky=W)

# Συνάρτηση για να εξαφανίζονται τα κείμενα placeholder όταν ο χρήστης ενεργοποιεί το πεδίο για να γράψει
def clear_placeholder(event, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, END)


# Καθάρισμα των υποδειγματικών κειμένων όταν ο χρήστης θέλει να γράψει
population_entry.bind("<FocusIn>", lambda event: clear_placeholder(event, population_entry, "π.χ. 10"))
crossover_entry.bind("<FocusIn>", lambda event: clear_placeholder(event, crossover_entry, "π.χ. 0.5"))
mutation_entry.bind("<FocusIn>", lambda event: clear_placeholder(event, mutation_entry, "π.χ. 0.03"))


# Δημιουργία πλαισίου για κουμπία
button_frame = Frame(root, bg="#728FCE")

button_frame.pack(side=TOP, pady=5, padx=10, anchor=W) #θέση και padding

# Κουμπί που καλεί την συνάρτηση execute_algorithm που τρέχει τον αλγόριθμο
execute_button = Button(button_frame, text="Εκτέλεση", font=font_style, command=execute_algorithm)
execute_button.grid(row=0, column=0, padx=(0, 10), pady=5)

# Κουμπί reset που καλεί τη συνάρτηση reset_fields για να κάνει reset
reset_button = Button(button_frame, text="Reset", font=font_style, command=reset_fields)
reset_button.grid(row=0, column=1, pady=5)


# Πεδίο εκτύπωσης αποτελεσμάτων
title_label2 = Label(root, text="🧬 Αποτελέσματα Γενετικού Αλγόριθμου", font=("Arial", 24), fg="navy", bg="#728FCE")
title_label2.pack(side=TOP, pady=10, anchor=W)

# Πλαίσιο λευκό που εκτυπώνονται τα αποτελέσματα του αλγορίθμου όπως τα ορίσαμε στην συνάρτηση
# execute algorithm στις μορφοποιημένες εξόδους
result_text_widget = Text(root, font=font_style, wrap=WORD, bg="white", fg="#000000")
result_text_widget.pack(side=TOP, pady=(0, 50), padx=(0, 40), anchor=W, fill=BOTH, expand=True, ipadx=10, ipady=10)

# Προσθήκη scrollbar στα δεξιά για να μπορεί ο χρήστης να κάνει κύλιση όταν προκύψουν πολλές γενιές.
scrollbar = Scrollbar(result_text_widget, orient=VERTICAL, command=result_text_widget.yview, bg="#728FCE",
                      troughcolor="#728FCE")
scrollbar.pack(side=RIGHT, fill=Y)
result_text_widget.config(yscrollcommand=scrollbar.set)

root.mainloop()  # εκτέλεση του βρόγχου γεγονότων για όσο το παράθυρο διεπαφής χρήστη παραμένει ανοικτό
