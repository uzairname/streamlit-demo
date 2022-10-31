import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split

dataframe = pd.read_csv("titanic.csv", index_col=0)
st.header("Data Analysis")
st.write("Titanic dataset, and the decision tree")
st.write(dataframe)


survived = dataframe["survived"]==1
features = dataframe.drop(["survived"], axis=1)
features, features_test, survived, survived_test = train_test_split(features, survived, test_size = 0.3)

# Create a decision tree

depth = st.number_input("max depth", min_value=1, max_value=5)

my_decision_tree = tree.DecisionTreeClassifier(max_depth=depth)

# Train the decision tree using the dataset
my_decision_tree.fit(features, survived)

# Display the decision tree as a flow chart

st.write(f"This decision tree is {round(my_decision_tree.score(features_test, survived_test) * 100, 2)}% accurate")
f = plt.figure(figsize=(10,10))
tree.plot_tree(my_decision_tree, feature_names=features.columns, class_names=["died", "survived"], filled=True)

st.pyplot(f)