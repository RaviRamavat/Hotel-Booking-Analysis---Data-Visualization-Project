import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
df = pd.read_csv("hotel_bookings.csv")
# Group the data by 'country' and get the count of guests from each country

time_dict = {1: "Jul-2015", 2: "Oct-2015", 3: "Jan-2016", 4: "Apr-2016", 
             5: "Jul-2016", 6: "Oct-2016", 7: "Jan-2017", 8: "Apr-2017", 
             9: "Jul-2017"}


# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20.5rem",
    "padding": "2rem 1rem",
    "background-color": "#2E3439",
    "color":"white"
    
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

tabs_content = {
    "tab-1": html.Div([
        html.H2("Booking Trends and Seasonality Insights",style={'font-size':'2.3rem','text-align':'center','padding':'1.1rem','color':'#cefff1',}),
        
        
        html.Div(
            [
                dcc.Graph(id='time-series-line-chart'),

                html.Div( 
                    dcc.RangeSlider(
                        id='year-month-range-slider-line-chart',
                        min=1,
                        max=9,
                        step=1,
                        marks= {
                            1 : {'label' : 'Jul-2015', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                            2 : {'label' : 'Oct-2015', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                            3 : {'label' : 'Jan-2016', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                            4 : {'label' : 'Apr-2016', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                            5 : {'label' : 'Jul-2016', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                            6 : {'label' : 'Oct-2016', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                            7 : {'label' : 'Jan-2017', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                            8 : {'label' : 'Apr-2017', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                            9 : {'label' : 'Jul-2017', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}},   
                        },
                        value=[1, 9], 
                        # tooltip={"placement": "bottom", "always_visible": False},
                        className="range-slider-custom",  # Add custom class
                    ), 
                    id='range-slider-output-container', 
                    style={'width': '93%', 'margin-left': '50px', 'height': '100px','margin-top':'4px'}
                ),

                dcc.Dropdown(
                    id='hotel-type-dropdown',
                    options=[
                        {'label': 'Resort Hotel', 'value': 'Resort Hotel'},
                        {'label': 'City Hotel', 'value': 'City Hotel'},
                        {'label': 'Both', 'value': 'Both'}
                    ],
                    value='Both',  # default value
                    clearable=False,
                    searchable=False,
                    style={'width': '180px', 'cursor': 'pointer', 'color' : '#185295',
                               'background-color' : '#d6ebf2','margin':'10px 5px 10px 0px ','font-family':'Verdana','font-weight':'bold',
                               'font-size':'1.1rem','text-align':'center'}
                ),
            ]
        ),

        html.Div([

            dcc.Graph(id='time-series-area-chart'),

            html.Div( 
                dcc.RangeSlider(
                    id='year-month-range-slider',
                    min=1,
                    max=9,
                    step=1,
                    marks= {
                        1 : {'label' : 'Jul-2015', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                        2 : {'label' : 'Oct-2015', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                        3 : {'label' : 'Jan-2016', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                        4 : {'label' : 'Apr-2016', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                        5 : {'label' : 'Jul-2016', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                        6 : {'label' : 'Oct-2016', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                        7 : {'label' : 'Jan-2017', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                        8 : {'label' : 'Apr-2017', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                        9 : {'label' : 'Jul-2017', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}},  
                    },
                    value=[1, 9], 
                    # tooltip={"placement": "bottom", "always_visible": False},
                    className="range-slider-custom",  # Add custom class
                ), 
                id='range-slider-output-container', 
                style={'width': '93%', 'margin-left': '50px', 'height': '100px','margin-top':'4px'}
            ),

            dcc.Dropdown(
                id='number-of-rooms-dropdown',
                options=[
                    {'label': '4', 'value': '4'},
                    {'label': '5', 'value': '5'},
                    {'label': '6', 'value': '6'},
                    {'label': '7', 'value': '7'},
                    {'label': '8', 'value': '8'},
                ],
                # value='4',  # default value
                value = '4',
                clearable=False,
                searchable=False,
                style={'width': '100px', 'cursor': 'pointer', 'color' : '#185295',
                            'background-color' : '#d6ebf2','margin':'10px 5px 10px 0px ','font-family':'Verdana','font-weight':'bold',
                            'font-size':'1.1rem','text-align':'center'}
            ),
            html.H2(html.H2("Select Top n Rooms (number of bookings wise)",style={'font-size':'1.6rem','color':'#cefff1'}))
        ])
        
        
        # dcc.Graph(id='heatmap'),
    ], style={'margin-left': '15%'}),  # Add left margin here
    "tab-2": html.Div([
        html.H2("Guest Behavior and Preferences Insights",style={'font-size':'2.3rem','text-align':'center','padding':'1.1rem','color':'#cefff1',}),

        
        html.Div([
            dcc.Input(id='dummy-trigger', style={'display': 'none'}, value='dummy'),
            html.Div([
                dcc.Graph(id='barplot', style={'height': '800px'}),
                html.Div([
                    dcc.Dropdown(
                        
                        id='hotel-type-dropdown-barplot',
                        options=[
                            {'label': 'Resort Hotel', 'value': 'Resort Hotel', 'style' : {'color' : 'white'}},
                            {'label': 'City Hotel', 'value': 'City Hotel', 'style' : {'color' : 'white'}},
                            {'label': 'Both', 'value': 'Both', 'style' : {'color' : 'white'}}
                        ],
                        value='Both',  # default value
                        clearable=False,
                        searchable=False,
                        style={'width': '180px', 'cursor': 'pointer', 'color' : '#185295',
                               'background-color' : '#d6ebf2','margin':'2px 5px 2px 0px ','font-family':'Verdana','font-weight':'bold',
                               'font-size':'1.1rem','text-align':'center'},
                        className='hotel-type-dropdown-barplot-class'
                        
                    ),
                    
                    
                    dcc.Dropdown(
                        id='meal-type-dropdown-barplot',
                        options=[
                            {'label': 'no meal', 'value': 'SC'},
                            {'label': 'Bed & Breakfast', 'value': 'BB'},
                            {'label': 'Half board', 'value': 'HB'},
                            {'label': 'Full board', 'value': 'FB'},
                            {'label': 'Any', 'value': 'Any'},
                        ],
                        value='Any',  # default value
                        clearable=False,
                        searchable=False,
                        style={'width': '180px', 'cursor': 'pointer', 'color' : '#185295',
                               'background-color' : '#d6ebf2','margin':'2px 5px 2px 0px ','font-family':'Verdana','font-weight':'bold',
                               'font-size':'1.1rem','text-align':'center'},
                    ),
                ], style={'display': 'flex'})
            ]),

            html.Div([
                dcc.Graph(id='heatmap', style={'height': '800px'}),  # Set height to 400px


                html.Div( dcc.RangeSlider(
                    id='month-range-slider',
                    min=1,
                    max=12,
                    step=1,
                    marks= {
                            1 : {'label' : 'Jan', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                            2 : {'label' : 'Feb', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                            3 : {'label' : 'Mar', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                            4 : {'label' : 'Apr', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                            5 : {'label' : 'May', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                            6 : {'label' : 'Jun', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                            7 : {'label' : 'Jul', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                            8 : {'label' : 'Aug', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}}, 
                            9 : {'label' : 'Sep', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}},   
                            10 : {'label' : 'Oct', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}},   
                            11 : {'label' : 'Nov', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}},   
                            12 : {'label' : 'Dec', 'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}},   
                        },
                    value=[1, 12], 
                    
                ), id='range-slider-output-container', style = {'width' : '800px', 'margin-left' : '50px', 'height' : '100px',"fontSize": "30px"})
                
            ]),
            

            html.Div([
                dcc.Graph(id='piechart', style={'height': '800px'}),

                html.Div( dcc.Slider(
                    id='slider-updatemode',
                    min=1,
                    max=10,
                    step=1,
                    value=5,
                    marks=[{'label': i, 'value': i,'style' : {'color': '#cefff1', 'font-size' : '1.2rem','font-family':'Trebuchet MS'}} for i in range(0, 11)],
                      # Display marks at each integer value from 0 to 10
                ), id='slider-output-container', style = {'width' : '800px', 'margin-left' : '50px', 'height' : '100px',"fontSize": "30px"}),
            ]),
              # Set height to 400px

            html.Div([
                dcc.Graph(id='boxplot', style={'height': '800px',}),  # Set height to 400px
                
                dcc.Dropdown(
                    id='meal-type-dropdown-boxplot',
                    options=[
                        {'label': 'no meal', 'value': 'SC'},
                        {'label': 'Bed & Breakfast', 'value': 'BB'},
                        {'label': 'Half board', 'value': 'HB'},
                        {'label': 'Full board', 'value': 'FB'},
                        {'label': 'Any', 'value': 'Any'},
                    ],
                    value='Any',  # default value
                    clearable=False,
                    searchable=False,
                    style={'width': '180px', 'cursor': 'pointer', 'color' : '#185295',
                            'background-color' : '#d6ebf2','margin':'2px 5px 2px 0px ','font-family':'Verdana','font-weight':'bold',
                            'font-size':'1.1rem','text-align':'center'},
                ),
            ])

        ], style={'display': 'grid', 'grid-template-columns': '1fr 1fr', 'grid-gap': '20px'})
    ], style={'margin-left': '15%'}),

    "tab-3": html.Div([
        html.H2("Revenue and Performance Insights",style={'font-size':'2.3rem','text-align':'center','padding':'1.1rem','color':'#cefff1',}),
        # dcc.Input(id='dummy-trigger', style={'display': 'none'}, value='dummy'),

        html.Div([

            dcc.Dropdown(
                id='hotel-type-dropdown-choropleth',
                options=[
                    {'label': 'Resort Hotel', 'value': 'Resort Hotel'},
                    {'label': 'City Hotel', 'value': 'City Hotel'},
                    {'label': 'Both', 'value': 'Both'}
                ],
                value='Both',  # default value
                clearable=False,
                searchable=False,
                style={'width': '180px', 'cursor': 'pointer', 'color' : '#185295',
                               'background-color' : '#d6ebf2','margin':'2px 5px 10px 0px ','font-family':'Verdana','font-weight':'bold',
                               'font-size':'1.1rem','text-align':'center'}
            ),
            dcc.Graph(id='choropleth-map'),
            
                ], style={'margin-left': '15%'}),  # Add left margin here
        ])
        
}

sidebar = html.Div(
    id='sidebar',
    children=[
        html.H2("Sidebar", className="display-4",style={'font-family':'Tahoma'}),
        html.Hr(),
        html.P(
            "Ravi Ramavat - B20CS053", className="lead-1",style={'font-family':'Verdana','font-weight':'450','font-size':'1.3rem','margin-bottom':'0px'}
        ),
        html.P(
            "Dhurv Viradiya - B20CS079", className="lead-2",style={'font-family':'Verdana','font-weight':'450','font-size':'1.3rem',}
        ),
        dbc.Nav(
        [
            dbc.NavItem(dbc.NavLink("Booking Trends and Seasonality", href="/tab1", active='exact')),
            dbc.NavItem(dbc.NavLink("Guest Behavior and Preferences", href="/tab2", active='exact')),
            dbc.NavItem(dbc.NavLink("Revenue and Performance", href="/tab3", active = 'exact')),
        ],
        vertical=True,
        pills=True,
        style={'margin-top':'2.5rem','font-size':'1.5rem','font-family':'Tahoma',}
        # style={'width': '200px', 'height': '100vh', 'position': 'fixed', 'left': '0', 'top': '0'}
        ),

    ],
    style=SIDEBAR_STYLE,
)


page_content = html.Div(id='tabs-content')

app.layout = html.Div([
    dcc.Location(id="url"),

    # html.H1("Hotel Booking Analysis -", style = {'margin-left' : '14%','font-family':'Trebuchet MS','padding':'10px 0px 10px 20px','background-color':'rgba(56, 60, 70, 0.81)','color':'white','padding':'1.6rem 1.1rem','font-size':'3rem'}),
    html.Div([
        html.H1("Hotel Booking Analysis -", style = {'color':'white','font-size':'3rem','font-family':'Trebuchet MS',}),
        html.H2(" Data Visualization Project", style = {'color':'#b3b3b3ad','font-size':'2.4rem','font-family':'Tahoma','margin-top':'7px','margin-left':'5px'})
    ], style={'display': 'flex','margin-left' : '14%','background-color':'rgba(56, 60, 70, 0.81)','padding':'1.6rem 1.1rem'}),
    sidebar,

    # # Tabs navigation
    # dcc.Tabs(id='tabs', value='tab-1', children=[
    #     dcc.Tab(label='Booking Trends and Seasonality', value='tab-1'),
    #     dcc.Tab(label='Guest Behavior and Preferences', value='tab-2'),
    #     dcc.Tab(label='Revenue and Performance', value='tab-3'),
    # ]),
    
    # Tabs content
    page_content,
],style={'background-color':'black','color':'whilte'})

@app.callback(
    Output('tabs-content', 'children'),
    [Input("url", "pathname")]
)
def update_tab_content(pathname):
    # print("clicked!")
    if pathname == '/tab1':
        return tabs_content["tab-1"]
    elif pathname == '/tab2':
        return tabs_content["tab-2"]
    elif pathname == '/tab3':
        return tabs_content["tab-3"]
    else:
        return tabs_content["tab-1"]


@app.callback(
    Output('time-series-line-chart', 'figure'),
    [Input('hotel-type-dropdown', 'value'),
     Input('year-month-range-slider-line-chart','value')]
)

def update_time_series_line_chart(hotel_type,time_range):

    # Filter data based on hotel type
    left_value = pd.to_datetime(time_dict[time_range[0]], format='%b-%Y')
    right_value = pd.to_datetime(time_dict[time_range[1]], format='%b-%Y')

    if hotel_type != 'Both':
        filtered_df = df[df['hotel'] == hotel_type]
        
        # Combine 'arrival_date_month' and 'arrival_date_year' into a new column
        filtered_df['arrival_date'] = filtered_df['arrival_date_month'] + '-' + filtered_df['arrival_date_year'].astype(str)
        
        filtered_df['arrival_date'] = pd.to_datetime(filtered_df['arrival_date'], format='%B-%Y')

        filtered_df = filtered_df[(filtered_df['arrival_date'] >= left_value) & (filtered_df['arrival_date'] <= right_value)]

        # Aggregate bookings count by 'arrival_date'
        year_bookings = filtered_df.groupby('arrival_date').size().reset_index(name='bookings_count')
        
        # Sort the DataFrame by the combined 'arrival_date' column
        year_bookings = year_bookings.sort_values('arrival_date')
        
        fig = px.line(year_bookings, x='arrival_date', y='bookings_count',
                  title='Booking Trends Over Time', 
                  labels={'arrival_date': 'Month', 'bookings_count': 'Bookings Count'},
                  markers=True,  # Add markers on the lines
                  template="plotly_dark",
                  )
    
    # Customize markers
        fig.update_traces(mode='markers+lines', marker=dict(size=8)) 
        # Customize layout
        fig.update_layout(
            legend_title_text=None,  # Remove legend title
            legend=dict(
                orientation="h",  # Set legend orientation to horizontal
                yanchor="bottom",  # Anchor legend to the bottom
                y=1.02,  # Adjust vertical position of legend
                xanchor="right",  # Anchor legend to the right
                x=1  # Adjust horizontal position of legend
            ),
            xaxis=dict(
                tickformat='%b-%Y',  # Format x-axis tick labels as month-year
                tickangle=-45,  # Rotate x-axis tick labels for better readability
            ),
            yaxis=dict(
                title='Bookings Count',  # Set y-axis title
            )
        )
        
    else:
        df['arrival_date'] = df['arrival_date_month'] + '-' + df['arrival_date_year'].astype(str)
    
        # Convert 'arrival_date' to datetime format
        df['arrival_date'] = pd.to_datetime(df['arrival_date'], format='%B-%Y')
        
        # Aggregate bookings count by 'arrival_date' and 'hotel'
        filtered_df = df[(df['arrival_date'] >= left_value) & (df['arrival_date'] <= right_value)]
        bookings_count = filtered_df.groupby(['arrival_date', 'hotel']).size().reset_index(name='bookings_count')
    
        fig = px.line(bookings_count, x='arrival_date', y='bookings_count', color='hotel',
                  title='Booking Trends Over Time', 
                  labels={'arrival_date': 'Month', 'bookings_count': 'Bookings Count', 'hotel': 'Hotel Type'},
                  markers=True,  # Add markers on the lines
                  line_dash_sequence=['solid', 'dash'],  # Set line dash style for each hotel type
                  template="plotly_dark",
                  )
    
    # Customize markers
        fig.update_traces(mode='markers+lines', marker=dict(size=8)) 
        # Customize layout

        fig.update_layout(
            legend_title_text=None,  # Remove legend title
            legend=dict(
                orientation="h",  # Set legend orientation to horizontal
                yanchor="bottom",  # Anchor legend to the bottom
                y=1.02,  # Adjust vertical position of legend
                xanchor="right",  # Anchor legend to the right
                x=1,  # Adjust horizontal position of legend
                font=dict(size=20)  # Increase legend font size
            ),
            xaxis=dict(
                tickformat='%b-%Y',  # Format x-axis tick labels as month-year
                tickangle=-45,  # Rotate x-axis tick labels for better readability
                titlefont=dict(size=25),  # Increase x-axis title font size
                tickfont = dict(size = 15)
            ),
            yaxis=dict(
                title='Bookings Count',  # Set y-axis title
                titlefont=dict(size=25),  # Increase y-axis title font size
                tickfont = dict(size = 15)
            ),
            titlefont=dict(size=30)  # Increase title font size
        )

    
    return fig


@app.callback(
    Output('time-series-area-chart', 'figure'),
    [Input('number-of-rooms-dropdown', 'value'),
     Input('year-month-range-slider', 'value')]
)
def update_time_series_area_chart(number_of_rooms, time_range):

    

    n = int(number_of_rooms)
    # number_of_rooms = int(number_of_rooms)
    
    left_value = pd.to_datetime(time_dict[time_range[0]], format='%b-%Y')
    right_value = pd.to_datetime(time_dict[time_range[1]], format='%b-%Y')

    df['arrival_date_area'] = df['arrival_date_month'] + '-' + df['arrival_date_year'].astype(str)
    
    # Convert 'arrival_date' to datetime format
    df['arrival_date_area'] = pd.to_datetime(df['arrival_date_area'], format='%B-%Y')

    filtered_df = df[(df['arrival_date_area'] >= left_value) & (df['arrival_date_area'] <= right_value)]
    
    # Aggregate bookings count by 'arrival_date' and 'hotel'
    bookings_count = filtered_df.groupby(['arrival_date_area', 'reserved_room_type']).size().reset_index(name='bookings_count_room')
    
    # Get the top 4 values based on bookings count
    # top_4_rooms = bookings_count.groupby('reserved_room_type')['bookings_count_room'].sum().nlargest(number_of_rooms).index
    top_n_rooms = bookings_count.groupby('reserved_room_type')['bookings_count_room'].sum().nlargest(n).index
    
    # legend_labels = {'A': 'Single Room', 'D': 'Double Room', 'E': 'Twin Room', 'F': 'Family Room'}
    legend_labels = {'A': 'Double Room', 'D': 'Family Room', 'E': 'Single Room', 'F': 'Twin Room',
                      'B' : 'Junior Suites', 'C' : 'Bridal Suits', 'G' : 'Penthouse', 'H' : 'Presidential Room'}

    # Filter the DataFrame to include only the top 4 rooms
    bookings_count_top_n = bookings_count[bookings_count['reserved_room_type'].isin(top_n_rooms)]
    bookings_count_top_n['reserved_room_type'] = bookings_count_top_n['reserved_room_type'].map(legend_labels)
    # Plot time series area chart
    fig = px.area(bookings_count_top_n, x='arrival_date_area', y='bookings_count_room', color='reserved_room_type',
                  title='Top 4 Booking Trends Over Time', 
                  labels={'arrival_date_area': 'Month', 'bookings_count_room': 'Bookings Count', 'reserved_room_type': 'Hotel Room Type'},
                  template="plotly_dark",
                  )
    
    fig.update_layout(
        legend_title_text=None,  # Remove legend title
        legend=dict(
            orientation="h",  # Set legend orientation to horizontal
            yanchor="bottom",  # Anchor legend to the bottom
            y=1.02,  # Adjust vertical position of legend
            xanchor="right",  # Anchor legend to the right
            x=1,  # Adjust horizontal position of legend
            font=dict(size=20)  # Increase legend font size
        ),
        xaxis=dict(
            tickformat='%b-%Y',  # Format x-axis tick labels as month-year
            tickangle=-45,  # Rotate x-axis tick labels for better readability
            titlefont=dict(size=25),  # Increase x-axis title font size
            tickfont=dict(size=15)  # Increase x-axis tick font size
        ),
        yaxis=dict(
            title='Bookings Count',  # Set y-axis title
            titlefont=dict(size=25),  # Increase y-axis title font size
            tickfont=dict(size=15)  # Increase y-axis tick font size
        ),
        titlefont=dict(size=30)  # Increase title font size
    )
    
    return fig


def getCountryData(df):
    country_data = df.groupby('country').size().reset_index(name='guest_count')

    country_data.columns = ["country", "Number of Guests"]

    total_guests = country_data["Number of Guests"].sum()

    country_data['Guests in %'] = round(country_data["Number of Guests"]/total_guests * 100 , 2)
    return country_data

@app.callback(
    Output('choropleth-map', 'figure'),
    [Input('hotel-type-dropdown-choropleth', 'value')]
)
def update_choropleth_map(hotel_type):
    # Filter data based on hotel type

    filtered_df = df
    if(hotel_type != "Both"):
        filtered_df = df[df["hotel"] == hotel_type]

    country_data = getCountryData(filtered_df)
    
    guest_map = px.choropleth(country_data,
                    locations=country_data['country'],
                    color=country_data["Guests in %"], 
                    hover_name=country_data['country'], 
                    color_continuous_scale=px.colors.sequential.Bluyl,
                    title="Home country of guests",
                    template='plotly_dark')
    
    guest_map.update_layout(
        title=dict(
            text="Home country of guests",
            x=0.5,  # Centering the title horizontally
            y=0.95,  # Adjusting vertical position of the title
            font=dict(
                size=30  # Set the font size for the title to 30
            )
        ),
        geo=dict(
            showframe=False,  # Removing frame around the map
            showcoastlines=False  # Removing coastlines
        ),
        height=1500,  # Adjusting map height
        width=2000,  # Adjusting map width
        margin={"l": 200, "r": 0, "t": 0, "b": 0, "pad": 0}
    )

    
    # guest_map.update_traces(colorbar=dict(len=0.4))
    
    return guest_map


@app.callback(
    Output('heatmap', 'figure'),
    [Input('month-range-slider', 'value')]
)
def update_heatmap(month_range):
    start_month = month_range[0]
    end_month = month_range[1]

    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df['arrival_date_month_cat'] = pd.Categorical(df['arrival_date_month'], categories=month_order, ordered=True)

    filtered_df = df[df['arrival_date_month_cat'].apply(lambda x: month_order.index(x)+1 in range(start_month, end_month+1))]

    filtered_df['arrival_date_month_cat'] = filtered_df['arrival_date_month_cat'].apply(lambda x : x[:3])
    cross_tab = pd.crosstab(index=filtered_df['arrival_date_month_cat'], columns='count')

    # Create a Heatmap trace for Plotly
    heatmap = go.Heatmap(
        z=cross_tab.values,  # Heatmap data
        x=cross_tab.columns,  # Column labels (x-axis)
        y=cross_tab.index.tolist(),  # Row labels (y-axis)
        colorbar=dict(),  # Add a colorbar
        colorscale='YlGnBu',  
        text=cross_tab.values.flatten(),  # Flatten values for text annotation
    )
    
    # Add count annotations on each heatbar
    annotations = []
    for i, row in enumerate(cross_tab.values):
        for j, value in enumerate(row):
            annotations.append(
                go.layout.Annotation(x=cross_tab.columns[j], y=cross_tab.index[i], text=str(value),
                                     font=dict(color='black', size=25), showarrow=False)  # Adjust font size here
            )
    
    # Update layout with annotations and template
    layout = go.Layout(
        title=dict(text='Arrival Date Month Counts', font=dict(size=30)),  # Increase title size
        xaxis=dict(title='Counts', titlefont=dict(size=25)),  # Increase x-axis label size
        yaxis=dict(title='Month', titlefont=dict(size=25),  tickfont=dict(size=23)),  # Increase y-axis label size
        annotations=annotations,
        template='plotly_dark',  # Add the 'presentation' template
    )

    # Create the figure
    fig = go.Figure(data=heatmap, layout=layout)
    return fig

@app.callback(
    Output('barplot', 'figure'),
    [Input('hotel-type-dropdown-barplot', 'value'),
     Input('meal-type-dropdown-barplot', 'value')]
)
def update_barplot(hotel_type, meal_type):

    if hotel_type != 'Both':
        filtered_df = df[df['hotel'] == hotel_type]
        if meal_type != 'Any':
            filtered_df = filtered_df[filtered_df['meal'] == meal_type]
    else:
        if meal_type != 'Any':
            filtered_df = df[df['meal'] == meal_type]
        else:
            filtered_df = df

    filtered_df['res_date'] = pd.to_datetime(filtered_df['reservation_status_date'])
    filtered_df['res_month'] = filtered_df['res_date'].dt.month
    grouped_data = (
    filtered_df.groupby(['res_month', 'is_canceled'])
    .size()
    .to_frame(name='count')
    .reset_index()
    )
    # print(df['res_month'])
    # Create the bar chart with Plotly Express
    fig = px.bar(grouped_data, x='res_month', y='count', color='is_canceled', barmode='group',template='plotly_dark')

    # Customize the plot
    fig.update_layout(
        title=dict(
            text='Reservation status per month',
            font=dict(
                size=30,  # Set the font size for the title
                family='Arial'  # Set the font family for the title
            )
        ),
        xaxis_title='Month',
        yaxis_title='Number of Reservations',
        xaxis=dict(
            titlefont=dict(
                size=25,  # Set the font size for the x-axis title
                family='Arial'  # Set the font family for the x-axis title
            )
        ),
        yaxis=dict(
            titlefont=dict(
                size=25,  # Set the font size for the y-axis title
                family='Arial'  # Set the font family for the y-axis title
            )
        )
    )

    fig.for_each_trace(lambda t: t.update(name='Canceled' if t.name == '1' else 'Not Canceled'))
    # Customize colors (optional)
    fig.update_traces(marker_line_color='black', marker_line_width=1)
    fig.update_coloraxes(showscale=False)

    return fig

@app.callback(
    Output('boxplot', 'figure'),
    [Input('meal-type-dropdown-boxplot', 'value')]
)
def update_boxplot(meal_type):

    data = df[df['is_canceled'] == 0]

    if meal_type != 'Any':
        data = data[data['meal'] == meal_type]


    fig = px.box(data_frame = data, x = 'reserved_room_type', y = 'adr', color = 'hotel', template = 'plotly_dark')

    fig.update_layout(
        title=dict(
            text='Box plot for Reserved Rooms',
            font=dict(
                size=30  # Set the font size for the title to 30
            )
        ),
        xaxis=dict(
            title='Reserved Rooms Type',
            titlefont=dict(
                size=25  # Set the font size for the x-axis title to 25
            ),
            tickfont=dict(
                size=20  # Set the font size for the x-axis tick labels to 20
            )
        ),
        yaxis=dict(
            title='Average Daily Rate',
            titlefont=dict(
                size=25  # Set the font size for the y-axis title to 25
            ),
            tickfont=dict(
                size=20  # Set the font size for the y-axis tick labels to 20
            )
        ),
        legend=dict(
            font=dict(
                size=20  # Set the font size for the legend to 20
            )
        )
    )

    return fig


@app.callback(
    Output('piechart', 'figure'),
    [Input('slider-updatemode', 'value')]
)
def update_piechart(slider_value):
    cancelled_data = df[df['is_canceled'] == 1]
    top_10_country = cancelled_data['country'].value_counts()[:slider_value]

    fig = px.pie(values=top_10_country, names=top_10_country.index,
                 labels={'names': 'Country', 'values': 'Count'}, 
                 template='plotly_dark')
    
    fig.update_layout(
        title=dict(
            text=f'Top {slider_value} countries with reservation canceled',
            font=dict(
                size=30,  # Set the font size for the title
                family='Arial'  # Set the font family for the title
            )
        ),

        legend=dict(
            font=dict(
                size=20  # Set the font size for the legend to 20
            )
        )
    )

    fig.update_traces(textfont=dict(size=20))

    return fig
# fig.show()

if __name__ == "__main__":
    app.run_server(port=8080)