import csv
import numpy as np
import re
from operator import attrgetter
import pandas as pd
import plotly.express as px
import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, ColumnsAutoSizeMode




#initialze all list
item_name_list = []
item_stats = []
item_list = []

Physical_Power = []
Physical_Pen = []
Physical_Armor = []
Magical_Power = []
Magical_Pen = []
Magical_Armor = []
Attack_Speed = []
Critical_Chance = []
Ability_Haste = []
Movement_Speed = []
Life_Steal = []
Health = []
Gold = []


class Item:

    Name:str
    Physical_Power:int
    Physical_Pen:int
    Physical_Armor:int
    Magical_Power:int
    Magical_Pen:int
    Magical_Armor:int
    Attack_Speed:int
    Critical_Chance:int
    Ability_Haste:int
    Movement_Speed:int
    Life_Steal:int
    Health:int
    Gold:int
    
    #Name is a single string, and stats is a list of all the stats for the one item
    def __init__(self, Name, stats):
     
        self.Name = Name
        self.Physical_Power = 0
        self.Physical_Pen = 0
        self.Physical_Armor = 0
        self.Magical_Power = 0
        self.Magical_Pen = 0
        self.Magical_Armor = 0
        self.Attack_Speed = 0
        self.Critical_Chance = 0
        self.Ability_Haste = 0
        self.Movement_Speed = 0
        self.Life_Steal = 0
        self.Health = 0
        self.Gold = 0

        for stat in stats:
            if "Physical Power" in stat:
                self.Physical_Power = int(re.sub(r'[^0-9]', '', stat))
            if "Physical Penetration" in stat:
                self.Physical_Pen = int(re.sub(r'[^0-9]', '', stat))
            if "Physical Armor" in stat:
                self.Physical_Armor = int(re.sub(r'[^0-9]', '', stat))
            if "Magical Power" in stat:
                self.Magical_Power = int(re.sub(r'[^0-9]', '', stat))
            if "Magical Penetration" in stat:
                self.Magical_Pen = int(re.sub(r'[^0-9]', '', stat))
            if "Magical Armor" in stat:
                self.Magical_Armor = int(re.sub(r'[^0-9]', '', stat))
            if "Attack Speed" in stat:
                self.Attack_Speed = int(re.sub(r'[^0-9]', '', stat))
            if "Critical Chance" in stat:
                self.Critical_Chance = int(re.sub(r'[^0-9]', '', stat))
            if "Ability Haste" in stat:
                self.Ability_Haste = int(re.sub(r'[^0-9]', '', stat))
            if "Movement Speed" in stat:
                self.Movement_Speed = int(re.sub(r'[^0-9]', '', stat))
            if "Lifesteal" in stat:
                self.Life_Steal = int(re.sub(r'[^0-9]', '', stat))
            if "Health" in stat:
                self.Health = int(re.sub(r'[^0-9]', '', stat))
            if "Gold" in stat:
                self.Gold = int(re.sub(r'[^0-9]', '', stat))

        return

