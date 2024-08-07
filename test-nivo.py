import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from streamlit_elements import elements, mui, html
from streamlit_elements import dashboard, nivo

st.set_page_config(layout="wide")



with elements("dashboard"):


    DATA = [
        { "taste": "fruity", "chardonay": 93, "carmenere": 61, "syrah": 114 },
        { "taste": "bitter", "chardonay": 91, "carmenere": 37, "syrah": 72 },
        { "taste": "heavy", "chardonay": 56, "carmenere": 95, "syrah": 99 },
        { "taste": "strong", "chardonay": 64, "carmenere": 90, "syrah": 30 },
        { "taste": "sunny", "chardonay": 119, "carmenere": 94, "syrah": 103 },
    ]

    bar_data = [
            {
                "country": "AD",
                "hot dog": 115,
                "hot dogColor": "hsl(93, 70%, 50%)",
                "burger": 198,
                "burgerColor": "hsl(121, 70%, 50%)",
                "sandwich": 56,
                "sandwichColor": "hsl(265, 70%, 50%)",
                "kebab": 159,
                "kebabColor": "hsl(100, 70%, 50%)",
                "fries": 163,
                "friesColor": "hsl(129, 70%, 50%)",
                "donut": 46,
                "donutColor": "hsl(36, 70%, 50%)"
            },
            {
                "country": "AE",
                "hot dog": 126,
                "hot dogColor": "hsl(183, 70%, 50%)",
                "burger": 43,
                "burgerColor": "hsl(262, 70%, 50%)",
                "sandwich": 133,
                "sandwichColor": "hsl(19, 70%, 50%)",
                "kebab": 197,
                "kebabColor": "hsl(173, 70%, 50%)",
                "fries": 157,
                "friesColor": "hsl(240, 70%, 50%)",
                "donut": 83,
                "donutColor": "hsl(21, 70%, 50%)"
            },
            {
                "country": "AF",
                "hot dog": 125,
                "hot dogColor": "hsl(148, 70%, 50%)",
                "burger": 62,
                "burgerColor": "hsl(256, 70%, 50%)",
                "sandwich": 19,
                "sandwichColor": "hsl(321, 70%, 50%)",
                "kebab": 89,
                "kebabColor": "hsl(331, 70%, 50%)",
                "fries": 94,
                "friesColor": "hsl(60, 70%, 50%)",
                "donut": 62,
                "donutColor": "hsl(90, 70%, 50%)"
            },
            {
                "country": "AG",
                "hot dog": 109,
                "hot dogColor": "hsl(97, 70%, 50%)",
                "burger": 146,
                "burgerColor": "hsl(51, 70%, 50%)",
                "sandwich": 35,
                "sandwichColor": "hsl(236, 70%, 50%)",
                "kebab": 76,
                "kebabColor": "hsl(249, 70%, 50%)",
                "fries": 91,
                "friesColor": "hsl(195, 70%, 50%)",
                "donut": 118,
                "donutColor": "hsl(99, 70%, 50%)"
            },
            {
                "country": "AI",
                "hot dog": 152,
                "hot dogColor": "hsl(173, 70%, 50%)",
                "burger": 119,
                "burgerColor": "hsl(122, 70%, 50%)",
                "sandwich": 106,
                "sandwichColor": "hsl(313, 70%, 50%)",
                "kebab": 163,
                "kebabColor": "hsl(218, 70%, 50%)",
                "fries": 37,
                "friesColor": "hsl(137, 70%, 50%)",
                "donut": 51,
                "donutColor": "hsl(162, 70%, 50%)"
            },
            {
                "country": "AL",
                "hot dog": 184,
                "hot dogColor": "hsl(104, 70%, 50%)",
                "burger": 66,
                "burgerColor": "hsl(284, 70%, 50%)",
                "sandwich": 136,
                "sandwichColor": "hsl(343, 70%, 50%)",
                "kebab": 188,
                "kebabColor": "hsl(162, 70%, 50%)",
                "fries": 29,
                "friesColor": "hsl(108, 70%, 50%)",
                "donut": 12,
                "donutColor": "hsl(291, 70%, 50%)"
            },
            {
                "country": "AM",
                "hot dog": 194,
                "hot dogColor": "hsl(354, 70%, 50%)",
                "burger": 182,
                "burgerColor": "hsl(41, 70%, 50%)",
                "sandwich": 21,
                "sandwichColor": "hsl(172, 70%, 50%)",
                "kebab": 44,
                "kebabColor": "hsl(153, 70%, 50%)",
                "fries": 42,
                "friesColor": "hsl(307, 70%, 50%)",
                "donut": 157,
                "donutColor": "hsl(244, 70%, 50%)"
            }
        ]

    data = pd.DataFrame({
                'x': range(10),
                'y1': range(10),
                'y2': [x**2 for x in range(10)],
                'y3': [x**0.5 for x in range(10)],
                'y4': [10 - x for x in range(10)]
            })
             
    line_data = [
                {
                    "id": "y1",
                    "data": [{"x": str(row['x']), "y": row['y1']} for _, row in data.iterrows()]
                },
                {
                    "id": "y2",
                    "data": [{"x": str(row['x']), "y": row['y2']} for _, row in data.iterrows()]
                },
                {
                    "id": "y3",
                    "data": [{"x": str(row['x']), "y": row['y3']} for _, row in data.iterrows()]
                },
                {
                    "id": "y4",
                    "data": [{"x": str(row['x']), "y": row['y4']} for _, row in data.iterrows()]
                }
            ]

    area_data = [
            {
                "Raoul": 73,
                "Josiane": 28,
                "Marcel": 181,
                "René": 52,
                "Paul": 177,
                "Jacques": 58
            },
            {
                "Raoul": 123,
                "Josiane": 77,
                "Marcel": 150,
                "René": 15,
                "Paul": 71,
                "Jacques": 200
            },
            {
                "Raoul": 31,
                "Josiane": 108,
                "Marcel": 170,
                "René": 168,
                "Paul": 69,
                "Jacques": 185
            },
            {
                "Raoul": 42,
                "Josiane": 149,
                "Marcel": 95,
                "René": 178,
                "Paul": 192,
                "Jacques": 22
            },
            {
                "Raoul": 158,
                "Josiane": 66,
                "Marcel": 51,
                "René": 155,
                "Paul": 187,
                "Jacques": 44
            },
            {
                "Raoul": 157,
                "Josiane": 31,
                "Marcel": 135,
                "René": 196,
                "Paul": 187,
                "Jacques": 200
            },
            {
                "Raoul": 28,
                "Josiane": 137,
                "Marcel": 160,
                "René": 47,
                "Paul": 173,
                "Jacques": 125
            },
            {
                "Raoul": 71,
                "Josiane": 124,
                "Marcel": 45,
                "René": 182,
                "Paul": 64,
                "Jacques": 50
            },
            {
                "Raoul": 150,
                "Josiane": 55,
                "Marcel": 169,
                "René": 138,
                "Paul": 46,
                "Jacques": 107
            }
            ]
    

    # Prepare data for Nivo chart
    lineBar_bar_data = [
        {
            "x": str(row['x']),
            "y1": row['y1']
        } for _, row in data.iterrows()
    ]

    lineBar_line_data = [
        {
            "id": "y2",
            "data": [{"x": str(row['x']), "y": row['y2']} for _, row in data.iterrows()]
        }
    ]


    bar_data_js = str(lineBar_bar_data).replace("'", '"')
    line_data_js = str(lineBar_line_data).replace("'", '"')

    # HTML and JavaScript code for Nivo combined chart
    html_code = """
        <div id="chart"></div>
        """
    
    script_run = """
            <script>
            const {{ ResponsiveBar }} = window['nivo-bar'];
            const {{ ResponsiveLine }} = window['nivo-line'];
            const data = """ + bar_data_js + """;
            const lineData = """ + line_data_js + """;

            const CombinedChart = () => (
                <div style={{ height: '500px' }}>
                    <ResponsiveBar
                        data={data}
                        keys={['y1']}
                        indexBy="x"
                        margin={{ top: 50, right: 110, bottom: 50, left: 60 }}
                        padding={0.3}
                        valueScale={{ type: 'linear' }}
                        indexScale={{ type: 'band', round: true }}
                        colors={{ scheme: 'nivo' }}
                        axisTop={null}
                        axisRight={null}
                        axisBottom={{
                            tickSize: 5,
                            tickPadding: 5,
                            tickRotation: 0,
                            legend: 'X-axis',
                            legendPosition: 'middle',
                            legendOffset: 32
                        }}
                        axisLeft={{
                            tickSize: 5,
                            tickPadding: 5,
                            tickRotation: 0,
                            legend: 'Y-axis',
                            legendPosition: 'middle',
                            legendOffset: -40
                        }}
                        labelSkipWidth={12}
                        labelSkipHeight={12}
                        labelTextColor={{ from: 'color', modifiers: [['darker', 1.6]] }}
                        legends={[
                            {
                                dataFrom: 'keys',
                                anchor: 'bottom-right',
                                direction: 'column',
                                justify: false,
                                translateX: 120,
                                translateY: 0,
                                itemsSpacing: 2,
                                itemWidth: 100,
                                itemHeight: 20,
                                itemDirection: 'left-to-right',
                                itemOpacity: 0.85,
                                symbolSize: 20,
                                effects: [
                                    {
                                        on: 'hover',
                                        style: {
                                            itemOpacity: 1
                                        }
                                    }
                                ]
                            }
                        ]}
                        animate={true}
                        motionStiffness={90}
                        motionDamping={15}
                        layers={[
                            'grid',
                            'axes',
                            'bars',
                            'markers',
                            'legends',
                            'annotations',
                            ({ bars, xScale, yScale }) => {
                                const line = {
                                    id: 'line',
                                    data: lineData[0].data.map(d => ({
                                        x: xScale(d.x),
                                        y: yScale(d.y)
                                    }))
                                };

                                return (
                                    <g>
                                        <path
                                            d={line.data
                                                .map((point, index) => {
                                                    if (index === 0) {
                                                        return `M${point.x},${point.y}`;
                                                    }
                                                    return `L${point.x},${point.y}`;
                                                })
                                                .join(' ')}
                                            fill="none"
                                            stroke="#e63946"
                                            strokeWidth={2}
                                        />
                                    </g>
                                );
                            }
                        ]}
                    />
                </div>
            );

            ReactDOM.render(<CombinedChart />, document.getElementById('chart'));
        </script>
    """

    # First, build a default layout for every element you want to include in your dashboard

    layout = [
        # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
        dashboard.Item("first_item", 0, 0, 5, 6),
        dashboard.Item("second_item", 7, 0, 7, 2),
        dashboard.Item("third_item", 7, 2, 7, 2),
        dashboard.Item("forth_item", 7, 4, 7, 2),

    ]

    # Next, create a dashboard layout using the 'with' syntax. It takes the layout
    # as first parameter, plus additional properties.

    with dashboard.Grid(layout):
        with mui.Paper(sx={"height": 500}, variant="outlined", square=True, key="first_item"):
             nivo.Bar(
                data=bar_data,
                keys=['hot','dog','burger','sandwich','kebab','fries','donut'],
                indexBy="country",
                groupMode="grouped", # default 'stacked'
                # layout='horizontal'  # default 'vertical'
                margin={ 'top': 50, 'right': 130, 'bottom': 50, 'left': 60 },
                padding=0.3,
                valueScale={ 'type': 'linear' },
                indexScale={ 'type': 'band', 'round': True },
                colors={ 'scheme': 'nivo' },
                defs=[
                    {
                        'id': 'dots',
                        'type': 'patternDots',
                        'background': 'inherit',
                        'color': '#38bcb2',
                        'size': 4,
                        'padding': 1,
                        'stagger': True
                    },
                    {
                        'id': 'lines',
                        'type': 'patternLines',
                        'background': 'inherit',
                        'color': '#eed312',
                        'rotation': -45,
                        'lineWidth': 6,
                        'spacing': 10
                    }
                ],
                fill=[
                    {
                        'match': {
                            'id': 'fries'
                        },
                        'id': 'dots'
                    },
                    {
                        'match': {
                            'id': 'sandwich'
                        },
                        'id': 'lines'
                    }
                ],
                axisBottom={
                    'tickSize': 5,
                    'tickPadding': 5,
                    'tickRotation': 0,
                    'legend': 'country',
                    'legendPosition': 'middle',
                    'legendOffset': 32,
                    'truncateTickAt': 0
                },
                axisLeft={
                    'tickSize': 5,
                    'tickPadding': 5,
                    'tickRotation': 0,
                    'legend': 'food',
                    'legendPosition': 'middle',
                    'legendOffset': -40,
                    'truncateTickAt': 0
                },
                labelSkipWidth=12,
                labelSkipHeight=12,
                labelTextColor={
                    'from': 'color',
                    'modifiers': [
                        [
                            'darker',
                            1.6
                        ]
                    ]
                },
                legends=[
                    {
                        'dataFrom': 'keys',
                        'anchor': 'bottom-right',
                        'direction': 'column',
                        'justify': False,
                        'translateX': 120,
                        'translateY': 0,
                        'itemsSpacing': 2,
                        'itemWidth': 100,
                        'itemHeight': 20,
                        'itemDirection': 'left-to-right',
                        'itemOpacity': 0.85,
                        'symbolSize': 20,
                        'effects': [
                            {
                                'on': 'hover',
                                'style': {
                                    'itemOpacity': 1
                                }
                            }
                        ]
                    }
                ],
                ariaLabel="Nivo bar chart demo",
                theme={
                    "background": "#FFFFFF",
                    "textColor": "#31333F",
                    "tooltip": {
                        "container": {
                            "background": "#FFFFFF",
                            "color": "#31333F",
                        }
                    }
                }
            )
             
        with mui.Paper(sx={"height": 500}, variant="outlined", square=True, key="second_item"):
            nivo.Stream(
                data=area_data,
                keys=['Raoul','Josiane','Marcel','René','Paul','Jacques'],
                margin={ 'top': 50, 'right': 110, 'bottom': 50, 'left': 60 },
                axisBottom={
                    'orient': 'bottom',
                    'tickSize': 5,
                    'tickPadding': 5,
                    'tickRotation': 0,
                    'legend': '',
                    'legendOffset': 36,
                    'truncateTickAt': 0
                },
                axisLeft={
                    'orient': 'left',
                    'tickSize': 5,
                    'tickPadding': 5,
                    'tickRotation': 0,
                    'legend': '',
                    'legendOffset': -40,
                    'truncateTickAt': 0
                },
                enableGridX=True,
                enableGridY=False,
                offsetType='none',
                colors={ 'scheme': 'nivo' },
                fillOpacity=0.85,
                borderColor={ 'theme': 'background' },
                defs=[
                    {
                        'id': 'dots',
                        'type': 'patternDots',
                        'background': 'inherit',
                        'color': '#2c998f',
                        'size': 4,
                        'padding': 2,
                        'stagger': True
                    },
                    {
                        'id': 'squares',
                        'type': 'patternSquares',
                        'background': 'inherit',
                        'color': '#e4c912',
                        'size': 6,
                        'padding': 2,
                        'stagger': True
                    }
                ],
                fill=[
                    {
                        'match': {
                            'id': 'Paul'
                        },
                        'id': 'dots'
                    },
                    {
                        'match': {
                            'id': 'Marcel'
                        },
                        'id': 'squares'
                    }
                ],
                dotSize=8,
                dotColor={ 'from': 'color' },
                dotBorderWidth=2,
                dotBorderColor={
                    'from': 'color',
                    'modifiers': [
                        [
                            'darker',
                            0.7
                        ]
                    ]
                },
                legends=[
                    {
                        'anchor': 'bottom-right',
                        'direction': 'column',
                        'translateX': 100,
                        'itemWidth': 80,
                        'itemHeight': 20,
                        'itemTextColor': '#999999',
                        'symbolSize': 12,
                        'symbolShape': 'circle',
                        'effects': [
                            {
                                'on': 'hover',
                                'style': {
                                    'itemTextColor': '#000000'
                                }
                            }
                        ]
                    }
                ],
                theme={
                    "background": "#FFFFFF",
                    "textColor": "#31333F",
                    "tooltip": {
                        "container": {
                            "background": "#FFFFFF",
                            "color": "#31333F",
                        }
                    }
                }
            )
             
        with mui.Paper(sx={"height": 500}, variant="outlined", square=True, key="third_item"):
            nivo.Line(
                data=line_data,
                xScale={"type": "point"},
                yScale={"type": "linear", "min": "auto", "max": "auto", "stacked": False, "reverse": False},
                axisBottom={"orient": "bottom", "legend": "X-axis", "legendOffset": 36, "legendPosition": "middle"},
                axisLeft={"orient": "left", "legend": "Y-axis", "legendOffset": -40, "legendPosition": "middle"},
                margin={"top": 50, "right": 110, "bottom": 50, "left": 60},
                pointSize=10,
                pointColor={"theme": "background"},
                pointBorderWidth=2,
                pointBorderColor={"from": "serieColor"},
                pointLabel="y",
                pointLabelYOffset=-12,
                useMesh=True,
                legends=[
                    {
                        "anchor": "bottom-right",
                        "direction": "column",
                        "justify": False,
                        "translateX": 100,
                        "translateY": 0,
                        "itemsSpacing": 0,
                        "itemDirection": "left-to-right",
                        "itemWidth": 80,
                        "itemHeight": 20,
                        "itemOpacity": 0.75,
                        "symbolSize": 12,
                        "symbolShape": "circle",
                        "symbolBorderColor": "rgba(0, 0, 0, .5)",
                        "effects": [
                            {
                                "on": "hover",
                                "style": {
                                    "itemBackground": "rgba(0, 0, 0, .03)",
                                    "itemOpacity": 1
                                }
                            }
                        ]
                    }
                ],
                theme={
                    "background": "#FFFFFF",
                    "textColor": "#31333F",
                    "tooltip": {
                        "container": {
                            "background": "#FFFFFF",
                            "color": "#31333F",
                        }
                    }
                }
            )

        with mui.Paper(sx={"height": 500}, variant="outlined", square=True, key="forth_item"):
            # mui.Box(
            #     "Some text in a styled box",
            #     sx={
            #         "bgcolor": "background.paper",
            #         "boxShadow": 1,
            #         "borderRadius": 2,
            #         "p": 2,
            #         "minWidth": 300,
            #     }
            # )
            # nivo.Composed(
            #     data=lineBar_bar_data,
            #     xScale={"type": "point"},
            #     yScale={"type": "linear", "min": "auto", "max": "auto", "stacked": False, "reverse": False},
            #     axisBottom={"orient": "bottom", "legend": "X-axis", "legendOffset": 36, "legendPosition": "middle"},
            #     axisLeft={"orient": "left", "legend": "Y-axis", "legendOffset": -40, "legendPosition": "middle"},
            #     margin={"top": 50, "right": 110, "bottom": 50, "left": 60},
            #     barData=[{
            #         "id": "bars",
            #         "type": "bar",
            #         "data": lineBar_bar_data,
            #         "key": "y1"
            #     }],
            #     lineData=lineBar_line_data,
            #     legends=[
            #         {
            #             "anchor": "bottom-right",
            #             "direction": "column",
            #             "justify": False,
            #             "translateX": 100,
            #             "translateY": 0,
            #             "itemsSpacing": 0,
            #             "itemDirection": "left-to-right",
            #             "itemWidth": 80,
            #             "itemHeight": 20,
            #             "itemOpacity": 0.75,
            #             "symbolSize": 12,
            #             "symbolShape": "circle",
            #             "symbolBorderColor": "rgba(0, 0, 0, .5)",
            #             "effects": [
            #                 {
            #                     "on": "hover",
            #                     "style": {
            #                         "itemBackground": "rgba(0, 0, 0, .03)",
            #                         "itemOpacity": 1
            #                     }
            #                 }
            #             ]
            #         }
            #     ],
            #     theme={
            #         "background": "#FFFFFF",
            #         "textColor": "#31333F",
            #         "tooltip": {
            #             "container": {
            #                 "background": "#FFFFFF",
            #                 "color": "#31333F",
            #             }
            #         }
            #     }
            # )

            # def LineGenerator(bars, xScale, yScale):
            #     return html.svg(f"""""", fill=None, stroke="rgba(200, 30, 15, 1)")

            st.markdown("""<script>
                            const LineLayer = ({ bars, xScale, yScale }) => {
                            const lineGenerator = line()
                                .x(d => xScale(d.data.index) + d.width / 2)
                                .y(d => yScale(d.data.data.lineValue));

                            return (
                                <path d={lineGenerator(bars)} fill="none" stroke="rgba(200, 30, 15, 1)" />
                            );
                            };
                        </script>""", unsafe_allow_html=True)

            nivo.Bar(
                data=lineBar_bar_data,
                keys=["y1"],
                indexBy="x",
                margin={"top": 50, "right": 130, "bottom": 50, "left": 60},
                padding=0.3,
                valueScale={"type": "linear"},
                indexScale={"type": "band", "round": True},
                colors={ "scheme": "nivo" },
                layers=['grid', 'axes', 'bars', 'totals', 'markers', 'legends', 'annotations', 'LineLayer'],
                axisTop=None,
                axisRight=None,
                axisBottom={
                    "tickSize": 5,
                    "tickPadding": 5,
                    "tickRotation": 0,
                    "legend": "X-axis",
                    "legendPosition": "middle",
                    "legendOffset": 32
                },
                axisLeft={
                    "tickSize": 5,
                    "tickPadding": 5,
                    "tickRotation": 0,
                    "legend": "Y-axis",
                    "legendPosition": "middle",
                    "legendOffset": -40
                },
                labelSkipWidth=12,
                labelSkipHeight=12,
                labelTextColor={ "from": "color", "modifiers": [["darker", 1.6]] },
                legends=[
                    {
                        "dataFrom": "keys",
                        "anchor": "bottom-right",
                        "direction": "column",
                        "justify": False,
                        "translateX": 120,
                        "translateY": 0,
                        "itemsSpacing": 2,
                        "itemWidth": 100,
                        "itemHeight": 20,
                        "itemDirection": "left-to-right",
                        "itemOpacity": 0.85,
                        "symbolSize": 20,
                        "effects": [
                            {
                                "on": "hover",
                                "style": {
                                    "itemOpacity": 1
                                }
                            }
                        ]
                    }
                ],
                animate=True,
                motionStiffness=90,
                motionDamping=15,
                theme={
                    "background": "#FFFFFF",
                    "textColor": "#31333F",
                    "tooltip": {
                        "container": {
                            "background": "#FFFFFF",
                            "color": "#31333F",
                        }
                    }
                }
            )

            

            # # # Display the Nivo line chart
            # nivo.Line(
            #     data=lineBar_line_data,
            #     xScale={"type": "point"},
            #     yScale={"type": "linear", "min": "auto", "max": "auto", "stacked": False, "reverse": False},
            #     axisBottom={"orient": "bottom", "legend": "X-axis", "legendOffset": 36, "legendPosition": "middle"},
            #     axisLeft={"orient": "left", "legend": "Y-axis", "legendOffset": -40, "legendPosition": "middle"},
            #     margin={"top": 50, "right": 110, "bottom": 50, "left": 60},
            #     pointSize=10,
            #     pointColor={"theme": "background"},
            #     pointBorderWidth=2,
            #     pointBorderColor={"from": "serieColor"},
            #     pointLabel="y",
            #     pointLabelYOffset=-12,
            #     useMesh=True,
            #     legends=[
            #         {
            #             "anchor": "bottom-right",
            #             "direction": "column",
            #             "justify": False,
            #             "translateX": 100,
            #             "translateY": 0,
            #             "itemsSpacing": 0,
            #             "itemDirection": "left-to-right",
            #             "itemWidth": 80,
            #             "itemHeight": 20,
            #             "itemOpacity": 0.75,
            #             "symbolSize": 12,
            #             "symbolShape": "circle",
            #             "symbolBorderColor": "rgba(0, 0, 0, .5)",
            #             "effects": [
            #                 {
            #                     "on": "hover",
            #                     "style": {
            #                         "itemBackground": "rgba(0, 0, 0, .03)",
            #                         "itemOpacity": 1
            #                     }
            #                 }
            #             ]
            #         }
            #     ],
            #     theme={
            #         "background": "#FFFFFF",
            #         "textColor": "#31333F",
            #         "tooltip": {
            #             "container": {
            #                 "background": "#FFFFFF",
            #                 "color": "#31333F",
            #             }
            #         }
            #     }
            # )
