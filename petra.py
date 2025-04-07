import random

def play_game():
    choices = ['πέτρα', 'ψαλίδι', 'χαρτί']
    user_score = 0
    computer_score = 0
    
    print("🎮 Παίζουμε Πέτρα, Ψαλίδι, Χαρτί! 🎴")
    print("Διάλεξε: πέτρα, ψαλίδι ή χαρτί (ή 'quit' για έξοδο).")
    
    while True:
        user_choice = input("\nΗ επιλογή σου: ").lower().strip()
        
        if user_choice == 'quit':
            print(f"\n🏁 Τελικό σκορ: Εσύ {user_score} - {computer_score} Υπολογιστής")
            if user_score > computer_score:
                print("🎉 Κέρδισες!")
            elif user_score < computer_score:
                print("🤖 Κέρδισε ο υπολογιστής!")
            else:
                print("🤝 Ισοπαλία!")
            break
        
        if user_choice not in choices:
            print("⚠ Λάθος επιλογή! Δοκίμασε ξανά.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"\nΕσύ: {user_choice}  vs  Υπολογιστής: {computer_choice}")
        
        # Κανόνες του παιχνιδιού
        if user_choice == computer_choice:
            print("👉 Ισοπαλία!")
        elif (user_choice == 'πέτρα' and computer_choice == 'ψαλίδι') or \
             (user_choice == 'ψαλίδι' and computer_choice == 'χαρτί') or \
             (user_choice == 'χαρτί' and computer_choice == 'πέτρα'):
            print("✅ Κέρδισες αυτόν τον γύρο!")
            user_score += 1
        else:
            print("❌ Έχασες αυτόν τον γύρο!")
            computer_score += 1
        
        print(f"Σκορ: Εσύ {user_score} - {computer_score} Υπολογιστής")

# Ξεκινάμε το παιχνίδι
if __name__ == "__main__":
    play_game()
