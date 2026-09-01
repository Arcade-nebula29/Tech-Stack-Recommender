# Technical Architecture: Content-Based Filtering Engine

## 1. Mathematical Framework
The recommendation engine transforms qualitative skill terms into high-dimensional numerical vectors to evaluate angular alignment.

# TF-IDF Feature Extraction
- *Term Frequency (TF)*: Evaluates the occurrence frequency of a specific skill within a single job profile.
- *Inverse Document Frequency (IDF)*: Applies logarithmic dampening to penalize ubiquitous, generic terms while heavily weighting distinct, highly specific skills
  
# Cosine Similarity Engine
To ensure evaluation is invariant to description length or magnitude, closeness is measured via the cosine of the angle between the user preference vector and item profile vector.


- *Score 1.0*: Perfect alignment (identical skill direction).
- *Score 0.0*: Orthogonal vectors (zero overlapping skill features).

## 2. Cold Start Mitigation Strategy
To address the User Cold Start problem (where an empty user profile yields a zero-vector), the system enforces a mandatory 3-input ingestion rule before computing similarity scores.
