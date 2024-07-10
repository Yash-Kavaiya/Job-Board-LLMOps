import requests
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Send a request to the Remotive API
url = "https://remotive.com/api/remote-jobs"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Step 2: Convert JSON data to DataFrame
    data = response.json()
    jobs = data['jobs']
    df = pd.DataFrame(jobs)
    pritn
    # Step 3: Display the DataFrame
    print(df.head())
    
    # Step 4: Save the DataFrame as a CSV file
    df.to_csv('remote_jobs.csv', index=False)
    
    # Optional: Plotting a simple graph (e.g., number of jobs per category)
    job_counts = df['category'].value_counts()
    job_counts.plot(kind='bar')
    plt.xlabel('Job Category')
    plt.ylabel('Number of Jobs')
    plt.title('Number of Remote Jobs per Category')
    plt.show()
else:
    print(f"Failed to retrieve data: {response.status_code}")
