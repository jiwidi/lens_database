import pandas as pd
import requests


def scrap():
    url = "https://lesdeuxpiedsdehors.com/en/leica-m-mount-lenses-list/"

    header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
    }

    r = requests.get(url, headers=header)

    dfs = pd.read_html(r.text)

    df = pd.concat(dfs)
    df["mount"] = "Leica M"
    df['Ø filter'] = df['Ø filtre'].combine_first(df['Ø filter'])
    df = df.drop(["Ø filtre", "Stab.", "Stabilization", "Autofocus", "Best Price"], axis=1)

    df.columns = df.columns.str.lower()
    df = df.rename(columns={"lens": "name", "max. aperture": "maxAperture","ø filter": "filterSize"})

    df['type'] = df['type'].apply(lambda x: 'Prime' if ("prime" in x or "Prime" in x) else 'Zoom')

    # Rname all columns to lower case

    print(df.head())
    original_length = len(df)
    df.drop_duplicates(subset='name', inplace=True)
    print(f"Removed {original_length - len(df)} duplicates. New length: {len(df)}")

    return df