import streamlit as st
import streamlit.components.v1 as components
p = open("map.html")
components.html(p.read(), height="1850", width="2280")
