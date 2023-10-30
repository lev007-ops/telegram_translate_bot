import nltk
from nltk.stem import SnowballStemmer

# Создайте объект лемматизатора для татарского языка
tatar_lemmatizer = SnowballStemmer("tatar")

# Ваш словарь слов с окончаниями
dictionary = {
    'китаплар': 'книги',
    'балаларга': 'детям',
    # Добавьте другие слова
}


# Функция для поиска слова без учёта окончаний
def search_word(word):
    lemma = tatar_lemmatizer.stem(word)  # Лемматизация
    return dictionary.get(lemma, 'Слово не найдено')


# Пример использования
word_to_translate = 'китапларнын'
translation = search_word(word_to_translate)
print(f'{word_to_translate} переводится как {translation}')
