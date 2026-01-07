import pandas as pd
from datetime import datetime, timedelta
import random # Used for randomizing subject allocation when multiple are available

# ================================
# CONFIGURATION SECTION
# ================================

start_date = datetime(2025, 6, 11)
end_date = datetime(2026, 2, 5)

# Class timings (Wednesday & Friday)
wed_slots = ["12:50–1:30", "1:30–2:10", "2:10–3:00", "3:00–3:40"]
fri_slots = ["9:20–10:00", "10:00–10:40", "10:40–11:20", "11:20–12:00"]

# Faculty allocation rules
faculties = {
    "ANO L Sushma": "Common Subjects",
    "BHM P Anand Rao": "Special Subjects",
}

# CATC Camp dates (no classes)
catc_dates = [
    ("2025-08-12", "2025-08-23"),
    ("2025-10-15", "2025-10-26"),
    ("2025-12-02", "2025-12-13"),
    ("2026-01-27", "2026-02-07"),
]
catc_ranges = [(datetime.strptime(s, "%Y-%m-%d"), datetime.strptime(e, "%Y-%m-%d")) for s, e in catc_dates]

# Exam & holiday breaks
breaks = [
    ("Mid Exams (II & III Yr)", "2025-07-28", "2025-07-30"),
    ("Dussehra Holidays", "2025-09-29", "2025-10-05"),
    ("Mid 2 Exams", "2025-10-22", "2025-10-24"),
    ("No NCC (II & III Yr)", "2025-10-25", "2025-11-16"),
    ("Sankranti Holidays", "2026-01-11", "2026-01-15"),
]
break_ranges = [(desc, datetime.strptime(s, "%Y-%m-%d"), datetime.strptime(e, "%Y-%m-%d")) for desc, s, e in breaks]

# ================================
# DETAILED SUBJECT STRUCTURE
# Period structure: {Subject: [Y1_Periods, Y2_Periods, Y3_Periods], ...}
# For I+II Year, we combine Y1 and Y2 periods.
# NOTE: The provided syllabus data is used to calculate the Y1, Y2, Y3 totals.
# ================================

# COMMON SUBJECTS (L - Lecture, P - Practical, D - Demonstration, Di - Discussion)
common_subjects = {
    "NCC General (N)": {
        "N-1: Aims, Objectives & Organisation": [1, 0, 0],
        "N-2: Incentives": [2, 0, 0],
        "N-3: Duties of NCC Cadets": [1, 0, 0],
        "N-4: NCC Camps: Types & Conduct": [2, 0, 0],
    },
    "National Integration & Awareness (NI)": {
        "NI-1: Importance & Necessity": [2, 0, 0],
        "NI-2: Factors Affecting National Integration": [1, 0, 0],
        "NI-3: Unity in Diversity & Role of NCC": [2, 0, 0],
        "NI-4: Threat to National Security": [0, 2, 0],
    },
    "Drill (D)": {
        # Foot Drill
        "D-1 to D-4: Drill Ki Aam Hidayaten, Savdhan, etc.": [6, 0, 0],
        "D-5: Tej Chal - Tham Aur Dhire Chal - Tham": [3, 3, 0],
        "D-6 to D-10: Kadam Lena, Mudna, Salute Karna, Kadam Taal": [6, 6, 0],
        "D-11: Teeno Teen se Ek File & vice versa": [0, 3, 0],
        # Arms Drill
        "AD-1 to AD-5: Rifle ke Saath Drill": [6, 0, 0],
        "AD-6: Salami Shastra": [0, 3, 3],
        "AD-7: Squad Drill": [0, 0, 3],
        # Ceremonial Drill
        "CD-1: Guard Mounting": [0, 1, 2],
        "CD-2: Guard of Honour": [0, 1, 2],
    },
    "Weapon Training (WT)": {
        "WT-1: Intro & Characteristics of .22 Rifle": [3, 0, 0],
        "WT-2: Handling of .22 Rifle": [3, 0, 0],
        "WT-3: Range Procedure & Theory of Group": [1, 0, 0],
        "WT-4: Short Range Firing": [6, 6, 6],
    },
    "Personality Dev. and Leadership (P)": {
        "P-1: Personality Dev. Capsule": [2, 0, 0],
        "P-2: Communication Skills": [0, 3, 0],
        "P-3: Group Discussion & Civic Sense": [1, 6, 6],
        "P-4: Career Counseling, SSB": [0, 0, 3],
        "P-5: Public Speaking": [2, 2, 3],
    },
    "Leadership Development (LD)": {
        "LD-1: Leadership Capsule": [3, 0, 0],
        "LD-2: Case Studies (Shivaji, Kalam, etc.)": [0, 4, 5],
    },
    "Disaster Management (DM)": {
        "DM-1: DM Capsule & Role of NCC": [3, 0, 0],
        "DM-2: Fire Service & Fire Fighting": [0, 0, 1],
        "DM-3: Initiative Training, Organizing Skills": [3, 3, 3],
    },
    "Social Service and Community Dev. (SS)": {
        "SS-1: Social Service Capsule & Basics": [3, 0, 0],
        "SS-2: Swatch Bharat Abhiyan": [3, 3, 3],
        "SS-3: Social Service & Community Dev. Activities": [1, 12, 12],
        "SS-4: Protection of Children & Women Safety": [1, 1, 1],
        "SS-5: Road / Rail Travel Safety": [0, 1, 0],
        "SS-6: New Initiatives": [1, 1, 1],
        "SS-7: Cyber & Mobile Security Awareness": [1, 1, 1],
    },
    "Health and Hygiene (HH)": {
        "HH-1: Hygiene & Sanitation": [1, 0, 0],
        "HH-2: First Aid, Wounds": [3, 3, 0],
        "HH-3: Introduction to Yoga & Exercises": [1, 1, 1],
    },
    "Adventure (ADV)": {
        "ADV-1: Introduction to Adventure Activities": [1, 0, 0],
    },
    "Environmental Awareness & Conservation (E)": {
        "E-1: Environmental Awareness, Waste & Energy Cons.": [0, 0, 3],
    },
    "Obstacle Training (OT)": {
        "OT-1: Obstacle Course": [3, 3, 3],
    },
    "General Awareness (GA)": {
        "GA-1: General Knowledge": [0, 0, 2],
        "GA-2: Logical & Analytical Reasoning": [0, 0, 2],
    },
}

