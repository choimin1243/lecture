import pandas as pd
from collections import defaultdict

df = pd.read_csv("data/enrolment_1.csv")

boolean=df["year"]==1
boolean1=df["course name"]=="information technology"

df["status"]="allowed"

df.loc[boolean1&boolean,"status"]="not allowed"

boolean2=df["course name"]=="commerce"
boolean3=df["year"]==4

df.loc[boolean2&boolean3,"status"]="not allowed"

allowed=df["status"]=="allowed"
couse_name=df.loc[allowed,"course name"].value_counts()
boolean4=couse_name.loc[couse_name<5]

a=list(boolean4.index)

for i in a:
    df.loc[df["course name"]==i,"status"]="not allowed"
    
df
    