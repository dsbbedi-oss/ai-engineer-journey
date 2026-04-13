def build_week_summary(study_log: dict[str, int]) -> str:
    total = sum(study_log.values())

    summary_lines =                     ekly Study Summary:"]

    for day, hours in study_log.items():
        if hours >= 2:
            status = "Good"
        else:
            status = "Low"

        summary_lines.append(f"{day}: {hours} hour(s) - {status}")

    summary_lines.append(f"Total: {total} hour(s)")

    return "\n".join(summary_lines)


"""if __name__ == "__main__":
    week_data = {
        "Monday": 5,
        "Tuesday": 1
    }
    print(build_week_summary(week_data))"""