def extract_claim(text):

    text = text.lower()

    issue_keywords = [
        "scratch",
        "scratched",
        "dent",
        "dented",
        "crack",
        "cracked",
        "broken",
        "tear",
        "torn"
    ]

    part_keywords = [
        "door",
        "bumper",
        "hood",
        "mirror",
        "screen",
        "lid",
        "corner"
    ]

    issue_type = None
    object_part = None

    for issue in issue_keywords:
        if issue in text:
            issue_type = issue
            break

    for part in part_keywords:
        if part in text:
            object_part = part
            break

    return {
        "issue_type": issue_type,
        "object_part": object_part
    }