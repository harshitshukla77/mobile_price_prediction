# mobile_price_prediction

# Application Link
https://mobilepriceprediction-harsh3it557shukla.streamlit.app/

# Problem Statement 

The mobile phone market is highly competitive, with numerous models released each year, varying widely in features and prices. Consumers often find it challenging to assess whether a mobile phone's price is justified based on its features. Additionally, manufacturers and retailers need to price their products competitively while maximizing profit. This project aims to develop a predictive model that can estimate the price of a mobile phone based on its features, helping both consumers and businesses make informed decisions.

# Project Summary 

 I gathered a comprehensive dataset of mobile phones, including essential features that influence their price using Web Scraping techniques and then stored the data in one place. The important features of the mobiles were extracted from the scraped data and the dataset with proper format was created. The dataset was then cleaned and preprocessed to address missing values, outliers, and inconsistencies, ensuring the quality and reliability of the data.

I conducted a thorough analysis of the dataset to understand the relationships and patterns between mobile phone features and their prices.Visualization techniques were employed to gain insights into the data, revealing key factors that impact pricing.

Categorical variables were encoded, and continuous variables were normalized to ensure compatibility with machine learning algorithms. Multiple regression models were evaluated, including Linear Regression, Decision Trees, Random Forests and Gradient Boosting. The models were trained on the historical data, and their performance was assessed using metrics such as Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R-squared. 

Cross-validation techniques were applied to ensure the robustness and generalizability of the selected model. The best-performing model was Random forest regressor and it was chosen based on its accuracy and consistency in predicting mobile phone prices. The final model demonstrated high accuracy in predicting the price range of mobile phones, with an R-squared value of approximately 0.94, indicating a strong correlation between the predicted and actual prices.

# Technologies Used

•	Programming Language: Python

•	Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

•	Model Deployment: Streamlit, GitHub


