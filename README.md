

# NorthStar Performance Intelligence

### AI-Powered Contact Centre Performance Analysis & Decision Support

NorthStar Performance Intelligence is a Python-based AI decision-support prototype designed to help operational leaders investigate service-level declines, identify potential performance drivers, and prioritize management interventions.

The project combines operational analytics, interactive visualization, and generative AI to support evidence-informed decisions.

## Business Problem

Contact centre leaders often face challenges understanding why service levels decline. Increased contact volumes, staffing shortages, absenteeism, and longer wait times can occur simultaneously, making it difficult to determine where management attention is most needed.

NorthStar explores how analytics and AI can help leaders investigate these challenges.

## Key Features

- **Performance Analysis:** Examines service levels, contact volumes, staffing, workload, and operational efficiency.
- **Team Prioritization:** Ranks teams for investigation using a weighted performance scoring model.
- **Sensitivity Analysis:** Tests how changing KPI weights affects management priorities.
- **AI-Powered Insights:** Uses OpenAI to interpret analytical findings and generate management recommendations.
- **Interactive Dashboard:** Visualizes operational performance through Streamlit.
- **Conversational Analysis:** Allows users to ask questions about operational performance.

## Technologies Used

- Python
- pandas
- Streamlit
- OpenAI API
- Microsoft Excel

## Example Analysis

Using simulated contact centre data, NorthStar identified:

- A 13.85-percentage-point decline in service level during Week 8.
- An 18.92% increase in contact volume.
- A 9.90% reduction in available staffing.
- A 31.98% increase in contacts per available staff member.

The model initially prioritized Team E for investigation.

However, when greater importance was assigned to customer wait-time increases, Team B became the highest-priority team.

This demonstrates how management objectives and model assumptions can influence operational decisions.

## How to Run

1. Download or clone this repository.
2. Install the required Python packages:

```bash
pip install pandas openpyxl streamlit openai
```

3. Configure your OpenAI API key as an environment variable.
4. Run the AI agent:

```bash
python northstar_agent.py
```

5. To launch the dashboard, run:

```bash
python -m streamlit run northstar_dashboard.py
```

## Data and Limitations

This project uses a synthetic dataset created for educational and portfolio purposes.

The findings are illustrative and do not represent actual organizational performance.

NorthStar identifies potential contributing factors and supports management investigation. Its analytical rankings and AI-generated recommendations should not be interpreted as proof of causation.

## Project Purpose

NorthStar was developed as a personal portfolio project combining professional experience in operational performance management with technical skills in business analytics, Python, and generative AI.

The objective is to demonstrate how data and AI can support more structured, evidence-informed operational decision-making.

---

**Developed by Ese Okposio**
