# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd



if 'kalender' not in st.session_state:
    df = pd.DataFrame({'Datum':['27.02.2023', '28.02.2023', '29.02.2023', 
                                '30.02.2023', '01.03.2023', '02.03.2023', 
                                '03.03.2023', '04.03.2023', '05.03.2023',
                                '06.03.2023', '07.03.2023', '08.03.2023',
                                '09.03.2023', '10.03.2023', '11.03.2023',
                                '12.03.2023', '13.03.2023', '14.03.2023',
                                '15.03.2023', '16.03.2023'],
                       'Titel':['Wir räumen auf', 'Wir putzen alles']*10,
                       'Treffpunkt':['Bootsverleih DHfK', 'Stadthafen']*10,
                       'Teilnehmer':[0]*20
        })
    st.session_state['kalender'] = df

#%%functions


#%% streamlit
st.markdown('# Gewässerschutz in Leipzig')
tab1,tab2=st.tabs(['Homepage','Kalender'])


with tab1:
    st.write('video')
    st.write('über uns irgendwas')
    st.write('')
    
    
    
    st.write('was können wir tun?')



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

    
    
    
    
    
    