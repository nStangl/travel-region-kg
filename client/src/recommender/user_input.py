import ipywidgets as widgets
from dataclasses import dataclass
from datetime import date

_preferences1 = ["nature", "hiking", "beach", "culture", "entertainment"]

_preferences2 = ["citiesArchitecture", "winterSports",
                 "waterSports", "culinary", "shopping"]

_region_descriptions = ["Europe", "North_America", "South_America",
                        "Middle_America_and_Caribbean", "Africa", "Asia",
                        "Oceania"]

budget_widget = widgets.BoundedIntText(
    value=4000,
    min=0,
    max=100000,
    step=100,
    description='Budget in Euro',
    disabled=False,
    indent=False,
    style=dict(description_width="initial")
)

start_at_widget = widgets.DatePicker(
    description='Start at',
    value=date.today(),
    disabled=False,
    indent=False
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
    description="Month:",
    disabled=False
)

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

dashboard = widgets.VBox([
    widgets.HBox([budget_widget, select_month_widget]),
    widgets.HBox([start_at_widget, max_num_days_widget]),
    widgets.Box([widgets.Label("Select the regions you want to visit:")]),
    regions_box,
    widgets.Box([widgets.Label("Select your preferences:")]),
    preferences_box1,
    preferences_box2
])


@dataclass
class DashboardData():
    budget: int
    month: str
    startAt: date
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
                         start_at_widget.value, max_num_days_widget.value,
                         regions, preferences)


# Example Query
# BASE <http://cit.tum.de/ressource/travelkg/>
# PREFIX mapper: <http://www.ontotext.com/mapper/>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# PREFIX dbo: <http://dbpedia.org/ontology/>
# PREFIX travelkg: <http://cit.tum.de/ontology/travelkg/>
# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# PREFIX travelregion: <http://cit.tum.de/ressource/travelkg/region/>

# select ?region ?costIRI ?costLabel
# where {
#     VALUES (?allowed_region) {
#         (travelregion:North_Europe)
#         (travelregion:Central_Europe)
#     }
#     ?region dbo:subregion* ?allowed_region .
#     ?region travelkg:avgCostPerWeek/rdfs:label ?costLabel .
#     FILTER(?costLabel < 550)
# } limit 20
