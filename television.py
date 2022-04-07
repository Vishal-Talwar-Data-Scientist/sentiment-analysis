#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re


# In[4]:


#AC
Rat=[re.compile('rat.*'),re.compile('expe.*'),re.compile('user.*')]
Gen=[re.compile('launch.*'),re.compile('brand.*'),re.compile('model.*'),re.compile('warrant.*'),re.compile('operat.*'),re.compile('box.*')]
Basic=[re.compile('type.*'),re.compile('capacit.*'),re.compile('star.*'),re.compile('bee.*'),re.compile('colo.*'),re.compile('type.*'),re.compile('cool.*'),re.compile('heat.*'),re.compile('compres.*'),re.compile('mode.*'),re.compile('condens.*'),re.compile('coil.*'),re.compile('remot.*'),re.compile('contr.*')]
Dimensions=[re.compile('dimens.*'),re.compile('length.*'),re.compile('width.*'),re.compile('heigh.*'),re.compile('weight.*'),re.compile('indo.*')]
Performance=[re.compile('noise.*'),re.compile('turb.*'),re.compile('pane.*'),re.compile('iseer.*'),re.compile('cool.*'),re.compile('indo.*')]
power=[re.compile('power.*'),re.compile('requir.*'),re.compile('consom.*')]
AirFlow_Filter=[re.compile('air.*'),re.compile('swing.*'),re.compile('bacteri.*'),re.compile('dust.*'),re.compile('filter.*')]
Remote=[re.compile('batter.*'),re.compile('back.*'),re.compile('button.*')]
convenience=[re.compile('restart.*'),re.compile('quiet.*'),re.compile('sleep.*'),re.compile('memor.*'),re.compile('diagnosis.*'),re.compile('self.*'),re.compile('convenience.*')]


# In[ ]:


for file in tqdm(t[1:]):
    data=pd.read_csv("D:/skyshine_technologies/reviews/air_conditioners/"+file)
    data['review_description']=data['review_description'].str.lower()
    Ratings=[]
    General=[]
    basic=[]
    Dimension=[]
    Perfor=[]
    Power=[]
    airflow=[]
    remot=[]
    conven=[]
    for rat in tqdm(data['review_description']):
        try:
            for r in Rat:
                if r.search(rat):
                    Ratings.append(rat)
            for r in Gen:
                if r.search(rat):
                    General.append(rat)
            for r in Basic:
                if r.search(rat):
                    basic.append(rat)
            for r in Dimensions:
                if r.search(rat):
                    Dimension.append(rat)
            for r in Performance:
                if r.search(rat):
                    Perfor.append(rat)
            for r in power:
                if r.search(rat):
                    Power.append(rat)
            for r in AirFlow_Filter:
                if r.search(rat):
                    airflow.append(rat)
            for r in Remote:
                if r.search(rat):
                    remot.append(rat)
            for r in convenience:
                if r.search(rat):
                    conven.append(rat)
        except:
            pass
        
    df={
        "Rating":list(set(Ratings)),
        "General":list(set(General)),
        "Basic":list(set(basic)),
        "Dimension":list(set(Dimension)),
        "Performance":list(set(Perfor)),
        "Power":list(set(Power)),
        "Airflow_filter":list(set(airflow)),
        "Remote":list(set(remot)),
        "Convenience":list(set(conven))}
    d = pd.concat([pd.DataFrame(list(set(v)), columns=[k]) for k, v in df.items()], axis=1)
    ru=[]
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
            ru.append(0)
        else:
            p=[]
            import re
            for a in label:
                temp = re.findall(r'\d+',a)
                res = list(map(int, temp))   
                p=p+res
            ru.append(round(mean(p),1))
    y=[]
    for a in zip(col,ru):
        y.append(a)
    u=pd.DataFrame(y).transpose()
    u.columns = u.iloc[0]
    u = u.drop(0)
    u.reset_index(inplace=True)
    u.drop(['index'],axis=1,inplace=True)
    r=u[-1:]
    pros=[]
    cons=[]
    for a in r:
        if float(r[a])>0.0:
            if a=='Rating':
                if float(r[a])<=3.4:
                    print(float(r[a]))
                    cons.append("Overall Rating"+" is "+ numpy.random.choice(['bad','not good','terrible']))
                else:
                    pros.append("Overall Rating"+" is "+numpy.random.choice(['good','excellent','great','awesome']))

            if a=='General':
                if float(r[a])<=3.4:
                    print(float(r[a]))
                    cons.append("Overall product"+" is "+ numpy.random.choice(['bad','not good','terrible']))
                else:
                    pros.append("Overall product"+" is "+numpy.random.choice(['good','excellent','great','awesome']))
            if a=='Basic':
                if float(r[a])<=3.4:
                    print(float(r[a]))
                    cons.append(a+" quality is "+ numpy.random.choice(['bad','not good','terrible']))
                else:
                    pros.append(a+" quality is "+numpy.random.choice(['good','excellent','great','awesome']))
            if a=='Dimension':
                if float(r[a])<=3.4:
                    print(float(r[a]))
                    cons.append("Product "+a+" is "+numpy.random.choice(['bad','not good','terrible']))
                else:
                    pros.append("Product "+a+" is "+numpy.random.choice(['good','excellent','great','awesome']))                 
            if a=='Performance':
                if float(r[a])<=3.4:
                    print(float(r[a]))
                    cons.append("Product "+a+" is "+numpy.random.choice(['bad','not good','terrible']))
                else:
                    pros.append("Product "+a+" is "+numpy.random.choice(['good','excellent','great','awesome']))
            if a=='Power':
                if float(r[a])<=3.4:
                    print(float(r[a]))
                    cons.append("Power consumption "+a+" is "+numpy.random.choice(['bad','not good','terrible']))
                else:
                    pros.append("Power consumption" +a+" is "+numpy.random.choice(['good','excellent','great','awesome']))
            if a=='Airflow_filter':
                if float(r[a])<=3.4:
                    print(float(r[a]))
                    cons.append(numpy.random.choice(['bad','terrible'])+" Remote access")
                else:
                    pros.append(numpy.random.choice(['excellent','great','awesome'])+" Remote access") 

            if a=='Remote':
                if float(r[a])<=3.4:
                    print(float(r[a]))
                    cons.append(numpy.random.choice(['bad','terrible'])+" Remote access")
                else:
                    pros.append(numpy.random.choice(['excellent','great','awesome'])+" Remote access")
            if a=='Convenience':
                if float(r[a])<=3.4:
                    print(float(r[a]))
                    cons.append(numpy.random.choice(['bad','terrible'])+" Smart Features")
                else:
                    pros.append(numpy.random.choice(['excellent','great'])+" Smart Features")
    if len(pros)==0:
        d['pros']=pd.Series(pros,dtype='float64')
    else:
        d['pros']=pd.Series(pros)
    if len(cons)==0:
        d['cons']=pd.Series(cons,dtype='float64')
    else:
        d['cons']=pd.Series(cons)

    y=[]
    for a in zip(rer,ru):
        y.append(a)
    rr=pd.DataFrame(y).transpose()
    rr.columns = rr.iloc[0]
    rr = rr.drop(0)
    rr.reset_index(inplace=True)
    rr.drop(['index'],axis=1,inplace=True)
    fin=pd.concat([d,rr], axis=1)
    fin.to_csv(r"D:/reviews/"+file,index=False)






    

    


# In[ ]:




