def calculate_placement_score(
    cgpa,
    internships,
    projects,
    coding,
    communication,
    backlogs
):

    score = 0

    # CGPA
    if cgpa >= 8:
        score += 30
    elif cgpa >= 6:
        score += 20
    else:
        score += 10

    # Internships
    if internships >= 2:
        score += 25
    elif internships == 1:
        score += 15
    else:
        score += 5

    # Projects
    if projects >= 3:
        score += 20
    elif projects >= 1:
        score += 15
    else:
        score += 5

    # Coding
    if coding == "Advanced":
        score += 15
    elif coding == "Intermediate":
        score += 10
    else:
        score += 5

    # Communication
    if communication == "Excellent":
        score += 10
    elif communication == "Average":
        score += 7
    else:
        score += 3

    # Backlogs penalty
    if backlogs >= 3:
        score -= 10
    elif backlogs >= 1:
        score -= 5

    return max(score, 0)


def detect_risk(score):

    if score >= 75:
        return "Low Risk"
    elif score >= 50:
        return "Medium Risk"
    else:
        return "High Risk"


def generate_recommendations(
    cgpa,
    internships,
    projects,
    coding,
    communication,
    backlogs
):

    recommendations = []

    if cgpa < 6:
        recommendations.append(
            "Improve CGPA above 6.5."
        )

    if internships == 0:
        recommendations.append(
            "Complete at least 1 internship."
        )

    if projects < 2:
        recommendations.append(
            "Build 2–3 real-world projects."
        )

    if coding == "Beginner":
        recommendations.append(
            "Practice coding daily."
        )

    if communication == "Poor":
        recommendations.append(
            "Improve communication skills."
        )

    if backlogs > 0:
        recommendations.append(
            "Clear all backlogs."
        )

    if not recommendations:
        recommendations.append(
            "You are placement ready!"
        )

    return recommendations