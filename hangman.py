import random
from hangman_words import word_list
from hangman_art import stages, logo

# Escolhe uma palavra # # randomicamente
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo)
print(f'Pssst, the solution is a word with {len(chosen_word)} letters.')

# Verifica a quantidade de letras que a palavra possui
# Cria uma lista com espaços correspondentes qtde.
display = []
for _ in range(word_length):
    display += '_'
print(display)

# Loop até todo os espaços sejam preenchidos
while not end_of_game:
    # Pede pro usuario digitar uma letra
    guess = input('Guess a letter: ').lower()

    # mostra a letra se já foi escolhida.
    if guess in display:
        print(f"You,ve already guessed: {guess}")

    # Percorre a palavra e verifica se a letra escolhida existe.
    for position in range(word_length):
        # Variavel recebe a letra em cada posição
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print()
            print('You lose.')

    print()
    print(f"{''.join(display)}")

    if "_" not in display:  # Se não houver espaços na lista display
        end_of_game = True
        print('You Win')

    print(stages[lives])  # Mostra a forca de acordo com a qtde
    # de erros (6 vidas)
