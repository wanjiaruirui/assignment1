import pandas as pd
'''
All clean steps depend on 'pandas'
'''

def clean(input1, input2, output):

    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)
    merged_file = pd.merge(df1, df2, left_on='respondent_id', right_on='id')        # Merge data

    merged_file.dropna(inplace=True)    # Drop missing values

    filter = ~merged_file['job'].str.contains('insurance|Insurance', case=False)    # Filter job values with 'insurance' and 'Insurance'
    cleaned_file = merged_file[filter]

    merged_file.drop('id', axis=1, inplace=True)    # Remove duplicated column

    cleaned_file = cleaned_file[['respondent_id', 'name', 'address', 'phone', 'job', 'company', 'birthdate']]   # Get column

    cleaned_file.reset_index(drop=True, inplace=True)   # Reset index

    cleaned_file.to_csv(output, index=False)    # Output


if __name__ == "__main__":
    input1 = r"respondent_contact.csv"
    input2 = r"respondent_other.csv"
    output = r"respondent_cleaned.csv"

    clean(input1, input2, output)   # Clean data

    output_file = pd.read_csv(output)
