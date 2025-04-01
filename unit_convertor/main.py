import streamlit as st

def convert_units(value, unit_from, unit_to):
    conversions = {
        "meter_kilometer": 0.001, # 1 meter = 0.001 kilometer
        "kilometer_meter": 1000, # 1 kilometer = 1000 meters
        "gram_kilogram": 0.001, # 1 gram = 0.001 kilogram
        "kilogram_gram": 1000, # 1 kilogram = 1000 grams
    }

    key = f"{unit_from}_{unit_to}" #Generate a key based on the input and output units

    # convert the value to the desired unit
    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not possible"
    
st.title("Unit Converter") # Set the title of the app

# Get the user input
value = st.number_input("Enter the value you want to convert", min_value=1.0, step=1.0)

# Get the units to convert from 
unit_form = st.selectbox("Select the unit you want to convert from", ["meter", "kilometer", "gram", "kilogram"])
# Get the units to convert to
unit_to = st.selectbox("Select the unit you want to convert to", ["meter", "kilometer", "gram", "kilogram"])

# Button to convert the units
if st.button("Convert"):
    # Call the function to convert the units
    result = convert_units(value, unit_form, unit_to)
    # Display the result
    st.write(f"Converted value: {result}")
