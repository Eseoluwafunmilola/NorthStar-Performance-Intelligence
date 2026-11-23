import pandas as pd
from openai import OpenAI

# NorthStar Performance Intelligence
# Step 1: Load the performance dataset

file_name = "NorthStar_Performance_Intelligence_Dataset.xlsx"

df = pd.read_excel(file_name, sheet_name="Performance Data")
print("EXCEL COLUMN NAMES:")
print(df.columns.tolist())

print("NORTHSTAR PERFORMANCE INTELLIGENCE")
print("----------------------------------")

print("\nDataset loaded successfully!")

print("\nNumber of records:", len(df))

print("\nNumber of columns:", len(df.columns))

print("\nTeams:")
print(df["Team"].unique())

print("\nFirst five records:")
print(df.head())


# Step 2: Compare baseline service level with Week 8

baseline = df[df["Week"].between(1, 7)]
week_8 = df[df["Week"] == 8]

baseline_sl = baseline["Service Level"].mean()
week_8_sl = week_8["Service Level"].mean()

change_pp = (week_8_sl - baseline_sl) * 100

print("\nSERVICE LEVEL ANALYSIS")
print("----------------------")
print(f"Baseline (Weeks 1-7): {baseline_sl:.2%}")
print(f"Week 8: {week_8_sl:.2%}")
print(f"Change: {change_pp:+.2f} percentage points")



# Step 2: Contact Volume Analysis

print("\nCONTACT VOLUME ANALYSIS")
print("-----------------------")

baseline_volume = df[df["Week"].between(1, 7)]["Contact Volume"].mean()

week8_volume = df[df["Week"] == 8]["Contact Volume"].mean()

volume_change = (
    (week8_volume - baseline_volume)
    / baseline_volume
) * 100

print(f"Baseline average contact volume: {baseline_volume:,.2f}")
print(f"Week 8 average contact volume: {week8_volume:,.2f}")
print(f"Contact volume change: {volume_change:+.2f}%")



# Step 3: Available Staffing Analysis

print("\nAVAILABLE STAFFING ANALYSIS")
print("---------------------------")

baseline_staff = df[df["Week"].between(1, 7)]["Available Staff"].mean()

week8_staff = df[df["Week"] == 8]["Available Staff"].mean()

staff_change = (
    (week8_staff - baseline_staff)
    / baseline_staff
) * 100

print(f"Baseline average staffing: {baseline_staff:.2f}")
print(f"Week 8 average staffing: {week8_staff:.2f}")
print(f"Staffing change: {staff_change:+.2f}%")



# Step 4: Workload Pressure Analysis

print("\nWORKLOAD PRESSURE ANALYSIS")
print("--------------------------")

baseline_workload = baseline_volume / baseline_staff
week8_workload = week8_volume / week8_staff

workload_change = (
    (week8_workload - baseline_workload)
    / baseline_workload
) * 100

print(f"Baseline contacts per staff: {baseline_workload:.2f}")
print(f"Week 8 contacts per staff: {week8_workload:.2f}")
print(f"Workload increase: {workload_change:+.2f}%")



# Step 5: Automated Performance Interpretation

print("\nNORTHSTAR MANAGEMENT INSIGHTS")
print("-----------------------------")

if workload_change > 20 and staff_change < 0:
    print("ALERT: Significant workload pressure detected.")
    print("Contact demand increased while staffing declined.")
    print("This may be contributing to the service level decline.")

    print("\nRecommended investigation:")
    print("1. Review staffing capacity and scheduling.")
    print("2. Investigate the increase in contact volume.")
    print("3. Examine absenteeism and schedule adherence.")
    print("4. Assess wait times and abandonment rates.")

else:
    print("No major combined workload and staffing alert.")
    print("Further operational analysis is recommended.")



# Step 6: Absenteeism Analysis

print("\nABSENTEEISM ANALYSIS")
print("--------------------")

baseline_absence = df[df["Week"].between(1, 7)]["Absenteeism Rate"].mean()

week8_absence = df[df["Week"] == 8]["Absenteeism Rate"].mean()

absence_change = (week8_absence - baseline_absence) * 100

print(f"Baseline absenteeism: {baseline_absence:.2%}")
print(f"Week 8 absenteeism: {week8_absence:.2%}")
print(f"Change: {absence_change:+.2f} percentage points")

