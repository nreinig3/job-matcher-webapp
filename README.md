# job-matcher-webapp

<a href="https://youtu.be/ARXXxXQmmQw?si=bmVXOmilV8PvpWmI">
    <img src="/media/job-matcher-thumbnail.png" alt="Thumbnail for Job Matcher Web App demo video" style="width: 60%; height: auto;">
</a>

*Deomonstration of the Job Matcher web application, showing the vizualization resulting from a user's input*

#### Problem:  
Traditional job search websites rely on keyword filters, which generate overwhelming yet imprecise results, forcing candidates to sift through many irrelevant postings while missing ideal opportunities disguised by different job titles. This inefficiency also causes problems for employers, who must contend with a high volume of misaligned applicants.

#### Solution: 
A web app that leverages natural language processesing (NLP) algorithms to itelligently match job postings to user input, ensuring alignment between important characteristics of the candidate and the job posting. Results are returned in a concept map-style visualization that allows users to see and interact with a large number of job postings at once. 

#### My team's approach:  

*Data*  

To create a database of job postings, job titles and raw job description text were extracted from two sources: a publicly available dataset from Techmap.io, and a public scraped dataset hosted on Google Drive. This data was converted into a word-tokenized format suitable for downstream NLP model training, with stop words, non-English sentences, and single-use words removed. 

*NLP Models*  

The project's two goals were to accurately match user input to job descriptions in the database in real-time (inference), and to determine the similarity between all job descriptions ahead of time. To accomplish this, three NLP models were tested: Doc2Vec, TF-IDF, and Big-Query ML (BQML). These models were used to numerically vectorize the job descriptions and user input text, and a cosine similarity function was employed to score relatedness between every pair of vectorized outputs.

*Interactive Vizualization*  
The visualization was built with Javascript, using the D3.js library. It was set up as a force-directed network graph, with the five job descriptions most closely related to the user input visualized as nodes connected to a central node representing the user input. When a user clicks on the 1st degree nodes, they see the job title, a snippet of the job description, and a similarity score (our cosine similarity function, expressed as a percentage). In order to supply the user with more information, but without significantly increasing inference time, pairwise similarity scores between the job postings (which had already been calculated) were used to add another set of job postings to the visualization. These 2nd degree nodes represent the jobs most closely related to each of the 1st degree nodes, and that were above a particular similarity threshold we chose. 


*Web App Architecture*  
Users' textual input is captured from the text box in the web app, and sent to a Flask backend. From Flask, the input is processed through the machine learning model (Doc2Vec), and the most similar job postings are determined. Next, D3.js is updated, after which the visualization is refreshed with the current selections. 


#### Results:
<img src="https://github.com/user-attachments/assets/990e0856-2d2f-48e1-8787-59c0aec38756" 
     alt="Description of image" 
     style="width: 60%; height: auto;">  

 *An example of the data visualization generated after a user submits the text input shown below the text box*

 

