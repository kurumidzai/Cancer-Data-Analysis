import pandas as pd

def analyze_cancer(data_file):
  # Load data from a CSV file using pandas
  data = pd.read_csv(data_file)

  # Calculate the mean and standard deviation of the different cancer characteristics
  mean = data.mean()
  std = data.std()

  # Display the results
  print("Means:")
  print(mean)
  print("Standard deviations:")
  print(std)

# Call the function and pass the name of the data file as an argument
analyze_cancer('cancer_data.csv')
