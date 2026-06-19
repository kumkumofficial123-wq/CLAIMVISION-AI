def assess_risk(user_record):

    flags = []

    if user_record.get("past_claim_count", 0) > 5:
        flags.append("high_claim_frequency")

    if user_record.get("rejected_claim_count", 0) > 2:
        flags.append("multiple_rejections")

    if user_record.get("last_90_days_claim_count", 0) > 3:
        flags.append("recent_claim_activity")

    history_flag = str(user_record.get("history_flags", "")).lower()

    if history_flag != "none" and history_flag != "nan":
        flags.append(history_flag)

    return flags