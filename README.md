House Price Prediction Web App

This project is a Flask-based web application that predicts house prices using a linear regression model trained on the California Housing dataset. 
It demonstrates the complete machine learning workflow—from data preprocessing to model training, serialization, and deployment as a web service.

Key Highlights
	Machine Learning Pipeline:
	Trained a linear regression model using key features (e.g., total bedrooms). Input features are scaled using StandardScaler to ensure consistent and accurate predictions.
	End-to-End Workflow:
	The project covers data cleaning, feature selection, model training, saving/loading models, and integrating the trained model into a web application.
	Interactive Web Interface:
	Users can enter relevant feature values through a user-friendly web form, and the app provides real-time predictions.
	RESTful API:
	A /predict API endpoint allows programmatic access to the model, enabling integration with other applications or services. The API receives input features in JSON format and returns predicted prices.
	Skills Demonstrated:
		Linear regression modeling and feature scaling
		Model serialization and reuse with joblib
		API design and integration using Flask
		Frontend-backend connectivity for seamless prediction
		Version control with Git and project organization

Future Improvements
	Deploy the application on cloud platforms (AWS) for public access
	Incorporate additional features for higher prediction accuracy
	Explore advanced regression models (Random Forest, XGBoost)
	Implement logging and user authentication for production readiness
