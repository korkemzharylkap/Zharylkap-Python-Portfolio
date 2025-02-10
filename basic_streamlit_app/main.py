st.title("Penguins Data Set")
# Interactive Filtering
species = st.selectbox("Select Species:", df["species"].unique())
island = st.multiselect("Select Island(s):", df["island"].unique(), default=df["island"].unique())
min_bill_length = st.slider("Minimum Bill Length (mm):", float(df["bill_length_mm"].min()), float(df["bill_length_mm"].max()), float(df["bill_length_mm"].min()))

# Apply filters
filtered_df = df[(df["species"] == species) & (df["island"].isin(island)) & (df["bill_length_mm"] >= min_bill_length)]

st.write(f"### Displaying {species} Penguins")
st.dataframe(filtered_df)