if absence_change > 1:
    print("ALERT: Absenteeism increased significantly.")
    print("Investigate whether employee absences reduced staffing capacity.")
else:
    print("No significant increase in absenteeism detected.")



# Step 7: Schedule Adherence Analysis

print("\nSCHEDULE ADHERENCE ANALYSIS")
print("---------------------------")

baseline_adherence = df[df["Week"].between(1, 7)]["Schedule Adherence"].mean()

week8_adherence = df[df["Week"] == 8]["Schedule Adherence"].mean()

adherence_change = (
    week8_adherence - baseline_adherence
) * 100

print(f"Baseline adherence: {baseline_adherence:.2%}")
print(f"Week 8 adherence: {week8_adherence:.2%}")
print(f"Change: {adherence_change:+.2f} percentage points")

if adherence_change < -1:
    print("ALERT: Schedule adherence has declined.")
    print("Investigate whether reduced adherence affected staffing coverage.")
else:
    print("No major schedule adherence decline detected.")




# AVERAGE WAIT TIME ANALYSIS

baseline_wait = df[df["Week"] <= 7]["Average Wait Time (sec)"].mean()
week8_wait = df[df["Week"] == 8]["Average Wait Time (sec)"].mean()

wait_change = ((week8_wait - baseline_wait) / baseline_wait) * 100

print("\nAVERAGE WAIT TIME ANALYSIS")
print("--------------------------")
print(f"Baseline average wait time: {baseline_wait:.2f} seconds")
print(f"Week 8 average wait time: {week8_wait:.2f} seconds")
print(f"Wait time increase: {wait_change:+.2f}%")

if wait_change > 20:
    print("ALERT: Customer wait times increased substantially.")
    print("Investigate whether workload pressure and staffing gaps contributed.")



# ABANDONMENT RATE ANALYSIS

baseline_abandonment = df[df["Week"] <= 7]["Abandonment Rate"].mean()
week8_abandonment = df[df["Week"] == 8]["Abandonment Rate"].mean()

abandonment_change = (week8_abandonment - baseline_abandonment) * 100

print("\nABANDONMENT RATE ANALYSIS")
print("-------------------------")
print(f"Baseline abandonment rate: {baseline_abandonment:.2%}")
print(f"Week 8 abandonment rate: {week8_abandonment:.2%}")
print(f"Change: {abandonment_change:+.2f} percentage points")

if abandonment_change > 2:
    print("ALERT: Call abandonment has increased substantially.")
    print("Investigate whether longer wait times contributed to customers abandoning calls.")


# TEAM-LEVEL SERVICE LEVEL ANALYSIS

print("\nTEAM-LEVEL SERVICE LEVEL ANALYSIS")
print("--------------------------------")

for team in sorted(df["Team"].unique()):

    team_data = df[df["Team"] == team]

    baseline = team_data[team_data["Week"] <= 7]["Service Level"].mean()

    week8 = team_data[team_data["Week"] == 8]["Service Level"].mean()

    change = (week8 - baseline) * 100

    print(f"\n{team}")
    print(f"Baseline service level: {baseline:.2%}")
    print(f"Week 8 service level: {week8:.2%}")
    print(f"Change: {change:+.2f} percentage points")

    if change < -5:
        print("ALERT: Significant service level deterioration detected.")


# TEAM-LEVEL ABSENTEEISM ANALYSIS

print("\nTEAM-LEVEL ABSENTEEISM ANALYSIS")
print("--------------------------------")

for team in sorted(df["Team"].unique()):

    team_data = df[df["Team"] == team]

    baseline = team_data[
        team_data["Week"] <= 7
    ]["Absenteeism Rate"].mean()

    week8 = team_data[
        team_data["Week"] == 8
    ]["Absenteeism Rate"].mean()

    change = (week8 - baseline) * 100

    print(f"\n{team}")
    print(f"Baseline absenteeism: {baseline:.2%}")
    print(f"Week 8 absenteeism: {week8:.2%}")
    print(f"Change: {change:+.2f} percentage points")


# TEAM-LEVEL WORKLOAD ANALYSIS

print("\nTEAM-LEVEL WORKLOAD ANALYSIS")
print("--------------------------------")

