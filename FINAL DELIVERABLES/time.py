'''from datetime import datetime
import pandas as pd
# Get current time in local timezone
current_time = datetime.now()
print('Current timestamp: ', current_time.strftime('%H:%M:%S'))

n = 2
# Add 2 minutes to datetime object containing current time
future_time = current_time + pd.DateOffset(minutes=n)
print('Future Time (2 minutes from now ): ', future_time)
# Convert datetime object to string in specific format
future_time_str = future_time.strftime('%H:%M:%S')
print('Future Time as string object: ', future_time_str)'''



from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = 'Welcome to geeksforgeeks!'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")
#myobj.save("welcome1.wav")
# Playing the converted file
#os.system("welcome.mp3")
#os.system("welcome1.mp3")






from pygame import mixer  # Load the popular external library

mixer.init()
mixer.music.load('./welcome.mp3')
mixer.music.play()