class Word:
    def __init__(self, file_instruction, file_word):
        """ With initialization open two files
        1: file with instruction
        2: file whit words for replace
        in attributes stored:
         list instruction for replace
         list words for replace letter
        """

        with open(file_instruction, 'r') as file:
            instruction = file.readlines()
            list_instruction = [record.replace('\n', '') for record in instruction]
            self.instruction = list_instruction

        with open(file_word, 'r') as file:
            words = file.readlines()
            list_word = [word.replace('\n', '') for word in words]
            self.words = list_word

    def replace_letter(self):
        new_words = {}
        for word in self.words:
            quantity = 0
            for record in self.instruction:
                quantity = quantity + word.count(record.split('=')[0])
                word = word.replace(record.split('=')[0], record.split('=')[1], -1)
            new_words[word] = quantity
        new_words = sorted(new_words.items(), key=lambda item: item[1], reverse=True)
        list_words = [pair[0] for pair in new_words]
        return list_words

instruction = input("Введите имя файла с инструкциями по замене: ")
list_word = input("Введите имя файла со списком слов в которых нужно заменить буквы или их сочетания: ")
result = Word(instruction, list_word).replace_letter()
for word in result:
    print(word)

