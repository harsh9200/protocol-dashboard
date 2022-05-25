import streamlit as st
from charts.Pie import TopVaultsByTVL
from streamlit_echarts import st_pyecharts

st.set_page_config(layout="wide")

from data import SubgraphData
from charts.Line import RevenueChart
from charts.BarMixedLine import DepositsAndWithdrawsChart, ActiveUsers

st.title("Convex Subgraph")
st.balloons()

number = st.number_input("Number Of Days: ", min_value=7, max_value=900, value=30)

SUBGRAPH_URL = "https://api.thegraph.com/subgraphs/name/harsh9200/convex"
SUBGRAPH_DATA = SubgraphData(url=SUBGRAPH_URL, number_of_days=number)

col_1, col_2 = st.columns([1, 1])
with col_1:
    st_pyecharts(
        chart=DepositsAndWithdrawsChart(SUBGRAPH_DATA.dataframe[0]).chart(),
        height="450px",
        key="DepositsAndWithdraws",
    )

with col_2:
    st_pyecharts(
        chart=ActiveUsers(SUBGRAPH_DATA.dataframe[0]).chart(),
        height="450px",
        key="ActiveUsers",
    )

with st.container():
    st_pyecharts(
        chart=RevenueChart(SUBGRAPH_DATA.dataframe[1]).chart(),
        height="600px",
        key="Revenue Chart",
    )

with st.container():
    st_pyecharts(
        chart=TopVaultsByTVL(SUBGRAPH_DATA.dataframe[2]).chart(),
        height="600px",
        key="TopVaults",
    )
