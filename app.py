from config import *
from subgrounds.subgrounds import Subgrounds
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from metrics import FinancialsDailySnapshots, LiquidityPools, MetricsDailySnapshots, Swaps

import streamlit as st
from streamlit_echarts import st_pyecharts

st.set_page_config(layout="wide")

st.title("Curve Subgraph")

SUBGROUND = Subgrounds()
SUBGRAPH = SUBGROUND.load_subgraph(SUBGRAPH_URL)

FinancialsSnapshot = FinancialsDailySnapshots(SUBGRAPH, SUBGROUND, initial_timestamp=1601322741)

col1, col2 = st.columns(2)

with col1:
    st_pyecharts(
        chart=FinancialsSnapshot.tvl_chart(),
        height="450px",
        key="TVLChart",
    )

with col2:
    st_pyecharts(
        chart=FinancialsSnapshot.volume_chart(),
        height="450px",
        key="VolumeChart",
    )

col1, col2 = st.columns(2)

with col1:
    st_pyecharts(
        chart=FinancialsSnapshot.revenue_chart(),
        height="450px",
        key="RevenueChart",
    )

with col2:
    st_pyecharts(
        chart=FinancialsSnapshot.cumulative_revenue_chart(),
        height="450px",
        key="CumulativeRevenueChart",
    )


MetricsSnapshot = MetricsDailySnapshots(SUBGRAPH, SUBGROUND, initial_timestamp=1601322741)

with st.container():
    st_pyecharts(
        chart=MetricsSnapshot.transactions_count_chart(),
        height="450px",
        key="TransactionChart",
    )

with st.container():
    st_pyecharts(
        chart=MetricsSnapshot.active_users_chart(),
        height="450px",
        key="ActiveUsersChart",
    )

liquidity_pool = LiquidityPools(SUBGRAPH, SUBGROUND, initial_timestamp=1601322741)

col1, col2 = st.columns(2)

with col1:
    st_pyecharts(
        chart=liquidity_pool.top_10_pools_by_tvl(),
        height="450px",
        key="Top10ByTVL",
    )

with col2:
    st_pyecharts(
        chart=liquidity_pool.top_10_pools_by_volume(),
        height="450px",
        key="Top10ByVolume",
    )

swap = Swaps(SUBGRAPH, SUBGROUND)

st.header("Swaps")
with st.container():
    AgGrid(swap.dataframe)