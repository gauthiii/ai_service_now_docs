### View data insights

*Pages 15–15 of the source PDF*

View data insights

You can view data insights to see metrics for your generated data and data collections.

Before you begin Role required: sn_data_kit.admin

Procedure

1.Navigate to All > Now Assist Data Kit > Home.

2. Select the dataset or data collection that you want to see data insights for.

Select the tab. 3. Data insights

Data insight metrics for datasets

| Metric | Description |
| --- | --- |
| Data volume | This metric identifies rows with unusually low character count or significantly fewer words compared to the dataset average. |
| Semantic similarity to seed | This metric is LLM-based and measures how closely each record’s meaning matches a given reference (seed). |
| Data hygiene | This metric is LLM-based and checks that fields follow the correct types and formats. |
| Missing/Empty values | This metric identifies fields that are null, empty, or contain placeholder values without valid justification. |
| Temporal consistency | This metric is LLM-based and ensures that data remains logically correct over time. |


> **[Screenshot: Now Assist Data Kit – Data Insights Dashboard (page 16)]**
>
> A three-tab interface: "Output data" | **"Data insights"** (active, teal underline) | "Input settings".
>
> **"Dataset insights"** section header with sub-text: "Evaluates dataset quality using provided inputs and a range of metrics such as structural integrity, domain validity, and more."
>
> **Quality Score Gauge** (semi-circular speedometer):
> - Needle pointing to score **90** (near the top/green zone)
> - Arc colours: red (0–50 = Low) → yellow/orange (51–79 = Moderate) → green (80+ = High)
> - Large text: "Quality Score 90" and label: "Quality score: 90/100" with green badge "✓ Excellent, ready to use"
> - Legend: Low 0–50 (red) | Moderate 51–79 (yellow) | High 80+ (green)
>
> **5 metric cards** ("Select a metric to evaluate dataset quality"):
> 1. **Data volume** — "Identifies rows with unusually low character count or significantly fewer words compared to the dataset average." — Green badge: "⚠ No issues detected"
> 2. **Semantic similarity to seed** — "Semantic similarity to seed measures how closely each record's meaning matches a given reference (seed). View seed data" — Orange badge: "⚠ Issues detected in 10 records" + "View records →"
> 3. **Data hygiene** — "Fields should follow correct types and formats (e.g., valid emails, numbers)" — Green badge: "⚠ No issues detected"
> 4. **Missing/Empty values** — "Identifies fields that are null, empty, or contain placeholder values (e.g., N/A) without valid justification." — Green badge: "⚠ No issues detected"
> 5. **Temporal consistency** — "Temporal consistency ensures data remains logically correct over time." — Green badge: "⚠ No issues detected"
