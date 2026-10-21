import pandas as pd


def team_results(data):
    home_wins = data[data['Result'] == 'H']

    home_win_counts = home_wins['HomeTeam'].value_counts()

    team_performance_home = (
        data.groupby('HomeTeam')['Result']
        .value_counts()
    )

    team_performance_away = (
        data.groupby('AwayTeam')['Result']
        .value_counts()
    )

    return home_win_counts, team_performance_home, team_performance_away


def home_away_average_goals(data):
    home_avg = data.groupby('HomeTeam')['Home_Goals'].mean()
    away_avg = data.groupby('AwayTeam')['Away_Goals'].mean()

    performance = pd.concat([home_avg, away_avg], axis=1)

    performance['Difference'] = (
        performance['Home_Goals'] - performance['Away_Goals']
    )

    performance = performance.sort_values(
        by='Difference',
        ascending=False
    )

    return performance


def add_analysis_features(data):
    data['TotalGoals'] = data['Home_Goals'] + data['Away_Goals']

    return data

def entertaining_teams(data):
    home_goal_avg = (
        data.groupby('HomeTeam')['TotalGoals']
        .mean()
        .sort_values(ascending=False)
    )

    away_goal_avg = (
        data.groupby('AwayTeam')['TotalGoals']
        .mean()
        .sort_values(ascending=False)
    )

    entertain_teams = pd.concat(
        [home_goal_avg, away_goal_avg],
        axis=1
    )

    return entertain_teams

def scoring_consistency(data):
    home_scoring = data[['HomeTeam', 'Home_Goals']]
    away_scoring = data[['AwayTeam', 'Away_Goals']]

    data_home = home_scoring.rename(
        columns={'HomeTeam': 'Team', 'Home_Goals': 'Goals_Scored'}
    )

    data_away = away_scoring.rename(
        columns={'AwayTeam': 'Team', 'Away_Goals': 'Goals_Scored'}
    )

    all_scoring = pd.concat([data_home, data_away], axis=0)

    overall_mean = all_scoring.groupby('Team')['Goals_Scored'].mean()
    overall_std = all_scoring.groupby('Team')['Goals_Scored'].std()

    consistency = pd.concat([overall_mean, overall_std], axis=1)

    consistency.columns = ['Mean_Goals', 'Std_Dev_Goals']

    consistency = consistency.sort_values(
        by='Std_Dev_Goals',
        ascending=True
    )

    return consistency

def clean_sheet_summary(data):
    data['Home_Fail_to_Score'] = data['Home_Goals'] == 0
    data['Home_clean_sheet'] = data['Away_Goals'] == 0

    data['Away_Fail_to_Score'] = data['Away_Goals'] == 0
    data['Away_clean_sheet'] = data['Home_Goals'] == 0

    home_summary = data.groupby('HomeTeam')[
        ['Home_Fail_to_Score', 'Home_clean_sheet']
    ].sum()

    away_summary = data.groupby('AwayTeam')[
        ['Away_Fail_to_Score', 'Away_clean_sheet']
    ].sum()

    home_summary = home_summary.rename(columns={
        'Home_Fail_to_Score': 'Fail_to_Score',
        'Home_clean_sheet': 'Clean_Sheet'
    })

    away_summary = away_summary.rename(columns={
        'Away_Fail_to_Score': 'Fail_to_Score',
        'Away_clean_sheet': 'Clean_Sheet'
    })

    overall_summary = home_summary + away_summary

    overall_summary = overall_summary.sort_values(
        by='Clean_Sheet',
        ascending=False
    )

    return overall_summary

def monthly_goal_summary(data):
    data['Month'] = data['Date'].dt.month

    monthly_summary = data.groupby('Month').agg(
        Total_Goals=('TotalGoals', 'sum'),
        Average_Goals_Per_Game=('TotalGoals', 'mean'),
        Games_Played=('Result', 'count')
    )

    monthly_summary = monthly_summary.sort_index()

    return monthly_summary

def team_goal_ranking(data):
    avg_home_ranking = data[
        ['HomeTeam', 'Home_Goals', 'Away_Goals']
    ].rename(
        columns={
            'HomeTeam': 'Team',
            'Home_Goals': 'Goals_Scored',
            'Away_Goals': 'Goals_Conceded'
        }
    )

    avg_away_ranking = data[
        ['AwayTeam', 'Away_Goals', 'Home_Goals']
    ].rename(
        columns={
            'AwayTeam': 'Team',
            'Away_Goals': 'Goals_Scored',
            'Home_Goals': 'Goals_Conceded'
        }
    )

    all_ranking = pd.concat(
        [avg_home_ranking, avg_away_ranking],
        axis=0
    )

    team_ranking = all_ranking.groupby('Team').agg(
        Average_Goals_Scored=('Goals_Scored', 'mean'),
        Average_Goals_Conceded=('Goals_Conceded', 'mean'),
        Total_Goals_Scored=('Goals_Scored', 'sum'),
        Total_Goals_Conceded=('Goals_Conceded', 'sum')
    )

    team_ranking['Goal_Difference'] = (
        team_ranking['Total_Goals_Scored']
        - team_ranking['Total_Goals_Conceded']
    )

    goal_diff_ranking = team_ranking.sort_values(
        by='Goal_Difference',
        ascending=False
    )

    return goal_diff_ranking

def total_goals_by_team(data):
    home_goals = data.groupby('HomeTeam')['Home_Goals'].sum()
    away_goals = data.groupby('AwayTeam')['Away_Goals'].sum()
    total_goals = home_goals.add(away_goals, fill_value=0)
    return total_goals

def add_analysis_features(data):
    data['TotalGoals'] = data['Home_Goals'] + data['Away_Goals']

    data['High_Scoring'] = data['TotalGoals'] >= 3

    data['Result_label'] = data['Result'].map({
        'H': 'Home Win',
        'A': 'Away Win',
        'D': 'Draw'
    })

    return data

def average_goals_summary(data):
    home_average_goals = (
        data.groupby('HomeTeam')['Home_Goals']
        .mean()
    )

    away_average_goals = (
        data.groupby('AwayTeam')['Away_Goals']
        .mean()
    )

    average_goals = pd.concat(
        [home_average_goals, away_average_goals],
        axis=1
    )

    average_goals.columns = [
        'Home_Average_Goals',
        'Away_Average_Goals'
    ]

    overall_home_avg = data['Home_Goals'].mean()
    overall_away_avg = data['Away_Goals'].mean()

    return average_goals, overall_home_avg, overall_away_avg