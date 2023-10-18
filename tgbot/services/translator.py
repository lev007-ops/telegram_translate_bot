# -*- coding: utf-8 -*-
import pyarabic.araby as araby
import re


def translate(text: str) -> str:
    for symbol in [".", ",", ";", "@", "$", "#"]:
        text = text.replace(symbol, f" {symbol}")
    lines = text.split('\n')  # Разделяем текст на строки
    translated_text = ""
    for line in lines:
        translated_line = ""
        words = line.split()
        for word in words:
            word = word.replace("ый", "ی")
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
                    translated_letter = "اي" if is_first else "ي"
                elif letter == "К":
                    is_letter_in_word1 = any(let in [
                        "а", "о", "у", "ы", "ъ"
                    ] for let in word)
                    is_letter_in_word2 = any(let in [
                        "ә", "ө", "ү", "е", "и", "ь"
                    ] for let in word)
                    if is_letter_in_word1:
                        translated_letter = "ق"
                    elif is_letter_in_word2:
                        translated_letter = "ك"
                    elif previous_letter == "ю":
                        translated_letter = "یوق"
                elif letter == "Ю":
                    if next_letter.upper() != "К":
                        translated_letter = "یو"
                    else:
                        translated_letter = ""
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
                # elif letter == "С":
                #     if (previous_letter in ["ә", "ү", "ө", "и", "ь"] or
                #             next_letter in ["ә", "ү", "ө", "и", "ь"]):
                #         translated_letter = "ﺱ"
                #     elif (previous_letter in ["а", "у", "о", "ы", "ъ"] or
                #             next_letter in c["а", "у", "о", "ы", "ъ"]):
                #         translated_letter = "ص"
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
                    is_letter_in_word1 = any(let in ["а", "у", "о", "ы"
                                                     ] for let in word)
                    is_letter_in_word2 = any(let in ["ә", "ү", "ө", "е", "и"
                                                     ] for let in word)
                    if (is_first and is_letter_in_word1
                            ) or previous_letter.upper() == "Ъ":
                        translated_letter = "یا"
                    elif (is_first and is_letter_in_word2
                          ) or previous_letter.upper() == "Ь":
                        translated_letter = "یە"
                elif letter == "М":
                    translated_letter = "م"
                elif letter == "Ь" or letter == "Ъ":
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
