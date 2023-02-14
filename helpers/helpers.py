import csv
import re
import emoji
import demoji
with open('random_reviews.tsv') as f:
    r_1 = []
    r_2 = []
    for line in f:
        fields = line.strip().split('\t')
        if 'a.py' in line:
            continue
        if hash(line) % 2:
            r_1.append(line)
        else:
            r_2.append(line)

SEPARATORS = {
    '!',
    '?',
    '.',
    ';',
    '\n',
}

NEED_TO_DELETE_CHAR = {
    ':)',
    '+/-',
    ':(',
    ')',
    '(',
    '"',
    '\n',
    '******',
    '**',
    '👍🏽',
    '🫣',
    ' 🫠',
    ' 🫶',
}


def deEmojify(text):
    regrex_pattern = re.compile(
        pattern="["
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                "]+",
        flags=re.UNICODE,
    )
    return regrex_pattern.sub(r'', text)

def remove_emoji(string):
    return emoji.get_aliases_unicode_dict().values().sub(u'', string)

def get_separated_line(line: str) -> list | None:
    for sep in SEPARATORS:
        line = line.replace(sep, '\t').strip()
    for del_char in NEED_TO_DELETE_CHAR:
        line = demoji.replace(
            line.replace(del_char, '').strip(), ""
        )

    line = line.replace('\t\t', '\t').split('\t')
    for i, l in enumerate(line):
        line[i] = deEmojify(l).strip()
    line = list(filter(lambda x: len(x) > 5, line))
    return list(filter(lambda x: x != '', line))


res_1 = []
res_2 = []

for row in r_1:
    for review in get_separated_line(row.split('\t')[1]):
        res_1.append([row.split('\t')[0], review])

for row in r_2:
    for review in get_separated_line(row.split('\t')[1]):
        res_2.append([row.split('\t')[0], review])

# SAVING
fields = ['блюдо', 'отзыв']
print('SAVING...')
with open(f'random_reviews_chunk_1.csv', 'w') as file:
    writer = csv.writer(file, )
    writer.writerow(fields)
    writer.writerows(res_1)

with open(f'random_reviews_chunk_2.csv', 'w') as file:
    writer = csv.writer(file, )
    writer.writerow(fields)
    writer.writerows(res_2)