# SPECIAL SUBJECTS
special_subjects = {
    "Armed Forces (AF)": {
        "AF-1: Armed Forces, Army and CAPF": [3, 3, 0],
        "AF-2: Modes of Entry to Army, CAPF & Police": [0, 0, 3],
    },
    "Map Reading (MR)": {
        "MR-1: Introduction to Map Reading": [3, 0, 0],
        "MR-2: Conduct of MR, Google & Tourist Maps and Apps": [6, 9, 6],
    },
    "Field Craft and Battle Craft (FC & BC)": {
        "FC & BC-1: Introduction to Field Craft": [3, 0, 0],
        "FC & BC-2: Indication of Landmark": [2, 2, 2],
        "FC & BC-3: Observation, Camouflage and Concealment": [3, 3, 0],
        "FC & BC-4: Fire & Move Capsule": [0, 3, 3],
        "FC & BC-5: Knots, Lashings & Stretchers": [0, 0, 1],
    },
    "Intro to Infantry Weapons & Equipment (INF)": {
        "INF-1: Organisation of Infantry Battalion and its Weapons": [3, 2, 1],
    },
    "Military History (MH)": {
        "MH-1: Biographies of Renowned Generals": [3, 0, 3],
        "MH-2: War Heroes – PVC Awardees": [0, 3, 0],
        "MH-3: Study of Battles": [2, 2, 2],
        "MH-4: War Movies": [2, 3, 3],
    },
    "Communication (C)": {
        "C-1: Introduction to Communication & Latest Trends": [0, 0, 3],
        "C-2: Basic Communication Procedure": [1, 1, 1],
    },
}

# ================================
# SUBJECT ALLOCATION ENGINE
# ================================

