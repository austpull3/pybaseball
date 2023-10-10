import streamlit as st
from pybaseball import statcast_batter, spraychart
import pymssql

st.title("Pybaseball Spraychart")

# Get the spraychart data for a specific player
player_name = st.text_input('Enter player name:')
data = statcast_batter('2021-01-01', '2021-12-31', 514888)
s = spraychart(data, 'astros', title = 'Jose Altuve')
fig = s.figure
# Display the spraychart
st.pyplot(fig)
