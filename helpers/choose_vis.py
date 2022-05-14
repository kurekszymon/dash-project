from .generate_charts import generate_bar_chart, generate_table


def choose_visualisation(visualisation, dataframe, x=None, y=None):
    if visualisation == "Table":
        return generate_table(dataframe=dataframe)
    if visualisation == "Bar Chart":
        return generate_bar_chart(dataframe=dataframe, x=x, y=y)
        
