import streamlit as st
import time








st.set_page_config(page_title="Pomodoro App",page_icon="⏳",layout="centered")



def local_css(filename):
    with open(filename) as ft:
        st.markdown(f"<style>{ft.read()}</style>", unsafe_allow_html=True)


local_css("styles.css")


st.title("POMODORO WEB APP")
c1, c2, c3 = st.columns([1,4,1])
c2.write("**This is only for Focus!**")





button_clicked = c2.button("Start", key="b")

t1=1500
t2=300

if button_clicked:
    with st.empty():
        while t1:
            mins, secs = divmod(t1, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.title(f'⏳ {timer}')
            time.sleep(1)
            t1 -= 1
            st.success("Take a Break ...")

    with st.empty():
        while t2:
            mins2, secs2 = divmod(t1, 60)
            timer2 = '{:02d}:{:02d}'.format(mins2, secs2)
            st.header(f'⏳ {timer}')
            time.sleep(1)
            t2 -= 1
            st.error("Go back and master it !")