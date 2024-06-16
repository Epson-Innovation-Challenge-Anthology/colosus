import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import STOPWORDS, WordCloud

MASK_PATH = "flower-image.jpeg"
TXT_PATH = "pink-muhly-paper.txt"
STOPWORDS_PATH = "stopwords.txt"
FONT_PATH = "PretendardVariable.ttf"

# mask layer ready
alice_mask = np.array(Image.open(MASK_PATH))

# read the text
with open(TXT_PATH, "r", encoding="utf-8") as f:
    text = f.read()

# read stopwords
with open(STOPWORDS_PATH, "r", encoding="utf-8") as f:
    stopwords = f.read().split("\n")

# stopwords
stopwords = set(STOPWORDS)
stopwords.union(set(stopwords))

# making wordcloud
wc = WordCloud(
    max_words=100,
    font_path=FONT_PATH,
    stopwords=stopwords,
    background_color="white",
    mask=alice_mask,
).generate(text)

# NOTE: DEBUG
# print(wc.words_)

# visualize
plt.figure(figsize=(20, 5))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()

# save
wc.to_file("wordcloud-result.png")
