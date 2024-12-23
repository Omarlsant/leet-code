# 1693. Daily Leads and Partners
import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    # Group by 'date_id' and 'make_name'
    grouped = daily_sales.groupby(['date_id', 'make_name']).agg({
        'lead_id': pd.Series.nunique,
        'partner_id': pd.Series.nunique
    }).reset_index()
    # Rename the columns as required
    grouped.rename(columns={
        'lead_id': 'unique_leads',
        'partner_id': 'unique_partners'
    }, inplace=True)
    
    return grouped
