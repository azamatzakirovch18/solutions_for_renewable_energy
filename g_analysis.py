def analysis():
    import streamlit as st
    from data_base import data

    df = data()
    with st.sidebar:
        countries = st.selectbox(
            "Please choose a country you want to analyze",
            options=['USA', "Russia", 'Australia', 'Canada', 'Japan', 'China', 'India', 'Germany',
                     'France', 'Brazil']
        )

        type_of_analyse = st.selectbox(
            "Method of analysis",
            options=['Renewable Energy Data',
                     "Socio-Economic Indicators",
                     'Environmental Factors']

        )


    if type_of_analyse == 'Renewable Energy Data':
        left, right = st.columns(2)
        # I need to select a year from 2000 to 2023 and i need to control user must not choose similar years like start == stop it is not possible
        with left:
            years = [i for i in range(2000, 2024)]
            start, stop = st.slider(
                'Select a range of years',
                min_value=min(years),
                max_value=max(years),
                value=(min(years), max(years))  # Default to full range
            )
        # In dataset has column named Energy Type so it is very important

        with right:
            energy_types = st.multiselect(
                "Select energy types",
                options=[
                    'Solar',
                    'Geothermal',
                    'Biomass',
                    'Wind',
                    'Hydro'
                ],
                default=['Solar']
            )

        # I should change the data set

        df = df[
            (df['Country'] == countries) &
            (df['Year'].between(start, stop)) &
            (df['Energy Type'].isin(energy_types))
            ]

        if start == stop:
            st.error('Years interval must be equal at least 1 year')
        else:
            left_producing, right_producing = st.columns(2)
            with left_producing:
                df_for_renewable_energy_data = df[['Country', 'Year', 'Energy Type', 'Production (GWh)']]

                o = df_for_renewable_energy_data.pivot_table(
                    index="Year",
                    columns="Energy Type",
                    values="Production (GWh)",
                    aggfunc="sum"
                )
                st.write("Production (GWh)")
                st.line_chart(o)

            with right_producing:
                df_for_renewable_energy_data = df[['Country', 'Year', 'Energy Type', 'Installed Capacity (MW)']]

                p = df_for_renewable_energy_data.pivot_table(
                    index="Year",
                    columns="Energy Type",
                    values="Installed Capacity (MW)",
                    aggfunc="sum"
                )
                st.write("Installed Capacity (MW)")
                st.line_chart(p)


            df_for_investments = df[['Country', 'Year', 'Energy Type', 'Investments (USD)']]

            p = df_for_investments.pivot_table(
                index="Year",
                columns="Energy Type",
                values="Investments (USD)",
                aggfunc="sum"
            )
            st.write("Investments (USD)")
            st.line_chart(p)

    if type_of_analyse == "Socio-Economic Indicators":
        left, right = st.columns(2)
        # I need to select a year from 2000 to 2023 and i need to control user must not choose similar years like start == stop it is not possible
        with left:
            years = [i for i in range(2000, 2024)]
            start, stop = st.slider(
                'Select a range of years',
                min_value=min(years),
                max_value=max(years),
                value=(min(years), max(years))  # Default to full range
            )
        # In dataset has column named Energy Type so it is very important

        with right:
            energy_types = st.selectbox(
                "Select energy types",
                options=[
                    'Solar',
                    'Geothermal',
                    'Biomass',
                    'Wind',
                    'Hydro'
                ],
                index = 0
            )

        # I should change the data set

        df = df[
            (df['Country'] == countries) &
            (df['Year'].between(start, stop)) &
            (df['Energy Type'] == (energy_types))
            ]

        if start == stop:
            st.error('Years interval must be equal at least 1 year')
        else:

            primary,private = st.columns(2)



            with primary:
                st.write('## Primary Sector')

                df_primary = df[df['Government Policies'] == True]
                df_primary = df_primary[['Country', 'Year', 'Energy Type', 'Energy Exports', "Energy Imports"]]

                df_primary_pivot = df_primary.pivot_table(
                    index="Year",
                    values=["Energy Exports", "Energy Imports"],
                    aggfunc="sum"
                )

                st.line_chart(df_primary_pivot)

            with private:
                st.write('## Private Sector')
                df_private = df[df['Government Policies'] == False]
                df_private = df_private[['Country', 'Year', 'Energy Type', 'Energy Exports',"Energy Imports"]]

                df_private = df_private.pivot_table(
                    index="Year",
                    values=["Energy Exports", "Energy Imports"],
                    aggfunc="sum"
                )

                st.line_chart(df_private)

            df_main = df[['Country', 'Year', 'Energy Type',"Energy Consumption","CO2 Emissions","Renewable Energy Jobs"]]
            pivot_of_main = df_main.pivot_table(
                index="Year",
                values=["Energy Consumption","CO2 Emissions","Renewable Energy Jobs"],
                aggfunc="sum"
            )
            st.write("Comparison between Energy Consumption,CO2 Emissions,Renewable Energy Jobs")
            st.line_chart(pivot_of_main)





