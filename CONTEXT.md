
# Project Context

## 1. Project Name
E-Commerce Cart Abandonment & Conversion Funnel Analytics

## 2. Business Problem
An e-commerce business experiences high shopping cart abandonment and low conversion rates. Management lacks clear visibility into customer journey drop-offs and cannot distinguish low-intent visitors from potentially valuable customers experiencing friction before purchase.

## 3. Project Objective
Analyze customer behavior and conversion patterns to identify measurable funnel drop-offs, understand cart abandonment, segment customers based on purchase history, and recommend data-driven conversion rate optimization (CRO) strategies.

## 4. Key Business Questions
- Where do customers drop off in the observed shopping journey?
- What proportion of sessions progress from product viewing to cart activity and purchase?
- How do conversion patterns vary by product category, price, and time?
- Which customer segments have higher observed purchase value and recency?
- Which customer cohorts show meaningful differences in conversion?
- What actions could improve conversion and customer recovery?

## 5. Technology Stack
- Database: PostgreSQL
- Programming: Python
- Data analysis: pandas, NumPy
- Visualization and EDA: Matplotlib, seaborn
- Statistical analysis: SciPy
- BI dashboard: Power BI
- Development: VS Code and Jupyter Notebook
- Version control: Git and GitHub
- API: To be confirmed; FastAPI is the proposed option.

## 6. Dataset
Planned source: Multi-Category E-Commerce Store Events / Behavior Dataset from Kaggle.

Dataset URL:
https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store

The exact downloaded files, date range, sampling strategy, and column availability must be verified before analysis.

## 7. Planned Analysis
- Data profiling and quality validation
- Data cleaning and exploratory data analysis
- Session-level conversion funnel analysis
- Cart abandonment measurement
- Product and category performance analysis
- Customer recency and monetary segmentation
- Cohort conversion analysis using chi-square tests where appropriate
- Power BI executive dashboard
- Evidence-based CRO recommendations

## 8. Important Metric Rules
- Define the session and observation window before calculating conversion.
- Distinguish event counts, session counts, customer counts, and order counts.
- Do not treat missing checkout events as observed checkout stages.
- Do not claim a specific abandonment cause without supporting evidence.
- Distinguish observed purchase-event value from verified revenue.
- Document assumptions, limitations, and validation results.

## 9. Git and Data Management Rules
- Keep raw source data unchanged.
- Do not commit large datasets, credentials, API keys, or environment files.
- Use meaningful Git commits for completed milestones.
- Document data transformations and analytical decisions.
- Validate analytical results before publishing them.

## 10. Expected Deliverables
- Reproducible SQL analysis
- Jupyter notebooks for cleaning, EDA, and statistical analysis
- Customer segmentation and funnel metrics
- Power BI dashboard
- Documentation, findings, and CRO recommendations
- GitHub repository with a clear project history

## 11. Current Status
- Project requirements reviewed.
- Repository setup: in progress.
- Context file: being created.
- Project structure: pending verification.
- API setup: pending confirmation of requirements.
- Dataset validation: pending.
