import allphotolenses
import lesdeuxpiedsdehors
import pandas as pd

def main():
    df1 = allphotolenses.scrap()
    df2 = lesdeuxpiedsdehors.scrap()
    # df = pd.concat([df1, df2])
    # df.to_csv("master_list.csv", index=False)

    _store_json_js(df1, "src/data/lenses.json")

def _store_json_js(df, filename):
    original_length = len(df)
    print(df.name.nunique())
    df.drop_duplicates(subset='name', inplace=True)
    print(f"Removed {original_length - len(df)} duplicates. New length: {len(df)}")
    df.to_json(filename, orient="records")



if __name__=="__main__":
    main()