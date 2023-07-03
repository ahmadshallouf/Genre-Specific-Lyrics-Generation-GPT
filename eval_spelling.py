from autocorrect import Speller
import evaluate
import json
import random
import time

start = time.time()

spell = Speller(lang='en')

# Opening JSON file and reading model predictions
f = open('generation_output.json')
data = json.load(f)
data.pop(0)
predictions = ""

random.seed = 42
count = 0

for i in data:
    if random.random() < 0.99:
        continue
    count += 1
    prompt = i[0]
    prediction = i[1]
    predictions = predictions + prediction

print('number of predictions to evaluate: ', count)
# Correct spelling
corrected_predictions = spell(predictions)

print('spelling corrected')

# Evaluate spelling
rouge = evaluate.load('rouge')
predictions = [predictions]
references = [corrected_predictions]

print('evaluating')

results = rouge.compute(predictions=predictions, references=references)

print(results)

end = time.time()
print(end - start)
