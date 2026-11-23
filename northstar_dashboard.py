import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
# Load NorthStar performance data
DATA_FILE = Path(__file__).parent / "NorthStar_Performance_Intelligence_Dataset.xlsx"

df = pd.read_excel(DATA_FILE, sheet_name="Performance Data")
# Identify the team with the largest Week 8 service-level decline
baseline_by_team = (
    df[df["Week"].between(1, 7)]
    .groupby("Team")["Service Level"].mean()
)

week8_by_team = (
    df[df["Week"] == 8]
    .groupby("Team")["Service Level"].mean()
)

service_level_change_by_team = (
    week8_by_team - baseline_by_team
) * 100

worst_team = service_level_change_by_team.idxmin()
worst_team_decline = service_level_change_by_team.min()
baseline_data = df[df["Week"].between(1, 7)]
week8_data = df[df["Week"] == 8]

baseline_service_level = baseline_data["Service Level"].mean()
week8_service_level = week8_data["Service Level"].mean()

service_level_change_pp = (
    week8_service_level - baseline_service_level
) * 100

baseline_workload = (
    baseline_data["Contact Volume"].mean()
    / baseline_data["Available Staff"].mean()
)

week8_workload = (
    week8_data["Contact Volume"].mean()
    / week8_data["Available Staff"].mean()
)

workload_change_pct = (
    (week8_workload - baseline_workload)
    / baseline_workload
) * 100


# Configure the dashboard
st.set_page_config(
    page_title="NorthStar Performance Intelligence",
    page_icon="📊",
    layout="wide"
)

# Dashboard title
st.title("📊 NorthStar Performance Intelligence")

st.subheader("AI-Powered Contact Centre Performance Analytics")

st.markdown(
    "Monitor operational performance, investigate service-level "
    "declines, and generate evidence-based management insights."
)

st.divider()

# Dashboard navigation
st.sidebar.title("NorthStar Navigation")

page = st.sidebar.radio(
    "Select a section:",
    [
        "Executive Overview",
        "Team Performance",
        "AI Performance Insights"
    ]
)



# Display selected page
if page == "Executive Overview":
    st.header("Executive Performance Overview")
    col1, col2, col3 = st.columns(3)

    # Filter data for baseline and Week 8
    baseline_data = df[df["Week"].between(1, 7)]
    week8_data = df[df["Week"] == 8]

    # Calculate service level
    baseline_service_level = baseline_data["Service Level"].mean()
    week8_service_level = week8_data["Service Level"].mean()

    service_level_change = (
        week8_service_level - baseline_service_level
    ) * 100

    # Display service level KPI
    with col1:
        st.metric(
            label="Week 8 Service Level",
            value=f"{week8_service_level:.2%}",
            delta=f"{service_level_change:.2f} pp",
            delta_color="normal"
        )

    
    # Calculate contact volume
    baseline_volume = baseline_data["Contact Volume"].mean()
    week8_volume = week8_data["Contact Volume"].mean()

    volume_change = (
        (week8_volume - baseline_volume) / baseline_volume
    ) * 100


    # Display contact volume KPI
    with col2:
        st.metric(
            label="Week 8 Average Contact Volume",
            value=f"{week8_volume:,.0f}",
            delta=f"{volume_change:+.2f}%",
            delta_color="normal"
        )

    
    

    # Calculate available staffing
    baseline_staff = baseline_data["Available Staff"].mean()
    week8_staff = week8_data["Available Staff"].mean()
    staffing_change = (
        (week8_staff - baseline_staff) / baseline_staff
    ) * 100


    # Display available staffing KPI
    with col3:
        st.metric(
            label="Week 8 Average Available Staff",
            value=f"{week8_staff:.1f}",
            delta=f"{staffing_change:+.2f}%",
            delta_color="normal"
        )


    

    
    
