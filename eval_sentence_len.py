import json
import pandas as pd


def process_prompt(param_prompt):
    if param_prompt.startswith("Generate music lyrics"):
        result = param_prompt.split("for genre ", 1)[1].split(", topic")[0]
    elif param_prompt.startswith("Generate lyrics in genre"):
        result = param_prompt.split("lyrics in ", 1)[1].split(" about")[0]
    elif param_prompt.startswith("For genre"):
        result = param_prompt.split("For genre ", 1)[1].split(" generate")[0]
    else:
        result = param_prompt.split("Generate ", 1)[1].split(" lyrics")[0]
    return result


# Opening JSON file and reading model predictions
f = open('generation_output.json')
data = json.load(f)
data.pop(0)
genres = {'pop': '', 'country': '', 'blues': '', 'jazz': '', 'reggae': '', 'hip hop': ''}
predictions = ""
for i in data:
    prompt = i[0]
    prediction = i[1]
    res = process_prompt(prompt)
    genres[res] = genres[res] + prediction

avg_sen_len_pred = {'pop': 0, 'country': 0, 'blues': 0, 'jazz': 0, 'reggae': 0, 'hip hop': 0}


def avg_sentence_len(text):
    sentences = text.split(".")  # split the text into a list of sentences.
    words = text.split(" ")  # split the input text into a list of separate words
    if sentences[len(sentences) - 1] == "":  # if the last value in sentences is an empty string
        average_sentence_length = len(words) / len(sentences) - 1
    else:
        average_sentence_length = len(words) / len(sentences)
    return average_sentence_length  # returning avg length of sentence


for key, value in genres.items():
    avg_sen_len_pred[key] = avg_sentence_len(value)

print(avg_sen_len_pred)

df = pd.read_csv('data/tcc_ceds_music.csv', index_col=0, encoding='unicode_escape')

cols = [3, 4, 28]
df = df[df.columns[cols]]
print(df)

avg_sen_len_dt = {'pop': 0, 'country': 0, 'blues': 0, 'jazz': 0, 'reggae': 0, 'hip hop': 0}
for genre in df.genre.unique():
    df_genre = df.loc[df['genre'] == genre]
    concatenated = '.'.join(df_genre['lyrics'].tolist())
    avg_sen_len_dt[genre] = avg_sentence_len(concatenated)

print(avg_sen_len_dt)
