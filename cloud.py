from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from arabic_reshaper import arabic_reshaper
from bidi.algorithm import get_display

file = open('txt-per.txt', encoding="utf-8")
reader = file.read()
text = arabic_reshaper.reshape(reader)
print(text)
text = get_display(arabic_reshaper.reshape(text))
stopwords = set(STOPWORDS)
stopwords.add("RT")
stopwords.add("text")
stopwords.add("https")
stopwords.add("co")

cloud = WordCloud(font_path='/Users/alisalehi/Library/Fonts/XNazanin.TTF', stopwords=stopwords).generate(get_display(arabic_reshaper.reshape(text))
)

image = cloud.to_image()
image.show()

#plt.imshow(cloud)
#plt.show()