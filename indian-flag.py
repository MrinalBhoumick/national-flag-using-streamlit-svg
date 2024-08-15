import streamlit as st
import svgwrite
import math
import time
from datetime import datetime
import base64

# Function to calculate the number of years since India's independence
def calculate_years_of_independence():
    current_year = datetime.now().year
    years_of_independence = current_year - 1947
    return years_of_independence

# Function to draw the Indian flag using svgwrite, updating the display at each step
def draw_indian_flag(flag_placeholder):
    # Initialize the SVG drawing
    dwg = svgwrite.Drawing(size=(800, 500))

    # Draw saffron rectangle
    dwg.add(dwg.rect(insert=(0, 0), size=(800, 167), fill="orange"))
    display_svg(dwg, flag_placeholder)
    time.sleep(0.5)

    # Draw green rectangle
    dwg.add(dwg.rect(insert=(0, 334), size=(800, 167), fill="green"))
    display_svg(dwg, flag_placeholder)
    time.sleep(0.5)

    # Draw the Ashoka Chakra (navy blue circle)
    dwg.add(dwg.circle(center=(400, 250), r=60, fill="white", stroke="navy", stroke_width=4))
    display_svg(dwg, flag_placeholder)
    time.sleep(0.5)

    # Draw 24 spokes inside the Ashoka Chakra
    for i in range(24):
        angle = i * 15
        x1 = 400 + 60 * math.sin(math.radians(angle))
        y1 = 250 - 60 * math.cos(math.radians(angle))
        dwg.add(dwg.line(start=(400, 250), end=(x1, y1), stroke="navy", stroke_width=2))
        display_svg(dwg, flag_placeholder)
        time.sleep(0.1)  # Short delay to simulate drawing each spoke

    return dwg

# Function to display SVG in Streamlit
def display_svg(dwg, flag_placeholder):
    flag_svg_data = dwg.tostring()
    b64_svg = base64.b64encode(flag_svg_data.encode("utf-8")).decode("utf-8")
    img_tag = f'<img src="data:image/svg+xml;base64,{b64_svg}" alt="Indian Flag" width="800" height="500">'
    flag_placeholder.markdown(img_tag, unsafe_allow_html=True)

# Streamlit App
st.title("National Flag")

# Calculate and display the number of years since independence
years_of_independence = calculate_years_of_independence()
st.subheader(f"Happy Independence Day")
st.write(f"India is celebrating {years_of_independence} years of independence.")

# Create an empty placeholder for the flag
flag_placeholder = st.empty()

# Draw the flag step by step
dwg = draw_indian_flag(flag_placeholder)

# Final display of the flag after completion
flag_svg_data = dwg.tostring()
display_svg(dwg, flag_placeholder)

# After the flag is drawn, ask the user for their name
name = st.text_input("Enter your name:")

# If a name is entered, display the greeting message
if name:
    st.write(f"Happy Independence Day, {name}")
    st.write("We all hope that the criminals in the R.G. Kar Young Doctor case will be punished and justice will be served.")

# Download button for the flag
st.download_button(
    label="Download Flag as SVG",
    data=flag_svg_data,
    file_name="indian_flag.svg",
    mime="image/svg+xml"
)