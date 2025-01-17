import spacy

def make_text(text, div):

    nlp = spacy.load("ru_core_news_sm")  # Используем модель для русского языка
    doc = nlp(text)

    title = ""
    subtitle = ""
    wrez =""
    for token in doc:
        if token.text in [".", "?", "!", ":", ","]:  # Проверяем, является ли токен разделителем
            title = " ".join([t.text for t in doc[:token.i]])
            subtitle = " ".join([t.text for t in doc[token.i + 1:]]).strip()
            print("Title:", title)
            break  # Выходим из цикла, если нашли разделитель

    doc = nlp(subtitle)
    for token in doc:
        if token.text in [".", "?", "!", ":", ",", "-"]:
            subtitle = " ".join([t.text for t in doc[:token.i]])
            wrez = " ".join([t.text for t in doc[token.i + 1:]]).strip()
            print("subtitle:", subtitle)
            print("wrez:", wrez)
            break

    if title == "":
        title = text
        print("Title:", title)

    if div ==1:
        return text
    if div==2:
        return title, subtitle+wrez
    if div ==3:
        return title, subtitle, wrez

