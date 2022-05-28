from utils import *
from pyecharts.types import JsCode
from pyecharts import options as opts
from pyecharts.charts import Bar, Line

class BarOverlapLineChart:
    def __init__(
        self,
        title,
        yaxis_name,
        xaxis_name,
        height="1000px",
    ):
        self.BAR_CHART = Bar(
            init_opts=opts.InitOpts(height=height, width="100%", bg_color="#232329")
        )
        self.BAR_CHART.set_global_opts(
            title_opts=opts.TitleOpts(
                title=title,
                pos_left="10",
                pos_right="0",
                pos_top="10",
                pos_bottom="0",
                padding=10,
                item_gap=0,
                title_textstyle_opts=opts.TextStyleOpts(
                    color="white",
                ),
            ),
            legend_opts=opts.LegendOpts(
                is_show=False,
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,
                trigger="axis",
                axis_pointer_type="line",
                background_color="#3C2E48",
                border_color=None,
                border_width=0,
                textstyle_opts=opts.TextStyleOpts(
                    color="#FFFFFF", 
                    font_size=14
                ),
                padding=12,
            ),
            toolbox_opts=opts.ToolboxOpts(
                is_show=True,
                pos_left = "82%",
                feature=opts.ToolBoxFeatureOpts(
                    save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(
                        is_show=True, title="Save"
                    ),
                    restore=opts.ToolBoxFeatureRestoreOpts(
                        is_show=True, title="Refresh"
                    ),
                    data_view=opts.ToolBoxFeatureDataViewOpts(
                        is_show=False
                    ),
                    data_zoom=opts.ToolBoxFeatureDataZoomOpts(
                        is_show=False
                    ),
                    magic_type=opts.ToolBoxFeatureMagicTypeOpts(
                        is_show=True,
                        line_title='Line',
                        bar_title='Bar',
                        stack_title='Stack',
                        tiled_title='Tiled',
                    ),
                    brush=opts.ToolBoxFeatureBrushOpts(
                        type_=False
                    ),
                ),
            ),
            xaxis_opts=opts.AxisOpts(
                type_="category",
                name=xaxis_name,
                is_show=True,
                name_gap=20,
                name_location="start",
                min_interval=5,
                position='10',
                axislabel_opts=opts.LabelOpts(
                    is_show=True,
                    formatter=JsCode(
                        """
                        function Formatter(n) {
                            let word = n.split(',');
                            
                            return word[0];
                        };
                        """
                    )
                ),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name=yaxis_name,
                is_show=True,
                name_location="middle",
                name_gap=40,
                offset=5,
                split_number=5,
                name_textstyle_opts=opts.TextStyleOpts(
                    font_size=15,
                ),
                axistick_opts=opts.AxisTickOpts(is_show=True),
                axisline_opts=opts.AxisLineOpts(
                    is_show=True,
                    is_on_zero=False,
                    on_zero_axis_index=0,
                    symbol=None,
                    linestyle_opts=opts.LineStyleOpts(
                        is_show=True,
                        width=1,
                        opacity=1,
                        curve=0,
                        type_="dash",
                        color=None,
                    ),
                ),
                axislabel_opts=opts.LabelOpts(
                    formatter=JsCode(
                        """
                        function Formatter(n) {
                            if (n < 1e3) return n;
                            if (n >= 1e3 && n < 1e6) return +(n / 1e3).toFixed(1) + "K";
                            if (n >= 1e6 && n < 1e9) return +(n / 1e6).toFixed(1) + "M";
                            if (n >= 1e9 && n < 1e12) return +(n / 1e9).toFixed(1) + "B";
                            if (n >= 1e12) return +(n / 1e12).toFixed(1) + "T";
                        };
                        """
                    )
                ),
                axispointer_opts=opts.AxisPointerOpts(),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True,
                    linestyle_opts=opts.LineStyleOpts(
                        type_="dashed", opacity=0.2, color="#FFFFFF"
                    ),
                ),
                splitarea_opts=opts.SplitAreaOpts(),
                minor_tick_opts=opts.MinorTickOpts(),
                minor_split_line_opts=opts.MinorSplitLineOpts(),
            ),
            datazoom_opts=[
                opts.DataZoomOpts(range_start=0, range_end=100),
                opts.DataZoomOpts(type_="inside"),
            ],
        )

        self.LINE_CHART = Line()

    def add_xaxis_line_chart(self, xaxis_data):
        self.LINE_CHART.add_xaxis(xaxis_data)
    
    def add_xaxis_bar_chart(self, xaxis_data):
        self.BAR_CHART.add_xaxis(xaxis_data)
    
    def add_yaxis_bar_chart(self, series_name, color, yaxis_data):
        self.BAR_CHART.add_yaxis(
            series_name=series_name,
            y_axis=yaxis_data,
            itemstyle_opts=opts.ItemStyleOpts(color=color),
            label_opts=opts.LabelOpts(is_show=False)
        )
    
    def add_yaxis_line_chart(self, series_name, color, yaxis_data):
        self.LINE_CHART.add_yaxis(
            series_name=series_name,
            y_axis=yaxis_data,
            yaxis_index=1,
            itemstyle_opts=opts.ItemStyleOpts(color=color),
            label_opts=opts.LabelOpts(is_show=False)
        )
    
    def extend_axis(self, name):
        self.BAR_CHART.extend_axis(
            yaxis=opts.AxisOpts(
                name=name,
                type_="value",
                name_location="middle",
                name_gap=50,
                name_rotate=-90,
                name_textstyle_opts=opts.TextStyleOpts(
                    font_size=15,
                ),
            )
        )

