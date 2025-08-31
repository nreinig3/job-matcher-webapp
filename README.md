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

To create a database of job postings, job titles and raw job description text were extracted from two sources: Techmap.io and a scraped dataset hosted on Google Drive. This data was converted into a word-tokenized format suitable for downstream NLP model training, with stop words, non-English sentences, and single-use words removed. 

*NLP Models*  

Our two goals were to accurately match user input to job descriptions in the database, as well as determining the similarity between all the job descriptions.  