class SubjectAllocator:
    def __init__(self, common_subjects, special_subjects):
        self.common_subjects = common_subjects
        self.special_subjects = special_subjects
        
        # Tracking consumed periods: [Y1, Y2, Y3]
        self.consumed = {
            'common': {
                sub_detail: [0, 0, 0] 
                for sub_group in common_subjects.values() 
                for sub_detail in sub_group
            },
            'special': {
                sub_detail: [0, 0, 0] 
                for sub_group in special_subjects.values() 
                for sub_detail in sub_group
            }
        }
    
    def get_remaining_periods(self, subject_type, year_index):
        """Calculates remaining periods for a given year index (0 for Y1, 1 for Y2, 2 for Y3)."""
        remaining = {}
        subjects = self.common_subjects if subject_type == 'common' else self.special_subjects
        
        for sub_group_name, sub_group in subjects.items():
            for sub_detail, periods in sub_group.items():
                
                # Use the relevant year index
                required = periods[year_index] 
                
                # For Y1+Y2 classes, the total class count is for both years. 
                # We assume the I+II Year class equally addresses the Y1 and Y2 syllabus for the combined subjects.
                # However, since the class is composed of Y1 and Y2 students together, we must track Y1 and Y2 separately.
                # For this schedule, we will only allocate based on remaining Y1 or Y2 periods, and allocate the class to the year with the requirement.
                
                # Check if there is a requirement for this year
                if required > 0:
                    consumed = self.consumed[subject_type][sub_detail][year_index]
                    remaining_count = required - consumed
                    
                    if remaining_count > 0:
                        full_name = f"{sub_detail} ({sub_group_name})"
                        remaining[full_name] = remaining_count
                        
        return remaining

    def get_next_subject(self, is_common_subject, is_i_ii_year):
        subject_type = 'common' if is_common_subject else 'special'
        
        # Prioritize which year's requirement to fulfill
        if is_i_ii_year:
            # For I + II Year: Alternately pick Y1 and Y2 requirements
            y1_remaining = self.get_remaining_periods(subject_type, 0)
            y2_remaining = self.get_remaining_periods(subject_type, 1)

            # Combine Y1 and Y2 topics, preferring Y1 if both are available to ensure freshers get priority
            available_topics = {}
            for topic, count in y1_remaining.items():
                available_topics[topic] = ('Y1', count)
            for topic, count in y2_remaining.items():
                if topic not in available_topics: # Prioritize Y1 topic if it's the same
                    available_topics[topic] = ('Y2', count)
            
            if not available_topics:
                return f"No {subject_type.capitalize()} Subject Remaining (I+II Year)"

            # Simple priority: Pick Y1 subjects until exhausted, then Y2 subjects.
            # Random selection for fairness among equally available subjects
            
            # Extract topics and their associated year index
            y1_topics = [topic for topic, (year, _) in available_topics.items() if year == 'Y1']
            y2_topics = [topic for topic, (year, _) in available_topics.items() if year == 'Y2']
            
            if y1_topics:
                selected_topic = random.choice(y1_topics)
                year_to_allocate = 0 # Y1 Index
                year_label = 'Y1'
            elif y2_topics:
                selected_topic = random.choice(y2_topics)
                year_to_allocate = 1 # Y2 Index
                year_label = 'Y2'
            else:
                return f"No {subject_type.capitalize()} Subject Remaining (I+II Year)"

            # Allocate and mark as consumed
            self.allocate_period(subject_type, selected_topic, year_to_allocate)
            return f"{selected_topic} ({year_label})"

        else:
            # For III Year: Only check Y3 requirements
            y3_remaining = self.get_remaining_periods(subject_type, 2)
            
            if not y3_remaining:
                return f"No {subject_type.capitalize()} Subject Remaining (III Year)"
            
            # Select randomly from available Y3 topics
            selected_topic = random.choice(list(y3_remaining.keys()))
            
            # Allocate and mark as consumed
            self.allocate_period(subject_type, selected_topic, 2)
            return f"{selected_topic} (Y3)"


    def allocate_period(self, subject_type, full_topic_name, year_index):
        """Marks a single period as consumed for a specific year."""
        
        # Extract the base subject detail (e.g., "NI-1: Importance & Necessity")
        topic_detail = full_topic_name.rsplit(' (', 1)[0]
        
        # Check if the topic exists in the consumed tracking structure
        if topic_detail in self.consumed[subject_type]:
            self.consumed[subject_type][topic_detail][year_index] += 1
        # else: This should not happen if topics are correctly extracted.

# Initialize the allocator
allocator = SubjectAllocator(common_subjects, special_subjects)


# ================================
# DATE GENERATION UTILITIES
# ================================