class DepositsAndWithdrawsChart(BarOverlapLineChart):
    def __init__(self, dataframe, height="1000px", width="100%", bg_color="#232329"):
        self.dataframe = dataframe
        self.dataframe.columns = [
            "id",
            "dailyActiveUsers",
            "cumulativeUniqueUsers",
            "dailyDepositCount",
            "dailyWithdrawCount",
            "dailyTransactionCount",
            "timestamp",
        ]

        super().__init__(
            "Deposits And Withdraws", "Traders", "UTC", height, width, bg_color
        )

    def chart(self):
        xaxis_data = format_xaxis(self.dataframe.id)

        self.BAR_CHART.add_xaxis(xaxis_data)
        self.BAR_CHART.add_yaxis(
            series_name="Deposits",
            y_axis=self.dataframe.dailyDepositCount.to_list(),
            itemstyle_opts=opts.ItemStyleOpts(color="#5a66f9"),
        )
        self.BAR_CHART.add_yaxis(
            series_name="Withdraws",
            y_axis=self.dataframe.dailyWithdrawCount.to_list(),
            itemstyle_opts=opts.ItemStyleOpts(color="#bb6bd9"),
        )
        self.BAR_CHART.extend_axis(
            yaxis=opts.AxisOpts(
                name="Transactions",
                type_="value",
                name_location="middle",
                name_gap=50,
                name_rotate=-90,
                name_textstyle_opts=opts.TextStyleOpts(
                    font_size=15,
                ),
            )
        )

        self.LINE_CHART.add_xaxis(xaxis_data=xaxis_data)
        self.LINE_CHART.add_yaxis(
            series_name="Transactions",
            yaxis_index=1,
            is_symbol_show=False,
            y_axis=self.dataframe.dailyTransactionCount.to_list(),
            itemstyle_opts=opts.ItemStyleOpts(color="#6ac5c8"),
            label_opts=opts.LabelOpts(is_show=False),
        )

        self.BAR_CHART.set_series_opts(label_opts=opts.LabelOpts(is_show=False))

        return self.BAR_CHART.overlap(self.LINE_CHART)

class ActiveUsers(BarOverlapLineChart):
    def __init__(self, dataframe, height="1000px", width="100%", bg_color="#232329"):
        self.dataframe = dataframe
        self.dataframe.columns = [
            "id",
            "dailyActiveUsers",
            "cumulativeUniqueUsers",
            "dailyDepositCount",
            "dailyWithdrawCount",
            "dailyTransactionCount",
            "timestamp",
        ]

        super().__init__(
            "Activity", "Daily Active Users", "UTC", height, width, bg_color
        )

    def chart(self):
        xaxis_data = format_xaxis(self.dataframe.id)

        self.BAR_CHART.add_xaxis(xaxis_data)
        self.BAR_CHART.add_yaxis(
            series_name="Daily Active Users",
            y_axis=self.dataframe.dailyActiveUsers.to_list(),
            itemstyle_opts=opts.ItemStyleOpts(color="#5a66f9"),
        )
        self.BAR_CHART.extend_axis(
            yaxis=opts.AxisOpts(
                name="Cumulative Unique Users",
                type_="value",
                name_location="middle",
                name_gap=50,
                name_rotate=-90,
                name_textstyle_opts=opts.TextStyleOpts(
                    font_size=15,
                ),
            )
        )

        self.LINE_CHART.add_xaxis(xaxis_data=xaxis_data)
        self.LINE_CHART.add_yaxis(
            series_name="Cumulative Unique Users",
            yaxis_index=1,
            is_symbol_show=False,
            y_axis=self.dataframe.cumulativeUniqueUsers.to_list(),
            itemstyle_opts=opts.ItemStyleOpts(color="#6ac5c8"),
            label_opts=opts.LabelOpts(is_show=False),
        )

        self.BAR_CHART.set_series_opts(label_opts=opts.LabelOpts(is_show=False))

        return self.BAR_CHART.overlap(self.LINE_CHART)
