DESCRIPTION
This project includes two main modeling code files employing different techniques to estimate job posting similarity, as well as a third method that involves training an ML model on the Google Cloud platform for the same purpose. 
Additionaly, we developed an interactive D3.js visualization based on a Flask backend framework. This web application uses one of our trained models to determine the jobs postings that most closely match a user's textual input, then graphs the results in real-time along with other pre-generated job linkages. 

This README begins with instructions for implementing the D3.js network graph visualization based on our trained Doc2Vec model. Next, it covers the installation and execution of code for the Doc2Vec model. The steps required to run the TF-IDF model code are subsequently described, and finally, we present instructions for creating the BigQuery-ML model on Google Cloud.

##-------------------------------------------------------------------------------------------------------------------------------##

INSTRUCTIONS: INSTALLING AND RUNNING THE VISUALIZATION DEMO ("JOB MATCHER" WEB APPLICATION)

Code file description:
team131final/CODE/doc2vec/code/app/app.py : Backend python file that runs the Flask app
team131final/CODE/doc2vec/code/app/doc2vecModel.py : Runs the trained Doc2Vec model on user-inputted text and returns the top 5 results
team131final/CODE/doc2vec/code/app/templates/viz.html : File containing HTML and Javascript for the front-end, including the D3.js network graph

Instructions:
1. Download and unzip the folder team131final.zip

2. In your terminal, navigate to the following subfolder within the unzipped folder (this is where the web app lives): "team131final/CODE/doc2vec/code/app"

3. (Optional but recommended): While inside the "app" folder, set up a virtual environment
   • Create the virtual environment
      - Command in terminal: `python3 -m venv venv`
   • Activate the virtual environment
      - Command on Mac: `source venv/bin/activate`
      - Command on Windows: `venv\Scripts\activate`

4. Install Flask and its dependencies using provided file “requirements.txt”
   • Command in terminal: `pip install -r requirements.txt` (installation should take about 1 minute)

5. Download the job postings datasets and the trained model (required by the web application)
   • Download the following job postings dataset and save it in folder "team131final/CODE/doc2vec/code/app/local_data": 
      https://storage.googleapis.com/cse6242-team131/_medium_data2.csv
   • Download our trained doc2vec model and vectors file (2 files total) and save them in the folder "team131final/CODE/doc2vec/code/app/local_models":
      https://storage.googleapis.com/cse6242-team131/medium_model2
      https://storage.googleapis.com/cse6242-team131/medium_model2.dv.vectors.npy
   • Download this graph data (pre-processed nodes and edges) to the folder "team131final/CODE/doc2vec/code/app/static": 
      https://storage.googleapis.com/cse6242-team131/_graph_data3.csv

6. In your terminal (you should still be in the "app" folder), run the Flask application using this command: `python app.py` 
   • It should take less than a minute to initialize the application; when it is ready it should print the local server location: "Running on http://127.0.0.1:5000"

7. In your browser (Chrome is recommended), navigate to "http://127.0.0.1:5000" or "http://localhost:5000" and the web app should appear in your browser. The title, text input box, and an empty “Job Description Details” box should be visible, but no graph will appear yet.

8. Enter job-related text input (such as job experience, skills, or desired job qualities) in the text box and press the “submit” button. The application can handle a range of text lengths, but very short (one sentence) or extremely long inputs may not work. As an example, the input used in Figure 3 of our report was "I have five years experience as a data analyst. I am proficient in Python, R, Java, C++, Javascript, HTML".

9. A few seconds after the user input is submitted, the graph should appear. Clicking on nodes (other than the central node) will populate the "Job Postings Details" box with information from the job posting represented by the node. A new graph is generated whenever the user submits new input. 

*** Formatting note: If the visualization text or graph is too large, try reducing the webpage size to 75% using your browser's zoom functionality.

