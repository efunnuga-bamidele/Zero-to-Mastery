from translate import Translator

translator =  Translator(to_lang="de")
try:
    with open('words.txt', mode='r') as my_text:
        text = my_text.read()
        translation = translator.translate(text);
        print(translation);
        with open('./test-de.txt', mode='w') as my_file:
            my_file.write(translation);
except FileNotFoundError as err:
    print('check your file please!')