def sort_attr_list(item_list):

    Sorted_Physical_Power = sorted(item_list, key= attrgetter('Physical_Power'))
    Sorted_Physical_Power.reverse()

    Sorted_Physical_Pen= sorted(item_list, key= attrgetter('Physical_Pen'))
    Sorted_Physical_Pen.reverse()

    Sorted_Physical_Armor= sorted(item_list, key= attrgetter('Physical_Armor'))
    Sorted_Physical_Armor.reverse()
    
    Sorted_Magical_Power= sorted(item_list, key= attrgetter('Magical_Power'))
    Sorted_Magical_Power.reverse()

    Sorted_Magical_Pen= sorted(item_list, key= attrgetter('Magical_Pen'))
    Sorted_Magical_Pen.reverse()

    Sorted_Magical_Armor= sorted(item_list, key= attrgetter('Magical_Armor'))
    Sorted_Magical_Armor.reverse()

    Sorted_Attack_Speed= sorted(item_list, key= attrgetter('Attack_Speed'))
    Sorted_Attack_Speed.reverse()

    Sorted_Critical_Chance= sorted(item_list, key= attrgetter('Critical_Chance'))
    Sorted_Critical_Chance.reverse()

    Sorted_Ability_Haste= sorted(item_list, key= attrgetter('Ability_Haste'))
    Sorted_Ability_Haste.reverse()

    Sorted_Movement_Speed= sorted(item_list, key= attrgetter('Movement_Speed'))
    Sorted_Movement_Speed.reverse()

    Sorted_Life_Steal= sorted(item_list, key= attrgetter('Life_Steal'))
    Sorted_Life_Steal.reverse()

    Sorted_Health= sorted(item_list, key= attrgetter('Health'))
    Sorted_Health.reverse()

    Sorted_Gold= sorted(item_list, key= attrgetter('Gold'))
    Sorted_Gold.reverse()

    return(Sorted_Physical_Power, Sorted_Physical_Pen, Sorted_Physical_Armor, Sorted_Magical_Power, Sorted_Magical_Pen,
    Sorted_Magical_Armor, Sorted_Attack_Speed, Sorted_Critical_Chance, Sorted_Ability_Haste, Sorted_Movement_Speed,
    Sorted_Life_Steal, Sorted_Health, Sorted_Gold)

#reading csv file and creating a list of names
with open('predecessor_item_name.csv', 'r') as f1:
    reader1 = csv.reader(f1, delimiter=',')
    for row in reader1:
        for name in row:
            item_name_list.append(name)

#reading csv file and creating a list of each list of stats
with open('predecessor_item_stats.csv', 'r') as f2:
    reader2 = csv.reader(f2, delimiter=',')
    for list in reader2:
        item_stats.append(list)

for item in item_name_list:

    item_class = Item(item, item_stats[item_name_list.index(item)])
    item_list.append(item_class)


(Physical_Power, Physical_Pen, Physical_Armor, Magical_Power, Magical_Pen, Magical_Armor, Attack_Speed, Critical_Chance,
Ability_Haste, Movement_Speed, Life_Steal, Health, Gold) = sort_attr_list(item_list)

df = pd.DataFrame([item.__dict__ for item in item_list])


#Creating the website and making it pretty with all the data
st.set_page_config(page_title='Predecessor Items', page_icon=":bar_chart:",
                    layout="wide")
st.header("Predecessor Fan Made Item Stat Chart")
st.caption("[All Item Stats are Gathered from Predecessor Wiki HERE](https://predecessor.fandom.com/wiki/Predecessor_Wiki)")
st.caption("Please Note this is a fanmade website by one person, not affilited with Omeda Studios or with anyone on the wikifandom team ")
st.caption("BASE STATS ONLY I.E NO PASSIVES")
st.subheader("Predecessor Item List")

#Data Modulue
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_pagination(paginationAutoPageSize=True) #Add Pagination
gb.configure_side_bar()
gb.configure_selection("multiple", use_checkbox=False, groupSelectsChildren="Group checkbox select children") #enables multi row selection
gridOptions = gb.build()

grid_response = AgGrid(
    df,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    theme='streamlit', #Add theme color to the table
    enable_enterprise_modules=True,
    height=800, 
    #width="100%",
    columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
    reload_data=True
)

df = grid_response['data']
selected = grid_response['selected_rows'] 
df = pd.DataFrame(selected) #Pass the selected rows to a new dataframe df


#-----BOTTOM SECTION---------

st.markdown("")

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("INFO")
    st.write("For any question, comments, or ideas on how to make this better dont be afraid to contact me on discord @TheGoatboy#0763")
with right_column:
    st.subheader("Predecessor wiki")
    st.write("Thanks to MeatyManLink & the community updating all the stats on the fan made wiki! 'https://predecessor.fandom.com/wiki/Predecessor_Wiki'")
st.markdown("")