for team in df["Team"].unique():

    team_data = df[df["Team"] == team]

    baseline = team_data[team_data["Week"] <= 7]
    week8 = team_data[team_data["Week"] == 8]

    # Calculate average workload for Weeks 1-7
    baseline_volume = baseline["Contact Volume"].mean()
    baseline_staff = baseline["Available Staff"].mean()

    baseline_workload = baseline_volume / baseline_staff

    # Calculate workload for Week 8
    week8_volume = week8["Contact Volume"].mean()
    week8_staff = week8["Available Staff"].mean()

    week8_workload = week8_volume / week8_staff

    # Calculate percentage change
    workload_change = (
        (week8_workload - baseline_workload)
        / baseline_workload
    ) * 100

    print(f"\n{team}")
    print(f"Baseline contacts per staff: {baseline_workload:.2f}")
    print(f"Week 8 contacts per staff: {week8_workload:.2f}")
    print(f"Workload change: {workload_change:+.2f}%")

    if workload_change > 20:
        print("ALERT: Significant increase in workload pressure.")
    elif workload_change > 0:
        print("NOTICE: Workload pressure increased.")
    else:
        print("Workload pressure did not increase.")


# TEAM-LEVEL SCHEDULE ADHERENCE ANALYSIS

print("\nTEAM-LEVEL SCHEDULE ADHERENCE ANALYSIS")
print("----------------------------------------")

for team in df["Team"].unique():

    team_data = df[df["Team"] == team]

    baseline = team_data[team_data["Week"] <= 7]
    week8 = team_data[team_data["Week"] == 8]

    # Calculate baseline schedule adherence
    baseline_adherence = baseline["Schedule Adherence"].mean()

    # Calculate Week 8 schedule adherence
    week8_adherence = week8["Schedule Adherence"].mean()

    # Calculate change in percentage points
    adherence_change = (
        week8_adherence - baseline_adherence
    ) * 100

    print(f"\n{team}")
    print(f"Baseline schedule adherence: {baseline_adherence:.2%}")
    print(f"Week 8 schedule adherence: {week8_adherence:.2%}")
    print(f"Change: {adherence_change:+.2f} percentage points")

    if adherence_change < -2:
        print("ALERT: Significant decline in schedule adherence.")
    elif adherence_change < 0:
        print("NOTICE: Schedule adherence declined.")
    else:
        print("Schedule adherence remained stable or improved.")

# TEAM-LEVEL AVERAGE HANDLE TIME ANALYSIS

print("\nTEAM-LEVEL AVERAGE HANDLE TIME ANALYSIS")
print("----------------------------------------")

for team in df["Team"].unique():

    team_data = df[df["Team"] == team]

    baseline = team_data[team_data["Week"] <= 7]
    week8 = team_data[team_data["Week"] == 8]

    baseline_aht = baseline["Average Handle Time (min)"].mean()
    week8_aht = week8["Average Handle Time (min)"].mean()

    aht_change = (
        (week8_aht - baseline_aht) / baseline_aht
    ) * 100

    print(f"\n{team}")
    print(f"Baseline AHT: {baseline_aht:.2f} minutes")
    print(f"Week 8 AHT: {week8_aht:.2f} minutes")
    print(f"AHT change: {aht_change:+.2f}%")

    if aht_change > 10:
        print("ALERT: Significant increase in handling time.")
    elif aht_change > 0:
        print("NOTICE: Average handling time increased.")
    else:
        print("Average handling time remained stable or decreased.")


# TEAM-LEVEL HANDLING DEMAND ANALYSIS

print("\nTEAM-LEVEL HANDLING DEMAND ANALYSIS")
print("----------------------------------------")

