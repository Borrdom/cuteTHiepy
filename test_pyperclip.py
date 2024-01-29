import pyperclip

# Create a list of lists
lst = [[1, 2], [3, 4], [5, 6]]

# Define headers for the columns
headers = ['Header1', 'Header2']

# Convert the list of lists to a string, with each row on a new line and tab-separated columns
lst_str = '\n'.join(['\t'.join(map(str, row)) for row in lst])

# Add headers to the top of the list string
lst_str = '\t'.join(headers) + '\n' + lst_str

# Copy the string to the clipboard
pyperclip.copy(lst_str)

# Now you can paste the list wherever you want, e.g., Excel