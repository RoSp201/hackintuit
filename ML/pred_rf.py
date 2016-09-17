from sklearn.ensemble import RandomForestClassifier

# Use random forest to predict salary from census data

# Will eventually get the data from another file, after Bryan finishes the data processing
# from data_processing.py import X_train, Y_Train


rf = RandomForestClassifier(n_estimators=15, max_depth=40, bootstrap=True)
rf.fit(X_train, Y_Train)


# Will mess around with hyperparameters tomorrow