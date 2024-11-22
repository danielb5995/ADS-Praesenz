#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import statsmodels.formula.api as smf
import sweetviz as sw

import os


# In[2]:


FILENAMEDATA = os.path.join("input", "research_dataset.csv")
FILENAMEDATAREPORT = os.path.join("reports", "research_dataset.html")
CREATEREPORT = True


# In[3]:


dfData = pd.read_csv(FILENAMEDATA)
dfData


# In[4]:


dfData.info()


# In[5]:


"""
sales_calls Anzahl Anrufe SalesTeam
interactions Zusätzliche Interaktionen mit Kunden, wie sales_calls
economy Wirtschaftliche Lage (Hoch = Gut)
last_upgrade Wann wurde zuletzt geupdatet
discount Rabatt
monthly_usage Benutzungshäufigkeit (Hoch = viel)
ad_spend Kunde zahlt für Produkt
bugs_reported Anzahl Fehler gemeldet
did_renew Abo erneuert Ja Nein
"""


# In[6]:


if CREATEREPORT:
    report = sw.analyze(dfData)
    report.show_html(FILENAMEDATAREPORT)


# In[7]:


dfData.corr()


# In[13]:


dfData["interactions"].value_counts()


# In[14]:


rowSel = dfData["interactions"] == 0
dfData.loc[rowSel, "did_renew"].mean()


# In[15]:


dfData.loc[~rowSel, "did_renew"].mean()


# In[8]:


"+".join(dfData.columns)


# In[9]:


m = smf.logit(formula = "did_renew ~ interactions+economy+last_upgrade+discount+monthly_usage+ad_spend+bugs_reported", data = dfData).fit()
print(m.summary())


# In[10]:


m = smf.logit(formula = "did_renew ~ interactions+economy+last_upgrade+monthly_usage+bugs_reported", data = dfData).fit()
print(m.summary())


# In[11]:


m = smf.logit(formula = "did_renew ~ discount + ad_spend", data = dfData).fit()
print(m.summary())

