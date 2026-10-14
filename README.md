# Auto Job Search & Tracker 📊💼

An automated Python script that monitors Google Jobs via SerpApi for target roles (Data Analyst, Business Analyst, remote & part-time roles) across multiple locations, filters out duplicates, and logs new job leads directly into an Excel spreadsheet.

---

## Features

- **Multi-Query Automation:** Runs batch searches across targeted keywords (e.g., Junior, Associate, Part-Time, Remote in UK, Canada, Australia).
- **Google Jobs Engine:** Leverages SerpApi to aggregate listings directly from Google Jobs.
- **Deduplication:** Checks existing entries by job share link so already-logged jobs are never added twice.
- **Auto-Provisioning Spreadsheet:** Creates a structured `Job.xlsx` file automatically if one does not already exist.
- **Pipeline Tracking:** Pre-fills application metadata like `Status: Not Applied`, date added, source, and listing status ready for tracking.

---

## Tracked Columns

The generated Excel file contains the following fields:

| Column | Description |
| :--- | :--- |
| **Job Title** | Title of the position |
| **Company** | Hiring organization |
| **Location** | Listed location/remote designation |
| **Country** | Target country (if specified) |
| **Job Type** | Detected employment type (e.g., Part-Time) |
| **Posted** | When the listing was published |
| **Source** | Original platform (via LinkedIn, Indeed, etc.) |
| **Job Listed** | Availability flag (`Yes`) |
| **Job Link** | Direct share link to the job listing |
| **Date Added** | Timestamp when the script saved the entry |
| **Status** | Application status (defaults to `Not Applied`) |
| **Notes** | Free-form space for interview dates or referral info |

---

## Tech Stack

- **Python 3.8+**
- **Libraries:**
  - `google-search-results` (SerpApi wrapper)
  - `pandas`
  - `openpyxl` (Excel read/write support)

---

## Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/Ankit-AK-47/Auto-job-search.git](https://github.com/Ankit-AK-47/Auto-job-search.git)
cd Auto-job-search
