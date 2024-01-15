class FeatureExtractor2:
  
  def __init__(self, words):
    self.words = words

  def extract_features(self, text: str):

    features = dict.fromkeys(self.words, 0)

    for word in self.words:
      word_count = text.count(word)
      features[word] = word_count

    return features