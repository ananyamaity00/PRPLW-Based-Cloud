# Parameters with CSP-specific rankings
parameters = {
    1: {"name": "establishment", "weight": [1, 0.75, 0.5]},
    2: {"name": "infrastructure", "weight": [1, 0.75, 0.5]},
    3: {"name": "number_of_services", "weight": [1, 0.75, 0.5]},
    4: {"name": "utilization", "weight": [1, 0.75, 0.5]},
    5: {"name": "pricing_models_cost_efficiency", "weight": [0.75, 0.5, 1]},
    6: {"name": "storage_service_options", "weight": [1, 0.75, 0.5]},
    7: {"name": "service_response_time", "weight": [1, 1, 1]},
    8: {"name": "accountability", "weight": [1, 1, 1]},
    9: {"name": "availability", "weight": [1, 1, 1]},
    10: {"name": "cloud_tools", "weight": [1, 1, 1]},
    11: {"name": "archival_backup", "weight": [1, 0.75, 0.5]},
    12: {"name": "market_share", "weight": [1, 0.75, 0.5]},
    13: {"name": "growth_rate", "weight": [0.5, 0.75, 1]},
    14: {"name": "offline_data_transfer", "weight": [1, 0.75, 0.5]},
    15: {"name": "disaster_recovery", "weight": [1, 1, 0]},
    16: {"name": "sla_flexibility", "weight": [1, 1, 1]},
    17: {"name": "compatibility_microsoft_products", "weight": [0.75, 1, 0.5]},
    18: {"name": "reputation", "weight": [1, 0.75, 0.5]}
}

# Priority level weightage
priority_weights = {"PL1": 0.5, "PL2": 0.3, "PL3": 0.2}

# Priority level assignment
priority_levels = {
    "establishment": "PL3",
    "infrastructure": "PL1",
    "number_of_services": "PL1",
    "utilization": "PL2",
    "pricing_models_cost_efficiency": "PL1",
    "storage_service_options": "PL2",
    "service_response_time": "PL2",
    "accountability": "PL1",
    "availability": "PL1",
    "cloud_tools": "PL2",
    "archival_backup": "PL1",
    "market_share": "PL3",
    "growth_rate": "PL3",
    "offline_data_transfer": "PL2",
    "disaster_recovery": "PL2",
    "sla_flexibility": "PL1",
    "compatibility_microsoft_products": "PL2",
    "reputation": "PL3"
}


# ------------------- FUNCTIONS -------------------

def calculate_weighted_sum(selected_parameters, priority_levels, priority_weights):
    """Calculate weighted sum for AWS, Azure, GCP based on selected parameters"""
    csp_scores = {'AWS': 0, 'Azure': 0, 'GCP': 0}

    # Count how many parameters fall into each priority level
    n1 = sum(1 for num in selected_parameters if priority_levels[parameters[num]["name"]] == "PL1")
    n2 = sum(1 for num in selected_parameters if priority_levels[parameters[num]["name"]] == "PL2")
    n3 = sum(1 for num in selected_parameters if priority_levels[parameters[num]["name"]] == "PL3")

    for param_number in selected_parameters:
        param = parameters[param_number]["name"]
        ranks = parameters[param_number]["weight"]
        priority = priority_levels[param]
        weight = priority_weights[priority]

        # Avoid division by zero
        if priority == "PL1" and n1 > 0:
            csp_scores['AWS'] += (ranks[0] / n1) * weight
            csp_scores['Azure'] += (ranks[1] / n1) * weight
            csp_scores['GCP'] += (ranks[2] / n1) * weight
        elif priority == "PL2" and n2 > 0:
            csp_scores['AWS'] += (ranks[0] / n2) * weight
            csp_scores['Azure'] += (ranks[1] / n2) * weight
            csp_scores['GCP'] += (ranks[2] / n2) * weight
        elif priority == "PL3" and n3 > 0:
            csp_scores['AWS'] += (ranks[0] / n3) * weight
            csp_scores['Azure'] += (ranks[1] / n3) * weight
            csp_scores['GCP'] += (ranks[2] / n3) * weight

    return csp_scores


def rank_csps(csp_scores):
    """Rank CSPs in descending order"""
    return sorted(csp_scores.items(), key=lambda item: item[1], reverse=True)


def select_best_csp():
    """Main function to execute CSP selection"""
    print("📌 Available Parameters:")
    for num, param in parameters.items():
        print(f"{num}. {param['name']}")

    # Take user input
    selected_numbers = input("\nEnter parameter numbers (comma-separated): ").split(',')
    selected_parameters = [int(num.strip()) for num in selected_numbers if num.strip().isdigit()]

    print("\n✅ Selected Parameters and Their Rankings:")
    for num in selected_parameters:
        param_name = parameters[num]["name"]
        ranks = parameters[num]["weight"]
        print(f" - {param_name}")
        print(f"    AWS: {ranks[0]}, Azure: {ranks[1]}, GCP: {ranks[2]}")

    # Calculate scores
    csp_scores = calculate_weighted_sum(selected_parameters, priority_levels, priority_weights)
    ranked_csps = rank_csps(csp_scores)

    # Display results
    print("\n📊 Final CSP Scores:")
    for csp, score in csp_scores.items():
        print(f"   {csp}: {score:.4f}")

    print("\n🏆 Ranked CSPs:")
    for i, (csp, score) in enumerate(ranked_csps, start=1):
        print(f"   {i}. {csp} → {score:.4f}")

    print("\n👉 Best CSP based on your selection:", ranked_csps[0][0])


# ------------------- RUN -------------------
if __name__ == "__main__":
    select_best_csp()
