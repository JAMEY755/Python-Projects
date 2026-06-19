import os
import pandas as pd
import math

def calculate_team_score(row):
    """
    Helper function to compute a weighted structural rating for each team.
    Utilizes weights based on their tournament data characteristics.
    """
    try:
        # Base stats
        strength = float(row['Team strength'])
        form = float(row['Team form'])
        fan_support = float(row['Fan support'])
        injuries = float(row['Number of injuries'])
        
        # Position-specific metrics
        keeper = float(row['Keeper ranking'])
        defender = float(row['Defender ranking'])
        midfielder = float(row['Midfielder ranking'])
        forward = float(row['Forward ranking'])
        
        # Experience adjustments
        wc_exp = float(row['Players with World Cup experience'])
        goat_effect = float(row['GOAT effect'])
        
        # Composite calculation logic
        squad_avg = (keeper + defender + midfielder + forward) / 4.0
        
        # Add values while penalizing injuries
        total_score = (strength * 0.35) + (form * 0.20) + (squad_avg * 0.25) + (fan_support * 0.05)
        total_score += (wc_exp * 0.5) + (goat_effect * 5.0)
        total_score -= (injuries * 1.5)  # Penalty for injured players
        
        return round(total_score, 2)
    except Exception:
        return 0.0

def main():
    excel_filename = "team_details.xlsx"
    csv_filename = "team_deatails.xlsx - Sheet1.csv"
    
    if os.path.exists(excel_filename):
        print(f"--- Loading Tournament Data from Excel file '{excel_filename}' ---")
        df = pd.read_excel(excel_filename)
    elif os.path.exists(csv_filename):
        print(f"--- Loading Tournament Data from CSV file '{csv_filename}' ---")
        df = pd.read_csv(csv_filename)
    else:
        print(f" Error: Could not find '{excel_filename}' or '{csv_filename}'. Ensure the file is in the same folder.")
        return

    # Cleaning up whitespaces from headers or strings if any
    df.columns = df.columns.str.strip()
    df['Team'] = df['Team'].str.strip()

    print("Processing team metrics and establishing simulation scores...")
    team_list = []
    
    # CONDITIONAL LOOPING: populating and filtering using CONTINUE
    
    for index, row in df.iterrows():
        team_name = row['Team']
        
        # Specific Condition: Ignore teams with extreme low ranking/strength defaults
        if pd.isna(team_name) or row['Team strength'] <= 0:
            continue  # Skip unviable data configurations
            
        score = calculate_team_score(row)
        team_list.append({"name": team_name, "score": score})

    # Sort teams by their calculated power ratings descending
    team_list.sort(key=lambda x: x['score'], reverse=True)

    print(f"\nSuccessfully processed {len(team_list)} international teams.")
    
    # DATA STRUCTURE METHOD: INSERTING a specific wildcard element
    
    # Let's dynamically inject a legendary tracking element or host benchmark structural marker
    benchmark_marker = {"name": "★ Tournament Baseline Alpha ★", "score": 85.0}
    
    # Using 'insert' at index 0 to position it temporarily at the top for testing/evaluation
    team_list.insert(0, benchmark_marker)
    print(f"Inserted temporary baseline node: {team_list[0]['name']} (Score: {team_list[0]['score']})")
    
    # Remove the placeholder item to ensure standard competitive simulation accuracy
    team_list.pop(0)

    # STAGE 1 SIMULATION: Group Stage & Round of 16 structural selection
    
    print("\n--- Phase 1: Filtering Top Contenders for Knockout Bracket Stage ---")
    qualified_teams = []
    
    for team in team_list:
        # Condition Check: Set an entry bar rating for Elite Top 8 Knockouts
        if len(qualified_teams) >= 8:
            break  # BREAK out of loop once the strict bracket spaces are full
            
        print(f"🏆 {team['name']} qualifies for Knockout Stage with Score: {team['score']}")
        qualified_teams.append(team)

     # STAGE 2 SIMULATION: Knockout Tree Bracket Rounds
    
    print("\n" + "="*50)
    print("🏟️  STARTING THE WORLD CUP FINALS BRACKET TOURNAMENT 🏟️")
    print("="*50)

    round_counter = 1
    while len(qualified_teams) > 1:
        print(f"\n--- TOURNAMENT ROUND: QUARTER-FINALS (Remaining: {len(qualified_teams)}) ---" if round_counter == 1 else f"\n--- TOURNAMENT ROUND: SEMI-FINALS (Remaining: {len(qualified_teams)}) ---")
        next_round_winners = []
        
        # Match up teams sequentially: index i vs index i+1
        for i in range(0, len(qualified_teams), 2):
            team_a = qualified_teams[i]
            team_b = qualified_teams[i+1]
            
            print(f"Matchup: {team_a['name']} (Rating: {team_a['score']}) vs {team_b['name']} (Rating: {team_b['score']})")
            
            # Match performance conditions with basic simulation variance logic
            if team_a['score'] >= team_b['score']:
                winner = team_a
                loser = team_b
            else:
                winner = team_b
                loser = team_a
                
            print(f"  👉 WINNER: {winner['name']}! ({loser['name']} is eliminated)")
            next_round_winners.append(winner)
            
        qualified_teams = next_round_winners
        round_counter += 1

    # FINAL PREDICTION OUTPUT
    
    champion = qualified_teams[0]
    print("\n" + "#"*60)
    print(f"🏆 🌍 CONGRATULATIONS TO THE PREDICTED WORLD CUP CHAMPION: {champion['name'].upper()} 🌍 🏆")
    print(f"Final Tournament Rating Performance Metric: {champion['score']}")
    print("#"*60)

if __name__ == "__main__":
    main()