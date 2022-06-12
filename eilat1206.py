import turtle
import tkinter as tk
from turtle import update
import streamlit as st
import pandas as pd
#st.title("Enter the password")
#password = st.text_input("", type="password")
#st.form(key=password, clear_on_submit=False)

#globals:
global start
global end
global adults
global kids
global babies
global hotel

st.title("Eilat")
st.image("eilat1020-2.jpeg")
start = int(st.selectbox("Enter the start", [10,11,12,13,14,15,16,17,18,19,20]))
end = int(st.selectbox("Enter the end", [10,11,12,13,14,15,16,17,18,19,20]))
adults = int(st.selectbox("Adults?",[2,1,3,4]))
kids = int(st.selectbox("Kids?",[0,1,2,3,4]))
babies = int(st.selectbox("Babies?",[0,1,2,3,4]))
hotel = st.selectbox("Hotel?", ["RB","KS","SP","LAG","RIV","ROG"])
if hotel == "RB":
    type = st.selectbox("Type?",["Bellavista","Royal"])
if hotel == "KS":
    type = st.selectbox("Type?",["Standard","Pool View"])
if hotel == "SP":
    type = st.selectbox("Type?",["Standard(PV)","Olympic"]) 
if hotel == "LAG":
    type = st.selectbox("Type?",["Standard","Pool View"])
if hotel == "RIV":
    type = st.selectbox("Type?",["Studio","Dironit"])   
if hotel == "ROG":
    type = st.selectbox("Type?",["Superior","Family/DLX"])

NC = st.selectbox("NC?",["Yes","No"])
upgrade = st.multiselect("Some upgrades?",["None","BB","HB","PV","Family Room","Door"])
Hug_shemesh = st.selectbox("Hug shemesh?",["No","Yes"])

num_nights = end - start


#REmarks to this
#kidsBool = st.button("Press if wanna add Kids / Babies")
#if (kidsBool):
#Some upgrades.. Nc, maybe flights.. single in dironit

# TESTS #

#total = (end-start) * 1000 
#st.success("Total: "+total)
#if total != 0:
    #st.balloons()
    #st.write(total)
#else:
#password = ""

# The real USE ---


# DATA ---- for one night: ..z: zol, ..y: yakar
#RB
RB_BEL_z = 1200
RB_BEL_y = 1665
RB_ROY_z = 1600
RB_ROY_y = 2065

#KS
KS_STD_z = 820
KS_STD_y = 1085
KS_PV_z = 870
KS_PV_y = 1135

#SP
SP_STD_z = 880
SP_STD_y = 1175
SP_OLY_z = 960
SP_OLY_y = 1275

#LAG
LAG_STD_z = 840
LAG_STD_y = 1135
LAG_PV_z = 895
LAG_PV_y = 1190

# RIV
RIV_STD_z = 400
RIV_STD_y = 600
RIV_DIR_3_z = 540
RIV_DIR_3_y = 730

# ROG
ROG_STD_z = 760
ROG_STD_y = 1150
ROG_DLX_z = 1090
ROG_DLX_y = 1495

#ADDONES
## RB ADDING PEOPLE
## add adult
RB_extra_adult_z = 456
RB_extra_adult_y = 610
## add kid
RB_kid_z = 285
RB_kid_y = 381
# add baby
RB_baby_z_y = 34

## KS adding people
KS_extra_adult_z = 324
KS_extra_adult_y = 434
## add kid
KS_kid_z = 203
KS_kid_y = 271
# add baby
KS_baby_z_y = 34

## SP adding people
SP_extra_adult_z = 330
SP_extra_adult_y = 444
## add kid
SP_kid_z = 206
SP_kid_y = 278
# add baby
SP_baby_z_y = 40

## LAG adding people
LAG_extra_adult_z = 318
LAG_extra_adult_y = 428
## add kid
LAG_kid_z = 199
LAG_kid_y = 268
# add baby
LAG_baby_z_y = 40

# Days fees
weekday = [12,13,14,15,16,19,20]
weekend = [10,11,17,18]

def WeekDaysCounter(start,end):
    Counter_weekdays = 0
    for day in range(start,end):
        if day in weekday:
            Counter_weekdays+=1
    return Counter_weekdays  

