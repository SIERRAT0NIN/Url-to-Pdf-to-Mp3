from gtts import gTTS
import PyPDF2


with open("article.pdf", "rb") as pdf_file:
    pdf_file = open("article.pdf", "rb")
    pdfreader = PyPDF2.PdfReader(pdf_file)

all_text = ""

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace("\n", " ")
    all_text += clean_text + " "


tts = gTTS(all_text, lang="en")
tts.save("audio.mp3")
pdf_file.close()
