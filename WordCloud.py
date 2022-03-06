import PyPDF4
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def pdfR(address):
    pdfFileObj = open(address, 'rb')
    pdfReader = PyPDF4.PdfFileReader(pdfFileObj)
    page = pdfReader.numPages

    pageObj = ''
    pageW = ''

    for i in range(page):
        pageObj= pdfReader.getPage(i)
        pageW = pageW + pageObj.extractText()
    
    pdfFileObj.close()
    return pageW

def WC(pdf,p):
    png = 'C:\\Users\\Dell\\Desktop\\Aditi\\img.png'
    ourMask = np.array(Image.open(png))

    stopw = set(STOPWORDS)
    cloud = WordCloud(background_color='black', mask=ourMask ,stopwords=stopw )
    wordcloud = cloud.generate(pdf)
    
    
    plt.imshow(cloud)
    plt.axis('off')
    plt.savefig("C:\\Users\\Dell\\Desktop\\Aditi\\MHealth_and_big-data_integration_Promises_for_heal.jpeg")
    print("Task Completed . Kindly Check WordCloud PNG in folder.")
def main():
    i = input("Provide Full Path of PDF File:-\n") #C:\Users\Dell\Desktop\Demo\MarvellousInfosystems_PlayPredictor - Copy.pdf
    p = input("Provide Image Full Path:-\n") #C:\Users\Dell\Desktop\Demo\png - Copy - Copy - Copy (2) - Copy - Copy - Copy - Copy.png
    WC(pdfR(i),p)
    
if __name__=="__main__":
    main() 