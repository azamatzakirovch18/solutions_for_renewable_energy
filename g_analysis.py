from statsmodels.graphics import agreement


def analysis():
    import streamlit as st
    from data_base import data
    import matplotlib.pyplot as plt

    flag = True
    df = data()
    with st.sidebar:
        st.write("# Filters")
        # st.write("_______________________")
        countries = st.selectbox(
            "Please choose a country you want to analyze",
            options=[
                "USA",
                "Russia",
                "Australia",
                "Canada",
                "Japan",
                "China",
                "India",
                "Germany",
                "France",
                "Brazil",
            ],
        )

        type_of_analyse = st.selectbox(
            "Method of analysis",
            options=[
                "Renewable Energy Data",
                "Socio-Economic Indicators",
                "Environmental Factors",
                "Additional Features",
            ],
        )

    if type_of_analyse == "Renewable Energy Data":
        left, right = st.columns(2)
        # I need to select a year from 2000 to 2023 and i need to control user must not choose similar years like start == stop it is not possible
        with left:
            years = [i for i in range(2000, 2024)]
            start, stop = st.slider(
                "Select a range of years",
                min_value=min(years),
                max_value=max(years),
                value=(min(years), max(years)),  # Default to full range
            )
        # In dataset has column named Energy Type so it is very important

        with right:
            energy_types = st.multiselect(
                "Select energy types",
                options=["Solar", "Geothermal", "Biomass", "Wind", "Hydro"],
                default=["Solar"],
            )

        # I should change the data set

        df = df[
            (df["Country"] == countries)
            & (df["Year"].between(start, stop))
            & (df["Energy Type"].isin(energy_types))
        ]

        if start == stop:
            st.error("Years interval must be equal at least 1 year")
        else:
            left_producing, right_producing = st.columns(2)
            with left_producing:
                df_for_renewable_energy_data = df[
                    ["Country", "Year", "Energy Type", "Production (GWh)"]
                ]

                o = df_for_renewable_energy_data.pivot_table(
                    index="Year",
                    columns="Energy Type",
                    values="Production (GWh)",
                    # aggfunc="sum",
                )
                st.write("Production (GWh)")
                st.line_chart(o)

            with right_producing:
                df_for_renewable_energy_data = df[
                    ["Country", "Year", "Energy Type", "Installed Capacity (MW)"]
                ]

                p = df_for_renewable_energy_data.pivot_table(
                    index="Year",
                    columns="Energy Type",
                    values="Installed Capacity (MW)",
                    # aggfunc="sum",
                )
                st.write("Installed Capacity (MW)")
                st.line_chart(p)

            df_for_investments = df[
                ["Country", "Year", "Energy Type", "Investments (USD)"]
            ]

            p = df_for_investments.pivot_table(
                index="Year",
                columns="Energy Type",
                values="Investments (USD)",
                # aggfunc="sum",
            )
            st.write("Investments (USD)")
            st.line_chart(p)

    if type_of_analyse == "Socio-Economic Indicators":
        left, right = st.columns(2)
        # I need to select a year from 2000 to 2023 and i need to control user must not choose similar years like start == stop it is not possible
        with left:
            years = [i for i in range(2000, 2024)]
            start, stop = st.slider(
                "Select a range of years",
                min_value=min(years),
                max_value=max(years),
                value=(min(years), max(years)),  # Default to full range
            )
        # In dataset has column named Energy Type so it is very important

        with right:
            energy_types = st.selectbox(
                "Select energy types",
                options=["Solar", "Geothermal", "Biomass", "Wind", "Hydro"],
                index=0,
            )

        # I should change the data set

        df = df[
            (df["Country"] == countries)
            & (df["Year"].between(start, stop))
            & (df["Energy Type"] == (energy_types))
        ]

        if start == stop:
            st.error("Years interval must be equal at least 1 year")
        else:

            primary, private = st.columns(2)

            with primary:
                st.write("## Primary Sector")

                df_primary = df[df["Government Policies"] == True]
                df_primary = df_primary[
                    [
                        "Country",
                        "Year",
                        "Energy Type",
                        "Energy Exports",
                        "Energy Imports",
                    ]
                ]

                df_primary_pivot = df_primary.pivot_table(
                    index="Year",
                    values=["Energy Exports", "Energy Imports"],
                    # aggfunc="sum",
                )

                st.line_chart(df_primary_pivot)

            with private:
                st.write("## Private Sector")
                df_private = df[df["Government Policies"] == False]
                df_private = df_private[
                    [
                        "Country",
                        "Year",
                        "Energy Type",
                        "Energy Exports",
                        "Energy Imports",
                    ]
                ]

                df_private = df_private.pivot_table(
                    index="Year",
                    values=["Energy Exports", "Energy Imports"],
                    # aggfunc="sum",
                )

                st.line_chart(df_private)

            df_main = df[
                [
                    "Country",
                    "Year",
                    "Energy Type",
                    "Energy Consumption",
                    "CO2 Emissions",
                    "Renewable Energy Jobs",
                ]
            ]
            pivot_of_main = df_main.pivot_table(
                index="Year",
                values=["Energy Consumption", "CO2 Emissions", "Renewable Energy Jobs"],
                # aggfunc="sum",
            )
            st.write(
                "Comparison between Energy Consumption,CO2 Emissions,Renewable Energy Jobs"
            )
            st.line_chart(pivot_of_main)

    if type_of_analyse == "Environmental Factors":

        on = st.toggle("Activate feature")

        if on:
            st.write("Feature activated!")

    if type_of_analyse == "Additional Features":
        # List of group names

        groups = [
            "Technical & Infrastructure Capacity",
            "Economic & Financial Aspects",
            "Innovation & Technology",
            "Education & Awareness",
            "Regulatory & Legal Framework",
            "Environmental Factors",
            "Social & Industrial Development",
        ]

        tab_1, tab_2, tab_3, tab_4, tab_5, tab_6, tab_7 = st.tabs(groups)
        with tab_1:
            left, middle, right = st.columns(3)
            # I need to select a year from 2000 to 2023 and i need to control user must not choose similar years like start == stop it is not possible
            with left:
                years = [i for i in range(2000, 2024)]
                start, stop = st.slider(
                    "Select a range of years",
                    min_value=min(years),
                    max_value=max(years),
                    value=(min(years), max(years)),
                )
            # In dataset has column named Energy Type so it is very important

            with middle:
                liberalization = st.selectbox(
                    "Select Your Liberation", ["Supported", "Unsupported", "Total"]
                )

            with right:
                energy_types = st.multiselect(
                    "Select energy types",
                    options=["Solar", "Geothermal", "Biomass", "Wind", "Hydro"],
                    default=["Solar"],
                )

            # I should change the data set

            df = data()
            df = df[
                (df["Country"] == countries)
                & (df["Year"].between(start, stop))
                & (df["Energy Type"].isin(energy_types))
            ]

            if liberalization == "Supported":
                new_lib = df[df["Energy Market Liberalization"] == True]
            elif liberalization == "Unsupported":
                new_lib = df[df["Energy Market Liberalization"] == False]
            elif liberalization == "Total":
                new_lib = df[
                    df["Energy Market Liberalization"]
                    == True & df["Energy Type"].isin(energy_types)
                ]

            left_capacity, right_capacity = st.columns(2)

            with left_capacity:
                st.write("## Energy Storage Capacity & Liberalization")
                tech_pivot = new_lib.pivot_table(
                    index="Year",
                    columns="Energy Type",
                    values="Energy Storage Capacity",
                    # aggfunc="sum",
                )

                st.line_chart(tech_pivot)

                liberalization_pivot = new_lib.pivot_table(
                    index="Year",
                    columns="Energy Type",
                    values="Grid Integration Capability",
                    # aggfunc="sum",
                )

                st.bar_chart(liberalization_pivot)

            with right_capacity:
                st.write(f"## Energy Storage Capacity of {stop}")

                filtered_df = new_lib

                labels = energy_types  # List of energy types

                # Group by 'Energy Type' and sum the 'Energy Storage Capacity'
                share = filtered_df.groupby("Energy Type")[
                    "Energy Storage Capacity"
                ].sum()
                share = share.reindex(
                    labels, fill_value=0
                )  # Ensuring the order matches labels

                colors = [
                    "#FF9999",
                    "#66B2FF",
                    "#99FF99",
                    "#FFCC39",
                    "#FF66CC",
                ]  # Five custom colors

                def absolute_value(val):
                    total = sum(share)
                    return f"{val:.2f}%\n({int(val * total / 100)} GWh)"

                # Plot the pie chart
                plt.figure()
                plt.style.use("ggplot")
                plt.pie(
                    x=share,
                    labels=labels,
                    autopct=absolute_value,
                    shadow=True,
                    startangle=90,
                    colors=colors,
                )
                plt.axis(
                    "equal"
                )  # Equal aspect ratio ensures the pie is drawn as a circle

                # Add a white circle in the center for the donut effect
                circle = plt.Circle((0, 0), 0.75, color="white")
                plt.gca().add_artist(circle)

                # Display the pie chart in Streamlit
                st.pyplot(plt)

                st.write(
                    f"""
                - Pie chart represents Energy Storage Capacity in {stop}. There are 5 different types of renewable
                 energies. Total percentage is 100%. All measurments in GWh
                - Linegraph represents Energy Storage Capacity between {start} and {stop} with 5 different types of renewable energies. 
                - Bar chart represents Anti Monopoly for countries and graded from 1 to 10 between {start} and {stop} years and 5 different types of renewable energies. 
                 
                 """
                )
        with tab_2:
            df_econ = data()
            left_aspect, right_aspect = st.columns(2)

            with left_aspect:
                years = [i for i in range(2000, 2024)]
                start_, stop_ = st.slider(
                    "Select a range of years",
                    min_value=min(years),
                    max_value=max(years),
                    value=(min(years), max(years)),
                    key="year_range_slider",
                )

            with right_aspect:
                energy_types = st.selectbox(
                    "Select energy types",
                    options=["Solar", "Geothermal", "Biomass", "Wind", "Hydro"],
                    # default=["Solar"],
                    index=0,
                    key=energy_types,
                )

            df_econ = df_econ[
                (df_econ["Year"].between(start_, stop_))
                & (df_econ["Energy Type"] == (energy_types))
                & (df_econ["Country"] == countries)
            ]

            left_econ, right_econ = st.columns(2)

            with left_econ:
                econ_pivot = df_econ.pivot_table(
                    index="Year",
                    columns="Energy Type",
                    values="Electricity Prices",
                    # aggfunc="sum",
                )
                st.write("## Electricity Prices")
                st.bar_chart(econ_pivot)
                # st.line_chart(econ_pivot)

                subsidies = df_econ.pivot_table(
                    index="Year", columns="Energy Type", values="Energy Subsidies"
                )

                st.write("## Energy Subsidies")

                st.line_chart(subsidies)

            with right_econ:
                econ_pivot = df_econ.pivot_table(
                    index="Year",
                    values=[
                        "Export Incentives for Energy Equipment",
                        "Import Tariffs on Energy Equipment",
                        "Economic Freedom Index",
                        "Ease of Doing Business",
                    ],
                )
                st.write("## Graph of 4 columns")
                st.line_chart(econ_pivot)

                aid_pivot = df_econ.pivot_table(
                    index="Year",
                    columns="Energy Type",
                    values="International Aid for Renewables",
                )

                st.write("## International Aid for Renewables")

                st.line_chart(aid_pivot)

        with tab_3:
            inno_left, inno_middle, inno_right = st.columns(3)
            inno_years = [i for i in range(2000, 2024)]
            with inno_left:
                inno_start, inno_end = st.slider(
                    "Select a range of years",
                    min_value=min(inno_years),
                    max_value=max(inno_years),
                    value=(min(inno_years), max(inno_years)),
                    key="inno_years_range",
                )
            with inno_middle:
                inno_agreement = st.selectbox(
                    "Technology Transfer Agreements",
                    options=["Agree", "Disagree", "Total"],
                )

            with inno_right:
                inno_energy = st.selectbox(
                    "Please choose your energy type you want !",
                    options=["Solar", "Geothermal", "Biomass", "Wind", "Hydro"],
                    index=0,
                )

            inno_df = data()
            inno_df = inno_df[
                inno_df["Year"].between(inno_start, inno_end)
                & (inno_df["Energy Type"] == inno_energy)
                & (inno_df["Country"] == countries)
            ]

            if inno_agreement == "Agree":
                inno_df = inno_df[inno_df["Technology Transfer Agreements"] == True]
            elif inno_agreement == "Disagree":
                inno_df = inno_df[inno_df["Technology Transfer Agreements"] == False]

            inno_left_g, inno_right_g = st.columns(2)
            with inno_left_g:
                inno_pivot = inno_df.pivot_table(
                    index="Year",
                    columns="Energy Type",
                    values="Renewable Energy Patents",
                )

                st.write("## Renewable Energy Patents")

                st.bar_chart(inno_pivot)

            with inno_right_g:
                # Create pivot table
                inno_pivot_2 = inno_df.pivot_table(
                    index="Year",
                    columns="Energy Type",
                    values=["Local Manufacturing Capacity", "Innovation Index"],
                )

                # Flatten the MultiIndex columns
                inno_pivot_2.columns = [
                    " ".join(col).strip() for col in inno_pivot_2.columns.values
                ]

                st.write("## Local Manufacturing Capacity & Innovation Index")
                st.line_chart(inno_pivot_2)

        with tab_4:
            st.write("## Education & Awareness")
            edu_left, edu_middle, edu_right = st.columns(3)

            with edu_left:
                edu_years_Range = [i for i in range(2000, 2024)]
                edu_start, edu_end = st.slider(
                    "Select a range of years",
                    min_value=min(edu_years_Range),
                    max_value=max(edu_years_Range),
                    value=(min(edu_years_Range), max(edu_years_Range)),
                    key="edu_years_range",
                )

            with edu_middle:
                edu_programs = st.selectbox(
                    "Renewable Energy Education Programs",
                    options=["Exist", "Unexist", "Total"],
                )

            with edu_right:
                edu_energy_types = st.multiselect(
                    "Please choose your energy type you want !",
                    options=["Solar", "Geothermal", "Biomass", "Wind", "Hydro"],
                    default=["Solar", "Geothermal"],
                )

            edu_df = data()

            edu_df = edu_df[
                (edu_df["Year"].between(edu_start, edu_end))
                & (edu_df["Energy Type"].isin(edu_energy_types))
                & (edu_df["Country"] == countries)
            ]

            if edu_programs == "Exist":
                edu_df = edu_df[edu_df["Renewable Energy Education Programs"] == True]
            elif edu_programs == "Unexist":
                edu_df = edu_df[edu_df["Renewable Energy Education Programs"] == False]

            edu_df = edu_df[
                [
                    "Year",
                    "Energy Type",
                    "Country",
                    "Public Awareness",
                    "Educational Level",
                ]
            ]

            edu_g_left, edu_g_right = st.columns(2)

            with edu_g_left:
                st.write("## Public Awareness")
                edu_g_left_pivot = edu_df.pivot_table(
                    index="Year", columns="Energy Type", values="Public Awareness"
                )

                st.line_chart(edu_g_left_pivot)

            with edu_g_right:
                st.write("## Educational Level")
                edu_g_right_pivot = edu_df.pivot_table(
                    index="Year", columns="Energy Type", values="Educational Level"
                )

                st.bar_chart(edu_g_right_pivot)
        with tab_5:
            side_a = [
                "Political Stability",
                "Regulatory Quality",
            ]
            side_b = [
                "Corruption Perception Index",
                "Rule of Law",
                "Control of Corruption",
            ]

            frame_df = data()

            framework_left, framework_right = st.columns(2)

            with framework_left:
                frame_years = [i for i in range(2000, 2024)]
                frame_s, frame_e = st.slider(
                    "Please choose years range",
                    min_value=min(frame_years),
                    max_value=max(frame_years),
                    value=(min(frame_years), max(frame_years)),
                )

            with framework_right:
                frame_energies = st.selectbox(
                    "Please choose energy type you want !",
                    options=["Solar", "Geothermal", "Biomass", "Wind", "Hydro"],
                    index=0,
                )

            frame_left, frame_right = st.columns(2)

            with frame_left:
                side_aa = frame_df[
                    (frame_df["Year"].between(frame_s, frame_e))
                    & (frame_df["Energy Type"] == frame_energies)
                    & (frame_df["Country"] == countries)
                ]
                a_help = side_aa[
                    [
                        "Year",
                        "Energy Type",
                        "Country",
                        "Political Stability",
                        "Regulatory Quality",
                    ]
                ]
                st.write("### About Politics")

                frame_a_pivot = a_help.pivot_table(
                    index="Year",
                    # columns = "Energy Type",
                    values=["Political Stability", "Regulatory Quality"],
                )

                st.line_chart(frame_a_pivot)

            with frame_right:
                st.write("### About Corruption")
                side_aa = frame_df[
                    (frame_df["Year"].between(frame_s, frame_e))
                    & (frame_df["Energy Type"] == frame_energies)
                    & (frame_df["Country"] == countries)
                ]
                a_help = side_aa[
                    [
                        "Year",
                        "Energy Type",
                        "Country",
                        "Corruption Perception Index",
                        "Rule of Law",
                        "Control of Corruption",
                    ]
                ]

                frame_a_pivot = a_help.pivot_table(
                    index="Year",
                    # columns = "Energy Type",
                    values=[
                        "Corruption Perception Index",
                        "Rule of Law",
                        "Control of Corruption",
                    ],
                )

                st.line_chart(frame_a_pivot)
        with tab_6:
            nature_left, nature_middle, nature_right = st.columns(3)

            with nature_left:
                nature_years = [i for i in range(2000, 2024)]
                nature_start, nature_end = st.slider(
                    "Please choose years range",
                    min_value=min(nature_years),
                    max_value=max(nature_years),
                    value=(min(nature_years), max(nature_years)),
                    key="nature_years",
                )
            with nature_middle:
                nature_disasters = st.selectbox(
                    "Please choose disaster you want !",
                    options=["Yes", "No", "Total"],
                    index=0,
                )

            with nature_right:
                nature_energy_types = st.multiselect(
                    "Please choose your energy type you want !",
                    options=["Solar", "Geothermal", "Biomass", "Wind", "Hydro"],
                    default=["Solar", "Geothermal"],
                    key="nature_energy_types",
                )
            nature_df = data()

            if nature_disasters == "Yes":
                nature_df = nature_df[
                    (nature_df["Energy Type"].isin(nature_energy_types))
                    & (nature_df["Country"] == countries)
                    & (nature_df["Year"].between(nature_start, nature_end))
                    & (nature_df["Natural Disasters"] == True)
                ]
            elif nature_disasters == "No":
                nature_df = nature_df[
                    (nature_df["Energy Type"].isin(nature_energy_types))
                    & (nature_df["Country"] == countries)
                    & (nature_df["Year"].between(nature_start, nature_end))
                    & (nature_df["Natural Disasters"] == False)
                ]
            elif nature_disasters == "Total":
                nature_df = nature_df[
                    (nature_df["Energy Type"].isin(nature_energy_types))
                    & (nature_df["Country"] == countries)
                    & (nature_df["Year"].between(nature_start, nature_end))
                ]
            # Remove duplicates based on 'Year' and 'Energy Type'
            nature_df = nature_df.drop_duplicates(subset=["Year", "Energy Type"])

            st.write("Proportion of Energy from Renewables")
            nature_df_pivot = nature_df.pivot(
                index="Year",
                columns="Energy Type",
                values="Proportion of Energy from Renewables",
            )

            st.line_chart(nature_df_pivot)
        with tab_7:
            social_industrial_development = [
                "Urbanization Rate",
                "Industrialization Rate",
                "Energy Sector Workforce",
                "Public-Private Partnerships in Energy",
            ]
            dffff = data()
            st.write(dffff[social_industrial_development])
