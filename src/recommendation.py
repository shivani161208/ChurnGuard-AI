def generate_recommendation(
    customer,
    churn_probability
):

    recommendations = []

    # Risk
    if churn_probability >= 0.70:
        risk = "High Risk"

    elif churn_probability >= 0.40:
        risk = "Medium Risk"

    else:
        risk = "Low Risk"

    # Contract
    if customer.get(
        "Contract"
    ) == "Month-to-month":

        recommendations.append(
            "Offer a long-term contract "
            "with a suitable incentive."
        )

    # Payment
    if customer.get(
        "PaymentMethod"
    ) == "Electronic check":

        recommendations.append(
            "Encourage automatic payment "
            "methods."
        )

    # Internet
    if customer.get(
        "InternetService"
    ) == "Fiber optic":

        recommendations.append(
            "Review internet service "
            "satisfaction and offer suitable support."
        )

    # New customer
    if customer.get(
        "tenure", 0
    ) <= 12:

        recommendations.append(
            "Provide an early-tenure "
            "retention offer."
        )

    # Tech support
    if customer.get(
        "TechSupport"
    ) == "No":

        recommendations.append(
            "Offer technical support assistance."
        )

    # Default
    if not recommendations:

        recommendations.append(
            "Continue regular customer engagement."
        )

    return {
        "risk_level": risk,
        "recommendations": recommendations
    }