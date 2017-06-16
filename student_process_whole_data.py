import pandas as pd
import numpy as np
f = "data//pisa2012.csv"
dataframe =pd.read_csv(f)


mother_edu_filter=["CNT","MISCED"]

education_filter=["ISCED 1","ISCED 2","ISCED 3B, C","ISCED 5A, 6","ISCED 3A, ISCED 4","ISCED 5B","None"]
#mother_edu_df=pd.DataFrame(columns=["country","ISCED 1","ISCED 2","ISCED 3B, C","ISCED 5A, 6","ISCED 3A,4","ISCED 5B","None","Math score"])

mother_qualification= "Math score with mother's qualification: "

index=0
scores={}
for filter,group in dataframe.groupby(mother_edu_filter):
    if filter[1] in education_filter:
        if filter[0] not in scores:
            scores[filter[0]] = {"country":filter[0],mother_qualification+filter[1]: ((group["PV1MATH"]+group["PV2MATH"]+group["PV3MATH"]
                                  +group["PV4MATH"]+group["PV5MATH"])/5).mean()}
        else:
            row=scores.get(filter[0])
            scores[filter[0]].update({mother_qualification+ filter[1] : ((group["PV1MATH"]+group["PV2MATH"]+group["PV3MATH"]
                                       +group["PV4MATH"]+group["PV5MATH"])/5).mean()})


father_edu_filter=["CNT","FISCED"]
father_qualification= "Math score with father's qualification: "
for filter, group in dataframe.groupby(father_edu_filter):
    if filter[1] in education_filter:
        if filter[0] not in scores:

            scores[filter[0]] =({"country": filter[0],father_qualification  + filter[1]: (
            group["PV1MATH"] + group["PV2MATH"] + group["PV3MATH"]
            + group["PV4MATH"] + group["PV5MATH"]).mean()})
        else:
            row = scores.get(filter[0])
            scores[filter[0]].update(
                {father_qualification+ filter[1]: ((group["PV1MATH"] + group["PV2MATH"] + group["PV3MATH"]
                                                    + group["PV4MATH"] + group["PV5MATH"])/5).mean()})

print scores

columns=["Country"]
columns.append("None")
columns.append("ISCED 1")
columns.append("ISCED 2")
columns.append("ISCED 3A, 4")
columns.append("ISCED 3B, C")
columns.append("ISCED 5A, 6")
columns.append("ISCED 5B")

df=pd.DataFrame(columns=columns)

for key,value in scores.items():
     df.loc[index] = np.array([key,value.get(mother_qualification + "None"), value.get(mother_qualification+"ISCED 1"),
                               value.get(mother_qualification+"ISCED 2"),
                               value.get(mother_qualification + "ISCED 3A, ISCED 4"),
                               value.get(mother_qualification + "ISCED 3B, C"),
                               value.get(mother_qualification + "ISCED 5A, 6"),value.get(mother_qualification + "ISCED 5B")

                               ])
     index = index + 1

df.to_csv("data//maths_grade_mother_education.csv", sep=',')


df_new=pd.DataFrame(columns=columns)

index=0
for key,value in scores.items():
    df_new.loc[index] = np.array([key,value.get(father_qualification + "None"),
                                value.get(father_qualification + "ISCED 1"),
                               value.get(father_qualification + "ISCED 2"),
                               value.get(father_qualification + "ISCED 3A, ISCED 4"),
                              value.get(father_qualification + "ISCED 3B, C"),
                               value.get(father_qualification + "ISCED 5A, 6"),value.get(father_qualification + "ISCED 5B")
                               ])
    index = index + 1

df_new.to_csv("data//maths_grade_father_education.csv", sep=',',)


df_sum=pd.DataFrame(columns=columns)

df_sum["Country"]=df_new["Country"]
df_sum["None"]=(df["None"]+df_new["None"])/2
df_sum["ISCED 1"]=(df["ISCED 1"]+df_new["ISCED 1"])/2
df_sum["ISCED 2"]=(df["ISCED 2"]+df_new["ISCED 2"])/2
df_sum["ISCED 3A, 4"]=(df["ISCED 3A, 4"]+df_new["ISCED 3A, 4"])/2
df_sum["ISCED 3B, C"]=(df["ISCED 3B, C"]+df_new["ISCED 3B, C"])/2
df_sum["ISCED 5A, 6"]=(df["ISCED 5A, 6"]+df_new["ISCED 5A, 6"])/2
df_sum["ISCED 5B"]=(df["ISCED 5B"]+df_new["ISCED 5B"])/2
df_sum.to_csv("data//maths_grade_parent_education.csv", sep=',')