import openpyxl
import json
 
# Define variable to load the dataframe
dataframe = openpyxl.load_workbook("words.xlsx")

with open("words_dict.json", "r", encoding="UTF-8") as file:
    words_dict = json.load(file)
# Define variable to read sheet
dataframe1 = dataframe.active
for row in range(1, dataframe1.max_row):
    tt_word = dataframe1[f"A{row}"]
    arab_word = dataframe1[f"B{row}"]
    
    if tt_word and arab_word:
        tt_word = tt_word.value
        arab_word = arab_word.value
        if tt_word and arab_word:
            words_dict["words"][tt_word] = arab_word
            print(f"{tt_word.lower()} - {arab_word}")
print(words_dict)
with open("words_dict.json", "w+", encoding="UTF-8") as file:
    json.dump(words_dict, file, ensure_ascii=False, indent=4)