def WeekDaysENDCounter(start,end):
    Counter_weekENDdays = 0
    for day in range(start,end):
        if day in weekend:
            Counter_weekENDdays+=1
    return Counter_weekENDdays


# Hotels fees 
global room_fee     
def RoomFeeRB(hotel,adults,kids,upgrade):
    weekday_sum = WeekDaysCounter(start,end)
    weekendday_sum = WeekDaysENDCounter(start,end)
    price_night_z = 0
    price_night_y = 0
    if hotel == "RB":
        if (type == "Bellavista"):
            price_night_z = RB_BEL_z
            price_night_y = RB_BEL_y 
        if (type == "Royal"):
            price_night_z = RB_ROY_z
            price_night_y = RB_ROY_y
        if adults >= 2:
            room_fee =  weekday_sum * price_night_z + weekendday_sum * price_night_y
            if adults == 3:
                room_fee += weekday_sum * RB_extra_adult_z + weekendday_sum * RB_extra_adult_y
            if adults == 4:
                room_fee += 2 * (weekday_sum * RB_extra_adult_z + weekendday_sum * RB_extra_adult_y)    
        if adults == 1 and kids == 0: #לטפל ב1+1 בהמשך 
            room_fee =  (weekday_sum * price_night_z + weekendday_sum * price_night_y) * 0.85 #single discount
        if kids != 0:
            room_fee +=  kids * (weekday_sum * RB_kid_z + weekendday_sum * RB_kid_y)
        if babies != 0:
            room_fee +=  babies * (weekday_sum * RB_baby_z_y + weekendday_sum * RB_baby_z_y) 
           
    if hotel == "KS":
        if (type == "Standard"):
            price_night_z = KS_STD_z
            price_night_y = KS_STD_y 
        if (type == "Pool View"):
            price_night_z = KS_PV_z
            price_night_y = KS_PV_y
        if adults >= 2:
            room_fee =  weekday_sum * price_night_z + weekendday_sum * price_night_y
            if adults == 3:
                room_fee += weekday_sum * KS_extra_adult_z + weekendday_sum * KS_extra_adult_y
            if adults == 4:
                room_fee += 2 * (weekday_sum * KS_extra_adult_z + weekendday_sum * KS_extra_adult_y)    
        if adults == 1 and kids == 0:
            room_fee =  (weekday_sum * KS_STD_z + weekendday_sum * KS_STD_y) * 0.85 #single discount
        if kids != 0:
            room_fee +=  kids * (weekday_sum * KS_kid_z + weekendday_sum * KS_kid_y)
        if babies != 0:
            room_fee +=  babies * (weekday_sum * KS_baby_z_y + weekendday_sum * KS_baby_z_y)

    if hotel == "SP":
        if (type == "Standard(PV)"):
            price_night_z = SP_STD_z
            price_night_y = SP_STD_y 
        if (type == "Olympic"):
            price_night_z = SP_OLY_z
            price_night_y = SP_OLY_y
        
        if adults >= 2:
            room_fee =  weekday_sum * price_night_z + weekendday_sum * price_night_y
            if adults == 3:
                room_fee += weekday_sum * SP_extra_adult_z + weekendday_sum * SP_extra_adult_y
            if adults == 4:
                room_fee += 2 * (weekday_sum * SP_extra_adult_z + weekendday_sum * SP_extra_adult_y)    
        if adults == 1 and kids == 0:
            room_fee =  (weekday_sum * price_night_z + weekendday_sum * price_night_y) * 0.85 #single discount
        if kids != 0:
            room_fee +=  kids * (weekday_sum * SP_kid_z + weekendday_sum * SP_kid_y)
        if babies != 0:
            room_fee +=  babies * (weekday_sum * SP_baby_z_y + weekendday_sum * SP_baby_z_y)
    
    if hotel == "LAG":
        if (type == "Standard"):
            price_night_z = LAG_STD_z
            price_night_y = LAG_STD_y 
        if (type == "Pool View"):
            price_night_z = LAG_PV_z
            price_night_y = LAG_PV_y
        
        if adults >= 2:
            room_fee =  weekday_sum * price_night_z + weekendday_sum * price_night_y
            if adults == 3:
                room_fee += weekday_sum * LAG_extra_adult_z + weekendday_sum * LAG_extra_adult_y
            if adults == 4:
                room_fee += 2 * (weekday_sum * LAG_extra_adult_z + weekendday_sum * LAG_extra_adult_y)    
        if adults == 1 and kids == 0:
            room_fee =  (weekday_sum * price_night_z + weekendday_sum * price_night_y) * 0.85 #single discount
        if kids != 0:
            room_fee +=  kids * (weekday_sum * LAG_kid_z + weekendday_sum * LAG_kid_y)
        if babies != 0:
            room_fee +=  babies * (weekday_sum * LAG_baby_z_y + weekendday_sum * LAG_baby_z_y)

    if hotel == "RIV":
        if (type == "Studio"):
            price_night_z = RIV_STD_z
            price_night_y = RIV_STD_y 
        if (type == "Dironit"):
            price_night_z = RIV_DIR_3_z
            price_night_y = RIV_DIR_3_y
        
        if adults+kids >= 2 and adults+kids <= 4:
            room_fee =  weekday_sum * price_night_z + weekendday_sum * price_night_y
        if adults == 1 and kids == 0:
            room_fee =  (weekday_sum * price_night_z + weekendday_sum * price_night_y) * 0.85 #single discount
        
    if hotel == "ROG":
        if (type == "Superior"):
            price_night_z = ROG_STD_z
            price_night_y = ROG_STD_y 
        if (type == "Family/DLX"):
            price_night_z = ROG_DLX_z
            price_night_y = ROG_DLX_y

        if adults+kids >= 2 and adults+kids <= 4:
            room_fee =  weekday_sum * price_night_z + weekendday_sum * price_night_y
        if adults == 1 and kids == 0:
            room_fee =  (weekday_sum * price_night_z + weekendday_sum * price_night_y) * 0.85 #single discount   
    return room_fee    

