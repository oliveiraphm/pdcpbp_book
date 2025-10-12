import random

def simulate_data_compliance(num_records):
    data_records = []
    compliant_count = 0

    for _ in range(num_records):
        age = random.randint(18, 100)
        consent_given = random.choice([True, False])

        age_rule = age >= 18
        consent_rule = age >= 18 and consent_given

        age_compliant = "Age Compliant" if age_rule else "Age Non-Compliant"
        consent_compliant = "Consent Compliant" if consent_rule else "Consent Non-Compliant"

        compliance_status = "Compliant" if age_rule and consent_rule else "Non-Compliant"

        if compliance_status == "Compliant":
            compliant_count += 1

        data_records.append({
            "Age": age,
            "Consent Given": consent_given,
            "Age Compliance": age_compliant,
            "Consent Compliance": consent_compliant,
            "Overall Compliance Status": compliance_status
        })

    percentage_compliant = (compliant_count / num_records) * 100

    return data_records, percentage_compliant

num_records = 100

data_records, percentage_compliant = simulate_data_compliance(num_records)

sample_size = 10
for record in data_records[:sample_size]:
    print(record)

print(f"\nPercentage of Compliant Records: {percentage_compliant:.2f}%")