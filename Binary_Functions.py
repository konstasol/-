# ΣΥΝΑΡΤΗΣΕΙΣ ΓΙΑ ΤΗ ΔΥΑΔΙΚΗ ΑΝΑΠΑΡΑΣΤΑΣΗ


"""
1. ΣΥΝΑΡΤΗΣΗ για μετατροπή πραγματικού αριθμού με δεκαδικά ψηφία σε δυαδικό -Δέχεται σαν ορίσματα τον πραγματικό
αριθμό, και την ακρίβεια δεκαδικών) - Με χρήση του τύπου ceil(log2(N+1)) βρίσκουμε ότι χρειαζόμαστε 5 δυαδικά ψηφία
για αναπαρασταση του ακέραιου μέρους (0-30) και 4,7,10 ή 14 για την αναπαράσταση 1,2,3 ή 4 δεκαδικών αντίστοιχα. -
Αφού βρούμε τον αριθμό των ψηφίων που θα αναπαριστούν τον αριθμό, μετατρέπουμε σε δυαδικό το ακέραιο μέρος
χρησιμοποιώντας την ενσωματωμένη συνάρτηση της Python. Στη συνέχει με συνεχείς πολλαπλασιασμούς με το 2 και
τοποθέτηση των δυαδικών με τη σειρά που τα βρίσκουμε παίρνουμε τη δυαδική αναπαράσταση του δεκαδικού μέρους. Τέλος,
ενώνουμε τους 2 αριθμούς και προκύπτει ο αριθμός σε δυαδική αναπαράσταση με αντίστοιχη ακρίβεια δεκαδικών με αυτή που
έχει επιλέξει ο χρήστης."""


def decimal_to_binary(pragmatikos, decimal_points):
    if decimal_points == 0:  # Βάση επιλογής χρήστη[1-4 δεκαδικά]
        binary_points = 0  # 0 δεκαδικά ==>> 0 bits
    elif decimal_points == 1:  # Βάση επιλογής χρήστη[1-4 δεκαδικά]
        binary_points = 4  # 1 δεκαδικό ==>> ceil log2[0.1]=4 bits
    elif decimal_points == 2:
        binary_points = 7  # 2 δεκαδικά ==>> log2[0.01]=7 bits
    elif decimal_points == 3:
        binary_points = 10  # 3 δεκαδικά ==>> log2[0.001]=10 bits
    else:
        binary_points = 14  # 4 δεκαδικά ==>> log2[0.0001]=14 bits

    akeraio_meros = format(int(pragmatikos), '05b')  # Μετατροπή ακέραιου μέρους σε 2αδικο με 5 ψηφία και leading zeros
    # 5 ψηφία γιατί: ceil(log2[(30)])=5 με 5
    # με 5 ψηφία μπορούμε να αναπαραστήσουμε εως και το 31 ->11111

    dekadiko = ''  # Μετατροπή δεκαδικού μέρους σε δυαδικό
    dekadiko_timh = pragmatikos - int(pragmatikos)  # Βρίσκουμε την τιμή του δεκαδικού μέρους πχ 1,26 -1 =0,26
    for _ in range(binary_points):  # Μετατροπή σε 2αδικό με συνεχείς πολ/σμους με το 2 τόσες φορές όσα τα binary_points
        dekadiko_timh *= 2
        bit = '1' if dekadiko_timh >= 1 else '0'  # αν το ακέραιο μέρος του αποτελέσματος του πολ/σμου είναι
        # μεγαλύτερο του 1, προσθέτουμε το ψηφίο 1 αλλιώς το 0

        dekadiko += bit  # Προσθέτουμε κάθε νέο ψηφίο στο string με τη σειρά που τα βρίσκουμε
        dekadiko_timh -= int(bit)  # αφαιρούμε το ακέραιο μέρος (Το bit που κρατήσαμε) για να ξαναβάλουμε το
        # δεκαδικό μέρος για πολλαπλασιασμό με το 2 ώστε να πάρουμε το επόμενο bit

    binary_rep = akeraio_meros + dekadiko  # Δημιουργούμε τον binary συνδυάζοντας τα 2 μέρη
    return str(binary_rep)  # Μετατροπή σε string και επιστροφή δυαδικού αριθμού με κόμμα


