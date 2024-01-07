# -*- coding: utf-8 -*-
import pyarabic.araby as araby
import json


def load_dict(path: str = "words_dict.json") -> dict:
    with open(path, "r", encoding="UTF-8") as file:
        words_dict = json.load(file)
    return words_dict["words"]


def load_endings_dict(path: str = "endings_dict.json") -> dict:
    with open(path, "r", encoding="UTF-8") as file:
        endings_dict = json.load(file)
    return endings_dict["endings"]


def translate(text: str) -> str:
    words_dict = load_dict()
    endings_dict = load_endings_dict()
    for symbol in [".", ",", ";", "@", "$", "#", "/", "?", "!"]:
        text = text.replace(symbol, f" {symbol}")
    text = text.replace("?", "؟")
    lines = text.split('\n')  # Разделяем текст на строки
    translated_text = ""
    for line in lines:
        translated_line = ""
        words = line.split()
        for word in words:
            if dict_word := words_dict.get(word.lower(), None):
                translated_line += f"{dict_word} "
                continue
            do_cont = True
            for ending in endings_dict.keys():
                if word.lower().endswith(ending):
                    im_word = word.lower().replace(ending, "")
                    if dict_word := words_dict.get(im_word.lower(), None):
                        translated_line += (f"{dict_word}"
                                            f"{endings_dict[ending]} ")
                        do_cont = False
                        break
            if not do_cont:
                continue
            original_word = word
            word = word.replace("ый", "ی")
            word = word.replace("ту", "تو")
            for let in ["да", "дә", "та", "тә"]:
                if word.endswith(let):
                    word = word.replace(let, "ده")
            for let in ["дан", "нән", "нан", "тән", "тан", "дән"]:
                if word.endswith(let):
                    word = word.replace(let, "دن")
            for let in ["лар", "ләр", "нар", "нәр"]:
                if word.endswith(let):
                    word = word.replace(let, "لر")
            for let in ["ып", "еп"]:
                if word.endswith(let):
                    word = word.replace(let, "وب")
            if word.endswith("ап"):
                word = word.replace(let, "اب")
            if word.endswith("әп"):
                word = word.replace(let, "ەب")
            for let in ["дыр", "дер", "тыр", "тер"]:
                if word.endswith(let):
                    word = word.replace(let, "در")
            for let in ["га", "ка"]:
                if word.endswith(let):
                    word = word.replace(let, "غە")
            for let in ["гә", "кә"]:
                if word.endswith(let):
                    word = word.replace(let, "گە")
            for let in ["ма", "мә"]:
                if word.endswith(let):
                    word = word.replace(let, "مە")
            for let in ["ча", "чә"]:
                if word.endswith(let):
                    word = word.replace(let, "چە")
            for let in ["ча", "чә"]:
                if word.endswith(let):
                    word = word.replace(let, "چە")
            for let in ["на", "нә"]:
                if word.endswith(let):
                    word = word.replace(let, "نە")

            translated_word = ""
            for index, letter in enumerate(list(word)):
                translated_letter = ""
                original_letter = letter
                letter = letter.upper()
                is_first = index == 0
                is_last = (index + 1) == len(word)
                previous_letter = "" if is_first else word[index - 1].lower()
                next_letter = "" if is_last else word[index + 1].lower()

                if letter == "А":
                    translated_letter = "آ" if is_first else "ا"
                elif letter == "Ә":
                    translated_letter = "ئە" if is_first else "ە"
                elif letter == "Б":
                    translated_letter = "ب"
                elif letter == "В":
                    translated_letter = "و"
                elif letter == "Г":
                    if next_letter in [
                        "а", "о", "у", "ы", "ъ"
                    ] or (previous_letter in [
                            "а", "о", "у", "ы", "ъ"]):
                        translated_letter = "غ"
                    elif (next_letter in [
                        "ә", "ө", "ү", "е", "и", "ь"
                    ]) or (previous_letter in [
                            "ә", "ө", "ү", "е", "и", "ь"]):
                        translated_letter = "گ"
                elif letter == "Д":
                    translated_letter = "د"
                elif letter == "Е":
                    if previous_letter in [
                        "а", "о", "у", "ә", "ө", "ү", "и", "ы"
                    ] or is_first:
                        translated_letter = "ي"
                    elif is_last:
                        translated_letter = "ی"
                elif letter == "Ж":
                    translated_letter = "ژ"
                elif letter == "Җ":
                    translated_letter = "ج"
                elif letter == "З":
                    translated_letter = "ز"
                elif letter == "И":
                    translated_letter = "اي" if is_first else "ي"
                elif letter == "Й":
                    translated_letter = "ي" if is_first else "ي"
                elif letter == "К":
                    is_letter_in_word1 = any(let in [
                        "а", "о", "у", "ы", "ъ"
                    ] for let in original_word)
                    is_letter_in_word2 = any(let in [
                        "ә", "ө", "ү", "е", "и", "ь"
                    ] for let in original_word)
                    if is_letter_in_word1:
                        translated_letter = "ق"
                    elif is_letter_in_word2:
                        translated_letter = "ك"
                elif letter == "Ю":
                    translated_letter = "يو"
                elif letter == "Л":
                    translated_letter = "ل"
                elif letter == "Н":
                    translated_letter = "ن"
                elif letter == "Ң":
                    translated_letter = "ڭ"
                elif letter == "О":
                    translated_letter = "او" if is_first else "و"
                elif letter == "Ө":
                    translated_letter = "ئو" if is_first else "و"
                elif letter == "П":
                    translated_letter = "پ"
                elif letter == "Р":
                    translated_letter = "ﺭ"
                elif letter == "С":
                    translated_letter = "س"
                elif letter == "Т":
                    translated_letter = "ت"
                elif letter == "У":
                    translated_letter = "او" if is_first else "و"
                elif letter == "Ү":
                    translated_letter = "ئو" if is_first else "و"
                elif letter == "Ф":
                    translated_letter = "ف"
                elif letter == "Х":
                    translated_letter = "خ"
                elif letter == "Һ":
                    translated_letter = "ه"
                elif letter == "Ц":
                    translated_letter = "تس"
                elif letter == "Ч":
                    translated_letter = "چ"
                elif letter == "Ш":
                    translated_letter = "ش"
                elif letter == "Щ":
                    translated_letter = "چ"
                elif letter == "Ы":
                    if is_last:
                        translated_letter = "ی"
                    elif is_first:
                        translated_letter = "ا"
                elif letter == "Э":
                    translated_letter = "ا" if is_first else "ي"
                elif letter == "Я":
                    if previous_letter in ["о", "у", "а", "ы"]:
                        translated_letter = "يا"
                    elif previous_letter in ["и", "ө", "ү", "ә", "е"]:
                        translated_letter = "يه"
                    elif is_first and any(let in ["ө", "ү", "ә", "е"] for let in original_word):
                        translated_letter = "يه"
                    elif is_first and any(let in ["о", "у", "а", "ы"] for let in original_word):
                        translated_letter = "يا"
                    else:
                        translated_letter = ""
                elif letter == "М":
                    translated_letter = "م"
                elif letter in ["Ь", "Ъ"]:
                    translated_letter = ""
                else:
                    translated_letter = original_letter
                translated_word += translated_letter.strip()
            translated_line += f"{translated_word} "
        translated_text += f"{translated_line.strip()}\n"

    # Замены для объединения букв
    ligature_replacements = {
        "ﺭﺭ": "رر",
        "ﺭ": "ر",
        "چی": "چی",
        "س": "س",

        # Добавьте другие замены по мере необходимости
    }

    # Проходим по словарю и заменяем соответствия в тексте
    for ligature, replacement in ligature_replacements.items():
        translated_text = translated_text.replace(ligature, replacement)
    # Функция araby.strip_tashkeel удаляет диакритические знаки
    text_stripped = araby.strip_tashkeel(translated_text)

    # Функция araby.normalize_ligature объединяет буквы в лигатуры
    translated_text = araby.normalize_ligature(text_stripped)

    return translated_text
