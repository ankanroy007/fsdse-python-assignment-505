import pandas as pd


def load_data():
    """
        Enter your code here
    """
    olympic_data = pd.read_csv("./files/olympics.csv",skiprows=[0])
    olympic_data = olympic_data.rename(columns = {'01 !' :'Gold', '02 !':'Silver',
    '03 !':'Bronze','01 !.1':'Gold.1','02 !.1':'Silver.1','03 !.1':'Bronze.1','01 !.2':'Gold.2',
    '02 !.2':'Silver.2','03 !.2':'Bronze.2',})
    country = olympic_data['Unnamed: 0'].str.split("(",expand = True)
    #print country[0].str.rstrip(' ')
    olympic_data = olympic_data.set_index(country[0].str.replace("\xc2\xa0", ""))
    #olympic_data.drop(olympic_data.row["Totals"], axis=0, inplace=True)
    return olympic_data.drop(olympic_data.index[len(olympic_data)-1])
    #print olympic_data.head()
    #print olympic_data



def first_country(df):
    """
        Enter your code here
    """
    return df.iloc[0]



def gold_medal(df):
    """
        Enter your code here
    """
    return df["Gold"].idxmax()


def biggest_difference_in_gold_medal(df):
    """
        Enter your code here
    """
    #print df[["Gold","Gold.1"]]
    gold_diff = df["Gold"] - df["Gold.1"]
    return gold_diff.idxmax()

def get_points(df):
    """
    Enter your code here
    """

    Points = df["Gold.2"]*3 + df["Silver.2"]*2 + df["Bronze.2"]
    df['Points'] = Points
    newDF = df['Points']
    return newDF


df = load_data()
#print first_country(df)
#print(gold_medal(df))
#print(biggest_difference_in_gold_medal(df))
print(get_points(df))
