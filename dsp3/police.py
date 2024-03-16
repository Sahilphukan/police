
import pandas as pd
data=pd.read_csv(r"C:\Users\Acer\Desktop\dsp\dsp3\police.csv")
print(data)


data_nul=data.isnull().sum()
print(data_nul)


data_cl=data.drop("country_name",axis=1)
data_cl2=data.drop("search_type",axis=1)
print(data_cl)



speeding_count=data[data["violation"]=="Speeding"]["driver_gender"].value_counts()
print(speeding_count)




gender_comp=data.groupby("driver_gender")["search_conducted"].value_counts()
print(gender_comp)



data["stop_duration"]=data["stop_duration"].map({"0-15 Min":7.5,"16-30 Min":23,"30+ Min":45})
data['stop_duration']=pd.to_numeric(data['stop_duration'],errors="coerce")
mean_stop_duration=data['stop_duration'].mean()
print(mean_stop_duration)



age_dis=data.groupby("violation")["driver_age"].describe()
print(age_dis)