def date_in_breaks(date):
    """Check if date falls within any break or CATC"""
    for _, s, e in break_ranges:
        if s.date() <= date.date() <= e.date():
            return True
    for s, e in catc_ranges:
        if s.date() <= date.date() <= e.date():
            return True
    return False

def get_catc_name(date):
    """Get the name of the break or CATC for a specific date"""
    for s, e in catc_ranges:
        if s.date() <= date.date() <= e.date():
            return "CATC Camp"
    for desc, s, e in break_ranges:
        if s.date() <= date.date() <= e.date():
            return desc
    return None

# ================================
# MAIN SCHEDULE GENERATION
# ================================

schedule_rows = []
date = start_date
sno = 1
year_toggle = True  # True: I+II = Common, III = Special | False: I+II = Special, III = Common

while date <= end_date:
    if date.weekday() in [2, 4]:  # Wednesday (2) or Friday (4)
        
        # Check for a specific 'No NCC' break rule that only applies to a certain date range
        # The 'No NCC' break is already in break_ranges, so the general check is sufficient.
        
        if not date_in_breaks(date):
            # Create 4 periods
            slots = wed_slots if date.weekday() == 2 else fri_slots
            
            # Determine subject type for each year group based on the toggle
            if year_toggle:
                # I+II Year: Common (ANO Sushma) | III Year: Special (BHM Anand Rao)
                i_ii_subject = allocator.get_next_subject(is_common_subject=True, is_i_ii_year=True)
                iii_subject = allocator.get_next_subject(is_common_subject=False, is_i_ii_year=False)
                i_ii_topic_faculty = f"{i_ii_subject} (ANO L Sushma)"
                iii_topic_faculty = f"{iii_subject} (BHM P Anand Rao)"
            else:
                # I+II Year: Special (BHM Anand Rao) | III Year: Common (ANO Sushma)
                i_ii_subject = allocator.get_next_subject(is_common_subject=False, is_i_ii_year=True)
                iii_subject = allocator.get_next_subject(is_common_subject=True, is_i_ii_year=False)
                i_ii_topic_faculty = f"{i_ii_subject} (BHM P Anand Rao)"
                iii_topic_faculty = f"{iii_subject} (ANO L Sushma)"
                
            # Populate 4 periods with the same subjects for the day
            for slot in slots:
                schedule_rows.append([sno, date.strftime("%d-%b-%Y"), slot, i_ii_topic_faculty, iii_topic_faculty])
                sno += 1
                
            year_toggle = not year_toggle
            
        else:
            # If in CATC or break period
            reason = get_catc_name(date)
            slots = wed_slots if date.weekday() == 2 else fri_slots
            for slot in slots:
                schedule_rows.append([sno, date.strftime("%d-%b-%Y"), slot, reason, reason])
                sno += 1
                
    date += timedelta(days=1)

# ================================
# TABLE 1 – Schedule
# ================================
df_schedule = pd.DataFrame(schedule_rows, columns=["S.No", "Date", "Time Slot", "I + II Year Topic (Faculty)", "III Year Topic (Faculty)"])

# ================================
# TABLE 2 – Faculty Totals
# ================================
faculty_summary = {
    "ANO L Sushma": [df_schedule["I + II Year Topic (Faculty)"].str.contains("Sushma").sum(),
                     df_schedule["III Year Topic (Faculty)"].str.contains("Sushma").sum()],
    "BHM P Anand Rao": [df_schedule["I + II Year Topic (Faculty)"].str.contains("Anand Rao").sum(),
                        df_schedule["III Year Topic (Faculty)"].str.contains("Anand Rao").sum()]
}
df_faculty = pd.DataFrame.from_dict(faculty_summary, orient='index', columns=["I + II Year Total Classes", "III Year Total Classes"]).reset_index().rename(columns={"index": "Faculty"})

# ================================
# TABLE 3 – Monthly Summary
# ================================
df_schedule["Month"] = pd.to_datetime(df_schedule["Date"], format="%d-%b-%Y").dt.strftime("%b-%Y")
monthly_summary = df_schedule.groupby("Month").size().reset_index(name="Total Periods")
# Count periods that are breaks/CATC (i.e., not a specific faculty name)
def count_non_teaching(series, faculty_keywords):
    is_teaching = series.str.contains('|'.join(faculty_keywords)).fillna(False)
    return (~is_teaching).sum()