for team in df["Team"].unique():

    team_data = df[df["Team"] == team].copy()

    # Calculate handling demand per available employee
    team_data["Handling Demand per Staff"] = (
        team_data["Contact Volume"]
        * team_data["Average Handle Time (min)"]
        / team_data["Available Staff"]
    )

    # Separate baseline and Week 8
    baseline = team_data[team_data["Week"].between(1, 7)]
    week8 = team_data[team_data["Week"] == 8]

    # Calculate average handling demand
    baseline_demand = baseline["Handling Demand per Staff"].mean()
    week8_demand = week8["Handling Demand per Staff"].mean()

    # Calculate percentage change
    demand_change = (
        (week8_demand - baseline_demand)
        / baseline_demand
    ) * 100

    print(f"\n{team}")
    print(f"Baseline handling demand: {baseline_demand:.2f} minutes per staff")
    print(f"Week 8 handling demand: {week8_demand:.2f} minutes per staff")
    print(f"Handling demand change: {demand_change:+.2f}%")

    if demand_change > 30:
        print("ALERT: Severe increase in handling demand.")
    elif demand_change > 15:
        print("ALERT: Significant increase in handling demand.")
    elif demand_change > 0:
        print("NOTICE: Handling demand increased.")
    else:
        print("Handling demand remained stable or decreased.")


# TEAM-LEVEL INTERACTION COMPLEXITY ANALYSIS

print("\nTEAM-LEVEL INTERACTION COMPLEXITY ANALYSIS")
print("------------------------------------------")

for team in df["Team"].unique():

    team_data = df[df["Team"] == team]

    baseline = team_data[team_data["Week"] <= 7]
    week8 = team_data[team_data["Week"] == 8]

    baseline_complexity = baseline["Interaction Complexity Index"].mean()
    week8_complexity = week8["Interaction Complexity Index"].mean()

    complexity_change = (
        (week8_complexity - baseline_complexity)
        / baseline_complexity
    ) * 100

    print(f"\n{team}")
    print(f"Baseline interaction complexity: {baseline_complexity:.2f}")
    print(f"Week 8 interaction complexity: {week8_complexity:.2f}")
    print(f"Complexity change: {complexity_change:+.2f}%")

    if complexity_change > 5:
        print("ALERT: Significant increase in interaction complexity.")
    elif complexity_change > 0:
        print("NOTICE: Interaction complexity increased.")
    else:
        print("NOTICE: Interaction complexity remained stable or declined.")


# TEAM-LEVEL CUSTOMER WAIT TIME ANALYSIS

print("\nTEAM-LEVEL CUSTOMER WAIT TIME ANALYSIS")
print("--------------------------------------")

for team in df["Team"].unique():

    team_data = df[df["Team"] == team]

    baseline = team_data[team_data["Week"] <= 7]
    week8 = team_data[team_data["Week"] == 8]

    baseline_wait = baseline["Average Wait Time (sec)"].mean()
    week8_wait = week8["Average Wait Time (sec)"].mean()

    wait_change = (
        (week8_wait - baseline_wait) / baseline_wait
    ) * 100

    print(f"\n{team}")
    print(f"Baseline average wait time: {baseline_wait:.2f} seconds")
    print(f"Week 8 average wait time: {week8_wait:.2f} seconds")
    print(f"Wait time change: {wait_change:+.2f}%")

    if wait_change > 50:
        print("ALERT: Substantial increase in customer wait time.")
    elif wait_change > 0:
        print("NOTICE: Customer wait time increased.")
    else:
        print("NOTICE: Customer wait time remained stable or declined.")



# TEAM-LEVEL ABANDONMENT RATE ANALYSIS

print("\nTEAM-LEVEL ABANDONMENT RATE ANALYSIS")
print("------------------------------------")

for team in df["Team"].unique():

    team_data = df[df["Team"] == team]

    baseline = team_data[team_data["Week"] <= 7]
    week8 = team_data[team_data["Week"] == 8]

    baseline_rate = baseline["Abandonment Rate"].mean()
    week8_rate = week8["Abandonment Rate"].mean()

    change = (week8_rate - baseline_rate) * 100

    print(f"\n{team}")
    print(f"Baseline abandonment rate: {baseline_rate * 100:.2f}%")
    print(f"Week 8 abandonment rate: {week8_rate * 100:.2f}%")
    print(f"Change: {change:+.2f} percentage points")

    if change > 3:
        print("ALERT: Substantial increase in abandonment.")
    elif change > 0:
        print("NOTICE: Abandonment rate increased.")
    else:
        print("NOTICE: Abandonment remained stable or declined.")


# MULTI-FACTOR DIAGNOSTIC ENGINE

print("\nMULTI-FACTOR DIAGNOSTIC ANALYSIS")
print("--------------------------------")

diagnostic_results = []

