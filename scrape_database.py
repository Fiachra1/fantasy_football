from urllib.request import Request, urlopen
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = [
    "https://www.footballdb.com/statistics/nfl/player-stats/passing/2021/regular-season?sort=passrate&limit=all",
    "https://www.footballdb.com/statistics/nfl/player-stats/rushing/2021/regular-season?sort=rushyds&limit=all",
]
hdr = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
}


def create_database_table(url, columns, table_class):
    req = Request(url, headers=hdr)
    page = urlopen(req).read()
    soup = BeautifulSoup(page, "html.parser")

    # print("Classes of each table:")
    # for table in soup.find_all("table"):
    # print(table.get("class"))

    data_table = soup.find("table", class_=table_class)

    df = pd.DataFrame(columns=columns)

    for row in data_table.tbody.find_all("tr"):
        html_columns = row.find_all("td")
        print(len(html_columns))

        if html_columns != []:
            col1 = html_columns[0].find_all("span")[0].text.strip()
            col2 = html_columns[1].text.strip()
            col3 = html_columns[2].text.strip()
            col4 = html_columns[3].text.strip()
            col5 = html_columns[4].text.strip()
            col6 = html_columns[5].text.strip()
            col7 = html_columns[6].text.strip()
            col8 = html_columns[7].text.strip()
            col9 = html_columns[8].text.strip()
            col10 = html_columns[9].text.strip()
            col11 = html_columns[10].text.strip()
            col12 = html_columns[11].text.strip()
            col13 = html_columns[12].text.strip()
            col14 = html_columns[13].text.strip()
            col15 = html_columns[14].text.strip()
            col16 = html_columns[15].text.strip()
            # area = columns[2].span.contents[0].strip('&0.')
            # area = columns[2].span.contents[0].strip('&0.')
            # population = columns[3].span.contents[0].strip('&0.')
            # density = columns[4].span.contents[0].strip('&0.')
            # homes_count = columns[5].span.contents[0].strip('&0.')

            df = df.append(
                {
                    "Player": col1,
                    "Team": col2,
                    "Games": col3,
                    "Att": col4,
                    "Cmp": col5,
                    "Pct": col6,
                    "Yds": col7,
                    "YPA": col8,
                    "TD": col9,
                    "TD%": col10,
                    "Int": col11,
                    "Int%": col12,
                    "Lg": col13,
                    "Sack": col4,
                    "Loss": col15,
                    "Rate": col16,
                },
                ignore_index=True,
            )
    print(df)


table_class = "statistics scrollable"
columns = [
    "Player",
    "Team",
    "Games",
    "Att",
    "Cmp",
    "Pct",
    "Yds",
    "YPA",
    "TD",
    "TD%",
    "Int",
    "Int%",
    "Lg",
    "Sack",
    "Loss",
    "Rate",
]
create_database_table(url[0], columns=columns, table_class=table_class)
