import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model

# Load the trained model
model = load_model('model')

# Define the Streamlit app
def main():
    st.title("Company Success Prediction")

    # User input for each feature
    industry = st.selectbox("Industry", ("Fintech", "Web3", "E-commerce", "Consumer Others", "EdTech", "ESG", "Enterprise SaaS", "Others"))
    
    # Initialize industry variables
    fintech = web3 = ecommerce = consumer_others = edtech = esg = enterprise_saas = others = 0
    
    # Set the selected industry variable to 1
    if industry == "Fintech":
        fintech = 1
    elif industry == "Web3":
        web3 = 1
    elif industry == "E-commerce":
        ecommerce = 1
    elif industry == "Consumer Others":
        consumer_others = 1
    elif industry == "EdTech":
        edtech = 1
    elif industry == "ESG":
        esg = 1
    elif industry == "Enterprise SaaS":
        enterprise_saas = 1
    else:
        others = 1

    business_model = st.selectbox("Business Model", ("B2B", "B2C", "B2B2C", "Others"))
    
    # Initialize business model variables
    B2B = B2C = B2B2C = Others = 0
    
    # Set the selected business model variable to 1
    if business_model == "B2B":
        B2B = 1
    elif business_model == "B2C":
        B2C = 1
    elif business_model == "B2B2C":
        B2B2C = 1
    else:
        Others = 1

    country = st.multiselect("Please select the country where your company is primarily based in",
                             ["Australia", "Indonesia", "Malaysia", "Philippines", "Singapore", "Thailand", "Vietnam", "Others"])
    
    # Convert list of countries to a single string
    country_str = ', '.join(country)

    glassdoor_total_employees = st.selectbox("Total Number of Employees", ("0 to 200", "201 to 500", "501 to 1000", "1001 to 5000", "5001 to 10000", "10000+"))

    # Initialize employee count variables
    employees_51_200 = employees_201_500 = employees_501_1000 = employees_1001_5000 = employees_5001_10000 = employees_10000_plus = 0
    
    # Set the selected employee count variable to 1
    if glassdoor_total_employees == "0 to 200":
        employees_51_200 = 1
    elif glassdoor_total_employees == "201 to 500":
        employees_201_500 = 1
    elif glassdoor_total_employees == "501 to 1000":
        employees_501_1000 = 1
    elif glassdoor_total_employees == "1001 to 5000":
        employees_1001_5000 = 1
    elif glassdoor_total_employees == "5001 to 10000":
        employees_5001_10000 = 1
    else:
        employees_10000_plus = 1

    glassdoor_rating = st.slider("Glassdoor Rating", 0.0, 5.0, 3.5)
    glassdoor_recommend_percentage = st.slider("Glassdoor Recommend Percentage", 0, 100, 50)

    # Initialize other variables
    sucessranking_four_gdranking = sucessranking_three_employees = valauation_divide_vdminusyf = sucessranking_two_valdivideyear = 0
    year_operating = years_to_unicorn = exit = 0
    
    similar_businessmodel_overseas = st.selectbox("Is there a Similar Business Model Overseas?", ("Yes", "No"))
    patent = st.selectbox("Does your company currently hold any patents or is it in the process of obtaining one?", ("Yes", "No"))
    pivot = st.selectbox("Has your company pivoted from its original idea or direction?", ("Yes", "No"))
    subsidiary_corporatespinoff = st.selectbox("Is your company a subsidiary of another company or a result of a corporate spinoff?", ("Yes", "No"))
    firsttime_founder = st.selectbox("Is anyone on your team a repeat founder", ("Yes", "No"))
    tech_founder = st.selectbox("Does any of your founders have a technical background?", ("Yes", "No"))
    
    foundersage_when_started = st.number_input("What was the founder's age when they started the company? If there is a team of founders, please provide the average age", min_value=0)
    graduated_overseas_uni = st.selectbox("Have any of your founders graduated from a university abroad?", ("Yes", "No"))

    university = st.multiselect("Select the country where your founders earned their university degrees (you may choose more than one)",
                                ["Australia University", "China University", "India University", "Singapore University", "University based in other Southeast Asia countries", "University based in Europe or US", "Others or Did not graduate from university"])
    
    # Convert list of universities to a single string
    university_str = ', '.join(university)

    investor = st.multiselect("Select the investor(s) that have invested in your company (you may choose more than one)",
                              ["500 Global", "Alpha JWC", "Cyber Agent Capital", "East Venture", "Golden Gate Venture", "Insignia", "Jungle Venture", "Openspace VC", "Sequoia", "Vertex", "Wavemaker", "Y Combinator", "Others"])
    
    # Convert list of investors to a single string
    investor_str = ', '.join(investor)

    # Create a dictionary with the inputs
    input_data = {
        'fintech': fintech,
        'web3': web3,
        'ecommerce': ecommerce,
        'consumer_others': consumer_others,
        'edtech ': edtech,
        'esg': esg,
        'enterprise_saas': enterprise_saas,
        'others ': others,
        'business_model': business_model,
        'glassdoor_rating': glassdoor_rating,
        'sucessranking_four_gdranking': sucessranking_four_gdranking,
        'employees_51_200': employees_51_200,
        'employees_201_500': employees_201_500,
        'employees_501_1000': employees_501_1000,
        'employees_1001_5000': employees_1001_5000,
        'employees_5001_10000': employees_5001_10000,
        'employees_10000_plus': employees_10000_plus,
        'glassdoor_recommend_percentage': glassdoor_recommend_percentage,
        'valauation_divide_vdminusyf': valauation_divide_vdminusyf,
        'sucessranking_two_valdivideyear': sucessranking_two_valdivideyear,
        'similar_businessmodel_overseas': similar_businessmodel_overseas,
        'year_operating': year_operating,
        'exit': exit,
        'country': country_str,  # converted to string
        'patent': patent,
        'pivot': pivot,
        'subsidiary_corporatespinoff': subsidiary_corporatespinoff,
        'firsttime_founder': firsttime_founder,
        'tech_founder': tech_founder,
        'foundersage_when_started': foundersage_when_started,
        'graduated_overseas_uni': graduated_overseas_uni,
        'university': university_str,  # converted to string
        'investor': investor_str  # converted to string
    }

    # Convert the dictionary to a DataFrame
    input_df = pd.DataFrame([input_data])

    # Make predictions
    if st.button("Predict"):
        prediction = predict_model(model, data=input_df)
        
        if int(prediction['prediction_label']) == 1:
            predicted_outcome = "Low"
        else:
            predicted_outcome = "High"            
        
        st.write("Predicted Startup Success is: ", predicted_outcome)

if __name__ == '__main__':
    main()
