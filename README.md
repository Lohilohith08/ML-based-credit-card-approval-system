Statement:

Machine learning based classification of credit card approval.
Dataset:

From UCI repository, dataset contains one target variable and fifteen
features(Age,Income,…)

Models used:

 ML Model Name	        Accuracy	AUC	       Precision	Recall	  F1	    MCC

Logistic Regression	    0.8043	    0.8816	   0.8676	    0.7662	  0.8138	0.6146

Decision Tree	        0.7899	    0.7947	   0.8529	    0.7532	  0.8000	0.5854

KNN	                    0.7971      0.8417	   0.8101	    0.8312	  0.8205	0.5875

Naive Bayes	            0.8261	    0.8610	   0.7912	    0.9351	  0.8571	0.6535

Random Forest	        0.8333	    0.9142	   0.8553	    0.8442	  0.8497	0.6628

Observations:

Logistic Regression:
Model has an precision of 86.76%, indicating good performance in correctly identifying positive cases,However Recall is of 76.62% suggests that it misses some positive cases.Overall a strong model.

Decision Tree:
Model’s Accuracy and AUC score are not good, making it a weakest model in terms of overall predictive performance.

KNN:
Models’Recall score is strong, means model has identified good proportion of p ositive cases.However its precision is lower than Logistic Regression,Randon Forest.Overall KNN showed moderate performance.

Naive Bayes:
Model has high Recall of 93.51% highest among all models, but Precision is comparatively lower suggesting model is highly effective in identifying positive case but also produces more false positives.

Random Forest:
Model has produced best overall performance among all other models in terms of all scores.Therefore it appears to be the suitable model for the problem.
