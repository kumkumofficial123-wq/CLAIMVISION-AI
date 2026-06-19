ClaimVision AI - Multi-Agent Insurance Claim Processing System
Overview

ClaimVision AI is a multi-agent AI system designed to automate insurance claim processing. The system analyzes customer claim conversations, evaluates supporting evidence, assesses user risk history, and generates claim decisions through a coordinated agent workflow.

The project demonstrates how multiple specialized AI agents can collaborate to process claims efficiently and produce structured outputs for insurance workflows.

Features
Claim Agent
Extracts claim information from customer conversations
Identifies claim object
Detects issue type
Identifies affected object part
Evidence Agent
Evaluates submitted evidence against claim requirements
Determines whether evidence standards are met
Generates evidence validation reasoning
Risk Agent
Analyzes historical user claim behavior
Flags potential risk indicators
Assesses claim risk level
Decision Agent
Combines claim, evidence, and risk analysis
Generates final claim decision
Produces justification and severity assessment
Orchestrator
Coordinates all agents
Manages workflow execution
Produces final structured output
Project Structure
ClaimVision-AI/
│
├── agents/
│   ├── claim_agent.py
│   ├── evidence_agent.py
│   ├── risk_agent.py
│   ├── decision_agent.py
│   └── orchestrator.py
│
├── dataset/
│   ├── claims.csv
│   ├── user_history.csv
│   ├── evidence_requirements.csv
│   └── output.csv
│
├── outputs/
│   └── final_output.csv
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
Workflow
Customer Claim
       │
       ▼
Claim Agent
       │
       ▼
Evidence Agent
       │
       ▼
Risk Agent
       │
       ▼
Decision Agent
       │
       ▼
Final Output Generation
Input Data
claims.csv

Contains:

User ID
Customer conversation
Claim object
Image paths
user_history.csv

Contains:

Previous claim history
Risk indicators
Historical claim summaries
evidence_requirements.csv

Contains:

Evidence requirements
Minimum image requirements
Applicable claim categories
Output Schema

The system generates:

user_id
image_paths
user_claim
claim_object
evidence_standard_met
evidence_standard_met_reason
risk_flags
issue_type
object_part
claim_status
claim_status_justification
supporting_image_ids
valid_image
severity
Installation

Clone the repository:

git clone https://github.com/kumkumofficial123-wq/CLAIMVISION-AI.git

Navigate to project folder:

cd CLAIMVISION-AI

Create virtual environment:

python -m venv venv

Activate environment:

Windows
venv\Scripts\activate
Linux/Mac
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
Running the Project

Execute:

python main.py

Output will be generated at:

outputs/final_output.csv
Sample Output
user_id	claim_object	claim_status	severity
user_001	car	Approved	Low
user_005	car	Manual Review	Medium
user_011	car	Approved	High
Technologies Used
Python
Pandas
CSV Data Processing
Multi-Agent Architecture
Rule-Based Decision System
Future Improvements
Real image inspection using Computer Vision
Damage detection with YOLO/OpenCV
LLM-powered claim understanding
Fraud detection models
Confidence scoring
Streamlit dashboard
Advanced evidence validation
Author

Kumkum Singh

B.Tech CSE (AI Specialization)
Gautam Buddha University

GitHub:
Kumkum Official GitHub

License

This project is developed for educational purposes, hackathons, and AI workflow experimentation.