for team in df["Team"].unique():

    team_data = df[df["Team"] == team]

    baseline = team_data[team_data["Week"] <= 7]
    week8 = team_data[team_data["Week"] == 8]

    # Workload pressure
    baseline_workload = (
        baseline["Contact Volume"].mean()
        / baseline["Available Staff"].mean()
    )

    week8_workload = (
        week8["Contact Volume"].mean()
        / week8["Available Staff"].mean()
    )

    workload_change = (
        (week8_workload / baseline_workload) - 1
    ) * 100

    # Absenteeism
    absenteeism_change = (
        week8["Absenteeism Rate"].mean()
        - baseline["Absenteeism Rate"].mean()
    ) * 100

    # Schedule adherence
    adherence_change = (
        week8["Schedule Adherence"].mean()
        - baseline["Schedule Adherence"].mean()
    ) * 100

    # Average handling time
    baseline_aht = baseline["Average Handle Time (min)"].mean()
    week8_aht = week8["Average Handle Time (min)"].mean()

    aht_change = (
        (week8_aht / baseline_aht) - 1
    ) * 100

    # Interaction complexity
    baseline_complexity = baseline[
        "Interaction Complexity Index"
    ].mean()

    week8_complexity = week8[
        "Interaction Complexity Index"
    ].mean()

    complexity_change = (
        (week8_complexity / baseline_complexity) - 1
    ) * 100

    diagnostic_results.append({
        "Team": team,
        "Workload Change (%)": round(workload_change, 2),
        "Absenteeism Change (pp)": round(absenteeism_change, 2),
        "Adherence Change (pp)": round(adherence_change, 2),
        "AHT Change (%)": round(aht_change, 2),
        "Complexity Change (%)": round(complexity_change, 2)
    })

diagnostic_df = pd.DataFrame(diagnostic_results)

print(diagnostic_df.to_string(index=False))



# NORTHSTAR DIAGNOSTIC REASONING ENGINE

print("\nNORTHSTAR DIAGNOSTIC REASONING ENGINE")
print("-------------------------------------")

for _, row in diagnostic_df.iterrows():

    team = row["Team"]

    workload = row["Workload Change (%)"]
    absenteeism = row["Absenteeism Change (pp)"]
    adherence = row["Adherence Change (pp)"]
    aht = row["AHT Change (%)"]
    complexity = row["Complexity Change (%)"]

    print(f"\n{team}")
    print("-" * 30)

    if workload > 20:
        print("OBSERVATION: Workload pressure increased substantially.")
        print("HYPOTHESIS: Demand may be exceeding available staffing capacity.")
        print("INVESTIGATION: Review contact forecasts, staffing levels and scheduling.")

    if absenteeism > 2:
        print("\nOBSERVATION: Absenteeism increased.")
        print("HYPOTHESIS: Employee absences may have reduced staffing availability.")
        print("INVESTIGATION: Review absence records and staffing coverage.")

    if adherence < -2:
        print("\nOBSERVATION: Schedule adherence deteriorated.")
        print("HYPOTHESIS: Reduced schedule adherence may have affected staffing coverage.")
        print("INVESTIGATION: Review adherence reports and employee availability.")

    if aht > 3 and complexity <= 0:
        print("\nOBSERVATION: AHT increased despite declining interaction complexity.")
        print("HYPOTHESIS: Knowledge gaps, system issues or process inefficiencies may be contributing.")
        print("INVESTIGATION: Review call recordings, hold times and system performance logs.")

    elif aht > 3 and complexity > 0:
        print("\nOBSERVATION: AHT and interaction complexity both increased.")
        print("HYPOTHESIS: More complex interactions may be contributing to longer handling times.")
        print("INVESTIGATION: Review interaction types, call recordings and advisor support needs.")

    print("\nCONFIDENCE: Hypotheses require further validation.")




print("\nNORTHSTAR MANAGEMENT RECOMMENDATIONS")
print("=" * 45)

