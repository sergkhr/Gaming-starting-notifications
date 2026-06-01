from config.notifier_rules import NOTIFICATION_RULES


def determine_action(score: int) -> str:
    """
    Determine action for message based on score.

    Returns:
        ignore
        watch
        notify
    """

    matched_rules = []

    for rule in NOTIFICATION_RULES:

        if score >= rule.min_score:
            matched_rules.append(rule)

    if not matched_rules:
        return "ignore"

    best_rule = max(
        matched_rules,
        key=lambda rule: rule.min_score
    )

    return best_rule.action