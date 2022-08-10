import streamlit as st
import streamlit.components.v1 as components
p = open("map.html")
components.html(p.read(), height="850", width="1280")