for _, row in diagnostic_df.iterrows():

    team = row["Team"]
    workload = row["Workload Change (%)"]
    absenteeism = row["Absenteeism Change (pp)"]
    adherence = row["Adherence Change (pp)"]
    aht = row["AHT Change (%)"]
    complexity = row["Complexity Change (%)"]

    print(f"\n{team}")
    print("-" * 30)

    if workload > 20:
        print("PRIORITY: Review staffing capacity")
        print(f"OBSERVATION: Workload increased by {workload:.2f}%.")
        print("RECOMMENDATION: Review staffing schedules against peak demand.")
        print("VALIDATION: Compare hourly contact volume and staffing coverage.")

    if absenteeism > 2:
        print("\nPRIORITY: Investigate absenteeism")
        print(f"OBSERVATION: Absenteeism increased by {absenteeism:.2f} pp.")
        print("RECOMMENDATION: Review absence patterns and coverage plans.")
        print("VALIDATION: Examine absence records and available staffing.")

    if adherence < -2:
        print("\nPRIORITY: Investigate schedule adherence")
        print(f"OBSERVATION: Adherence changed by {adherence:.2f} pp.")
        print("RECOMMENDATION: Review schedule compliance and coverage gaps.")
        print("VALIDATION: Examine adherence reports by time interval.")

    if aht > 3:
        print("\nPRIORITY: Investigate handling efficiency")
        print(f"OBSERVATION: AHT increased by {aht:.2f}%.")
        if complexity > 0:
            print("HYPOTHESIS: More complex calls may be contributing.")
        else:
            print("HYPOTHESIS: Process, knowledge or system issues may be contributing.")
        print("VALIDATION: Review call recordings and system performance.")

    print("\nCONFIDENCE: Preliminary; further evidence required.")



print("\nNORTHSTAR INVESTIGATION PRIORITIZATION")
print("=" * 45)

for _, row in diagnostic_df.iterrows():

    team = row["Team"]
    workload = row["Workload Change (%)"]

    print(f"\n{team}")

    if workload > 20:
        print("PRIORITY LEVEL: HIGH")
        print("PRIMARY INVESTIGATION: Staffing capacity")
        print(f"EVIDENCE: Workload per staff increased by {workload:.2f}%.")
        print("NEXT STEP: Compare contact demand with available staffing.")
    else:
        print("PRIORITY LEVEL: REVIEW REQUIRED")
        print("NEXT STEP: Examine other operational performance indicators.")




print("\nNORTHSTAR TEAM INVESTIGATION RANKING")
print("=" * 45)

# Automatically calculate service-level declines from Excel

service_level_declines = {}

for team in df["Team"].unique():

    team_data = df[df["Team"] == team]

    baseline = team_data[
        team_data["Week"] <= 7
    ]["Service Level"].mean()

    week_8 = team_data[
        team_data["Week"] == 8
    ]["Service Level"].mean()

    decline = (baseline - week_8) * 100

    service_level_declines[team] = round(decline, 2)


ranking_df = diagnostic_df[["Team", "Workload Change (%)"]].copy()

ranking_df["Service Level Decline (pp)"] = (
    ranking_df["Team"].map(service_level_declines)
)

# Normalize each metric relative to the largest observed change
ranking_df["Workload Score"] = (
    ranking_df["Workload Change (%)"] /
    ranking_df["Workload Change (%)"].max()
)

ranking_df["Service Level Score"] = (
    ranking_df["Service Level Decline (pp)"] /
    ranking_df["Service Level Decline (pp)"].max()
)

# Calculate average wait time increase for each team
wait_time_changes = {}

for team in df["Team"].unique():
    team_data = df[df["Team"] == team]

    baseline_wait = team_data[
        team_data["Week"] <= 7
    ]["Average Wait Time (sec)"].mean()

    week8_wait = team_data[
        team_data["Week"] == 8
    ]["Average Wait Time (sec)"].mean()

    wait_change = ((week8_wait / baseline_wait) - 1) * 100

    wait_time_changes[team] = round(wait_change, 2)

ranking_df["Wait Time Change (%)"] = (
    ranking_df["Team"].map(wait_time_changes)
)

# Normalize average wait time increase
ranking_df["Wait Time Score"] = (
    ranking_df["Wait Time Change (%)"] /
    ranking_df["Wait Time Change (%)"].max()
)

# Sensitivity analysis: compare different management priorities
weight_scenarios = {
    "Equal Weighting": (1/3, 1/3, 1/3),
    "Service Level Focus": (0.60, 0.20, 0.20),
    "Workload Focus": (0.20, 0.60, 0.20),
    "Wait Time Focus": (0.20, 0.20, 0.60)
}

