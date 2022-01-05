from app.db_access import get_all_entries

import pandas as pd
import plotly.express as px
import plotly
import json

def get_plot():
    entries = get_all_entries()
    df = pd.DataFrame.from_records([e.to_dict() for e in entries])
    fig = px.line(df, x='date', y='temperature')
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

