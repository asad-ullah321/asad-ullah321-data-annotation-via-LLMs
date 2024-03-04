import pandas as pd
import csv
import openpyxl
# Read the CSV file
df = pd.read_csv("Corona_NLP_test.csv")


tweets_str = """
You will help me label the training dataset for sentiment analysis. tweets will be provided and you will label them with the following four tags 

1. "Positive"

2.  "Extremely positive"  

3. "Extremely Negative"

4. "Negative"

Information Related to Dataset: The dataset contains tweets about corona virus and related things from the period of covid 19

for reference here are some example for you

tweet: "TRENDING: New Yorkers encounter empty supermarket shelves (pictured, Wegmans in Brooklyn), sold-out online grocers (FoodKick, MaxDelivery) as #coronavirus-fearing shoppers stock up https://t.co/Gr76pcrLWh https://t.co/ivMKMsqdT1"
label: "Extremely Negative"

tweet: "When I couldn't find hand sanitizer at Fred Meyer, I turned to #Amazon. But $114.97 for a 2 pack of Purell??!!Check out how  #coronavirus concerns are driving up prices. https://t.co/ygbipBflMY"
label: "Positive"

tweet: "Find out how you can protect yourself and loved ones from #coronavirus. ?"
label: "Extremely Positive"

tweet: "#Panic buying hits #NewYork City as anxious shoppers stock up on food&amp;medical supplies after #healthcare worker in her 30s becomes #BigApple 1st confirmed #coronavirus patient OR a #Bloomberg staged event? https://t.co/IASiReGPC4 #QAnon #QAnon2018 #QAnon2020 #Election2020 #CDC https://t.co/29isZOewxu"
label: "Negative"

tweet: "Voting in the age of #coronavirus = hand sanitizer ? #SuperTuesday https://t.co/z0BeL4O6Dk"
Label: "Positive"

tweet: "HI TWITTER! I am a pharmacist. I sell hand sanitizer for a living! Or I do when any exists. Like masks, it is sold the fuck out everywhere. SHOULD YOU BE WORRIED? No. Use soap. SHOULD YOU VISIT TWENTY PHARMACIES LOOKING FOR THE LAST BOTTLE? No. Pharmacies are full of sick people."
Label: "Extremely Negative"

tweet: "Anyone been in a supermarket over the last few days? Went to do my NORMAL shop last night &amp; ??is the sight that greeted me. Barmy! (Btw, whatÂ’s so special about tinned tomatoes? ????????????). #Covid_19 #Dublin https://t.co/rGsM8xUxr6"
Label: "Extremely Positive"

tweet: ""Best quality couches at unbelievably low prices available to order.
We are in Boksburg GP 
For more info WhatsApp:
084 764 8086
#SuperTuesdsy #PowerTalk 
#Covid_19 #SayEntrepreneur 
#DJSBU https://t.co/HhDJhyQ2Dc"
Label: "Positive"

tweet: "Beware of counterfeits trying to sell fake masks at cheap prices. Let's defeat coronavirus threat, #Covid_19 collectively. #BeSafe #BeACascader #CoronavirusReachesDelhi 
#coronavirusindia 
https://t.co/2Ikkmimj4f https://t.co/RB9rtt7Nkc"
Label: "Extremely Negative"

tweet: "Panic food buying in Germany due to #coronavirus has begun.  But the #organic is left behind! #Hamsterkauf
Panic buying is called ""Hamster purchases""(HamsterkÃ¤ufe) in German, taken from the way Hamsters stuff their cheeks with food.  
https://t.co/aYQtLLGW1m"
Label: "Extremely Negative"

tweet: "#Covid_19 Went to the Grocery Store, turns out all cleaning supplies have been bought out for fear of Coronavirus. My daughter's substitute teacher showed her class how to make hand sanitizer. Now I just need to buy some 100% alcohol. Wish me luck that any stores will have it."
Label: "Extremely Positive"

tweet: "While we were busy watching election returns and bracing for a Covid-19 outbreak, Trump nominated a chemical-industry lobbyist to head the Consumer Product Safety Commission https://t.co/M2ShHI1Tn0"
Label: "Positive"

tweet: "What Precautionary measures have you all taken in your respective Restaurants and Hotels, Comment below...
#COVID-19 #Coronavirus
COVID-19: Hotel chains enforce precautionary measures, issue safety, hygiene advisories
https://t.co/7Zo2vqSPzY"
Label: "Extremely Positive"

here is a tweet which you will label

tweet: 
"""

prompt_part3 = """ label:
Note: There is a difference between negative and extremely negative, on default, you label extremely label as negative try your best to distinguish between them. The same goes for Positive and extremely positive. And sentiment should be based on what it said regarding virus and how this tweet will effect the knowldge of people regarding virus

answer format: your response should only contain the label and reason why you label it like that\
    """

# Iterate over each row in the dataframe
prompts = []
for index, row in df.iterrows():
    tweet = row['OriginalTweet']
    newPrompt = tweets_str + tweet + prompt_part3
    prompts.append(newPrompt)

    
  


xlsx_file = "prompts.xlsx"

# Create a new workbook
workbook = openpyxl.Workbook()

# Get the active worksheet
sheet = workbook.active

# Writing 1D array (single column) data to Excel file
for item in prompts:
    sheet.append([item])

# Save the workbook to an Excel file
workbook.save(xlsx_file)

print("Excel file has been created successfully!")
