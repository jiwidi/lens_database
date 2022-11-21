import pandas as pd
import requests
from tqdm import tqdm


def scrap():
    url = "https://allphotolenses.com/lenses.html"

    header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
    }

    r = requests.get(url, headers=header)
    dfs = [pd.read_html(r.text)[1]]

    for i in tqdm(range(2,242)):
        url = f"https://allphotolenses.com/lenses/p_{i}.html"
        r = requests.get(url, headers=header)
        aux_dfs = pd.read_html(r.text)[1]
        dfs.append(aux_dfs)

    df = pd.concat(dfs).dropna(how="all")
    df[1] = df[1].str.replace('Add to comparison list ', '')
    df[["name", "mount"]] = df[1].str.split("Lens mounts:", 1, expand=True)
    df.drop([0,1],axis=1, inplace=True)
    df["mount"] = df.mount.str.strip().str.split("Posted",expand=True)[0].apply(lambda s: s.split(' ')[:-4]).str.join(" ")

    return df