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

st.set_page_config(page_title='Nuclear Powerplants',
                   page_icon=":chart_with_upwards_trend:",
                   layout='wide', initial_sidebar_state='collapsed')

st.title('Nuclear Powerplants', )

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

col1, col2, col3, col4 = st.columns([2, 2, 2, 2, ])
query_params = st.experimental_get_query_params()

col3.write("**[Linkedin](https://www.linkedin.com/in/manishsahuiitbhu/)<br>[:beer:]**",
           unsafe_allow_html=True)
options = ['Infection', 'Vaccines']

what = col1.radio('Type of Data', options)
area = col2.selectbox("Region", list(['India', 'USA', 'Germany']))

st.header('Real time data updated till {}'.format(
    current_date.strftime('%Y-%m-%d')))

col1, line, col3, col4, col5, col6, col7, col8 = st.columns(
    [10, 1, 8, 8, 8, 8, 8, 8])
line.markdown(LINE, unsafe_allow_html=True)

nuclear_dataloader = dataloader.NuclearDataLoader(path_csv=params.path_nuclear_csv)
energy_dataloader = dataloader.EnergyDataLoader(path_csv=params.path_energy_csv)

data_nuclear = nuclear_dataloader.load_dataset()
data_energy = energy_dataloader.load_dataset()

# Loading Full india or State wise
if area == 'nuclear':
    data = data_nuclear
    cols = nuclear_dataloader.cols

else:
    data = data_energy
    cols = energy_dataloader.cols

with col1:
    rule = st.radio('', list(['r1', 'r2', 'r3']))
    st.write('')
    log = st.checkbox('Log Scale', False)

# Daily Confirmed Cases
with col3:
    st.markdown("<h3 style='text-align: center;'>Daily Cases</h2>",
                unsafe_allow_html=True)

    value = 0
    text = f''
    st.markdown(
        f"<h2 style='text-align: center; color: red;'>{text}</h1>", unsafe_allow_html=True)

# Daily Deaths
with col4:
    st.markdown("<h3 style='text-align: center;'>Daily Deceased</h2>",
                unsafe_allow_html=True)

    value = 0
    text = f''
    st.markdown(
        f"<h2 style='text-align: center; color: red;'>{text}</h1>", unsafe_allow_html=True)

# Daily Recovered
with col5:
    st.markdown("<h3 style='text-align: center;'>Daily Recovery</h2>",
                unsafe_allow_html=True)

    value = 0
    text = f''
    st.markdown(
        f"<h2 style='text-align: center; color: red;'>{text}</h1>", unsafe_allow_html=True)

# Daily Tested
with col6:
    st.markdown("<h3 style='text-align: center;'>Daily Tests</h2>",
                unsafe_allow_html=True)

    value = 0
    text = f''
    st.markdown(
        f"<h2 style='text-align: center; color: red;'>{text}</h1>", unsafe_allow_html=True)

# Total Recovered
with col7:
    st.markdown("<h3 style='text-align: center;'>Total Recovered</h2>",
                unsafe_allow_html=True)
    
    value = 0 
    text = f''
    st.markdown(
        f"<h2 style='text-align: center; color: red;'>{text}</h1>", unsafe_allow_html=True)

coln, _, _, _, _, _, _ = st.columns([8, 4, 8, 8, 8, 8, 8])
type_of_timeseries = coln.selectbox(
    "", ['Daily Cases', 'Daily Recoveries', 'Daily Deaths', 'Daily Tests', 'Positivity Rate'])


y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fig2 = px.line(y=y,
                x=x,
                title='Daily Statistics',
                labels={'y': type_of_timeseries,
                        'x': 'Time Period'},
                line_shape='spline',
                )

fig2.add_vline(x='2020-09-16',
                line_width=1,
                line_dash="dash",
                line_color="Orange")

fig2.add_vline(x='2021-02-18',
                line_width=1,
                line_dash="dash",
                line_color="Red")

fig2.add_hline(y=5,
                line_width=1,
                line_dash="dash",
                line_color="Green",
                annotation_text="Required Positivity Rate",
                annotation_position="bottom left",
                )

fig2.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
),
    xaxis_fixedrange=True,
    yaxis_fixedrange=True,
    dragmode=False,
    plot_bgcolor="white"
)

st.plotly_chart(fig2, use_container_width=True)

########################### Second Chart #################################
fig = px.area(y=y,
              x=x,
              title='Overall India Growth Rate of Active Cases (7 Day Moving Average)',
              labels={'y': '% Growth Active Case',
                     'x': 'Time Period'},
              line_shape='spline',
            )

fig.add_hline(y=0,
                line_width=1,
                line_dash="dash",
                line_color="Green",
                annotation_text="Recovery > Cases",
                annotation_position="bottom left",
                )

fig.add_vline(x='2020-09-16',
                line_width=1,
                line_dash="dash",
                line_color="Orange")

fig.add_vline(x='2021-02-18',
                line_width=1,
                line_dash="dash",
                line_color="Red")

fig.update_layout(legend=dict(bgcolor='rgba(0,0,0,0)'),
                    xaxis_fixedrange=True,
                    yaxis_fixedrange=True,
                    dragmode=False,
                    plot_bgcolor="white",)
st.plotly_chart(fig, use_container_width=True)

########################### Third Chart #################################
rule = st.selectbox('Variables', params.rules_cols)

# st.plotly_chart(custom_plot.summary(
#     data_state_cls.data, rule), use_container_width=True)

st.write("**:beer: Buy me a [beer]**")
expander = st.beta_expander("This app is developed by Manish Sahu.")
expander.write(
    "Contact me on [Linkedin](https://www.linkedin.com/in/manishsahuiitbhu/)")
expander.write(
    "The source code is on [GitHub](https://github.com/ManishSahu53/streamlit-covid-dashboard)")
