# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd



#%% init
if 'kalender' not in st.session_state:
    df = pd.DataFrame({'Datum':['27.02.2023', '28.02.2023', '29.02.2023', 
                                '30.02.2023', '01.03.2023', '02.03.2023', 
                                '03.03.2023', '04.03.2023'],
                       'Titel':['Wir räumen auf', 'Wir putzen alles']*4,
                       'Treffpunkt':['Bootsverleigh DHfK', 'Stadthafen']*4,
                       'Teilnehmer':[0]*8
        })
    st.session_state['kalender'] = df

#%%functions


#%% streamlit
st.markdown('# Gewässerschutz in Leipzig')
tab1,tab2=st.tabs(['Übersicht','Kalender'])


with tab1:

    st.write('Inhaltsverzeichnis')
    st.write('Video')
    st.write('Wie geht es den Gewässern?')
    st.write('Was können wir tun?')
    st.write('Warum wir sie benötigen')
    st.write('Bild')
    st.write('Unsere Projekt Idee')
    st.write('Was wir im Detail machen wollen')
    st.write('Was wir für unseren Plan Benötigen')
    st.write('Video mit Podcast')
    
with tab2:
    st.write('Inhalt von tab')
    st.table(st.session_state['kalender'])
    ausgewaehlte_daten = st.multiselect('Bitte Termin(e) zum mitmachen auswählen',
                   st.session_state['kalender']['Datum'],
                   key='ausgewaehlte_daten'
                   )
    mitmachen = st.button('Ich möchte mitmachen',)
    if mitmachen:
        for datum in ausgewaehlte_daten:
            df = st.session_state['kalender']
            df.loc[df.Datum == datum,'Teilnehmer'] = df.loc[df.Datum == datum,'Teilnehmer'] + 1    
        st.experimental_rerun()

    
    
    
    
    
    