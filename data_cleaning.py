import pandas as pd 

def load_and_clean_data(health_file, life_file):
    health_df = pd.read_csv(r"C:\Users\user\Documents\Winter 2025\BA1501\2704Project\HealthExpenditure.csv", skiprows=4)
    life_df = pd.read_csv(r"C:\Users\user\Documents\Winter 2025\BA1501\2704Project\LifeExpectancy.csv", skiprows=4)
    
    # Standardize column names
    health_df.columns = health_df.columns.astype(str).str.strip()
    life_df.columns = life_df.columns.astype(str).str.strip()

    excluded_columns = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code']
    health_years = [col for col in health_df.columns if col not in excluded_columns]
    life_years = [col for col in life_df.columns if col not in excluded_columns]
    common_years = [year for year in health_years if year in life_years]

    # Sort and filter years if needed
    common_years = sorted([y for y in common_years if y.isdigit()], key=lambda y: int(y))

    all_years_data = []

    for year in common_years:
        try:
            health_temp = health_df[['Country Name', year]].rename(columns={year: 'HealthExpenditure'})
            life_temp = life_df[['Country Name', year]].rename(columns={year: 'LifeExpectancy'})

            merged = pd.merge(health_temp, life_temp, on='Country Name').dropna()
            merged['Year'] = int(year)
            all_years_data.append(merged)

        except KeyError as e:
            print(f"Skipping year {year} due to missing data: {e}")

    if all_years_data:
        return pd.concat(all_years_data, ignore_index=True)
    else:
        print("No common year data could be merged.")
        return pd.DataFrame()
