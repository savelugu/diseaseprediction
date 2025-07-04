import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Disease Detector", layout="wide", page_icon="🤖")

st.sidebar.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
    }
    .sidebar img {
        max-width: 100%;
        margin-left: auto;
        margin-right: auto;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True
)

st.sidebar.image('./images/mo.jpg')



# Helper function for input validation
def validate_input(value, default=0):
    """
    Validate and convert input to a numeric value.
    If conversion fails, return the default value.
    """
    try:
        return float(value)
    except ValueError:
        return default


# Loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
liver_disease_model=pickle.load(open('liver_disease_model.sav', 'rb'))
kidney_disease_model=pickle.load(open('kidney_disease_model.sav', 'rb'))
lung_disease_model=pickle.load(open('lung_disease_model.sav', 'rb'))
pregnancy_model=pickle.load(open('pregnancy_model.sav', 'rb'))
# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Home','Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 'Liver Disease Prediction','CKD Prediction','Lung Cancer Prediction','Pregnancy Outcome Prediction'],
        icons=['person','activity', 'heart', 'person','person','person','person','person'],
        default_index=0
    )

st.title("Multiple Disease Prediction System")

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.subheader('Diabetes Prediction')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = validate_input(st.text_input('Number of Pregnancies'))
    with col2:
        Glucose = validate_input(st.text_input('Glucose Level'))
    with col3:
        BloodPressure = validate_input(st.text_input('Blood Pressure value'))
    with col1:
        SkinThickness = validate_input(st.text_input('Skin Thickness value'))
    with col2:
        Insulin = validate_input(st.text_input('Insulin Level'))
    with col3:
        BMI = validate_input(st.text_input('BMI value'))
    with col1:
        DiabetesPedigreeFunction = validate_input(st.text_input('Diabetes Pedigree Function value'))
    with col2:
        Age = validate_input(st.text_input('Age of the Person'))

    # Code for Prediction
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.subheader('Heart Disease Prediction')

    # Getting input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        age = validate_input(st.text_input('Age'))
    with col2:
        sex = validate_input(st.text_input('Sex'))
    with col3:
        cp = validate_input(st.text_input('Chest Pain types'))
    with col1:
        trestbps = validate_input(st.text_input('Resting Blood Pressure'))
    with col2:
        chol = validate_input(st.text_input('Serum Cholesterol in mg/dl'))
    with col3:
        fbs = validate_input(st.text_input('Fasting Blood Sugar > 120 mg/dl'))
    with col1:
        restecg = validate_input(st.text_input('Resting Electrocardiographic results'))
    with col2:
        thalach = validate_input(st.text_input('Maximum Heart Rate achieved'))
    with col3:
        exang = validate_input(st.text_input('Exercise Induced Angina'))
    with col1:
        oldpeak = validate_input(st.text_input('ST depression induced by exercise'))
    with col2:
        slope = validate_input(st.text_input('Slope of the peak exercise ST segment'))
    with col3:
        ca = validate_input(st.text_input('Major vessels colored by fluoroscopy'))
    with col1:
        thal = validate_input(st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect'))

    # Code for Prediction
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.subheader("Parkinson's Disease Prediction")

    # Getting input data from the user
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo = validate_input(st.text_input('MDVP:Fo(Hz)'))
    with col2:
        fhi = validate_input(st.text_input('MDVP:Fhi(Hz)'))
    with col3:
        flo = validate_input(st.text_input('MDVP:Flo(Hz)'))
    with col4:
        Jitter_percent = validate_input(st.text_input('MDVP:Jitter(%)'))
    with col5:
        Jitter_Abs = validate_input(st.text_input('MDVP:Jitter(Abs)'))
    with col1:
        RAP = validate_input(st.text_input('MDVP:RAP'))
    with col2:
        PPQ = validate_input(st.text_input('MDVP:PPQ'))
    with col3:
        DDP = validate_input(st.text_input('Jitter:DDP'))
    with col4:
        Shimmer = validate_input(st.text_input('MDVP:Shimmer'))
    with col5:
        Shimmer_dB = validate_input(st.text_input('MDVP:Shimmer(dB)'))
    with col1:
        APQ3 = validate_input(st.text_input('Shimmer:APQ3'))
    with col2:
        APQ5 = validate_input(st.text_input('Shimmer:APQ5'))
    with col3:
        APQ = validate_input(st.text_input('MDVP:APQ'))
    with col4:
        DDA = validate_input(st.text_input('Shimmer:DDA'))
    with col5:
        NHR = validate_input(st.text_input('NHR'))
    with col1:
        HNR = validate_input(st.text_input('HNR'))
    with col2:
        RPDE = validate_input(st.text_input('RPDE'))
    with col3:
        DFA = validate_input(st.text_input('DFA'))
    with col4:
        spread1 = validate_input(st.text_input('Spread1'))
    with col5:
        spread2 = validate_input(st.text_input('Spread2'))
    with col1:
        D2 = validate_input(st.text_input('D2'))
    with col2:
        PPE = validate_input(st.text_input('PPE'))

    # Code for Prediction
    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    
    
    
    # Liver Disease Prediction Page
if selected == 'Liver Disease Prediction':
    st.subheader('Liver Disease Prediction')

    # Getting input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        age = validate_input(st.text_input('Age'))
    with col2:
        total_bilirubin = validate_input(st.text_input('Total Bilirubin'))
    with col3:
        direct_bilirubin = validate_input(st.text_input('Direct Bilirubin'))
    with col1:
        alkaline_phosphotase = validate_input(st.text_input('Alkaline Phosphotase'))
    with col2:
        alamine_aminotransferase = validate_input(st.text_input('Alamine Aminotransferase'))
    with col3:
        aspartate_aminotransferase = validate_input(st.text_input('Aspartate Aminotransferase'))
    with col1:
        total_proteins = validate_input(st.text_input('Total Proteins'))
    with col2:
        albumin = validate_input(st.text_input('Albumin'))
    with col3:
        albumin_and_globulin_ratio = validate_input(st.text_input('Albumin and Globulin Ratio'))
    with col1:
        gender_male = validate_input(st.text_input('Gender (1 for Male, 0 for Female)'))

    # Code for Prediction
    liver_diagnosis = ''
    if st.button('Liver Disease Test Result'):
        liver_prediction = liver_disease_model.predict([[age, total_bilirubin, direct_bilirubin, alkaline_phosphotase, 
                                                         alamine_aminotransferase, aspartate_aminotransferase, total_proteins, 
                                                         albumin, albumin_and_globulin_ratio, gender_male]])
        liver_diagnosis = 'The person has liver disease' if liver_prediction[0] == 1 else 'The person does not have liver disease'

    st.success(liver_diagnosis)

    
# CKD Prediction Page
if selected == 'CKD Prediction':
    st.subheader('Chronic Kidney Disease (CKD) Prediction')

    # Getting input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        age = validate_input(st.text_input('Age'))
    with col2:
        bp = validate_input(st.text_input('Blood Pressure'))
    with col3:
        al = validate_input(st.text_input('Albumin Level'))
    with col1:
        su = validate_input(st.text_input('Sugar Level'))
    with col2:
        rbc = validate_input(st.text_input('Red Blood Cells (1 for normal, 0 for abnormal)'))
    with col3:
        pc = validate_input(st.text_input('Pus Cell (1 for normal, 0 for abnormal)'))
    with col1:
        pcc = validate_input(st.text_input('Pus Cell Clumps (1 for present, 0 for not present)'))
    with col2:
        ba = validate_input(st.text_input('Bacteria (1 for present, 0 for not present)'))
    with col3:
        bgr = validate_input(st.text_input('Blood Glucose Random'))
    with col1:
        bu = validate_input(st.text_input('Blood Urea'))
    with col2:
        sc = validate_input(st.text_input('Serum Creatinine'))
    with col3:
        pot = validate_input(st.text_input('Potassium Level'))
    with col1:
        wc = validate_input(st.text_input('White Blood Cell Count'))
    with col2:
        htn = validate_input(st.text_input('Hypertension (1 for yes, 0 for no)'))
    with col3:
        dm = validate_input(st.text_input('Diabetes Mellitus (1 for yes, 0 for no)'))
    with col1:
        cad = validate_input(st.text_input('Coronary Artery Disease (1 for yes, 0 for no)'))
    with col2:
        pe = validate_input(st.text_input('Pedal Edema (1 for yes, 0 for no)'))
    with col3:
        ane = validate_input(st.text_input('Anemia (1 for yes, 0 for no)'))

    # Code for Prediction
    ckd_diagnosis = ''
    if st.button('CKD Test Result'):
        ckd_prediction = kidney_disease_model.predict([[age, bp, al, su, rbc, pc, pcc, ba, bgr, bu, sc, pot, wc, htn, dm, cad, pe, ane]])
        ckd_diagnosis = 'The person has Chronic Kidney Disease' if ckd_prediction[0] == 1 else 'The person does not have Chronic Kidney Disease'

    st.success(ckd_diagnosis)
    
    
    
    # Prediction Page for the given features
if selected == 'Lung Cancer Prediction':
    st.subheader('Lung Cancer Prediction')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        GENDER = validate_input(st.text_input('Gender (1 for Male, 0 for Female)'))
    with col2:
        AGE = validate_input(st.text_input('Age'))
    with col3:
        SMOKING = validate_input(st.text_input('Smoking (1 for Yes, 0 for No)'))
    with col1:
        YELLOW_FINGERS = validate_input(st.text_input('Yellow Fingers (1 for Yes, 0 for No)'))
    with col2:
        ANXIETY = validate_input(st.text_input('Anxiety (1 for Yes, 0 for No)'))
    with col3:
        PEER_PRESSURE = validate_input(st.text_input('Peer Pressure (1 for Yes, 0 for No)'))
    with col1:
        CHRONIC_DISEASE = validate_input(st.text_input('Chronic Disease (1 for Yes, 0 for No)'))
    with col2:
        FATIGUE = validate_input(st.text_input('Fatigue (1 for Yes, 0 for No)'))
    with col3:
        ALLERGY = validate_input(st.text_input('Allergy (1 for Yes, 0 for No)'))
    with col1:
        WHEEZING = validate_input(st.text_input('Wheezing (1 for Yes, 0 for No)'))
    with col2:
        ALCOHOL_CONSUMING = validate_input(st.text_input('Alcohol Consuming (1 for Yes, 0 for No)'))
    with col3:
        COUGHING = validate_input(st.text_input('Coughing (1 for Yes, 0 for No)'))
    with col1:
        SHORTNESS_OF_BREATH = validate_input(st.text_input('Shortness of Breath (1 for Yes, 0 for No)'))
    with col2:
        SWALLOWING_DIFFICULTY = validate_input(st.text_input('Swallowing Difficulty (1 for Yes, 0 for No)'))
    with col3:
        CHEST_PAIN = validate_input(st.text_input('Chest Pain (1 for Yes, 0 for No)'))

    # Code for Prediction
    health_diagnosis = ''
    if st.button('Health Test Result'):
        health_prediction = lung_disease_model.predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, 
                                                   CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, 
                                                   ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, 
                                                   SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        health_diagnosis = 'The person is likely to have the condition' if health_prediction[0] == 1 else 'The person is not likely to have the condition'

    st.success(health_diagnosis)
    
    


# Pregnancy Outcome Prediction Page
if selected == 'Pregnancy Outcome Prediction':
        st.subheader('Pregnancy Outcome Prediction')

        # Getting the input data from the user
        col1, col2, col3 = st.columns(3)

        with col1:
            Age = validate_input(st.text_input('Age of the Person'))
        with col2:
            Pregnancies = validate_input(st.text_input('Number of Pregnancies'))
        with col3:
            Glucose = validate_input(st.text_input('Glucose Level'))
        with col1:
            BloodPressure = validate_input(st.text_input('Blood Pressure value'))
        with col2:
            SkinThickness = validate_input(st.text_input('Skin Thickness value'))
        with col3:
            Insulin = validate_input(st.text_input('Insulin Level'))
        with col1:
            BMI = validate_input(st.text_input('BMI value'))
        with col2:
            DiabetesPedigreeFunction = validate_input(st.text_input('Diabetes Pedigree Function value'))

        # Code for Prediction
        pregnancy_outcome = ''
        if st.button('Predict Pregnancy Outcome'):
            outcome_prediction = pregnancy_model.predict([[Age, Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction]])
            pregnancy_outcome = 'High risk pregnancy' if outcome_prediction[0] == 1 else 'Low risk pregnancy'

        st.success(pregnancy_outcome)



    
    # Liver Disease Prediction Page
if selected == 'Home':
      st.subheader('About the App')
      
      

        # Title and introductory text
      st.markdown("""
            <h1 style="text-align: center; color: #4CAF50;">Basic Machine Learning and Deep Learning WebApp</h1>
            <p style="text-align: center; font-size: 18px;">
                This is a basic Machine Learning and Deep Learning-based WebApp. <br>
                These Machine Learning models and Deep Learning models are trained on large datasets and thousands of images.
            </p>
            <hr style="border: 1px solid #ddd;">
        """, unsafe_allow_html=True)
        
        # Model Accuracies
      st.markdown("""
            <h2 style="color: #2196F3;">Model Accuracies</h2>
            <ul style="font-size: 16px;">
                <li><strong>Diabetes Model:</strong> 98.25%</li>
                <li><strong>Breast Cancer Model:</strong> 98.25%</li>
                <li><strong>Heart Disease Model:</strong> 85.25%</li>
                <li><strong>Kidney Disease Model:</strong> 99%</li>
                <li><strong>Liver Disease Model:</strong> 78%</li>
                <li><strong>Malaria Model:</strong> 96%</li>
                <li><strong>Pneumonia Model:</strong> 95%</li>
                <li><strong>Pregnancy Outcome Model:</strong> 98%</li>
            </ul>
            <hr style="border: 1px solid #ddd;">
        """, unsafe_allow_html=True)
        
        # Disease Information
      st.markdown("""
            <h2 style="color: #FF5722;">Information about the Diseases</h2>
        """, unsafe_allow_html=True)
        
        # Diabetes Section
      st.markdown("""
            <h3 style="color: #9C27B0;">Diabetes</h3>
            <p>
                Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high. 
                Blood glucose is your main source of energy and comes from the food you eat. Insulin, a hormone made 
                by the pancreas, helps glucose from food get into your cells to be used for energy. Sometimes your body 
                doesn’t make enough—or any—insulin or doesn’t use insulin well. Glucose then stays in your blood and 
                doesn’t reach your cells.
            </p>
            <strong>Symptoms:</strong>
            <ul>
                <li>Urinating often.</li>
                <li>Feeling very thirsty.</li>
                <li>Extreme fatigue.</li>
                <li>Blurry vision.</li>
            </ul>
        """, unsafe_allow_html=True)
        
        # Breast Cancer Section
      st.markdown("""
            <h3 style="color: #9C27B0;">Breast Cancer</h3>
            <p>
                Breast cancer is cancer that forms in the cells of the breasts. After skin cancer, breast cancer is the 
                most common cancer diagnosed in women in the United States. Breast cancer can occur in both men and women, 
                but it's far more common in women.
            </p>
            <strong>Symptoms:</strong>
            <ul>
                <li>A breast lump or thickening that feels different from the surrounding tissue.</li>
                <li>Change in the size, shape, or appearance of a breast.</li>
                <li>Changes to the skin over the breast, such as dimpling.</li>
                <li>Redness or pitting of the skin over your breast, like the skin of an orange.</li>
            </ul>
        """, unsafe_allow_html=True)
        
        # Chronic Kidney Disease Section
      st.markdown("""
            <h3 style="color: #9C27B0;">Chronic Kidney Disease</h3>
            <p>
                Chronic kidney disease, also called chronic kidney failure, describes the gradual loss of kidney function. 
                Your kidneys filter wastes and excess fluids from your blood, which are then excreted in your urine. When 
                chronic kidney disease reaches an advanced stage, dangerous levels of fluid, electrolytes and wastes can 
                build up in your body.
            </p>
            <strong>Symptoms:</strong>
            <ul>
                <li>Nausea</li>
                <li>Vomiting</li>
                <li>Fatigue and weakness</li>
                <li>Muscle twitches and cramps</li>
            </ul>
        """, unsafe_allow_html=True)
        
        # Liver Disease Section
      st.markdown("""
            <h3 style="color: #9C27B0;">Liver Disease</h3>
            <p>
                Symptoms of liver disease can vary, but they often include swelling of the abdomen and legs, bruising easily, 
                changes in the color of your stool and urine, and jaundice, or yellowing of the skin and eyes. Sometimes there 
                are no symptoms. Tests such as imaging tests and liver function tests can check for liver damage and help to 
                diagnose liver diseases.
            </p>
        """, unsafe_allow_html=True)
        
        # Malaria Section
      st.markdown("""
            <h3 style="color: #9C27B0;">Malaria</h3>
            <p>
                Malaria is a mosquito-borne infectious disease that affects humans and other animals. Malaria causes symptoms 
                that typically include fever, tiredness, vomiting, and headaches. In severe cases, it can cause yellow skin, 
                seizures, coma, or death. Symptoms usually begin ten to fifteen days after being bitten by an infected mosquito. 
                If not properly treated, people may have recurrences of the disease months later.
            </p>
            <strong>Symptoms:</strong>
            <ul>
                <li>Fever. This is the most common symptom.</li>
                <li>Chills</li>
                <li>Headache</li>
                <li>Nausea and vomiting</li>
            </ul>
        """, unsafe_allow_html=True)
        
        # Pneumonia Section
      st.markdown("""
            <h3 style="color: #9C27B0;">Pneumonia</h3>
            <p>
                Pneumonia is an infection that inflames the air sacs in one or both lungs. The air sacs may fill with fluid or pus 
                (purulent material), causing cough with phlegm or pus, fever, chills, and difficulty breathing. A variety of organisms, 
                including bacteria, viruses, and fungi, can cause pneumonia.
            </p>
            <strong>Symptoms:</strong>
            <ul>
                <li>Cough, which may produce greenish, yellow, or even bloody mucus.</li>
                <li>Fever, sweating, and shaking chills.</li>
                <li>Shortness of breath.</li>
                <li>Rapid, shallow breathing.</li>
            </ul>
        """, unsafe_allow_html=True)

      st.markdown("""
            <h3 style="color: #9C27B0;">Lung Cancer</h3>
            <p>
                Lung cancer is a disease that occurs when abnormal cells in the lung grow uncontrollably. These cells 
                can form tumors, interfere with the lung's normal function, and spread to other parts of the body. 
                Smoking is the leading cause of lung cancer, but it can also occur in non-smokers due to exposure to 
                harmful substances like radon, asbestos, or air pollution, as well as genetic factors.
            </p>
            <strong>Symptoms:</strong>
            <ul>
                <li>Persistent cough that doesn’t go away or worsens.</li>
                <li>Chest pain, often worse with deep breathing or coughing.</li>
                <li>Shortness of breath.</li>
                <li>Unexplained weight loss.</li>
            </ul>
        """, unsafe_allow_html=True)

      st.markdown("""
            <h3 style="color: #9C27B0;">Chronic Kidney Disease</h3>
            <p>
                Chronic kidney disease is a condition where the kidneys gradually lose their ability to filter waste and 
                excess fluids from the blood. This can lead to harmful substances building up in the body and affecting 
                overall health. CKD often develops slowly and may not show symptoms in its early stages. It is commonly 
                caused by diabetes, high blood pressure, and other conditions that damage the kidneys over time.
            </p>
            <strong>Symptoms:</strong>
            <ul>
                <li>Swelling in the ankles, feet, or hands (edema).</li>
                <li>Fatigue or low energy levels.</li>
                <li>Nausea or vomiting.</li>
                <li>Difficulty concentrating or mental fog.</li>
                <li>Changes in urination (frequency or appearance).</li>
            </ul>
        """, unsafe_allow_html=True)
      
      st.markdown("""
    <h3 style="color: #9C27B0;">Pregnancy Outcome</h3>
    <p>
        Pregnancy outcome refers to the result of a pregnancy, which can be influenced by several maternal health factors. 
        Monitoring key health indicators such as blood pressure, glucose levels, and BMI can help predict and manage pregnancy risks. 
        Understanding these factors allows for better maternal and fetal health care during pregnancy.
    </p>
    <strong>Key Factors Affecting Pregnancy Outcome:</strong>
    <ul>
        <li><strong>Age:</strong> Maternal age impacts pregnancy risks, with higher risks in teenage and advanced maternal age pregnancies.</li>
        <li><strong>Number of Pregnancies:</strong> Previous pregnancies can influence future pregnancy outcomes.</li>
        <li><strong>Glucose Levels:</strong> High glucose may indicate gestational diabetes, affecting both mother and baby.</li>
        <li><strong>Blood Pressure:</strong> Hypertension during pregnancy can lead to complications such as preeclampsia.</li>
        <li><strong>Skin Thickness:</strong> Related to body fat distribution, which can influence pregnancy metabolism.</li>
        <li><strong>Insulin Levels:</strong> Important for managing glucose and preventing gestational diabetes.</li>
        <li><strong>BMI (Body Mass Index):</strong> A high or low BMI can lead to complications such as preterm birth or gestational diabetes.</li>
        <li><strong>Diabetes Pedigree Function:</strong> Genetic predisposition to diabetes can increase pregnancy risks.</li>
    </ul>
      
    <strong>Common Symptoms of Pregnancy Complications:</strong>
    <ul>
        <li>Severe headaches and dizziness.</li>
        <li>Blurred vision or sudden vision changes.</li>
        <li>Swelling in hands, face, or legs (signs of preeclampsia).</li>
        <li>Severe abdominal pain or cramping.</li>
        <li>High blood pressure readings.</li>
        <li>Excessive thirst or frequent urination (possible gestational diabetes).</li>
        <li>Decreased fetal movement.</li>
        <li>Unusual weight gain or loss.</li>
        <li>Preterm contractions before 37 weeks.</li>
        <li>Excessive nausea and vomiting leading to dehydration.</li>
    </ul>
    """, unsafe_allow_html=True)


    


# Background Styling Function
def set_bg_from_url(url, opacity=1):
    footer = """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <footer>
        <div style='margin-top:7rem; justify-content:center; display:flex;'>
            <p>Made by Zakari Moro</p>
        </div>
    </footer>
    """
    st.markdown(footer, unsafe_allow_html=True)
    st.markdown(
        f"""
        <style>
            body {{
                background: url('{url}') no-repeat center center fixed;
                background-size: cover;
                opacity: {opacity};
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_from_url("https://images.everydayhealth.com/homepage/health-topics-2.jpg?w=768", opacity=0.875)
