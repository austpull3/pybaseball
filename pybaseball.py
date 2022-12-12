import streamlit as st
from pybaseball import spray_chart

def main():
  player_name = "Mike Trout"
  season = 2019
  st.pyplot(spray_chart(player_name, season))
  