faculty_keywords = list(faculties.keys())
monthly_summary["Break/CATC Periods"] = df_schedule.groupby("Month")["I + II Year Topic (Faculty)"].apply(lambda x: count_non_teaching(x, faculty_keywords))
monthly_summary["Taught Periods"] = monthly_summary["Total Periods"] - monthly_summary["Break/CATC Periods"]
df_monthly = monthly_summary.rename(columns={"Total Periods": "Total Periods (Weds/Fris)", 
                                           "Break/CATC Periods": "Break/CATC Periods", 
                                           "Taught Periods": "Taught Periods"})

# ================================
# TABLE 4 – Summary
# ================================
df_summary = pd.DataFrame({
    "S.No": [1],
    "Total Periods": [len(df_schedule)],
    "Break/CATC Periods (I+II Yr)": [df_schedule["I + II Year Topic (Faculty)"].apply(lambda x: not any(kw in x for kw in faculty_keywords)).sum()],
    "Break/CATC Periods (III Yr)": [df_schedule["III Year Topic (Faculty)"].apply(lambda x: not any(kw in x for kw in faculty_keywords)).sum()],
    "ANO Periods (Sushma)": [df_schedule["I + II Year Topic (Faculty)"].str.contains("Sushma").sum() + df_schedule["III Year Topic (Faculty)"].str.contains("Sushma").sum()],
    "TO Periods (Anand Rao)": [df_schedule["I + II Year Topic (Faculty)"].str.contains("Anand Rao").sum() + df_schedule["III Year Topic (Faculty)"].str.contains("Anand Rao").sum()],
})

# ================================
# TABLE 5 - Subject Coverage Report
# ================================

def generate_coverage_report(allocator, subjects_dict, subject_type):
    report_data = []
    year_labels = ["1st Year Required", "2nd Year Required", "3rd Year Required", 
                   "1st Year Taught", "2nd Year Taught", "3rd Year Taught", 
                   "Remaining Total"]
    
    # Iterate through subject groups and their details
    for sub_group_name, sub_group in subjects_dict.items():
        for sub_detail, required_periods in sub_group.items():
            
            consumed_periods = allocator.consumed[subject_type].get(sub_detail, [0, 0, 0])
            
            # Calculate remaining periods
            remaining = (required_periods[0] - consumed_periods[0]) + \
                        (required_periods[1] - consumed_periods[1]) + \
                        (required_periods[2] - consumed_periods[2])

            row = [
                f"{sub_detail} ({sub_group_name})",
                required_periods[0],
                required_periods[1],
                required_periods[2],
                consumed_periods[0],
                consumed_periods[1],
                consumed_periods[2],
                remaining
            ]
            report_data.append(row)
            
    df_report = pd.DataFrame(report_data, columns=["Subject Detail"] + year_labels)
    # Re-order the columns for better comparison
    df_report = df_report[["Subject Detail", "1st Year Required", "1st Year Taught", 
                           "2nd Year Required", "2nd Year Taught", 
                           "3rd Year Required", "3rd Year Taught", 
                           "Remaining Total"]]
    
    return df_report

df_common_coverage = generate_coverage_report(allocator, common_subjects, 'common')
df_special_coverage = generate_coverage_report(allocator, special_subjects, 'special')


# ================================
# EXPORT TO EXCEL
# ================================
with pd.ExcelWriter("NCC_Schedule_MRCET_2025_26_Detailed.xlsx", engine="openpyxl") as writer:
    df_schedule.to_excel(writer, sheet_name="1. Schedule", index=False)
    df_faculty.to_excel(writer, sheet_name="2. Faculty Totals", index=False)
    df_monthly.to_excel(writer, sheet_name="3. Monthly Summary", index=False)
    df_summary.to_excel(writer, sheet_name="4. Overall Summary", index=False)
    df_common_coverage.to_excel(writer, sheet_name="5. Common Subject Coverage", index=False)
    df_special_coverage.to_excel(writer, sheet_name="6. Special Subject Coverage", index=False)

print("✅ NCC Schedule Excel file generated with detailed syllabus: NCC_Schedule_MRCET_2025_26_Detailed.xlsx")

from IPython.display import FileLink
# Assuming the file has been created
FileLink('NCC_Schedule_MRCET_2025_26_Detailed.xlsx')