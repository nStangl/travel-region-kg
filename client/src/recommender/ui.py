import ipywidgets as widgets
from IPython.display import display, Markdown
from dataclasses import dataclass
from recommender.lib import execute


@dataclass
class DashboardData():
    budget: int
    month: str
    maxDays: int
    regions: dict()
    preferences: dict()


def getDashboardInput():
    regions = dict()
    for check in regions_box.children:
        regions[check.description] = check.value

    preferences = dict()
    for check in preferences_box1.children:
        preferences[check.description] = check.value

    for check in preferences_box2.children:
        preferences[check.description] = check.value

    return DashboardData(budget_widget.value, select_month_widget.value,
                         max_num_days_widget.value, regions, preferences)


def recommend_handler(x):
    with recommendation_output:
        recommendation_output.clear_output()
        output = execute(getDashboardInput())
        display(Markdown(output))


budget_widget = widgets.BoundedIntText(
    value=2000,
    min=0,
    max=100000,
    step=100,
    description='Budget in Euro',
    disabled=False,
    indent=False,
    style=dict(description_width="initial")
)

max_num_days_widget = widgets.BoundedIntText(
    value=45,
    min=1,
    max=365,
    step=1,
    description='Max. number of days',
    disabled=False,
    indent=False,
    style=dict(description_width="initial")
)

select_month_widget = widgets.Dropdown(
    options=["january", "february", "march", "april", "may",
             "june", "july", "august", "september", "december"],
    value="january",
    description="Month of visit:",
    disabled=False,
    style=dict(description_width="initial")
)

_preferences1 = ["nature", "hiking", "beach", "culture", "entertainment"]

_preferences2 = ["citiesArchitecture", "winterSports",
                 "waterSports", "culinary", "shopping"]

_region_descriptions = ["Europe", "North_America", "South_America",
                        "Middle_America_and_Caribbean", "Africa", "Asia",
                        "Oceania"]

regions_box = widgets.HBox(
    [widgets.Checkbox(value=True, description=desc,
                      disabled=False, indent=False)
        for desc in _region_descriptions])

preferences_box1 = widgets.HBox(
    [widgets.Checkbox(value=False, description=desc,
                      disabled=False, indent=False)
        for desc in _preferences1])

preferences_box2 = widgets.HBox(
    [widgets.Checkbox(value=False, description=desc,
                      disabled=False, indent=False)
        for desc in _preferences2])

query_button = widgets.Button(
    description='Recommend me',
    disabled=False,
    button_style='info',
    tooltip='Click me',
    icon='',
    layout=widgets.Layout(position='right')
)

recommendation_output = widgets.Output()

query_button.on_click(recommend_handler)

dashboard = widgets.VBox([
    widgets.HTML(value="<b>Travel Region Recommender</b>"),
    widgets.Box([widgets.Label("Input your constraints:")]),
    widgets.HBox([budget_widget, select_month_widget, max_num_days_widget]),
    widgets.Box([widgets.Label("Select the regions you want to visit:")]),
    regions_box,
    widgets.Box([widgets.Label("Select your preferences:")]),
    preferences_box1,
    preferences_box2,
    query_button,
    recommendation_output,
])
