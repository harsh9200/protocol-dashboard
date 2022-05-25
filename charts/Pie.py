import data
from utils import *
from pyecharts.charts import Pie
from pyecharts import options as opts


class PieChart:
    def __init__(
        self,
        title_name,
        yaxis_name,
        xaxis_name,
        height="1000px",
        width="100%",
        bg_color="#232329",
    ):
        self.PIE_CHART = Pie(
            init_opts=opts.InitOpts(width=width, height=height, bg_color=bg_color)
        )

        self.PIE_CHART.set_global_opts(
            title_opts=opts.TitleOpts(
                title=title_name,
                pos_left="60",
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
                type_="scroll", 
                pos_left="70%", 
                pos_top = "10%",
                orient="vertical",
                textstyle_opts=opts.TextStyleOpts(
                    color='#FFFFFF'
                )
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,
                trigger="item",
                axis_pointer_type="line",
                background_color="#3C2E48",
                border_color=None,
                border_width=0,
                formatter="{b}: {d}%",
                textstyle_opts=opts.TextStyleOpts(color="#FFFFFF", font_size=14),
                padding=12,
            ),
            toolbox_opts=opts.ToolboxOpts(
                is_show=True,
                pos_left="82%",
                feature=opts.ToolBoxFeatureOpts(
                    save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(
                        is_show=True, title="Save"
                    ),
                    restore=opts.ToolBoxFeatureRestoreOpts(
                        is_show=True, title="Refresh"
                    ),
                    data_view=opts.ToolBoxFeatureDataViewOpts(is_show=False),
                    data_zoom=opts.ToolBoxFeatureDataZoomOpts(is_show=False),
                    magic_type=opts.ToolBoxFeatureMagicTypeOpts(
                        is_show=True,
                        line_title="Line",
                        bar_title="Bar",
                        stack_title="Stack",
                        tiled_title="Tiled",
                    ),
                    brush=opts.ToolBoxFeatureBrushOpts(type_=False),
                ),
            ),
            xaxis_opts=opts.AxisOpts(
                type_="category",
                name=xaxis_name,
                is_show=True,
                name_gap=50,
                name_location="start",
                min_interval=5,
                axislabel_opts=opts.LabelOpts(is_show=True),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name=yaxis_name,
                is_show=True,
                name_location="middle",
                name_gap=50,
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
                axislabel_opts=opts.LabelOpts(),
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


class TopVaultsByTVL(PieChart):
    def __init__(self, dataframe, height="1000px", width="100%", bg_color="#232329"):
        self.dataframe = dataframe
        self.dataframe.columns = [
            "name",
            "totalValueLockedUSD",
            "inputTokenBalance",
            "outputTokenSupply",
        ]

        super().__init__(
            "Top 10 Vaults (By TVL)", "", "", height, width, bg_color
        )

    def chart(self):
        self.PIE_CHART.add(
            series_name='', 
            data_pair=[list(z) for z in zip(self.dataframe.name.to_list(), self.dataframe.totalValueLockedUSD.round(1).to_list())],
            center=["40%", "50%"],
        )
        self.PIE_CHART.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        return self.PIE_CHART
