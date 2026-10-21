from clean_data import load_and_clean_data

from analyze import (
    add_analysis_features,
    monthly_goal_summary,
    scoring_consistency,
    team_goal_ranking,
    team_results,
    home_away_average_goals,
    entertaining_teams,
    clean_sheet_summary,
    total_goals_by_team,
    average_goals_summary,
)

from visualize import (
    plot_total_goals,
    plot_average_goals,
    plot_monthly_goals,
    plot_goal_difference,
    plot_high_scoring_matches,
    plot_clean_sheets,
)


# Load and prepare data
data = load_and_clean_data()
data = add_analysis_features(data)


# Run analyses
consistency = scoring_consistency(data)
overall_summary = clean_sheet_summary(data)
monthly_summary = monthly_goal_summary(data)
goal_diff_ranking = team_goal_ranking(data)

home_win_counts, team_performance_home, team_performance_away = team_results(data)

performance = home_away_average_goals(data)
entertain_teams = entertaining_teams(data)
goals_scored = total_goals_by_team(data)

average_goals, overall_home_avg, overall_away_avg = average_goals_summary(data)


# Print selected results
print(goals_scored)
print(goal_diff_ranking)
print(monthly_summary)
print(overall_summary)
print(consistency)


# Create visualizations
plot_total_goals(goals_scored)
plot_average_goals(average_goals)
plot_monthly_goals(monthly_summary)
plot_goal_difference(goal_diff_ranking)
plot_high_scoring_matches(data)
plot_clean_sheets(overall_summary)