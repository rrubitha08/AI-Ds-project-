from model import train_model

model = train_model()

# Predict for 5 hours of study
prediction = model.predict([[5]])

print(f"Predicted Marks: {prediction[0]}")
