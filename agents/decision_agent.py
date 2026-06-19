def make_decision(claim_info, evidence_result, risk_flags):

    if not evidence_result["evidence_standard_met"]:

        return {
            "claim_status": "insufficient_information",
            "severity": "unknown",
            "justification": evidence_result["reason"]
        }

    if len(risk_flags) > 0:

        return {
            "claim_status": "manual_review",
            "severity": "medium",
            "justification": "Risk flags detected: " + ", ".join(risk_flags)
        }

    return {
        "claim_status": "supported",
        "severity": "low",
        "justification": "Claim description and evidence requirements are satisfied."
    }