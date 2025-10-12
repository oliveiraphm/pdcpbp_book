import random 

def simulate_data_usage():
    num_users = 500

    data_utilization_rates = [random.uniform(20, 90) for _ in range(num_users)]

    data_requests = [random.randint(1, 100) for _ in range(num_users)]

    organization_data_utilization_rate = sum(data_utilization_rates) / num_users

    total_data_requests = sum(data_requests)

    user_satisfaction_scores = [random.randint(1, 5) for _ in range(num_users)]

    avg_user_satisfaction_score = sum(user_satisfaction_scores) / num_users

    return {
        "data_utilization_rates": data_utilization_rates,
        "organization_data_utilization_rate": organization_data_utilization_rate,
        "data_requests": data_requests,
        "total_data_requests": total_data_requests,
        "user_satisfaction_scores": user_satisfaction_scores,
        "avg_user_satisfaction_score": avg_user_satisfaction_score,  
    }

data_usage_metrics = simulate_data_usage()

print("\nOrganization Data Utilization Rate:")
print(f"{data_usage_metrics['organization_data_utilization_rate']:.2f}%")
print("\nTotal Number of Data Requests or Queries:")
print(data_usage_metrics["total_data_requests"])
print("\nAverage User Satisfaction Score:")
print(f"{data_usage_metrics['avg_user_satisfaction_score']:.2f}")