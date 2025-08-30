DESCRIPTION
This project includes two main modeling code files employing different techniques to estimate job posting similarity, as well as a third method that involves training an ML model on the Google Cloud platform for the same purpose. 
Additionaly, we developed an interactive D3.js visualization based on a Flask backend framework. This web application uses one of our trained models to determine the jobs postings that most closely match a user's textual input, then graphs the results in real-time along with other pre-generated job linkages. 

This README begins with instructions for implementing the D3.js network graph visualization based on our trained Doc2Vec model. Next, it covers the installation and execution of code for the Doc2Vec model. The steps required to run the TF-IDF model code are subsequently described, and finally, we present instructions for creating the BigQuery-ML model on Google Cloud.

##-------------------------------------------------------------------------------------------------------------------------------##

SECTION 1: INSTALLING AND RUNNING THE VISUALIZATION DEMO ("JOB MATCHER" WEB APPLICATION)

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

*** Model note: These instructions have assumed you want to use our already-trained doc2vec model. If you prefer to train your own model, please follow the instructions in section 2 of this document. 

*** Formatting note: If the visualization text or graph is too large, try reducing the webpage size to 75% using your browser's zoom functionality.

##-------------------------------------------------------------------------------------------------------------------------------##

SECTION 2: SETUP AND EXECUTION OF THE DOC2VEC MODEL FOR ESTIMATING JOB POSTING SIMILARITY

File description:
4_train_doc2vec_eval_model.ipynb : Used to train doc2vec model using downloaded data. Few additional cells for visualizing simplified vector embeddings (of random jobs)
6_create_graph_data.ipynb (Not required to run) : Used to calculate similarity matrix and graph data for similar jobs. Takes 30+ minutes to run 

Instruction:
1. install python dependencies listed in ./requirements.txt

2. Download the following data from the link below and place it under `./local_data` directory prior to running 4_train_doc2vec_eval_model
   • Link to download `_large_data3.csv` (1.3GB) : https://storage.googleapis.com/cse6242-team131/_large_data3.csv

3. Run 4_train_doc2vec_eval_model.ipynb, which will do the following:
   • Train doc2vec model using downloaded data
   • Pick out random job titles (you can run these cells multiple times) and visualize their simplified vector embeddings (using PCA) to see how job each descriptions are quantified 
   • Outputs index of training / test data as .npy file, which was used for evaluation down the road.
   • If you run into issues, below are download links for model outputs (both to be placed in ./local_models folder):
	- `_large_model2` : https://storage.googleapis.com/cse6242-team131/large_model2
 	- `_large_model2.dv.vectors.npy` : https://storage.googleapis.com/cse6242-team131/large_model2.dv.vectors.npy

4. (Optional) Run 6_create_graph_data.ipynb which will do the following:
   • Uses doc2vec model to create pairwise consine similarity matrix
   • Extract pairwise similarity value greater than threshold to create a graph data.
   • If you run into memory issues, these are alternative links to be able to download outputs:
	- `_graph_data3.csv` : https://storage.googleapis.com/cse6242-team131/_graph_data3.csv

##-------------------------------------------------------------------------------------------------------------------------------##

SECTION 3: SETUP AND EXECUTION OF THE TF-IDF MODEL FOR ESTIMATING JOB POSTING SIMILARITY
Step 1:
   • Download data from https://storage.googleapis.com/cse6242-team131/_large_data3.csv

Step 2:
   • Install necessary packages:
       - nltk

Step 3:
   • Execute the code file "TF-IDF large data V3.ipynb"

Step 4:
   • Update "input_description" to your preferred job descriptions, then view the top 15 similar jobs within the dataset.

##-------------------------------------------------------------------------------------------------------------------------------##

SECTION 4: SETUP AND EXECUTION OF THE BIGQUERY-ML MODEL FOR ESTIMATING JOB POSTING SIMILARITY
Step 1: Create a dataset
   • In the Google Cloud console, go to the BigQuery page.
   • In the Explorer pane, click your project name.
   • Click View actions > Create dataset.
   • On the Create dataset page, do the following:
	- For Dataset ID, enter model_dataset.
	- For Location type, select Multi-region, and then select US (multiple regions in United States)
	- Leave the remaining default settings as they are, and click Create dataset.

Step 2: Create a connection
   • Go to the BigQuery page
   • To create a connection, click add Add data, and then click Connections to external data sources.
   • In the Connection type list, select Vertex AI remote models, remote functions and BigLake (Cloud Resource).
   • In the Connection ID field, enter a name for your connection.
   • Click Create connection.
   • Click Go to connection.
   • In the Connection info pane, copy the service account ID for use in a later step.

Step 3: Grant the service account access
   • Go to the IAM & Admin page.
   • Click person_add Grant Access.
   • In the New principals field, enter the service account ID that you copied earlier.
   • In the Select a role field, choose Vertex AI, and then select Vertex AI User role.
   • Click Save.

Step 4: Create the remote model
   • Go to the BigQuery page
   • Run Query 4

Step 5: Generate Text Embeddings
   • Go to the BigQuery page
   • Run Query 5

Step 6: Create a vector index
   • Go to the BigQuery page
   • Run Query 6

Step 7: Perform similarity text search
   • Go to the BigQuery page
   • Run Query 7



