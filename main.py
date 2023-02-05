import json

def compare_json_files(file1, file2):
    # Load JSON files
    with open(file1, 'r') as f1:
        data1 = json.load(f1)
    with open(file2, 'r') as f2:
        data2 = json.load(f2)
    
    # Compare the data from both files
    missing_data = [line for line in data1 if line not in data2]
    
    # Print the missing lines
    if missing_data:
        print("The following lines are missing in file2 compared to file1:")
        for line in missing_data:
            print(line)
    else:
        print("No missing lines found.")
