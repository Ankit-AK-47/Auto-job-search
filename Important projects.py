''' Practice code 2 = Automation of Job Search '''

from serpapi import GoogleSearch
import pandas as pd
import os
from datetime import datetime

# =====================================================
# ADD YOUR SERPAPI KEY HERE
# =====================================================
API_KEY = "Enter Your API"

# =====================================================
# Excel File
# =====================================================
EXCEL_FILE = r"C:\Users\Admin\Downloads\Job.xlsx"

# =====================================================
# Search Queries
# =====================================================
SEARCHES = [
    "Part Time Business Analyst ",
    "Part Time Data Analyst ",
    "Junior Business Analyst ",
    "Junior Data Analyst ",
    "Associate Business Analyst ",
    "Associate Data Analyst ",
    "Remote Business Analyst",
    "Remote Data Analyst",
    "Part Time Business Analyst UK",
    "Part Time Data Analyst UK",
    "Part Time Business Analyst Australia",
    "Part Time Data Analyst Australia",
    "Part Time Business Analyst Canada",
    "Part Time Data Analyst Canada"
]

columns = [
    "Job Title",
    "Company",
    "Location",
    "Country",
    "Job Type",
    "Posted",
    "Source",
    "Job Listed",
    "Job Link",
    "Date Added",
    "Status",
    "Notes"
]

# -----------------------------------------------------
# Create Excel if it doesn't exist
# -----------------------------------------------------
if not os.path.exists(EXCEL_FILE):
    pd.DataFrame(columns=columns).to_excel(EXCEL_FILE, index=False)

existing = pd.read_excel(EXCEL_FILE)

existing_links = set()

if "Job Link" in existing.columns:
    existing_links = set(
        existing["Job Link"].astype(str).str.strip()
    )

new_jobs = []

# =====================================================
# Search Loop
# =====================================================
for query in SEARCHES:

    print(f"Searching: {query}")

    params = {
        "engine": "google_jobs",
        "q": query,
        "hl": "en",
        "api_key": API_KEY
    }

    search = GoogleSearch(params)

    results = search.get_dict()

    jobs = results.get("jobs_results", [])

    for job in jobs:

        title = job.get("title", "")
        company = job.get("company_name", "")
        location = job.get("location", "")
        posted = job.get("detected_extensions", {}).get("posted_at", "")
        via = job.get("via", "")
        link = job.get("share_link", "")

        if link in existing_links:
            continue

        existing_links.add(link)

        new_jobs.append({
            "Job Title": title,
            "Company": company,
            "Location": location,
            "Country": "",
            "Job Type": "Part Time" if "part" in query.lower() else "",
            "Posted": posted,
            "Source": via,
            "Job Listed": "Yes",
            "Job Link": link,
            "Date Added": datetime.today().strftime("%Y-%m-%d"),
            "Status": "Not Applied",
            "Notes": ""
        })

# =====================================================
# Save
# =====================================================
if new_jobs:

    df = pd.DataFrame(new_jobs)

    final = pd.concat([existing, df], ignore_index=True)

    final.to_excel(EXCEL_FILE, index=False)

    print(f"\nAdded {len(new_jobs)} new jobs.")

else:
    print("\nNo new jobs found.")

print("-------------------------------------------------------------------------------------------------------")