# "None","BB","HB","PV","Family Room","Door"
# Upgrades RB-
upg_RB_HB_adult_z = 160
upg_RB_HB_adult_y = 225
upg_RB_HB_kid_z = 80
upg_RB_HB_kid_y = 115
upg_RB_FamilyRoom = 250
upg_RB_Half_Door = 40

# Upgrades KS-
upg_KS_HB_adult_z_y = 105
upg_KS_HB_kid_z_y = 53
upg_KS_fam_junior = 200
upg_KS_fam_pv = 260
upg_KS_king_floor = 300
upg_KS_gan_room = 400
upg_KS_Half_Door = 25

# Upgrades SP-
upg_SP_DLX = 80
upg_SP_DLX_OLY = 130
upg_SP_Studio = 130
upg_SP_suite_jun_OLY = 210
upg_SP_suite_DLX_OLY = 290
upg_SP_FamilyRoom = 250
upg_SP_Half_Door = 25

# Upgrades LAG-
upg_LAG_FamilyRoom = 300
upg_LAG_Studio = 120
upg_LAG_Half_Door = 25

# Upgrades RIV-
upg_RIV_BB_adult_z_y = 60
upg_RIV_BB_kid_z_y = 35
upg_RIV_HB_adult_z_y = 110
upg_RIV_HB_kid_z_y = 60


def UpgradesFee(hotel,num_nights,upgrade):
    total_upgrade_fee = 0
    weekday_sum = WeekDaysCounter(start,end)
    weekendday_sum = WeekDaysENDCounter(start,end)
    if "None" in upgrade:
        return total_upgrade_fee
    if hotel == "RB":
        if "HB" in upgrade:
            for _ in range(start,end):
                if _ == 12:
                    total_upgrade_fee += adults * (upg_RB_HB_adult_z * weekday_sum-1 +  upg_RB_HB_adult_y * weekendday_sum)
                    total_upgrade_fee += kids * (upg_RB_HB_kid_z * weekday_sum-1 +  upg_RB_HB_kid_y * weekendday_sum)
                elif _ == 17:
                    total_upgrade_fee += adults * (upg_RB_HB_adult_z * weekday_sum +  upg_RB_HB_adult_y * weekendday_sum-1)
                    total_upgrade_fee += kids * (upg_RB_HB_kid_z * weekday_sum +  upg_RB_HB_kid_y * weekendday_sum-1)
                else:
                    total_upgrade_fee += adults * (upg_RB_HB_adult_z * weekday_sum +  upg_RB_HB_adult_y * weekendday_sum)
                    total_upgrade_fee += kids * (upg_RB_HB_kid_z * weekday_sum +  upg_RB_HB_kid_y * weekendday_sum)
        if "Family Room" in upgrade:
            total_upgrade_fee += num_nights * upg_RB_FamilyRoom
        if "Door" in upgrade:
            total_upgrade_fee += num_nights * upg_RB_Half_Door
    
    return total_upgrade_fee  
  
