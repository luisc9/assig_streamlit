import streamlit as st
import pandas as pd

st.title("Favorite Soccer Player Goals Tracker")

goalscorers = pd.read_csv('football_data/goalscorers.csv')
goalscorers['date'] = pd.to_datetime(goalscorers['date'])
goalscorers['year'] = goalscorers['date'].dt.year.astype(int)
goalscorers['scorer'] = goalscorers['scorer'].str.lower()
goalscorers['scorer'] = goalscorers['scorer'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
goalscorers = goalscorers[['scorer', 'year']]

def get_player_goals(player_name, year):
    player_goals = goalscorers[(goalscorers['scorer'].str.contains(player_name.lower())) & (goalscorers['year'] == year)]
    if player_goals.empty:
        return False, 'Player not found or data not available.'
    else:
        return True, player_goals.shape[0]

player_name = st.text_input("Enter the name of your favorite soccer player")
year = st.slider("Select the year", min_value=1916, max_value=2024)

if st.button("Show Goals"):
    if player_name:
        player_found, goals = get_player_goals(player_name, year)
        st.write(f"Player found: {player_found}. Number of goals for the year {year}: {goals}")
    else:
        st.write("Player not found or data not available.")
