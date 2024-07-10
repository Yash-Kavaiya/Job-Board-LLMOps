from langchain_community.document_loaders.csv_loader import CSVLoader

loader = CSVLoader(file_path="Job-Board-LLMOps/Data/remote_jobs.csv")
data = loader.load()
print(data)