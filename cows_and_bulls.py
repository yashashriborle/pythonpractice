import random

def generate_secret():
    digits = list(range(10))  # List of digits 0–9
    random.shuffle(digits)    # Shuffle the digits
    return ''.join([str(digit) for digit in digits[:4]])  # Take first 4 digits and return as string

def calculate_cows_and_bulls(secret, guess):
    bulls = sum([1 for i in range(4) if guess[i] == secret[i]])  # Right digit, right place
    cows = sum([1 for i in range(4) if guess[i] in secret]) - bulls  # Right digit, wrong place
    return cows, bulls

def main():
    secret = generate_secret()
    print('I have generated a 4-digit number with unique digits. Try to guess it!')
    print(f"(Secret number for testing: {secret})")  # 🔍 Remove this line in production

    while True:
        guess = input('Guess: ')
        if len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4:
            cows, bulls = calculate_cows_and_bulls(secret, guess)
            print(f'{cows} cows, {bulls} bulls')

            if bulls == 4:
                print('🎉 Congratulations! You guessed the correct number.')
                break
        else:
            print('❌ Invalid guess. Please enter a 4-digit number with unique digits.')

if __name__ == '__main__':
    main()
