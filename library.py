import ipywidgets as widgets
from ipywidgets import Checkbox

row1_desc = ["Nature & Wildlife", "Hiking",
             "Beach", "Culture", "Entertainment"]
row2_desc = ["Cities & Architecture", "Wintersports",
             "Watersports", "Culinary", "Shopping"]

row1 = widgets.HBox([widgets.Checkbox(value=False, description=desc,
                                      disabled=False, indent=False) for desc in row1_desc])
row2 = widgets.HBox([widgets.Checkbox(value=False, description=desc,
                                      disabled=False, indent=False) for desc in row2_desc])

budget = widgets.BoundedIntText(
    value=4000,
    min=0,
    max=100000,
    step=100,
    description='Budget in Euro',
    disabled=False,
    indent=False
)

start_at = widgets.DatePicker(
    description='Start at',
    disabled=False,
    indent=False
)

max_num_days = widgets.BoundedIntText(
    value=45,
    min=1,
    max=365,
    step=1,
    description='Max. number of days',
    disabled=False,
    indent=False
)
row0 = widgets.HBox([start_at, max_num_days])

dashboard = widgets.VBox([budget, row0, row1, row2])
