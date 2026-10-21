import matplotlib.pyplot as plt

def plot_total_goals(goals_scored):
    goals_scored.plot(kind='bar')

    plt.title('Total Goals Scored by Team')
    plt.xlabel('Team')
    plt.ylabel('Total Goals')
    plt.xticks(rotation=90)
    plt.tight_layout()

    plt.savefig('charts/total_goals_by_team.png')
    plt.show()

def plot_average_goals(average_goals):
    average_goals.plot(kind='bar')

    plt.title('Average Goals Scored by Team')
    plt.xlabel('Team')
    plt.ylabel('Average Goals')
    plt.xticks(rotation=90)
    plt.tight_layout()

    plt.savefig('charts/average_goal_scored_by_team.png')
    plt.show()

def plot_monthly_goals(monthly_summary):
    monthly_summary['Average_Goals_Per_Game'].plot(kind='line')

    plt.title('Average Goals Scored per Month')
    plt.xlabel('Month')
    plt.ylabel('Average Goals per Match')
    plt.tight_layout()

    plt.savefig('charts/average_goals_per_month.png')
    plt.show()


def plot_goal_difference(goal_diff_ranking):
    goal_diff_ranking['Goal_Difference'].plot(kind='bar')

    plt.title('Goal Difference by Team')
    plt.xlabel('Team')
    plt.ylabel('Goal Difference')
    plt.xticks(rotation=90)
    plt.tight_layout()

    plt.savefig('charts/goal_difference_by_team.png')
    plt.show()

def plot_high_scoring_matches(data):
    high_scoring_matches = data['High_Scoring'].value_counts()

    high_scoring_matches.plot(kind='pie', autopct='%1.1f%%')

    plt.title('High Scoring Matches Distribution')
    plt.ylabel('')
    plt.tight_layout()

    plt.savefig('charts/high_scoring_matches_distribution.png')
    plt.show()

def plot_clean_sheets(overall_summary):
    clean_sheet_data = (
        overall_summary[['Clean_Sheet']]
        .sort_values(by='Clean_Sheet', ascending=False)
    )

    clean_sheet_data.plot(kind='bar')

    plt.title('Clean Sheets by Team')
    plt.xlabel('Team')
    plt.ylabel('Number of Clean Sheets')
    plt.xticks(rotation=90)
    plt.tight_layout()

    plt.savefig('charts/clean_sheets_by_team.png')
    plt.show()