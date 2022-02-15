import random


def generate_word() -> str:
    """
    :return: a random word (str) from file "russian.txt"
    """
    with open("russian.txt", encoding='utf-8') as russian_words:
        russian_words = [word.strip().lower() for word in russian_words if word.strip().isalpha()]
        return random.choice(russian_words)


def check_input(input_word_or_letter: str) -> str:
    """
    :return: the verdict (the word is correct, the word contains the input letter, etc.) (str)
    """

    if len(input_word_or_letter) > 0 and input_word_or_letter[0] == '!':
        return recognize_command(input_word_or_letter)
    elif check_word(input_word_or_letter):
        # The input is a word
        if input_word_or_letter in used_words:
            return "Вы уже называли это слово"

        used_words.add(input_word_or_letter)

        if input_word_or_letter == correct_word:
            return "Вы угадали слово!"  # The word is correct
        else:
            return "Вы не угадали слово. Попробуйте еще раз."  # The word isn't correct
    elif len(input_word_or_letter) != 1:
        # The input is not a letter neither a word with length == length of correct word
        return "Вы должны ввести 1 букву или загаданное слово."
    else:
        # The input is a letter
        if input_word_or_letter in used_letters:
            return "Вы уже называли эту букву"

        used_letters.add(input_word_or_letter)
        guessed = False
        for i in range(len(correct_word)):
            if input_word_or_letter == correct_word[i]:  # Correct word contains the input letter
                guessed = True
                current_word[i] = input_word_or_letter
                if current_word == list(correct_word):
                    return "Вы угадали слово!"  # The user has guessed all the letters
        if guessed:
            return "Вы угадали букву!"

        return "Вы не угадали букву."  # Correct word doesn't contain the input letter


def check_word(word: str) -> bool:
    """
    :return: True if the word can be the correct word, else False
    """
    if len(word) != len(correct_word) or not word.isalpha():
        return False
    for i in range(len(word)):
        if current_word[i] != '*' and word[i] != current_word[i]:
            return False
    return True


def recognize_command(input_command: str) -> str:
    """
        :return: the result of the command or !help command if the command is incorrect (str)
    """
    global moves

    moves -= 1  # A command is not a move
    for command in COMMANDS.keys():
        if input_command == command:  # The command is correct
            if command == '!moves':
                return get_moves()
            if command == '!left':
                return get_left_letters()
            if command == '!used':
                return get_used_letters() + ' ' + get_used_words()
            if command == '!used_letters':
                return get_used_letters()
            if command == '!used_words':
                return get_used_words()
            if command == '!give_up':
                return give_up()
            if command == '!help':
                return help_command()
    else:  # The command is incorrect
        return "Такой команды нет.\n" + help_command()


def help_command() -> str:
    commands_to_print = '\n'.join('\t' + key + ' - ' + value for key, value in COMMANDS.items())
    return f"""Загадано слово. Нужно его угадать, назвав само слово или все его буквы.
У Вас есть {max_moves} попыток (количество различных букв в слове * 3).

Список доступных команд:
{commands_to_print}
"""


def get_moves() -> str:
    return str(moves)


def get_left_letters() -> str:
    return ' '.join(sorted(list(ALPHABET - used_letters)))


def get_used_letters() -> str:
    return ' '.join(sorted(list(used_letters)))


def get_used_words() -> str:
    return ' '.join(sorted(list(used_words)))


def give_up() -> str:
    return f"Вы сдались. Загаданное слово - {correct_word}"


ALPHABET = set(list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"))
COMMANDS = {
    "!moves": "показать количество ходов",
    "!left": "показать оставшиеся в алфавите буквы",
    "!used": "показать использованные буквы и слова",
    "!used_letters": "показать использованные буквы",
    "!used_words": "показать использованные слова",
    "!give_up": "сдаться и показать загаданное слово",
    "!help": "показать доступные команды"
}
moves = 0
used_letters = set()
used_words = set()

correct_word = generate_word()
current_word = ['*'] * len(correct_word)
max_moves = len(list(set(correct_word))) * 3

print(help_command())

# Main cycle
while True:
    moves += 1

    # Print the word (with '*' instead of not guessed letters) and check the input
    verdict = check_input(input('Слово: ' + ''.join(current_word) + '\n').lower())
    print(verdict)
    if verdict == "Вы угадали слово!" or verdict == give_up():  # The user has won or given up
        print(correct_word)
        print(f"Количество ходов: {get_moves()}")
        break
    if moves == max_moves:  # The user has reached the moves limit
        print('Game over. Вы превысили максимальное количество ходов.')
        print(f"Загаданное слово: {correct_word}")
        break
