# Execution Pipeline Workflow

The application executes a linear 4-step assembly line to process user requests:
# Step 1: Ingestion
- Prompts the user sequentially for 3 technical skills or preferences.
- Concatenates the inputs into a single active user profile string.

# Step 2: Scoring
- Loads `raw_skills.csv` into a Pandas DataFrame.
- Transforms the dataset into a TF-IDF vector matrix.
- Transforms the user profile string into the matching vector space.
- Computes Cosine Similarity scores between the user vector and all dataset role vectors.

# Step 3: Sorting
- Appends the resulting scores to the dataset.
- Sorts all candidate roles in descending numerical order based on match alignment.

# Step 4: Filtering
- Truncates the array to extract only the Top-3 highest-scoring matches.
- Formats and displays the top job roles along with their percentage match scores.