import os
from google.analytics.admin import AnalyticsAdminServiceClient
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest

def get_property_id():
    return "properties/537653433"

def main():
    property_name = get_property_id()
    if not property_name:
        print("No GA4 property found.")
        return

    print(f"Using Property: {property_name}")
    client = BetaAnalyticsDataClient()
    
    request = RunReportRequest(
        property=property_name,
        dimensions=[Dimension(name="date")],
        metrics=[Metric(name="screenPageViews"), Metric(name="activeUsers"), Metric(name="averageSessionDuration"), Metric(name="bounceRate")],
        date_ranges=[DateRange(start_date="2026-05-01", end_date="today")],
    )
    
    response = client.run_report(request)
    
    print("Date | Pageviews | Active Users | Avg Session Duration | Bounce Rate")
    for row in response.rows:
        print(f"{row.dimension_values[0].value} | {row.metric_values[0].value} | {row.metric_values[1].value} | {row.metric_values[2].value} | {row.metric_values[3].value}")

if __name__ == "__main__":
    main()