""" 
2. ΣΥΝΑΡΤΗΣΗ για μετατροπή δυαδικού με υποδιαστολή σε δεκαδικό με δεκαδικά ψηφία
-Παίρνει σαν ορίσματα binary string με κόμμα(πχ 1101.0001) και την ακρίβεια δεκαδικών (1-4)
-Χωρίζει το ακέραιο και κλασματικό μέρος και τα μετατρέπει σε δεκαδικό σύστημα
Το ακέραιο με την ενσωματωμένη συνάρτηση της Python
για το κλασματικό χρησιμοποιούμε τον τύπο της παράστασης μετατροπής σε δεκαδικό
πχ
Ο δυαδικός αριθμός 10011,1 στο δεκαδικό σύστημα έχει την τιμή
1*2**4 + 0*2**3 + 0*2**2 + 1*2**1+ 1+1*2**(-1) = 16+2+1+0,5 = 19,5.
Επειδή όλοι οι αριθμοί είναι μετά την υποδιαστολή
ξεκινάμε από το -1 διατρέχοντας το δεκαδικό μέρος.
Στη συνέχεια προσθέτουμε δεκαδικό και κλασματικό μέρος
και επιστρέφουμε τον πραγματικό αριθμό σε δεκαδικό σύστημα αρίθμησης.

"""


#
def binary_to_decimal(binary_number, decimal_points):
    # Χωρίζουμε σε ακέραιο και δεκαδικό μέρος και τα αποθηκεύουμε σε 2 βοηθητικές μεταβλητές

    akeraio = binary_number[:5]
    dekadiko_meros = binary_number[5:]

    dekadiko_akeraios = int(akeraio, 2)  # Μετατρέπουμε το ακέραιο σε δεκαδικό
    dekadiko_conv = sum(int(bit) * 2 ** -(i + 1) for i, bit in enumerate(dekadiko_meros))
    # Μετατρέπουμε το κλασματικό μέρος του δυαδικού σε δεκαδική αναπαράσταση
    dekadiko_conv = round(dekadiko_conv, decimal_points)  # Στρογγυλοποιούμε ώς το δοθέν αριθμό δεκαδικών
    dekadikh_anapar = dekadiko_akeraios + dekadiko_conv  # Συνδυάζουμε τα δύο μέρη για να πάρουμε τον δεκαδικό

    return dekadikh_anapar


"""
# 3. Συνάρτηση DECODING για να πάρουμε πίσω τους τρεις αριθμούς από το ενιαίο δυαδικό
Παίρνει σαν ορίσματα το ενιαίο string και την ακρίβεια δεκαδικών
Διαίρει στα 3 τη συμβολοσειρά 
Διαχωρίζει την κάθε συμβολοσείρα από τις 3 σε ακέραιο και δεκαδικό
Τα ενώνει με τελεία
ώστε να κάνει για το κάθε ένα κλήση στη συνάρτηση binary to decimal
Επιστρέφει τους τρεις πραγματικούς αριθμούς που απαρτίζουν την ενιαία δυαδική συμβολοσειρά
"""


def split_binary(binary_string, decimals):
    # Βρίσκουμε το μήκος της συμβολοσειράς
    length = len(binary_string)
    part_length = length // 3  # Διαιρούμε με το 3 για να πάρουμε το μήκος της κάθε μεταβλητής
    first_part, second_part, third_part = (binary_string[:part_length], binary_string[part_length:2 * part_length],
                                           binary_string[2 * part_length:])
    # με slicing αποθηκέψουμε τα αντίστοιχα string κομμάτια στην κάθε μεταβλητή

    first_integer_part = first_part[:5]  # βρίσκουμε το κομμάτι που αναπαριστά τον ακέραιο
    first_fractional_part = first_part[5:]  # τα υπόλοιπα είναι το κλασματικό μέρος
    second_integer_part = second_part[:5]  # ομοίως, για το 2ο κομμάτι
    second_fractional_part = second_part[5:]
    third_integer_part = third_part[:5]  # ομοίως, για το 3ο
    third_fractional_part = third_part[5:]

    # Ενώνουμε το ακέραιο και κλασματικό με τελεία ώστε να τα περάσουμε στη συνάρτηση binary_to_decimal
    first_binary = first_integer_part + first_fractional_part
    second_binary = second_integer_part + second_fractional_part
    third_binary = third_integer_part + third_fractional_part

    # Κλήση στην αντίστοιχη συνάρτηση
    first = binary_to_decimal(first_binary, decimals)
    second = binary_to_decimal(second_binary, decimals)
    third = binary_to_decimal(third_binary, decimals)

    return first, second, third  # Επιστροφή των 3 πραγματικών αριθμών (DECODING)
