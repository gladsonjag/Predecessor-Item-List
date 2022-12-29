import csv
import numpy as np
import re
from operator import attrgetter
import pandas as pd
import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, ColumnsAutoSizeMode
import math




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
                try:
                    self.Gold = int(re.sub(r'[^0-9]', '', stat))
                except:
                    self.Gold = int(0)

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
df = df.rename(columns={"Physical_Power" : "Phys Power", "Physical_Pen" : "Phys Pen", "Physical_Armor": "Phys Armor", "Magical_Power" : "Mag Power", "Magical_Pen" : "Mag Pen", "Magical_Armor" : "Mag Armor", 
"Attack_Speed" : " Atk Speed", "Critical_Chance" : "Crit Chance", "Ability_Haste" : "Ability Haste", "Movement_Speed" : "Movement Speed", "Life_Steal" : "Life Steal"})

#-----------------WEBSITE-------------------

#-----------------HEADER---------------------
def create_header():
    st.set_page_config(page_title='Predecessor Items', page_icon=":bar_chart:", layout="wide")
                        
    st.header("Predecessor Fan Made Item Stat Chart")
    st.caption("[All Item Stats are Gathered from Predecessor Wiki HERE](https://predecessor.fandom.com/wiki/Predecessor_Wiki)")
    st.caption("Please Note this is a fanmade website by one person, not affiliated with Omeda Studios or with anyone on the wikifandom team ")
    st.caption("BASE STATS ONLY I.E NO PASSIVES")
    st.subheader("Predecessor Item List")
    return
create_header()
#----------------HEADER(CLOSED)-------------------

#----------------ITEM DATA TABLE------------------
#Data Modulue
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_pagination(paginationAutoPageSize=True) #Add Pagination
gb.configure_side_bar()
gb.configure_selection("single", use_checkbox=False, groupSelectsChildren="Group checkbox select children") #enables multi row selection
gridOptions = gb.build()

grid_response = AgGrid(
    df,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=True,
    theme='streamlit', #Add theme color to the table
    enable_enterprise_modules=True,
    height=600, 
    width=800,
    columns_auto_size_mode=ColumnsAutoSizeMode.FIT_ALL_COLUMNS_TO_VIEW,
    reload_data=True
)

df = grid_response['data']
selected = grid_response['selected_rows'] 
df_select = pd.DataFrame(selected) #Pass the selected rows to a new dataframe df
#--------------ITEM DATA TABLE(CLOSED)--------------

#--------------Expanded SPG--------------------------
#creates a list of list of all the new SPG data for each item
gpi_data_list = []
df_iterate = df.set_index("Name")
for row in df_iterate.itertuples(index=False):
    row_iter = []
    for index in row:
        try:
            new_gpi = round((index / row[-1]), 5)
        except:
            new_gpi = 0
        row_iter.append(new_gpi)
    gpi_data_list.append(row_iter)

gpi_data = pd.DataFrame(gpi_data_list)
#for loop to get the names on the y axis (index)
for name in item_name_list:
    gpi_data = gpi_data.rename(index = {item_name_list.index(name) : name})

gpi_data = gpi_data.rename(columns={0 : "Phys Power", 1 : "Phys Pen", 2: "Phys Armor", 3 : "Mag Power", 4 : "Mag Pen", 5 : "Mag Armor", 
6 : " Atk Speed", 7 : "Crit Chance", 8 : "Ability Haste", 9 : "Movement Speed", 10 : "Life Steal", 11 : "health", 12 : "Gold"})


#creates a usable dataframe for selecting which stat to see a GPI chart for
gpi_arr = df.columns.values
gpi_arr = np.delete(gpi_arr, 0, 0)
gpi_arr = np.delete(gpi_arr, -1, 0)
with st.expander(label = "Stat per Gold", expanded=True):
    st.header("Stat per Gold")
    st.caption("Bigger is better, i.e higher stat per gold spent on item")
    col_select = st.selectbox(
        "Select stat type",
        options = gpi_arr,
        
    )
    gpi_data = gpi_data.loc[gpi_data[col_select]>0]
    #creates the bar chart by creating a new data frame with the gold per item
    st.bar_chart(gpi_data, y=col_select, use_container_width=True, height=500)





#--------------------SIDEBAR--------------------

st.sidebar.header("Gold Per Stat")
st.sidebar.caption("i.e How efficent the item is in terms of the stats you are getting to gold, LOWER IS BETTER")
st.sidebar.subheader("Click on item to see GPS")


#gets all stat types to show user in sidebar
stat_int_list = [0,0,0,0,0,0,0,0,0,0,0,0]

def user_select(df_select):
    stat_int_list = []
    for type_ in df_select:
        stat_int = getattr(df_select, type_)
        stat_int = pd.DataFrame([stat_int])
        stat_int = stat_int[0][0]
        if isinstance(stat_int, np.int64):
            stat_int_list.append(stat_int)

    del stat_int_list[-1]
    return (stat_int_list)


if df_select.shape[0] != 0:
    stat_int_list = user_select(df_select)


#gets the Gold value from the selcted row user is clicking
gold2 = df_select.get("Gold")
gold1 = pd.DataFrame([gold2])
gold = gold1[0][0]

gpi_list = []
for stat in stat_int_list:
    try:
        gpi = gold / stat
    except:
        gpi = 0
    if math.isinf(gpi):
        gpi = 0
    else:
        gpi=round(gpi, 2 )
    gpi_list.append(gpi)
    
df_gps = pd.DataFrame(gpi_list, columns=(["GPS"]), index=["Phys Power","Phys Pen","Phys Armor","Mag Power",
"Mag Pen","Mag Armor","Atk Speed","Crit Chance","Ability Haste","Movement Speed","Life Steal", "Health"])

st.sidebar.table(df_gps.style.format("{:.2f}"))

st.sidebar.caption("I may add a section here to read the item passive, just for refrence")
#-----------------SIDEBAR(CLOSED)-----------------

#-----------------BOTTOM SECTION------------------

st.markdown("")

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("INFO")
    st.write("For any question, comments, or ideas on how to make this better dont be afraid to contact me on discord @TheGoatboy#0763")
with right_column:
    st.subheader("Predecessor wiki")
    st.write("Thanks to MeatyManLink & the community updating all the stats on the fan made wiki! 'https://predecessor.fandom.com/wiki/Predecessor_Wiki'")
st.markdown("")

#-------------BOTTOM SECTION(CLOSED)-----------------