# Import the required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(layout="wide")

# Path to your CSV file
csv_file_path = 'data/data.csv'

# Read the file to a dataframe using pandas
df = pd.read_csv(csv_file_path)

# Functions for each of the pages
def home():
    st.header('Begin exploring the data using the menu on the left')
    st.text('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nec mi sit amet arcu vulputate malesuada. Donec eu lobortis quam. Aliquam id rhoncus nunc, in posuere ex. Phasellus dictum fringilla quam ac varius. Nulla posuere eu ex ut varius. Praesent nunc nunc, auctor ac fermentum id, vulputate quis tortor. Vivamus id est arcu. Mauris commodo, nulla quis viverra pellentesque, magna metus fermentum enim, efficitur rutrum ante eros id eros. Nulla facilisi. Maecenas tempor placerat nulla, vitae porttitor velit interdum nec. Nullam felis turpis, sollicitudin vitae aliquet id, eleifend sed sem. Sed blandit, nunc sed fringilla scelerisque, lacus tellus luctus ligula, quis mattis ligula lacus id magna. Nulla viverra commodo elit, quis tincidunt tellus bibendum et. Morbi gravida massa vitae purus consectetur, sit amet vehicula felis consectetur. Cras eget lacus vitae nunc convallis gravida. Donec pellentesque magna est, id lacinia quam accumsan eu.')

def data_summary():
    st.header('Statistics of Dataframe')
    st.write(df.describe())

def data_header():
    st.header('Header of Dataframe')
    st.write(df.head())

import plotly.express as px

def plot_acres_vs_funding():
    st.header('Treatment Acres vs. Federal Funding Amount')

    fig = px.scatter(df, x='TreatmentAcresReported', y='FederalFundingAmount', 
                     color='TreatmentStatus',
                     hover_data=['TreatmentAcresReported', 'FederalFundingAmount'])
    st.plotly_chart(fig)


def plot_treatments_by_state():
    st.header('Number of Treatments by State')

    treatments_by_state = df['Source'].value_counts().reset_index()
    treatments_by_state.columns = ['State', 'Number of Treatments']

    fig = px.bar(treatments_by_state, x='State', y='Number of Treatments', 
                 color='Number of Treatments',
                 hover_data=['State', 'Number of Treatments'])
    st.plotly_chart(fig)


def plot_acres_histogram():
    st.header('Histogram of Treatment Acres')

    fig = px.histogram(df, x='TreatmentAcresReported', color='TreatmentStatus')
    st.plotly_chart(fig)


def plot_funding_by_status():
    st.header('Federal Funding by Treatment Status')

    fig = px.box(df, x='TreatmentStatus', y='FederalFundingAmount', 
                 color='TreatmentStatus')
    st.plotly_chart(fig)

def plot_treatments_by_category():
    st.header('Number of Treatments per Treatment Category')

    treatments_by_category = df['TreatmentCategory'].value_counts().reset_index()
    treatments_by_category.columns = ['Treatment Category', 'Number of Treatments']

    fig = px.bar(treatments_by_category, x='Treatment Category', y='Number of Treatments', 
                 color='Treatment Category',
                 hover_data=['Treatment Category', 'Number of Treatments'])
    st.plotly_chart(fig)

def plot_treatments_by_status():
    st.header('Number of Treatments per Treatment Status')

    treatments_by_status = df['TreatmentStatus'].value_counts().reset_index()
    treatments_by_status.columns = ['Treatment Status', 'Number of Treatments']

    fig = px.bar(treatments_by_status, x='Treatment Status', y='Number of Treatments', 
                 color='Treatment Status',
                 hover_data=['Treatment Status', 'Number of Treatments'])
    st.plotly_chart(fig)

# Add a title and intro text
st.title('NFT Data Explorer')
st.text('This is a web app to allow exploration of NFT Data')

# Sidebar setup
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:', [
    'Home', 
    'Data Summary', 
    'Data Header', 
    'Treatment Acres vs. Federal Funding',
    'Number of Treatments by State',
    'Number of Treatments per Treatment Category',
    'Number of Treatments per Treatment Status',
    'Histogram of Treatment Acres',
    'Federal Funding by Treatment Status'
])


# Navigation options
if options == 'Home':
    home()
elif options == 'Data Summary':
    data_summary()
elif options == 'Data Header':
    data_header()
elif options == 'Treatment Acres vs. Federal Funding':
    plot_acres_vs_funding()
elif options == 'Number of Treatments by State':
    plot_treatments_by_state()
elif options == 'Number of Treatments per Treatment Category':
    plot_treatments_by_category()
elif options == 'Number of Treatments per Treatment Status':
    plot_treatments_by_status()
elif options == 'Histogram of Treatment Acres':
    plot_acres_histogram()
elif options == 'Federal Funding by Treatment Status':
    plot_funding_by_status()

