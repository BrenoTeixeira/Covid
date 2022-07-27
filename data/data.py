import os
import sqlite3
import pandas as pd

os.remove('COVID.db') if os.path.exists('COVID.db') else None

conn = sqlite3.connect('COVID.db')

type(conn)

CovidDeaths = pd.read_excel("covid_deaths.xlsx")
CovidVacc = pd.read_excel("covid_vac.xlsx")

CovidDeaths.to_sql('CovidDeaths', con=conn, index=False,
                   dtype={
                       'iso_code': 'VARCHAR(255)', 
                       'continent': 'VARCHAR(255)', 
                       'location': 'VARCHAR(255)', 
                       'date': 'DATETIME', 
                       'population': 'FLOAT',
                       'total_cases': 'FLOAT', 
                       'new_cases': 'FLOAT', 
                       'new_cases_smoothed': 'FLOAT', 
                       'total_deaths': 'FLOAT',
                       'new_deaths': 'FLOAT', 
                       'new_deaths_smoothed': 'FLOAT', 
                       'total_cases_per_million': 'FLOAT', 
                       'new_cases_per_million': 'FLOAT',
                       'new_cases_smoothed_per_million': 'FLOAT', 
                       'total_deaths_per_million': 'FLOAT', 
                       'new_deaths_per_million': 'FLOAT', 
                       'new_deaths_smoothed_per_million': 'FLOAT', 
                       'reproduction_rate': 'FLOAT', 
                       'icu_patients': 'FLOAT',
                       'icu_patients_per_million': 'FLOAT', 
                       'hosp_patients': 'FLOAT',
                       'hosp_patients_per_million': 'FLOAT', 
                       'weekly_icu_admissions': 'FLOAT',
                       'weekly_icu_admissions_per_million': 'FLOAT', 
                       'weekly_hosp_admissions': 'FLOAT',
                       'weekly_hosp_admissions_per_million': 'FLOAT'
                   })

CovidVacc.to_sql("CovidVac", con=conn, index=False,
                dtype={
                       'iso_code': 'VARCHAR(255)', 
                       'continent': 'VARCHAR(255)', 
                       'location': 'VARCHAR(255)', 
                       'date': 'DATETIME', 
                       'total_tests': 'FLOAT', 
                       'new_tests': 'FLOAT',
                       'total_tests_per_thousand': 'FLOAT', 
                       'new_tests_per_thousand': 'FLOAT',
                       'new_tests_smoothed': 'FLOAT', 
                       'new_tests_smoothed_per_thousand': 'FLOAT',
                       'positive_rate': 'FLOAT', 
                       'tests_per_case': 'FLOAT', 
                       'tests_units': 'VARCHAR(255)', 
                       'total_vaccinations': 'FLOAT',
                       'people_vaccinated': 'FLOAT', 
                       'people_fully_vaccinated': 'FLOAT', 
                       'total_boosters': 'FLOAT',
                       'new_vaccinations': 'FLOAT', 
                       'new_vaccinations_smoothed': 'FLOAT',
                       'total_vaccinations_per_hundred': 'FLOAT', 
                       'people_vaccinated_per_hundred': 'FLOAT',
                       'people_fully_vaccinated_per_hundred': 'FLOAT', 
                       'total_boosters_per_hundred': 'FLOAT',
                       'new_vaccinations_smoothed_per_million': 'FLOAT',
                       'new_people_vaccinated_smoothed': 'FLOAT',
                       'new_people_vaccinated_smoothed_per_hundred': 'FLOAT', 
                       'stringency_index': 'FLOAT',
                       'population_density': 'FLOAT',
                       'median_age': 'FLOAT',
                       'aged_65_older': 'FLOAT',
                       'aged_70_older': 'FLOAT',
                       'gdp_per_capita': 'FLOAT',
                       'extreme_poverty': 'FLOAT',
                       'cardiovasc_death_rate': 'FLOAT',
                       'diabetes_prevalence': 'FLOAT',
                       'female_smokers': 'FLOAT', 
                       'male_smokers': 'FLOAT',
                       'handwashing_facilities': 'FLOAT',
                       'hospital_beds_per_thousand': 'FLOAT',
                       'life_expectancy': 'FLOAT', 
                       'human_development_index': 'FLOAT',
                       'excess_mortality_cumulative_absolute': 'FLOAT',
                       'excess_mortality_cumulative': 'FLOAT',
                       'excess_mortality': 'FLOAT', 
                       'excess_mortality_cumulative_per_million': 'FLOAT'
                })

conn.commit()

conn.close()