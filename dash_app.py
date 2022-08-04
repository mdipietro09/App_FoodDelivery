###############################################################################
#                            RUN MAIN                                         #
###############################################################################

# setup
import warnings
warnings.filterwarnings("ignore")

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from python.model import Model
import config


# App Instance
app = dash.Dash(name=config.app_name, assets_folder="static", external_stylesheets=[dbc.themes.LUX, config.fontawesome])
app.title = config.app_name



########################## Navbar ##########################
navbar = dbc.Nav(className="nav nav-pills", children=[
    ## logo/home
    dbc.NavItem(html.Img(src=app.get_asset_url("logo.PNG"), height="40px")),
    ## about
    dbc.NavItem(html.Div([
        dbc.NavLink("About", href="/", id="about-popover", active=False),
        dbc.Popover(id="about", is_open=False, target="about-popover", children=[
            dbc.PopoverHeader("How it works"), dbc.PopoverBody(config.about)
        ])
    ])),
    ## links
    dbc.DropdownMenu(label="Links", nav=True, children=[
        dbc.DropdownMenuItem([html.I(className="fa fa-linkedin"), "  Contacts"], href=config.contacts, target="_blank"), 
        dbc.DropdownMenuItem([html.I(className="fa fa-github"), "  Code"], href=config.code, target="_blank"),
        dbc.DropdownMenuItem([html.I(className="fa fa-medium"), "  Tutorial"], href=config.tutorial, target="_blank")
    ])
])


# Callbacks
@app.callback(output=[Output(component_id="about", component_property="is_open"), 
                      Output(component_id="about-popover", component_property="active")], 
              inputs=[Input(component_id="about-popover", component_property="n_clicks")], 
              state=[State("about","is_open"), State("about-popover","active")])
def about_popover(n, is_open, active):
    if n:
        return not is_open, active
    return is_open, active



########################## Body ##########################
body = html.Div([
        ## input for plot
        dbc.FormGroup([
            dbc.Row([
                dbc.Col(md=2, children=[dbc.Input(id="start-id", placeholder="city", type="text", value="Hong Kong")]),
                dbc.Col(dbc.Button("Reset", id="reset-button", color="primary"))
            ])
        ]),
        
        ## output
        dcc.Loading(type='cube', color='black', children=[
            html.Iframe(id="map", src="static/output.html", width="80%", height="500", style={"border":"none"})
        ])
])


# Callbacks
@app.callback(output=Output(component_id="map", component_property="children"),
              inputs=Input(component_id="reset-button", component_property="n_clicks"), 
              state=[State("start-id","value")])
def plot_map(n, start):
    end = (22.30, 114.17)
    model = Model(start.strip(), end)
    route = model.calculate_route()
    model.create_map(route) 
    


########################## App Layout ##########################
app.layout = dbc.Container(fluid=True, children=[
    html.H1(config.app_name, id="nav-pills"),
    navbar,
    html.Br(),html.Br(),html.Br(),
    body
])



########################## Run ##########################
if __name__ == "__main__":
    debug = True if config.ENV == "DEV" else False
    app.run_server(debug=debug, host=config.host, port=config.port)
        