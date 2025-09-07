import streamlit as st

st.markdown(
    """
<style>
    body, section, .appview-container, div {
        padding :0;
        margin: 0;
        width:100%;
    }
</style>
""",
    unsafe_allow_html=True,
)

st.title("Person Profile")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A")
    st.selectbox("City", ["Tehran", "Shiraz", "Isfahan"])

    description = st.checkbox("Show Description", True)
    gender = st.radio("Gender", options=["Male", "Female"])

with col2:
    st.header("B")
    name = st.text_input("Name")
    family = st.text_input("Family")
    age = st.number_input("Age", min_value=1, max_value=1, step=1)

with col3:
    st.header("C")
    if st.button("Save"):
        # person_controller = person_controller()
        # status,person = person_controller.save(name, family, age)
        # if status :
        st.write("Person Saved")
        # else:
        #     st.write("Person Not Saved",person)



persons = [{'id': None, 'name': 'A', 'family': 'B', 'age': 10}, {'id': None, 'name': 'A', 'family': 'B', 'age': 10}, {'id': None, 'name': 'A', 'family': 'B', 'age': 10}]

st.table(persons)