for scenario, weights in weight_scenarios.items():
    ranking_df[scenario] = (
        ranking_df["Service Level Score"] * weights[0] +
        ranking_df["Workload Score"] * weights[1] +
        ranking_df["Wait Time Score"] * weights[2]
    )

# Preserve the original equal-weight ranking
ranking_df["Priority Score"] = ranking_df["Equal Weighting"]

print("\nSENSITIVITY ANALYSIS RESULTS")

for scenario in weight_scenarios:
    scenario_ranking = ranking_df.sort_values(
        scenario, ascending=False
    )
    print(f"\n{scenario}:")
    print(
        scenario_ranking[["Team", scenario]]
        .round(3)
        .to_string(index=False)
    )


ranking_df = ranking_df.sort_values(
    "Priority Score", ascending=False
)

print(
    ranking_df[
        ["Team", "Service Level Decline (pp)",
         "Workload Change (%)", "Priority Score"]
    ].to_string(index=False)
)

print("\nFIRST TEAM TO INVESTIGATE:")
print(ranking_df.iloc[0]["Team"])


# Export NorthStar team investigation report
ranking_df.to_csv(
    "NorthStar_Management_Report.csv",
    index=False
)

print("\nManagement report exported successfully!")


# Prepare NorthStar findings for AI interpretation
top_team = ranking_df.iloc[0]["Team"]

analysis_summary = ranking_df[
    [
        "Team",
        "Service Level Decline (pp)",
        "Workload Change (%)",
        "Wait Time Change (%)",
        "Priority Score"
    ]
].to_string(index=False)

analysis_summary += "\n\nAdditional Team-Level Performance Drivers:\n"
analysis_summary += ranking_df.round(2).to_string(index=False)


print("\nNorthStar AI analysis prepared for:", top_team)



# Generate AI-powered management analysis
client = OpenAI()

prompt = f"""
You are NorthStar, an AI-powered contact centre
performance intelligence assistant.

Analyze the following team performance results:

{analysis_summary}

The highest-priority team is {top_team}.

Provide:
1. An executive summary of the performance concerns.
2. The main performance indicators requiring investigation.
3. Three practical management recommendations.
4. Additional data needed to confirm the root causes.

Important:
- Use only the supplied performance figures.
- Distinguish observed evidence from possible explanations.
- Do not claim that correlation proves causation.
- Keep your response professional and concise.
"""

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print("\nNORTHSTAR AI MANAGEMENT ANALYSIS")
print("=" * 45)
print(response.output_text)


print(response.output_text)


# NORTHSTAR INTERACTIVE AI ASSISTANT

print("\n" + "=" * 50)
print("WELCOME TO NORTHSTAR PERFORMANCE INTELLIGENCE")
print("Ask questions about your contact centre performance.")
print("Type 'exit' to end the conversation.")
print("=" * 50)

conversation = [
    {
        "role": "developer",
        "content": f"""
You are NorthStar Performance Intelligence,
an AI-powered contact centre performance assistant.

Use the following calculated performance data
to answer management questions:

{analysis_summary}

Highest-priority team: {top_team}

Rules:
1. Base numerical claims on the supplied data.
2. Explain performance changes in business language.
3. Distinguish evidence from possible causes.
4. Do not invent performance figures.
5. Recommend practical management actions.
6. Identify additional data needed when appropriate.
7. Keep answers clear, professional, and concise.
8. Check the supplied performance data before requesting additional information.
9. Clearly distinguish available data from missing data.
10. When evaluating management assumptions, compare evidence across teams.
11. Do not present possible causes as confirmed root causes.
"""
    }
]

while True:

    question = input("\nAsk NorthStar a question: ").strip()

    if question.lower() == "exit":
        print("\nThank you for using NorthStar!")
        break

    if not question:
        continue

    conversation.append({
        "role": "user",
        "content": question
    })

    try:
        ai_response = client.responses.create(
            model="gpt-4.1-mini",
            input=conversation
        )

        answer = ai_response.output_text

        print("\nNORTHSTAR:")
        print(answer)

        conversation.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as error:
        conversation.pop()
        print("\nUnable to complete the request:", error)







