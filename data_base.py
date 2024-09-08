def data():
    import pandas as pd

    # reading part
    df = pd.read_csv("1 copy.csv")

    # in .ipynb file I did it important works so i copied all of them in to python file!

    to_int = [
        "Investments (USD)",
        "GDP",
        "R&D Expenditure",
        "Energy Subsidies",
        "International Aid for Renewables",
    ]

    to_bool = [
        "Government Policies",
        "Renewable Energy Targets",
        "Energy Efficiency Programs",
        "Energy Market Liberalization",
        "Technology Transfer Agreements",
        "Renewable Energy Education Programs",
        "Natural Disasters",
        "Public-Private Partnerships in Energy",
        "Regional Renewable Energy Cooperation",
    ]
    df[to_int] = df[to_int].astype(int)
    df[to_bool] = df[to_bool].astype(bool)

    # everything is ready I've got database. I need to return it as .csv file
    return df
