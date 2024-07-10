import mosspy
from bs4 import BeautifulSoup
import requests
import os
import regex as re

# Reemplaza esto con tu ID de usuario MOSS
userid = "908437891"

# Crear una instancia de Moss con tu ID de usuario y el lenguaje C#
m = mosspy.Moss(userid, "csharp")

def getting_files_from_proy(proy_addr):
    project_files = []
    for root, _, files in os.walk(proy_addr):
        for file in files:
            if file.endswith(".cs"):
                file_path = os.path.join(root, file)
                print(file_path)
                project_files.append(file_path)
    return project_files

import time

def compare_files(file_a, file_b):
    m = mosspy.Moss(userid, "csharp")
    m.addBaseFile(file_a)
    m.addFile(file_b)
    
    max_attempts = 10  # Maximum number of attempts to send files
    attempt = 0
    while attempt < max_attempts:
        print(f'Requesting to compare {file_a} with file {file_b}')
        url = m.send()  # Sends the matches to the Moss service
        
        if url:  # If the response is not an empty string, exit the loop
            print(f'request succesfull {url}')
            break
        else:
            attempt += 1
            print(f"Attempt {attempt} failed. Retrying in 60 seconds...")
            time.sleep(60)  # Wait for 60 seconds before retrying
            
    return url

def get_similarity_for_files(file_a, file_b):
    url = compare_files(file_a, file_b)
    # response = requests.get(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Assuming the similarity score is in the first table cell
    similarity_row_0 = soup.find('table').find('tr').find('td')
    if not similarity_row_0:
        print(f'comparing {file_a} with {file_b} resulted in no similarity')
        return 0
    similarity_row_1 = similarity_row_0.find('a').text
    similarity = re.findall(r'\(.*?\)', similarity_row_1)[0][1:-2]
    print(f'comparing {file_a} with {file_b} resulted in similarity {similarity}%')
    return float(similarity)

def compare_proyects(project_a, project_b):
    files_a = getting_files_from_proy(project_a)
    files_b = getting_files_from_proy(project_b)
    
    similarities = []
    for file_a in files_a:
        max_similarity = 0  # Initialize with a high value
        for file_b in files_b:
            similarity = get_similarity_for_files(file_a, file_b)
            max_similarity = max(max_similarity, similarity)
        similarities.append(max_similarity)
    
    mean_similarity = sum(similarities) / len(similarities) if similarities else 0
    return mean_similarity

def get_results(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Assuming the results are in table format, extract the relevant data
    results = []
    tables = soup.find_all('table')
    for table in tables:
        rows = table.find_all('tr')
        for row in rows[1:]:  # Skipping header row
            cols = row.find_all('td')
            results.append({
                'file_a': cols[0].text.strip(),
                'file_b': cols[1].text.strip(),
                'similarity': cols[2].text.strip()
            })
    return results

def process_results(results):
    for result in results:
        print(f"{result['file_a']} vs {result['file_b']}: Similarity - {result['similarity']}")

def dump_results(results):
    with open('moss_comparison_results.txt', 'w') as f:
        for result in results:
            f.write(f"{result['file_a']} vs {result['file_b']}: Similarity - {result['similarity']}\n")

def compare_all_projects():
    root_dir = os.getcwd() + "/Projects"
    project_types = os.listdir(root_dir)
    
    for i in range(len(project_types)):
        for j in range(i+1, len(project_types)):
            type_i_path = os.path.join(root_dir, project_types[i])
            type_j_path = os.path.join(root_dir, project_types[j])
            
            projects_i = os.listdir(type_i_path)
            projects_j = os.listdir(type_j_path)
            
            for project_a in projects_i:
                for project_b in projects_j:
                    proyect_a_path = os.path.join(type_i_path, project_a)
                    proyect_b_path = os.path.join(type_j_path, project_b)
                    
                    mean_similarity = compare_proyects(proyect_a_path, proyect_b_path)
                    print(f"Mean similarity between {project_a} and {project_b}: {mean_similarity}%")

if __name__ == "__main__":
    compare_all_projects()