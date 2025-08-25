import sys
from collections import Counter, defaultdict

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <input_file> <letters>")
    sys.exit(1)

input_file = sys.argv[1]
letters = sys.argv[2].lower()
letters_count = Counter(letters)

def can_construct(word, letters_count):
    word_count = Counter(word.lower())
    for letter, count in word_count.items():
        if letters_count.get(letter, 0) < count:
            return False
    return True

# uložíme slová podľa dĺžky, vylúčime slová dĺžky 1
words_by_length = defaultdict(list)

with open(input_file, "r", encoding="utf-8") as infile:
    for line in infile:
        word = line.strip()
        if len(word) > 1 and can_construct(word, letters_count):
            words_by_length[len(word)].append(word)

# odstránime duplicity a zoradíme slová v každom stĺpci abecedne
for length in words_by_length:
    unique_words = sorted(set(words_by_length[length]))
    words_by_length[length] = unique_words

# zoradíme stĺpce podľa dĺžky slova (najdlhšie ako prvé)
lengths = sorted(words_by_length.keys(), reverse=True)

# zistíme maximálny počet riadkov
max_rows = max(len(words_by_length[l]) for l in lengths)

# doplníme prázdne reťazce tam, kde je menej slov
columns = []
for l in lengths:
    col = words_by_length[l]
    if len(col) < max_rows:
        col += [""] * (max_rows - len(col))
    columns.append(col)

# zistíme šírku stĺpcov pre zarovnanie (vrátane hlavičky)
col_widths = []
for i, l in enumerate(lengths):
    max_len = max(len(word) for word in columns[i])
    max_len = max(max_len, len(str(l)))  # aby sa hlavička zmestila
    col_widths.append(max_len)

# vypíšeme hlavičky (dĺžku slova)
header = ""
for i, l in enumerate(lengths):
    header += str(l).ljust(col_widths[i] + 2)
print(header)
print("-" * len(header))  # oddelovacia čiara

# vypíšeme riadky
for i in range(max_rows):
    row = ""
    for j, col in enumerate(columns):
        row += col[i].ljust(col_widths[j] + 2)
    print(row)

# vypíšeme počet slov pod stĺpcami
count_row = ""
for i, col in enumerate(columns):
    count_row += str(len([w for w in col if w != ""])).ljust(col_widths[i] + 2)
print("-" * len(header))
print(count_row)
