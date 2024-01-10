import re
from constants import words, chars


class EmailClassifier:
    def __init__(self, model, scaler):
        self.model = model
        self.scaler = scaler

    def extract_frequency(self, text):
        text_lower = text.lower()

        total_words = len(re.findall(r'\b\w+\b', text_lower))
        total_cahrs = len(text_lower)

        word_frequency = {}
        for word in words:
            word_count = len(re.findall(r'\b' + re.escape(word) + r'\b', text_lower))
            word_frequency[word] = 100 * (word_count / total_words)

        char_frequency = {}
        for char in chars:
            char_count = text_lower.count(char)
            char_frequency[char] = 100 * (char_count / total_cahrs)

        return word_frequency, char_frequency


    def average_length(self, sequences):
        if not sequences:
            return 0
        total_length = sum(len(seq) for seq in sequences)
        return total_length / len(sequences)


    def longest_sequence_length(self, sequences):
        if not sequences:
            return 0
        return max(len(seq) for seq in sequences)


    def extract_capital(self, text):
        import re
        capital_sequences = re.findall(r'[A-Z]+', text)

        avg_length = self.average_length(capital_sequences)
        longest_length = self.longest_sequence_length(capital_sequences)
        total_capital_letters = sum(len(seq) for seq in capital_sequences)

        return avg_length, longest_length, total_capital_letters


    def extract_features(self, text):

        word_frequency, char_frequency = self.extract_frequency(text)
        avg_length, longest_length, total_capital_letters = self.extract_capital(text)

        features = {}

        for word in word_frequency:
            features[f"word_freq_{word}"] = word_frequency[word]
        
        for char in char_frequency:
            features[f"char_freq_{char}"] = char_frequency[char]

        features["capital_run_length_average"] = avg_length
        features["capital_run_length_longest"] = longest_length
        features["capital_run_length_total"] = total_capital_letters

        return features

    def predict(self, text):
        features = self.extract_features(text)
        x = list(features.values())
        x = self.scaler.transform([x])
        pred = self.model.predict(x)
        return int(pred[0])
