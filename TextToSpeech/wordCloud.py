from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd



tokens = "Hello World my name is Gaurav Srivastava I live in Noida ,basically I am from Raebareli uttar pradesh".split()

tokens = "Potential use cases: Distracted driver detection (Gaurav Srivastava) According to the CDC motor vehicle " \
         "safety division, one in five car accidents is caused by a distracted driver. Sadly, this translates to 425," \
         "000 people injured and 3,000 people killed by distracted driving every year. We can use computer vision " \
         "deep learning techniques to build such product and deploy over raspberry pi ,and it can be used as smart " \
         "tracker that raises alarms in case driver is texting or calling or distracted while driving … for more " \
         "details we can refer https://www.kaggle.com/c/state-farm-distracted-driver-detection/overview We can use " \
         "edge device(raspberry pi) to deploy this and can be sold/projected as KSOLVES product .. maybe we need more " \
         "brainstorming over this . Mask and no Mask app (Gaurav Srivastava)  Integrating this app with doors , " \
         "allow people if they are wearing masks Data can be generated for this , for people wearing mask and no mask " \
         ". Helmet and no Helmet app (Amit Chand) Integrating this app with doors , ATM, if the whole face is " \
         "covered. Do not let the door open or use the ATM machine. Social Distancing Application (Gaurav Srivastava) " \
         "AI-enabled social distancing detection tool that can detect if people are keeping a safe distance from each " \
         "other by analyzing real time video streams from the camera. For example, at a factory that produces " \
         "protective equipment, technicians could integrate this software into their security camera systems to " \
         "monitor the working environment with easy calibration steps. As the demo shows below, the detector could " \
         "highlight people whose distance is below the minimum acceptable distance in red, and draw a line between to " \
         "emphasize this. The system will also be able to issue an alert to remind people to keep a safe distance if " \
         "the protocol is violated. Demo  For more details "


#tokens = tokens.split()


print(tokens)

comment_words = ''

comment_words += " ".join(tokens)+" "

print(comment_words)

wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',

                min_font_size = 10).generate(tokens)

# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()


