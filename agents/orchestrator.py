import pandas as pd

from agents.claim_agent import extract_claim
from agents.evidence_agent import validate_evidence
from agents.risk_agent import assess_risk
from agents.decision_agent import make_decision


def process_claim(claim_row, history_df, requirements_df):

    claim_info = extract_claim(
        str(claim_row["user_claim"])
    )

    user_history = history_df[
        history_df["user_id"] == claim_row["user_id"]
    ]

    if len(user_history) > 0:
        user_record = user_history.iloc[0].to_dict()
    else:
        user_record = {}

    risk_flags = assess_risk(user_record)

    evidence_result = validate_evidence(
        claim_info,
        requirements_df
    )

    decision = make_decision(
        claim_info,
        evidence_result,
        risk_flags
    )

    return {
        "user_id": claim_row["user_id"],
        "image_paths": claim_row["image_paths"],
        "user_claim": claim_row["user_claim"],
        "claim_object": claim_row["claim_object"],

        "evidence_standard_met":
            evidence_result["evidence_standard_met"],

        "evidence_standard_met_reason":
            evidence_result["reason"],

        "risk_flags":
            ";".join(risk_flags),

        "issue_type":
            claim_info["issue_type"],

        "object_part":
            claim_info["object_part"],

        "claim_status":
            decision["claim_status"],

        "claim_status_justification":
            decision["justification"],

        "supporting_image_ids":
            "",

        "valid_image":
            False,

        "severity":
            decision["severity"]
    }