import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ステップ2で作成した関数をインポート
from fetch_apps import fetch_app_data

# Streamlitアプリのタイトル
st.title('iTunes Store Search Data Visualization')

# ユーザー入力
search_term = st.text_input('Search Term', 'カレンダー')
data = fetch_app_data(search_term, 'JP')

# データをPandas DataFrameに変換
df = pd.DataFrame(data)

# 簡単なデータ表示
if not df.empty:
    st.write(df.head(100))

#     # グラフの描画例（ここではジャンルごとの件数を表示）
#     genre_counts = df['primaryGenreName'].value_counts()
#     plt.figure(figsize=(10, 6))
#     plt.bar(genre_counts.index, genre_counts.values)
#     plt.xticks(rotation=45)
#     plt.ylabel('Counts')
#     plt.title('Counts by Genre')
#     st.pyplot(plt)
# else:
#     st.write("No data found for the term: ", search_term)