elif page == "Team Performance":
    st.header("Team Performance Analysis")
    # Calculate Week 8 service level for each team
    team_service_level = df[df["Week"] == 8].groupby("Team")["Service Level"].mean()
    # Display Week 8 service level by team
    st.subheader("Week 8 Service Level by Team")
    st.bar_chart(team_service_level)
    # Calculate baseline service level for each team
    team_baseline = df[df["Week"].between(1, 7)].groupby("Team")["Service Level"].mean()
    # Calculate service level change in percentage points
    team_change = (team_service_level - team_baseline) * 100
    # Display service level change by team
    st.subheader("Service Level Change by Team (Percentage Points)")
    st.bar_chart(team_change)
    # Identify the team with the largest service level decline
    worst_team = team_change.idxmin()
    worst_decline = team_change.min()
    # Display the most affected team
    st.warning(f"{worst_team} experienced the largest service-level decline: {abs(worst_decline):.2f} percentage points.")

    # Calculate Week 8 absenteeism for each team
    team_absenteeism = df[df["Week"] == 8].groupby("Team")["Absenteeism Rate"].mean()

    # Calculate baseline absenteeism (Weeks 1-7)
    baseline_absenteeism = df[df["Week"].between(1, 7)].groupby("Team")["Absenteeism Rate"].mean()

    # Calculate absenteeism change in percentage points
    absenteeism_change = (team_absenteeism - baseline_absenteeism) * 100

    # Display Week 8 absenteeism by team
    st.subheader("Week 8 Absenteeism by Team")
    st.bar_chart(team_absenteeism)

    # Display absenteeism change by team
    st.subheader("Absenteeism Change by Team (Percentage Points)")
    st.bar_chart(absenteeism_change)

    # Identify the team with the largest absenteeism increase
    highest_absence_team = absenteeism_change.idxmax()
    highest_absence_increase = absenteeism_change.max()
    team_staffing = df[df["Week"] == 8].groupby("Team")["Available Staff"].mean()

    baseline_staffing = df[df["Week"].between(1, 7)].groupby("Team")["Available Staff"].mean()
    week8_staffing = df[df["Week"] == 8].groupby("Team")["Available Staff"].mean()

    staffing_change = ((team_staffing - baseline_staffing) / baseline_staffing) * 100
    # Compare service-level and absenteeism changes
    # Calculate Week 8 interaction complexity by team
    team_complexity = df[df["Week"] == 8].groupby("Team")["Interaction Complexity Index"].mean()

    # Calculate baseline interaction complexity (Weeks 1–7)
    baseline_complexity = df[df["Week"].between(1, 7)].groupby("Team")["Interaction Complexity Index"].mean()

    # Calculate interaction complexity percentage change by team
    complexity_change = ((team_complexity - baseline_complexity) / baseline_complexity) * 100

    # Calculate Week 8 average handle time by team

    team_aht = df[df["Week"] == 8].groupby("Team")["Average Handle Time (min)"].mean()

    baseline_aht = df[df["Week"].between(1, 7)].groupby("Team")["Average Handle Time (min)"].mean()

        # Calculate AHT percentage change by team
    aht_change = ((team_aht - baseline_aht) / baseline_aht) * 100

    # Identify teams with significant AHT increases
    high_aht_teams = aht_change[aht_change > 5]

    if not high_aht_teams.empty:
        st.warning(
            "AHT Alert: The following teams experienced "
            "an increase greater than 5%: "
            + ", ".join(high_aht_teams.index)
        )


    




    comparison = pd.DataFrame({
        "Service Level Change (pp)": team_change,
        "Absenteeism Change (pp)": absenteeism_change,
        "Staffing Change (%)": staffing_change,
        
        "Interaction Complexity Change (%)": complexity_change,
        "AHT Change (%)": aht_change

    })


    # Identify the team with the largest service-level decline
    # Calculate contact volume change by team
    baseline_volume = (
        df[df["Week"].between(1, 7)]
        .groupby("Team")["Contact Volume"].mean()
    )

    week8_volume = (
        df[df["Week"] == 8]
        .groupby("Team")["Contact Volume"].mean()
    )

    volume_change = (
        (week8_volume - baseline_volume) / baseline_volume
    ) * 100

    comparison["Contact Volume Change (%)"] = volume_change
    # Calculate contacts per available staff member by team
    baseline_workload = baseline_volume / baseline_staffing
    week8_workload = week8_volume / week8_staffing

    workload_change = (
        (week8_workload - baseline_workload) / baseline_workload
) * 100

    comparison["Workload Change (%)"] = workload_change


    st.subheader("Team Performance Driver Comparison")
    st.dataframe(comparison.round(2))
    st.warning(
        f"{highest_absence_team} experienced the largest absenteeism increase: "
        f"{highest_absence_increase:.2f} percentage points."
    )


    
         
    # Calculate Week 8 available staffing for each team
    
    # Display staffing percentage change by team
    st.subheader("Staffing Change by Team (%)")
    st.bar_chart(staffing_change)
    # Display interaction complexity change by team
    st.subheader("Interaction Complexity Change by Team (%)")
    st.bar_chart(complexity_change)
    # Display average handle time percentage change by team
    st.subheader("Average Handle Time Change by Team (%)")
    st.bar_chart(aht_change)

    


elif page == "AI Performance Insights":
    st.header("NorthStar AI Insights")
    st.subheader("Week 8 Performance Diagnosis")

    st.write(
        "NorthStar examines changes in service level, "
        "contact volume, staffing, and operational efficiency "
        "to identify potential performance drivers."
    )
    st.subheader("Key Performance Changes")

    st.write("Service Level: -13.85 percentage points")
    st.write("Contact Volume: +18.92%")
    st.write("Available Staffing: -9.90%")
    st.write(
    f"Contacts per Available Staff: +{workload_change_pct:.2f}%"
)
    st.subheader("Preliminary Performance Assessment")

    st.write(
        f"During Week 8, contact volume increased by 18.92% "
        f"while available staffing declined by 9.90%. "
        f"As a result, contacts per available staff member "
        f"increased by {workload_change_pct:.2f}%. "
        f"This increased workload pressure may have contributed "
        f"to the 13.85 percentage-point decline in service level. "
        f"Further investigation is required to assess other "
        f"potential contributing factors."
)



    st.subheader("Team-Level Performance Alert")

    st.warning(
        f"{worst_team} experienced the largest service-level decline "
        f"of {abs(worst_team_decline):.2f} percentage points "
        "during Week 8 compared with the baseline."
    )
    st.subheader("Management Recommendations")

    st.markdown("""
    **Priority 1 — Team E: Capacity and Service Recovery**

    Review peak-period staffing coverage and queue allocation.
    Investigate the combined impact of higher contact volume,
    reduced staffing, absenteeism, and longer handling times.

    **Priority 2 — Team B: Workload and Handling Efficiency**

    Review interaction types and the reasons for increased
    average handle time. Identify opportunities for targeted
    coaching, knowledge support, and workload redistribution.

    **Priority 3 — Team C: Operational Investigation**

    Investigate schedule adherence, contact arrival patterns,
    and potential workflow bottlenecks to understand why
    service level deteriorated significantly.

    **Management Note:** These recommendations are based on
    observed operational changes. Further investigation is
    required before confirming root causes.
    """)


        
