import gspread
from oauth2client.service_account import ServiceAccountCredentials


class CloudSave:
    def __init__(self, sheet, credentials_file):
        try:
            scope = ["https://spreadsheets.google.com/feeds",
                     "https://www.googleapis.com/auth/drive"]
            credentials = ServiceAccountCredentials.from_json_keyfile_name(
                credentials_file, scope)
            gc = gspread.authorize(credentials)
        except OSError as e:
            print("JSON file with Google account credentials not found!")
            exit(1)

        self.datasheet = gc.open(sheet).worksheet("data")  # Open google sheet
        self._update()

    def add_win(self, player_number):
        if player_number == 1:
            self.datasheet.update("E6", self.p1_data["wins"]+1)
            self.datasheet.update("E9", self.p1_data["current_win_streak"]+1)
            self.datasheet.update("E8", max(
                self.p1_data["current_win_streak"]+1, self.p1_data["longest_win_streak"]))
            self.datasheet.update("J9", 0)

        elif player_number == 2:
            self.datasheet.update("J6", self.p2_data["wins"]+1)
            self.datasheet.update("J9", self.p2_data["current_win_streak"]+1)
            self.datasheet.update("J8", max(
                self.p2_data["current_win_streak"]+1, self.p2_data["longest_win_streak"]))
            self.datasheet.update("E9", 0)

        self.datasheet.update("E2", self.total_games+1)
        self._update()

    # Clear data
    def reset(self):
        self.datasheet.update("E6", 0)
        self.datasheet.update("E9", 0)
        self.datasheet.update("E8", 0)
        self.datasheet.update("J9", 0)
        self.datasheet.update("J6", 0)
        self.datasheet.update("J9", 0)
        self.datasheet.update("J8", 0)
        self.datasheet.update("E9", 0)
        self.datasheet.update("E2", 0)
        self._update()

    def display_scoreboard(self):
        print("Go to go.param.me/score to view the full scoreboard! Here's a summary:")
        print(f"Total games played: {self.total_games}")
        print(f"Player 1 wins: {self.p1_data['wins']}")
        print(f"Player 2 wins: {self.p2_data['wins']}")
        print()

    # Load stats from google sheet

    def _update(self):
        self.total_games = int(self.datasheet.cell(2, 5).value)
        self.p1_data = {"wins": int(self.datasheet.cell(6, 5).value),
                        "longest_win_streak": int(self.datasheet.cell(8, 5).value),
                        "current_win_streak": int(self.datasheet.cell(9, 5).value)}

        self.p2_data = {"wins": int(self.datasheet.cell(6, 10).value),
                        "longest_win_streak": int(self.datasheet.cell(8, 10).value),
                        "current_win_streak": int(self.datasheet.cell(9, 10).value)}
