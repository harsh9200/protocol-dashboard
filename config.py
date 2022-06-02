SUBGRAPH_URL = {
    'Balancer v2': "https://api.thegraph.com/subgraphs/name/messari/balancer-v2-ethereum", 
    'Curve': "https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum", 
    'Saddle Finance': "https://api.thegraph.com/subgraphs/name/messari/saddle-finance-ethereum",
    'Sushiswap': "https://api.thegraph.com/subgraphs/name/messari/sushiswap-ethereum", 
    'Uniswap v3': "https://api.thegraph.com/subgraphs/name/messari/uniswap-v3-ethereum"
}

LINE_CHART_GLOBAL_CONFIG = {
    "title_opts": {
        # ? title:
        "pos_left": "60",
        "pos_right": "0",
        "pos_top": "10",
        "pos_bottom": "0",
        "padding": 10,
        "item_gap": 0,
        "title_textstyle_opts": {
            "color": "white",
        },
    },
    "legend_opts": {
        "is_show": False,
    },
    "tooltip_opts": {
        "is_show": True,
        "trigger": "axis",
        "axis_pointer_type": "line",
        "background_color": "#3C2E48",
        "border_width": 0,
        "textstyle_opts": {"color": "#FFFFFF", "font_size": 14},
        "padding": 12,
    },
    "toolbox_opts": {
        "is_show": True,
        "pos_left": "82%",
        "feature": {
            "save_as_image": {"is_show": True, "title": "Save"},
            "restore": {"is_show": True, "title": "Refresh"},
            "data_view": {"is_show": False},
            "data_zoom": {"is_show": False},
            "magic_type": {
                "is_show": True,
                "line_title": "Line",
                "bar_title": "Bar",
                "stack_title": "Stack",
                "tiled_title": "Tiled",
            },
            "brush": {"type_": False},
        },
    },
    "xaxis_opts": {
        "type_": "category",
        # ? 'name': xaxis_name
        "is_show": True,
        "name_gap": 50,
        "name_location": "start",
        "min_interval": 5,
        "axislabel_opts": {"is_show": True},
    },
    "yaxis_opts": {
        "type_": "value",
        #? 'name': yaxis_name,
        "is_show": True,
        "name_location": "middle",
        "name_gap": 50,
        "offset": 5,
        "split_number": 5,
        "name_textstyle_opts": {
            "font_size": 15,
        },
        "axistick_opts": {"is_show": True},
        "axisline_opts": {
            "is_show": True,
            "is_on_zero": False,
            "on_zero_axis_index": 0,
            "symbol": None,
            "linestyle_opts": {
                "is_show": True,
                "width": 1,
                "opacity": 1,
                "curve": 0,
                "type_": "dash",
                "color": None,
            },
        },
        "splitline_opts": {
            "is_show": True,
            "linestyle_opts": {"type_": "dashed", "opacity": 0.2, "color": "#FFFFFF"},
        },
    },
    "datazoom_opts": [
        {"range_start": 0, "range_end": 100},
        {"type_": "inside"},
    ],
}