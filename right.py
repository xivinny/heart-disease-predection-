#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pickle
import numpy as np
pkl_filename = 'ANN_classifier.pkl'


# In[5]:


model_pkl = open(pkl_filename, 'rb')
model = pickle.load(model_pkl)


# In[6]:


Xnew =np.array([[63.0,1.0,1.0,145.0,233.0,1.0,2.0,150.0,0.0,2.3,3.0,0.0,6.0]])
# make a prediction
ynew = model.predict(Xnew)
# show the inputs and predicted outputs
#print(ynew)


# In[7]:


Xnew =np.array([[62.0,0.0,4.0,140.0,268.0,0.0,2.0,160.0,0.0,3.6,3.0,2.0,3.0]])
# make a prediction
ynew = model.predict(Xnew)
# show the inputs and predicted outputs
#print(ynew)


# In[8]:


#print(Xnew.shape)
#print(Xnew)


# In[15]:


file1 = open("pythondata.txt","r")
#print (file1.read())
for line in file1:
    fields=line.split(",")
aa=np.asarray(fields)
#print(fields)
y = aa.astype(np.float)
#print(y)


# In[16]:


#print(y.shape)
y=y.reshape((y.shape[0],1))
y.shape =(1,13)
#print(y.shape)
#print(y)


# In[17]:


ynew = model.predict(y)
# show the inputs and predicted outputs
f = open("result_of_heart-disease.txt","w+")
print(ynew)
if(ynew == ['1']):
	f.write("YES")
else:
	f.write("NO")
f.close()
print("anwar")


# In[ ]:




