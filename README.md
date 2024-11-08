# Streamlit examples

In order to run the code snippets, first create a virtual environment. We'll make an example using venv:

`python3 -m venv streamlit-env`

Then activate it: `source streamlit-env/bin/activate`

Install the requirements: `pip install -r requirements.txt` and run `streamlit run <script.py>` where `script.py` can be any of those in the directory.

# Assignment

We provide you with two code snippets already completed: the first one (`data_analysis.py`) to perform interactive data analysis with a CSV file uploaded by the user, and another one (`goal_tracker.py`) to interact with a CSV file containing the goals record for different footbal players.

1. Run these files and check the code to familiarize with Streamlit. Try to modify them and include new types of widgets in the UI.

2. Then, you will have to complete the `classify_image.py` file. This is a UI which should give you the chance to upload an image, then make a prediction using the ResNet50 we provide, and finally show the class predicted for the image. Check the documentation of `st.file_uploader` and `st.image` to see how to upload and then show an image in your UI.