#st.success(RoomFeeRB(hotel,adults,kids,upgrade))
# Hotes discounts
# RB:
 
def Disc_Room(hotel,room_fee):
    if num_nights >= 6:
        disc_1_4_7f6 = 0.95
        disc_1_4_7f6_7_8_9 = 0.9
        disc_1_4_7f10 = 0.85
        disc_3_5_f69 = 0.97
        disc_3_5_f10 = 0.9
        disc_2_6f9 = 0.87
        disc_2_f10 = 0.85
        if (hotel == "RB" or hotel == "LAG" or hotel == "ROG"):
            if num_nights == 6:
                room_fee = disc_1_4_7f6 * room_fee
            if num_nights >= 7 and num_nights <= 9:
                room_fee = disc_1_4_7f6_7_8_9 * room_fee
            if num_nights == 10:
                room_fee = disc_1_4_7f10 * room_fee

        if (hotel == "RIV" or hotel == "SP"):
            if num_nights >= 6 and num_nights <= 9:
                room_fee = disc_3_5_f69 * room_fee
            if num_nights == 10:
                room_fee = disc_3_5_f10 * room_fee

        if (hotel == "KS"):
            if num_nights >= 6 and num_nights <= 9:
                room_fee = disc_2_6f9 * room_fee
            if num_nights == 10:
                room_fee = disc_2_f10 * room_fee
    else:
        pass   
    return room_fee
        
        
    

#EVENTS ----
#DEFining the fee in the function itself
def EVE_cocktail_10_16(start,end):
    cocktail_1_fee = 150 #define the fee of the event
    cocktail_10_16_fee = 0
    for _ in range(start,end):
        if cocktail_10_16_fee == 0:
            if _ == 10 or _ == 16:
                cocktail_10_16_fee = adults * cocktail_1_fee
                #if not (_ == 16 and "HB" in upgrade):#check
        else:
            break
    return cocktail_10_16_fee
        
def EVE_soups_14(start,end):
    soups_14_fee = 0
    soups_1_fee = 80 #define the fee of the event
    for _ in range(start,end):
        if _ == 14:
            soups_14_fee = adults * soups_1_fee
    return soups_14_fee

def EVE_RB_bbq(start,end,hotel):
    bbq_12_17_ad_kd_fee = 0
    bbq_1_fee_adult = 150 #define the fee of the event
    bbq_1_fee_kid = 75 #define the fee of the event
    if hotel == "RB":
        for _ in range(start,end):
            if _ == 12 or _ == 17:
                bbq_12_17_ad_kd_fee += bbq_1_fee_adult * adults
                bbq_12_17_ad_kd_fee += bbq_1_fee_kid * kids
        return bbq_12_17_ad_kd_fee
    else:
        return bbq_12_17_ad_kd_fee     


def FINAL_price(start,end,adults,kids,babies,hotel,NC,upgrade):
    lia = 0
    lia += RoomFeeRB(hotel,adults,kids,upgrade)
    lia += UpgradesFee(hotel,num_nights,upgrade)
    lia = Disc_Room(hotel,lia)
    if NC == "Yes":
        lia += EVE_cocktail_10_16(start,end)
    lia += EVE_soups_14(start,end)
    lia += EVE_RB_bbq(start,end,hotel)
    if Hug_shemesh == "Yes":
        lia = lia*0.90
    return lia
    
lia = FINAL_price(start,end,adults,kids,babies,hotel,NC,upgrade)
st.success(lia)
