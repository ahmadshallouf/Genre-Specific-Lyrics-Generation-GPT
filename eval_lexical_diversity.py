from lexical_diversity import lex_div as ld
import json

# Opening JSON file and reading model predictions
f = open('generation_output.json')
data = json.load(f)
data.pop(0)
predictions = ""
for i in data:
    prompt = i[0]
    prediction = i[1]
    predictions = predictions + prediction


# Tokenize
tok = ld.tokenize(predictions)

# templatize
flt = ld.flemmatize(predictions)

print(ld.ttr(flt))
print(ld.mtld(flt))
#print(ld.mtld_ma_wrap(flt))
