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
            print(self.instruction)

        with open(file_word, 'r') as file:
            words = file.readlines()
            list_word = [word.replace('\n', '') for word in words]
            self.words = list_word
            print(self.words)

    def replace_letter(self):
        new_words = {}
        for word in self.words:
            quantity = 0
            for record in self.instruction:
                quantity = quantity + word.count(record.split('=')[0])
                word = word.replace(record.split('=')[0], record.split('=')[1], -1)
            new_words[word] = quantity
        return new_words


zapros = Word('instruction.txt', 'word.txt').replace_letter()
print(zapros)
