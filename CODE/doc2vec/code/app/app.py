import json
import pandas as pd
from flask import Flask, request, jsonify, render_template
from doc2vecModel import run_model, get_node_details_all

app = Flask(__name__)

# Load pre-processed graph data from flat file
csv_data = pd.read_csv('static/_graph_data3.csv')


@app.route('/', methods=['GET', 'POST'])
def home():

    user_input = None
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
        processed_data = run_model(user_input, model='model', data_size='medium') # Run doc2vec on user input

        # Process related job postings from graph_data csv
        nodes_connected = processed_data['node'].values.tolist() # Get connecting nodes from processed data
        new_column_names = {'node_from': 'source', 'node_to': 'target', 'from_title': 'source_title', 'to_title': 'target_title', 'from_job_name': 'source_job_name', 'to_job_name': 'target_job_name'}
        csv_data.rename(columns=new_column_names, inplace=True) # Renaming columns
        cols_remove = ['source_title', 'target_title'] # Remove title columns because unescaped characters etc. break code (use job name instead)
        filtered_data = csv_data.drop(columns=cols_remove)
        filtered_data['source_description'] = 'Job ID: ' + filtered_data['source'].astype(str)
        filtered_data['target_description'] = 'Job ID: ' + filtered_data['target'].astype(str)
        filtered_data['similarity_string'] = "Similarity to parent node: " + round(filtered_data['measure']*100, 1).astype(str) + '%'
        #filtered_data = filtered_data[(csv_data['source'].isin(nodes_connected)) | (csv_data['target'].isin(nodes_connected))] #Pulling in 2nd level nodes
        #filtered_data = filtered_data[filtered_data['measure'] >= 0.97] #Setting similarity threshold between 1st and 2nd level nodes
        nodes_level2 = pd.DataFrame()
        for node in nodes_connected:
            connected_to_node = filtered_data[(filtered_data['source'] == node) | (filtered_data['target'] == node)]
            connected_to_node = connected_to_node.sort_values(by='measure', ascending=False).head(7)
            nodes_level2 = pd.concat([nodes_level2, connected_to_node], ignore_index=True)

        return render_template('viz.html',
                               user_input=user_input,
                               processed_data=processed_data.to_json(),
                               filtered_data=nodes_level2.to_json(orient='records'),
                               nodes_connected=nodes_connected)


    return render_template('viz.html', user_input=None)

if __name__ == '__main__':
    app.run(debug=True)
