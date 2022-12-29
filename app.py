# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import datetime
import traceback
import logging

import config
from src import util
from src import dataloader

import numpy as np
import pandas as pd

import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title='Powerplant Analysis',
                   page_icon=":chart_with_upwards_trend:",
                   layout='wide', initial_sidebar_state='collapsed')

st.title('Powerplant Statistics', )


LINE = """<style>
        .vl {
        border-left: 2px solid black;
        height: 100px;
        position: absolute;
        left: 50%;
        margin-left: -3px;
        top: 0;
        }
    </style>
    <div class="vl"></div>"""

params = config.Config()
# Calculating Yesterday date
current_date = datetime.datetime.now(
    params.tzinfo) - datetime.timedelta(1, minutes=0, hours=12)

logging.info(f'Processing for Date: {current_date}')

row1_col1, row1_col2, row1_col3, row1_col4, row1_col5 = st.columns([4, 10, 10, 10, 2, ])
query_params = st.experimental_get_query_params()

row1_col5.write("**[Linkedin](https://www.linkedin.com/in/manishsahuiitbhu/):beer:**",
           unsafe_allow_html=True)

# event_options = ['Energy', 'Nuclear Accidents']
# event_options_value = col1.radio('Type of Events', event_options)
event_options_value  = 'Energy'

nuclear_dataloader = dataloader.NuclearDataLoader(path_csv=params.path_nuclear_csv)
energy_dataloader = dataloader.EnergyDataLoader(path_csv=params.path_energy_csv)

data_nuclear = nuclear_dataloader.load_dataset()
data_energy = energy_dataloader.load_dataset()


if event_options_value == 'Nuclear Accidents':
    pass

else:
    default_index = 3
    energy_type = row1_col4.selectbox("Filter by Energy Types", params.ENERGY_TYPES, index=default_index)

    ############################ Frist Chart #################################

    # with row1_col1:
    #     text_col1 = f'Nuclear Capacity (GW)'
    #     st.markdown(f"<h3 style='text-align: center;'>{text_col1}</h3>",
    #                 unsafe_allow_html=True)

    #     ## Here Nuclear Energy
    #     default_energy_type = params.ENERGY_TYPES[default_index]
    #     default_energy_value = energy_dataloader.get_specific_energy_capacity(energy_type=default_energy_type)

    #     value = int(default_energy_value/1000) # For GW
    #     st.markdown(
    #         f"<h3 style='text-align: center; color: blue;'>{value}</h3>", unsafe_allow_html=True)


    ############################ Second Chart #################################

    row2_col1, row2_line, row2_col2, row2_col3 = st.columns([4, 2, 20, 2])

    with st.container():
        # row2_line.markdown(LINE, unsafe_allow_html=True)

        with row2_col1:
            text_row2_col1 = f'Installed Capacity by Fuel Source'
            st.markdown(f"<h3 style='text-align: left;'>{text_row2_col1}</h3>",
                        unsafe_allow_html=True)

        with row2_col2:
            energy_capacity_fuel_wise = energy_dataloader.get_energy_capacity_fuel_wise()

            fig = px.bar(energy_capacity_fuel_wise, x='primary_fuel', y='capacity_mw', height=300, )
            st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            # st.bar_chart(energy_capacity_fuel_wise, use_container_width=True)


    ############################ Third Chart #################################


    row2_col1, row2_line, row2_col2, row2_col3 = st.columns([4, 2, 20, 2])

    with st.container():
        # row2_line.markdown(LINE, unsafe_allow_html=True)

        with row2_col1:
            text_row2_col1 = f'Average Plant Size (MW)'
            st.markdown(f"<h3 style='text-align: left;'>{text_row2_col1}</h3>",
                        unsafe_allow_html=True)


        with row2_col2:
            avg_power_plant_Size_fuel_wise = energy_dataloader.get_average_plant_size_fuel_size()

            fig = px.bar(avg_power_plant_Size_fuel_wise, x='primary_fuel', y='capacity_mw', height=300,)
            st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            # st.bar_chart(energy_capacity_fuel_wise, use_container_width=True)


     ############################ Fourth Chart #################################

    row3_col1, row2_line, row3_col2, row3_col3 = st.columns([4, 2, 20, 2])
 
    with st.container():
        # row2_line.markdown(LINE, unsafe_allow_html=True)

        with row3_col1:
            text_row2_col1 = f'Installed Capacity in Top 10 Countries in ({energy_type})'
            st.markdown(f"<h3 style='text-align: left;'>{text_row2_col1}</h3>",
                        unsafe_allow_html=True)

            value = int(energy_dataloader.get_specific_energy_capacity(energy_type=energy_type)/1000) # For GW
            st.markdown(
                f"<h3 style='text-align: left; color: blue;'>{value} GW</h3>", unsafe_allow_html=True)


        with row3_col2:
            top_12_country_capacity = energy_dataloader.get_top_12_country_energy_capacity_fuel_wise(energy_type=energy_type)
            fig = px.bar(top_12_country_capacity, x='country_long', y='capacity_mw', height=300, )
            st.plotly_chart(fig, theme="streamlit", use_container_width=True)

            # st.bar_chart(top_12_country_capacity, use_container_width=True)


    ############################ Fifth Chart #################################
    tab1, _ = st.tabs(["GeoSpatial Map", "."])
    px.set_mapbox_access_token(params.MAPBOX_TOKEN)

    with st.container():
        fig = px.scatter_mapbox(data_energy, 
                                lat="latitude", lon="longitude", 
                                color="primary_fuel", size="map_size",
                                color_discrete_sequence=px.colors.qualitative.G10_r,
                                # color_continuous_scale=px.colors.sequential.Jet, 
                                size_max=25, zoom=2,
                                hover_data=['name', 'capacity_mw', 'primary_fuel'],
                                height=700)
        # fig.show()
        with tab1:
            # Use the Streamlit theme.
            # This is the default. So you can also omit the theme argument.
            st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    

# rule = st.selectbox('Variables', params.rules_cols)

# st.plotly_chart(custom_plot.summary(
#     data_state_cls.data, rule), use_container_width=True)

# st.write("**:beer: Buy me a [beer]**")
expander = st.expander("This app is developed by Gunjan Indauliya.")
expander.write(
    "Contact me on [Linkedin](https://www.linkedin.com/in/gunjan-indauliya/)")
expander.write(
    "The source code is on [GitHub](https://github.com/ManishSahu53/streamlit-covid-dashboard)")
