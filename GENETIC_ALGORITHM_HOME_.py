# -------- ΓΕΝΕΤΙΚΟΣ ΑΛΓΟΡΙΘΜΟΣ HOME------------------------------------------------------------------------------------

# Εισαγωγή συναρτήσεων Γενετικού Αλγόριθμου
# Χρησιμοποιούμε συναρτήσεις από τα αρχεία Genetic_Functions και Mutation_Function

from Genetic_Functions import (initialize_population, calculate_fitness_scores, selection, select_parent_pairs,
                               crossover_dec, crossover_bin)
from Mutation_Function import mutate_population_binary, mutate_population_dekadiko

# --------- ΣΥΝΑΡΤΗΣΗ ΓΕΝΕΤΙΚΟΥ ΑΛΓΟΡΙΘΜΟΥ -----------------------------------------------------------------------------
"""
genetic_algortihm  ==> Συνάρτηση Γ.Α την οποία καλεί το TKINTER (ή το Alternative_menu)
με παραμέτρους τις επιλογές χρήστη:
(τύπος αναπαράστασης, πλήθος δεκαδικών, πληθυσμός, πιθανότητα αναπαραγωγής, πιθανότητα διασταύρωσης)
"""


def genetic_algortihm(variable_type, decimals, population_input, mating_p, mutation_p):
    generation_toper = []  # Λίστα που αποθηκεύουμε το άτομο με την καλύτερη απόδοση σε κάθε γενιά
    generation = 1  # Αρχικοποίηση αριθμού γενιάς, ώστε να τις μετράμε

    # --------- 1.ΑΡΧΙΚΟΠΟΙΗΣΗ ΠΛΗΘΥΣΜΟΥ ------------------------------------------------------------------------------

    pop = initialize_population(population_input, variable_type, decimals)  # Κλήση συνάρτησης αρχικοποίησης
    # Αποθήκευση ατόμων στη λίστα pop

    # Επαναληπτική δομή με πρώτο κριτήριο τερματισμού τις 40 γενιές
    while generation <= 40:

        # ---------2.ΑΞΙΟΛΟΓΗΣΗ ----------------------------------------------------------------------------------
        fitness_scores_list, sumarize = calculate_fitness_scores(pop, variable_type, decimals)

        max_score = max(fitness_scores_list)  # Υπολογισμός του max score τρέχουσας γενιάς
        max_score_index = fitness_scores_list.index(max_score)  # βρίσκουμε το index του ατόμου με το max score
        max_score_individual = pop[max_score_index]  # Βρίσκουμε το άτομο με το max score

        generation_toper.append([generation, max_score_individual, max_score])
        # φτιάχνουμε μια λίστα από λίστες με τα στοιχεία του καλύτερου μέλους κάθε γενιάς (αρ.γενιάς, σκορ, άτομο)
        # σε κάθε τρέχουσα γενιά προσθέτουμε το βέλτιστο μέλος (append)

        # 2η συνθήκη τερματισμού: αν για 3 συνεχόμενες γενιές έχουμε μηδενική βελτίωση σταματά ο αλγόριθμος
        # ο έλεγχος ξεκινά μετά την δεύτερη γενιά (αφού συγκρίνει 2 γενιές πίσω)
        if (generation > 2 and
                (generation_toper[generation - 1][2] == generation_toper[generation - 2][2] and
                 generation_toper[generation - 1][2] == generation_toper[generation - 3][2])):
            break

        # -------3. ΕΠΙΛΟΓΗ------------------------------------------------------------------------

        chosen_parents= selection(fitness_scores_list, sumarize, population_input, pop)
        # Κλήση συνάρτησης selection με εξαναγκασμένη ρουλέτα
        # Σε μια λίστα διατηρούμε τους επιλεγμένους γονείς και σε μία άλλη τα id_των επιλεγμένων ατόμων (index)

        # ------4. ΔΙΑΣΤΑΥΡΩΣΗ--------------------------------------------------------------------------

        # Κλήση συνάρτησης επιλογής ζευγαριών γονιών βάση του συντελεστή αναπαραγωγής
        # Παίρνουμε μία λίστα με ζευγάρια γονέων, και μία λίστα με τα index των ατόμων που θα αναπαραχθούν
        parent_pairs, reproced = select_parent_pairs(chosen_parents, mating_p)
        children = []  # Δημιουργία λίστας για τα παιδιά που θα προκύψουν

        # Αναπαραγωγή ανά ζευγάρι μέ κλήση της συνάρτησης crossover
        for parent1, parent2 in parent_pairs:
            if variable_type == 2 or variable_type == 3:  # Για ακέραια και πραγματική αναπαράσταση
                child1, child2 = crossover_dec(parent1, parent2)  # κλήση συνάρτησης crossover
            elif variable_type == 1:  # Για δυαδική αναπαράσταση
                child1, child2 = crossover_bin(parent1, parent2, decimals)
                # κλήση ειδικής crossover για binary

            children.append(child1)  # ενημέρωση της λίστας παιδιών με το 1ο παιδί
            children.append(child2)  # ενημέρωση της λίστας παιδιών με το 2ο παιδί
            if len(children) == len(pop):  # συνθήκη για να παραμείνει ο πληθυσμός ίδιος
                break

        children_index = 0  # αρχικοποίηση δείκτη λίστας παιδιών

        # Αντικατάσταση των αναπαραχθέντων γονέων (ζεύγος) με τα παιδιά τους (2)
        for i in range(len(reproced)):  # διατρέχουμε με τη σειρά τα index των γονέων που αναπαράχθηκαν
            chosen_parents[reproced[i]] = children[children_index]
            # διατρέχουμε με τη σειρά τα παιδιά που αναπαράχθηκαν
            # για κάθε αναπαραχθέντα γονέα, αντικαθιστούμε ένα αναπαραγμένο παιδί, δε μας ενδιαφέρει η σειρά,
            # αρκεί στη νέα γενιά τα παιδιά να έχουν αντικαταστήσει τους αναπαραχθέντες γονείς
            children_index = children_index + 1  # αυξάνουμε το index των παιδιών κατά ένα

        # Τώρα η λίστα chosen parents Έχει μέσα της τα νεα παιδιά που αντικατέστησαν τους γονείς που αναπαράχθηκαν
        new_generation = []  # Δημιουργία λίστας για τη νέα γενιά που θα προκύψει μετά τη μετάλλαξη

        # Μετάλλαξη βάση του συντελεστή μετάλλαξης
        # Κλήση αντίστοιχων συναρτήσεων
        if variable_type == 2 or variable_type == 3:  # ακέραιοι και πραγματικοί
            new_generation = mutate_population_dekadiko(chosen_parents, mutation_p, variable_type, decimals)
        elif variable_type == 1:  # δυαδική αναπαράσταση
            new_generation = mutate_population_binary(chosen_parents, mutation_p, decimals)
        # διαφορετική συνάρτηση για δυαδική αναπαράσταση

        generation += 1  # αυξάνουμε γενιά κατά 1 για το κριτήριο τερματισμού και τις εκτυπώσεις μας

        pop = new_generation.copy()  # αντιγραφούμε τη νέα μας γενιά στο pop κ
        # ώστε να μπει πάλι στην επαναληπτική δομή και να υποστεί την ίδια διαδικασία εως ότου ικανοποιηθεί
        # ένα από τα δύο κριτήρια τερματισμού

    return generation_toper  # H συνάρτηση επιστρέφει μια λίστα με λίστες
    # Κάθε εσωτερική λίστα είναι τα στοιχεία του βέλτιστου ατόμου κάθε γενιάς (αρ.γενιάς, ατομο,score)
