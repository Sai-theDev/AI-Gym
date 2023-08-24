import streamlit as st
import matplotlib.pyplot as plt

def single_plot(frames,left_angle,label1,y1,y2):
    plt.rcParams["figure.figsize"] = (20, 5)
    fig, ax = plt.subplots()
    ax.plot(frames, left_angle, '-', color='red', label=label1)
    ax.axhline(y=y1, color='g', linestyle='--')
    ax.axhline(y=y2, color='g', linestyle='--')
    ax.legend(loc='center left')
    ax.set_xlabel('Frames')
    ax.set_ylabel('Angle')
    st.pyplot(fig)

def double_plot(frames,left_angle,right_angle,label1,label2,y1,y2):
    plt.rcParams["figure.figsize"] = (20, 5)

    fig, ax = plt.subplots()
    ax.plot(frames, left_angle, '-', color='red', label=label1)
    ax.plot(frames, right_angle, '-', color='blue', label=label2)
    ax.axhline(y=y1, color='g', linestyle='--')
    ax.axhline(y=y2, color='g', linestyle='--')
    ax.legend(loc='center left')
    ax.set_xlabel('Frames')
    ax.set_ylabel('Angle')
    st.pyplot(fig)


