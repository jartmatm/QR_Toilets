# Quayclean Toilets Data Processor

This project **filters, cleans, and organizes** restroom cleaning data from **Southern Cross Station**, preparing it for **Power BI** to generate valuable insights.

## Description
The script processes **Excel files exported from Office Forms** containing cleaning records for three specific areas:
- **Collins**
- **Luggage**
- **BIF**

The process includes:
- Removing unnecessary columns.
- Renaming columns based on a predefined standard.
- Cleaning cleaner names (keeping only the first name).
- Converting dates and assigning shifts (*Shift*).
- Filtering by a user-defined date range.
- Exporting the three datasets into **a single Excel file**, each on its own sheet.

This workflow ensures the data is ready for analysis in Power BI, where key metrics and visualizations are generated for decision-making.

---

## Process Flow

```mermaid
flowchart LR
    A[Office Forms Excel Export] --> B[Python Script]
    B --> C[Data Cleaning & Transformation]
    C --> D[Excel with Multiple Sheets]
    D --> E[Power BI Reports & Insights]


