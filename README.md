Statement:

Machine learning based classification of credit card approval.
Dataset:

From UCI repository, dataset contains one target variable and fifteen
features(Age,Income,…)

Models used:
| ML Model Name | Accuracy | AUC | Precision | Recall | F1 | MCC |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.8043 | 0.8816 | 0.8676 | 0.7662 | 0.8138 | 0.6146 |
| Decision Tree | 0.7899 | 0.7947 | 0.8529 | 0.7532 | 0.8000 | 0.5854 |
| KNN | 0.7971 | 0.8417 | 0.8101 | 0.8312 | 0.8205 | 0.5875 |
| Naive Bayes | 0.8261 | 0.8610 | 0.7912 | 0.9351 | 0.8571 | 0.6535 |
| Random Forest | 0.8333 | 0.9142 | 0.8553 | 0.8442 | 0.8497 | 0.6628 |

Observations:
| ML Model Name | Observation about model performance |
|---|---|
| **Logistic Regression** | Model has a precision of 86.76%, indicating good performance in correctly identifying positive cases. However, recall is 76.62%, suggesting that it misses some positive cases. Overall, it is a strong model. |
| **Decision Tree** | Model’s Accuracy and AUC scores are relatively low, making it the weakest model in terms of overall predictive performance. |
| **KNN** | The model’s recall score is strong, meaning it has identified a good proportion of positive cases. However, its precision is lower than Logistic Regression and Random Forest. Overall, KNN showed moderate performance. |
| **Naive Bayes** | The model has a high recall of 93.51%, the highest among all models, but its precision is comparatively lower, suggesting that the model is highly effective in identifying positive cases but also produces more false positives. |
| **Random Forest** | The model produced the best overall performance among all the models in terms of the evaluation scores. Therefore, it appears to be the most suitable model for this problem. |
