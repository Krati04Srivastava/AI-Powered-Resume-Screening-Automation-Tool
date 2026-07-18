import pandas as pd
def generate(data):
    df=pd.DataFrame(data)
    df=df.sort_values(by='ATS Score',ascending=False)
    df.to_csv("output/ATS_report.csv",index=False)
    print("Successful")