import pandas as pd

from agents.orchestrator import process_claim

claims = pd.read_csv("dataset/claims.csv")
history = pd.read_csv("dataset/user_history.csv")
requirements = pd.read_csv("dataset/evidence_requirements.csv")

results = []

for _, row in claims.iterrows():

    result = process_claim(
        row,
        history,
        requirements
    )

    results.append(result)

output_df = pd.DataFrame(results)

output_df.to_csv(
    "outputs/final_output.csv",
    index=False
)

print("Done!")
print("Saved: outputs/final_output.csv")