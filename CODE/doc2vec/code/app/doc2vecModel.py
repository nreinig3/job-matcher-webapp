# from cgitb import text
import re
import pandas as pd
import gensim
from gensim import corpora
from gensim.models.doc2vec import Doc2Vec, TaggedDocument


########################################################
##     model :
##     path = '../local_models/sample_model'
##     loaded_model = Doc2Vec.load(path) # load using path to `sample_model` file
##     job_desc_data:
##     data_path = '../local_data/_' + data_size + '_data.csv' # read "../local_data/_medium_data.csv"
########################################################


def run_model(input_text, model, data_size):
    loaded_model = get_model(model,data_size)
    job_desc_df = get_job_desc_data(data_size)
    tokenized = text_to_tokens(input_text)
    inferred_vector = loaded_model.infer_vector(tokenized)
    sims = loaded_model.dv.most_similar([inferred_vector], topn=len(loaded_model.dv))
    ass_rec_df = pd.DataFrame(columns=['node', 'similarity_num', 'job_title', 'description'])
    assoc_rec_df = find_associated_records(sims, job_desc_df, ass_rec_df)

    return assoc_rec_df


def get_model(model, data_size):
    model_name = data_size + '_model2'
    path = 'local_models/' + model_name
    loaded_model = Doc2Vec.load(path)
    print("loaded_model")
    return loaded_model


def get_job_desc_data(data_size):
    data_size = data_size
    data_path = 'local_data/_' + data_size + '_data2.csv'
    df = pd.read_csv(data_path)
    df = df[['index', 'job_name', 'job_index', 'tokenized_text', 'extracted_text']]
    print(df)
    return df


def text_to_tokens(input_text):
    no_space = re.sub(r"[\n\t]+", "", input_text)
    subbed = re.sub(r"[\[\],'\.]", "", no_space)
    split = subbed.split(" ")
    return split


def get_node_details_all(node_id, data_size='large'):
    job_desc_df = get_job_desc_data(data_size)
    mask = job_desc_df['index'] == node_id
    node_details = job_desc_df[job_desc_df['index'] == int(node_id)]
    return node_details



def find_associated_records(sims, job_desc_df, ass_rec_df):
    for i in sims[:5]:
        mask = job_desc_df['index'] == i[0]
        job_desc_df['sim_num'] = i[1]
        closest_document = job_desc_df[mask]

        def truncate(job_desc):
            # Split the text into words
            words = job_desc.split()
            truncated_text = ' '.join(words[:25]) #37
            return truncated_text

        node_val = closest_document['index'].values[0]
        sim_num_val = closest_document['sim_num'].values[0]
        job_title_val = closest_document['job_name'].values[0]
        job_desc = closest_document['extracted_text'].values[0] # Change back to 'extracted_text' after testing
        job_desc = truncate(job_desc)


        # Output data
        dict_new_data = {'node': node_val, 'similarity_num': sim_num_val, 'job_title': job_title_val, 'description': "Job Description: " + job_desc + "...", 'similarity_string': "Similarity to user input: " + round(sim_num_val*100, 1).astype(str) + '%'}
        new_row_df = pd.DataFrame([dict_new_data])


        ass_rec_df = pd.concat([ass_rec_df, new_row_df], ignore_index=True)

    return ass_rec_df


import os

print(" Get CWD ", os.getcwd())

input_text = \
"""
Threat Monitoring: Continuously monitor networks, systems, and applications for security incidents, suspicious activities, and potential threats using intrusion detection/prevention systems, security information and event management (SIEM) tools, and other security monitoring platforms.
Incident Response: Respond promptly to security incidents, alerts, and breaches by investigating root causes, containing threats, and implementing remediation measures to minimize impact and prevent recurrence, following incident response protocols and procedures.
Vulnerability Management: Conduct vulnerability assessments and scans on networks, servers, and applications to identify security weaknesses, prioritize vulnerabilities based on risk severity, and coordinate remediation efforts with relevant stakeholders to mitigate security risks effectively.
Security Analysis: Analyze security logs, traffic patterns, and system logs to detect patterns, trends, and anomalies indicative of potential security threats or malicious activities, leveraging security analytics tools and techniques to identify and investigate security incidents.
Security Compliance: Ensure compliance with regulatory requirements, industry standards, and organizational security policies by conducting security audits, assessments, and reviews, identifying gaps or non-compliance issues, and implementing corrective actions to maintain a strong security posture.
Threat Intelligence: Stay informed about emerging cyber threats, attack vectors, and security vulnerabilities by monitoring threat intelligence sources, security advisories, and industry reports, and leveraging this information to enhance security controls and strategies proactively.
Security Awareness: Promote security awareness and best practices among employees through training sessions, educational materials, and communication initiatives, fostering a culture of security awareness and accountability across the organization.
Security Tool Management: Manage and maintain security tools and technologies, such as firewalls, antivirus software, endpoint detection and response (EDR) solutions, and security appliances, ensuring their proper configuration, updates, and functionality to support security operations.
Security Documentation: Document security incidents, investigations, findings, and remediation activities in detailed incident reports, security policies, procedures, and documentation, maintaining accurate records for audit trail purposes and knowledge sharing.
Collaboration: Collaborate with cross-functional teams, including IT operations, software development, and business units, to integrate security controls into systems and processes, provide security guidance and support, and facilitate a holistic approach to cybersecurity risk management.
Continuous Improvement: Participate in security assessments, post-incident reviews, and lessons learned sessions to identify areas for improvement, implement security enhancements, and refine security practices and protocols to adapt to evolving threats and technologies.
Training and Development: Stay current with industry trends, advancements in cybersecurity technologies, and relevant certifications by participating in training programs, workshops, and professional development activities to enhance skills and knowledge in cybersecurity.
"""

#print(run_model(input_text, 'model', data_size='medium').to_json(orient='records'))