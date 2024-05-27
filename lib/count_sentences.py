import re

class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            raise ValueError("Value must be a string")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Using a regex to split on ., !, or ?
        sentence_endings = re.split(r'[.!?]', self.value)
        # Filter out any empty strings from the list
        sentences = [s for s in sentence_endings if s.strip()]
        return len(sentences)

# Example usage:
string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.is_sentence())        # False
print(string.is_question())        # True
print(string.is_exclamation())     # False
print(string.count_sentences())    # 3
