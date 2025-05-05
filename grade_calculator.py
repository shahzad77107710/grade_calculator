import streamlit as st

# Set up the page
st.set_page_config(page_title="Student Grade Calculator", page_icon="📚")
st.title("📚 Student Grade Calculator")

# Create a form for input
with st.form("student_form"):
    st.header("Enter Student Details")
    
    # Input fields
    name = st.text_input("Student Name")
    roll_number = st.number_input("Roll Number", min_value=1, step=1)
    math = st.number_input("Math Marks", min_value=0.0, max_value=100.0, step=0.5)
    english = st.number_input("English Marks", min_value=0.0, max_value=100.0, step=0.5)
    computer = st.number_input("Computer Marks", min_value=0.0, max_value=100.0, step=0.5)
    
    # Submit button
    submitted = st.form_submit_button("Calculate Results")

# Process and display results when form is submitted
if submitted:
    if not name:
        st.warning("Please enter student name")
    else:
        # Calculate results
        total = math + english + computer
        percentage = (total / 300) * 100
        
        # Determine grade
        if percentage >= 90:
            grade = 'A+'
        elif percentage >= 80:
            grade = 'A'
        elif percentage >= 70:
            grade = 'B'
        elif percentage >= 60:
            grade = 'C'
        elif percentage >= 50:
            grade = 'D'
        else:
            grade = 'F'
        
        # Display results in a nicer format
        st.success("### Results Summary")
        
        # Create two columns for better layout
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            **Student Name:** {name}  
            **Roll Number:** {roll_number}  
            **Math Marks:** {math}  
            **English Marks:** {english}
            """)
            
        with col2:
            st.markdown(f"""
            **Computer Marks:** {computer}  
            **Total Marks:** {total}/300  
            **Percentage:** {percentage:.2f}%  
            **Grade:** {grade}
            """)
        
        # Visual indicator
        st.progress(percentage/100)
        st.caption(f"Performance: {grade} ({percentage:.2f}%)")
        
        # Add some color based on performance
        if grade in ['A+', 'A']:
            st.balloons()
        elif grade == 'F':
            st.error("The student has failed and needs improvement")