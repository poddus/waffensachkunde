import pandas as pd

df1 = pd.read_csv("../preparsed/questions_delimited.csv", sep='@', quotechar='~', index_col=0)
df2 = pd.read_csv("../preparsed/answers_only_multiple_choice_delimited.csv", sep='@', quotechar='~', index_col=0)

pass