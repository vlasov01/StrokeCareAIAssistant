import sqlite3 # read data
import numpy as np  # np mean, np random
import pandas as pd  # df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development

st.set_page_config(
    page_title="Stroke Care AI Assistant",
    page_icon="🌟",
    layout="wide",
)

# Connect to the SQLite database
conn = sqlite3.connect('interact.db')

# Fetch data from the database table
df = pd.read_sql_query("""
SELECT strftime('%Y-%m-%d', datetime(d3, 'unixepoch')) as day,
       sum(length(user_text) - length(replace(user_text, ' ', '')) + 1) as words,
       count(*) as interactions
FROM prompt
GROUP BY day
""", conn)

# Fetch data from the database table
df_day_hour = pd.read_sql_query("""
SELECT strftime('%Y-%m-%d', datetime(d3, 'unixepoch')) as day,
       strftime('%H', datetime(d3, 'unixepoch')) as hour,
       sum(length(user_text) - length(replace(user_text, ' ', '')) + 1) as words,
       count(*) as interactions
FROM prompt
GROUP BY day, hour
""", conn)

df_details = pd.read_sql_query("""
SELECT strftime('%Y-%m-%d', datetime(d3, 'unixepoch')) as day,
strftime('%H:%M', datetime(d3, 'unixepoch')) as time,
user_text, output
FROM prompt
ORDER BY day DESC
""", conn)

# Close the database connection
conn.close()

# creating KPIs
avg_interactions = np.mean(df["interactions"])
avg_words = np.mean(df["words"])

# dashboard title
st.title("Stroke Care Activity Dashboard ⏳")

# top-level filters
day_filter = st.selectbox("Select the day", pd.unique(df_details["day"]))

# creating a single-element container
placeholder = st.empty()

# dataframe filter
df_details = df_details[df_details["day"] == day_filter]

with placeholder.container():

    # create two columns
    kpi1, kpi2 = st.columns(2)

    # fill in those three columns with respective metrics or KPIs
    kpi1.metric(
        label="Interactions per day 🌟",
        value=len(df_details),
        delta=len(df_details) - round(avg_interactions),
    )
    kpi2.metric(
        label="Words per day ✅",
        value=round(df[df["day"] == day_filter].iloc[0]['words']),
        delta=round(df[df["day"] == day_filter].iloc[0]['words'] - avg_words),
    )
    # create two columns for charts
    fig_col1, fig_col2, fig_col3 = st.columns(3)
    with fig_col1:
        st.markdown("### Interactions per day and hour")
        fig1 = px.scatter_3d(
            data_frame=df_day_hour, x='day', y='hour', z='interactions', size_max=18, opacity=0.7)
        st.write(fig1)
    with fig_col2:
        st.markdown("### Interactions per day")
        fig2 = px.bar(df, x='day', y='interactions')
        st.write(fig2)
    with fig_col3:
        st.markdown("### Words per day")
        fig3 = px.bar(df, x='day', y='words')
        st.write(fig3)
    st.markdown("### Detailed Data View")
    st.dataframe(df_details)

# tight layout
#fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
#fig.show()
