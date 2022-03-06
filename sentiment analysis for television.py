#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import os
from tqdm import tqdm


# In[ ]:


pip install transformers==4.16.2


# In[ ]:


print(transformers.__version__)


# In[ ]:


from transformers import pipeline


# In[ ]:


classifier=pipeline('sentiment-analysis',model='nlptown/bert-base-multilingual-uncased-sentiment')


# In[2]:


#Parameters for television
Rat=['rating','expert','user']
Gen=['launch','brand','model','warranty','box']
Dis=['type','size','resolution','refresh','rate','aspect','ratio','response','curved','slim','angles','viewing']
Phy=['colour','weight','dimension']
Vid=['analog','format','video','image']
Aud=['sound','audio','speakers']
Con=['connection','usb','ports','hdmi','mhl','3.5mm','port','input','socket','nfc']
Sma=['smart','wifi','band','mirroring','bluetooth','processor','apps']
Rem=['parent','remote','touch','internet','control','access']
Pow=['voltage','power','consumption','saving']


# In[ ]:


files=os.listdir(r"D:\skyshine_technologies\reviews\televisions")#Path where all review of products are stored


# In[ ]:


len(files)


# In[ ]:


for file in tqdm(files):
    print(file)
    data=pd.read_csv("D:/skyshine_technologies/reviews/televisions/"+file)
    data['review_description']=data['review_description'].str.lower()
    Ratings=[]
    General=[]
    Display=[]
    Physical_Design=[]
    Video=[]
    Audio=[]
    Connectivity_Ports=[]
    Smart_TV_Features=[]
    Remote=[]
    Power_Supply=[]
    for rat in tqdm(data['review_description']):
        try:
            for ra in Rat:
                if ra in rat:
                    Ratings.append(rat)
            for ge in Gen:
                if ge in rat:
                    General.append(rat)
            for di in Dis:
                if di in rat:
                    Display.append(rat)
            for ph in Phy:
                if ph in rat:
                    Physical_Design.append(rat)
            for vi in Vid:
                if vi in rat:
                    Video.append(rat)
            for au in Aud:
                if au in rat:
                    Audio.append(rat)
            for con in Con:
                if con in rat:
                    Connectivity_Ports.append(rat)
            for sma in Sma:
                if sma in rat:
                    Smart_TV_Features.append(rat)
            for rem in Rem:
                if rem in rat:
                    Remote.append(rat)
            for po in Pow:
                if po in rat:
                    Power_Supply.append(rat)
        except:
            pass
    df={
        "General":General,
        "Display":Display,
        "Design":Physical_Design,
        "Video":Video,
        "Audio":Audio,
        "Connection":Connectivity_Ports,
        "Smart_features":Smart_TV_Features,
        "Remote":Remote,
        "Power":Power_Supply}
    d = pd.concat([pd.DataFrame(list(set(v)), columns=[k]) for k, v in df.items()], axis=1)
    

    r=[]
    p=[]
    for a in tqdm(d):
        u=d[a].tolist()
        label=[]
        score=[]
        for b in u:
            try:
              label.append(classifier(b)[0]['label'])
              score.append(classifier(b)[0]['score'])
            except:
                pass
        if len(label) == 0:
            r.append(0)
        else:
            p=[]
            import re
            for a in label:
                temp = re.findall(r'\d+',a)
                res = list(map(int, temp))   
                p=p+res
            r.append(round(mean(p),1))
    a_series = pd.Series(r, index = d.columns)
    d = d.append(a_series, ignore_index=True)
    
    
    d.to_csv("D:/reviews/"+file,index=False)#Path to store output of all products 


# In[ ]:




