from openai import OpenAI
client = OpenAI(api_key='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')

import pandas as pd
import re
import csv
import time


# Define the path to your Excel file
file_path = 'prompts.xlsx'

# Define the starting and ending points for the loop
start_point = 0 # Index of the first prompt to process
end_point = 100 # Index of the last prompt to process (exclusive)

# Read the Excel file without a header
df = pd.read_excel(file_path, engine='openpyxl', header=None)

# Extract the prompts from the first column, starting from row 1
prompts = df[0].iloc[start_point:end_point].tolist()



# Initialize a counter for the iterations
iteration_counter = 0

# Record the start time of the loop
start_time = time.time()

# Loop through the prompts and process them
results = {"response" :[], "label":[], "reason":[]}
for prompt in prompts:
    iteration_start_time = time.time()
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant. which will help me to label the tweets for sentiment analysis"},
        {"role": "user", "content": prompt}
    ]
    )
    iteration_end_time = time.time()
    response = completion.choices[0].message.content
    
    label_pattern = r'Label:\s+"?([\w\s]+)"?'
    reason_pattern = r'Reason:\s+(.*)'

    # Find the label and reason using regex
    label_match = re.search(label_pattern, response)
    reason_match = re.search(reason_pattern, response)

    # Extract the label and reason
    label = label_match.group(1) if label_match else None
    reason = reason_match.group(1) if reason_match else None

    # Print the extracted label and reason
    # print(response)
    print(f"Label: {label}")
    # print(f"Reason: {reason}")
    results['response'].append(response)
    results['label'].append(label)
    results['reason'].append(reason)
    
    processing_time = iteration_end_time - iteration_start_time
    print(f"Processing time for iteration {iteration_counter}: {processing_time:.2f} seconds")
    
    # Increment the iteration counter
    iteration_counter += 1
    
    # Calculate the delay needed to achieve approximately 3 iterations per minute
    delay_seconds = 60 / 3 - (time.time() - start_time) % (60 / 3)
    if delay_seconds > 0:
        time.sleep(delay_seconds)
    

csv_file = "response_gpt.csv"
# Write data to CSV file
with open(csv_file, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=results.keys())
    # Write the header
    writer.writeheader()
    # Write the data rows
    for i in range(len(results["response"])):
        row = {key: results[key][i] for key in results}
        writer.writerow(row)


print(f"CSV file '{csv_file}' has been created successfully.")

