import time
import os

class BreathingGame:
    def __init__(self):
        self.level = 1
        self.is_playing = False
        self.phase = "ready"  # ready, inhale, hold, exhale, complete
        self.time_remaining = 0
        self.score = 0
        self.completed_cycles = 0
        self.total_cycles = 0

    def get_exercise_params(self, current_level):
        base_inhale = 4
        base_hold = 4
        base_exhale = 4
        base_cycles = 3

        return {
            "inhaleTime": base_inhale + (current_level - 1) // 2,
            "holdTime": base_hold + (current_level - 1) // 3,
            "exhaleTime": base_exhale + (current_level - 1) // 2,
            "cycles": base_cycles + (current_level - 1) // 4
        }

    def start_exercise(self):
        self.is_playing = True
        params = self.get_exercise_params(self.level)
        self.phase = "inhale"
        self.time_remaining = params["inhaleTime"]
        self.completed_cycles = 0
        self.total_cycles = params["cycles"]

        while self.is_playing:
            self.run_phase(params)

    def run_phase(self, params):
        while self.time_remaining > 0 and self.is_playing:
            self.display_status()
            time.sleep(1)
            self.time_remaining -= 1

        if self.phase == "inhale":
            self.phase = "hold"
            self.time_remaining = params["holdTime"]
        elif self.phase == "hold":
            self.phase = "exhale"
            self.time_remaining = params["exhaleTime"]
        elif self.phase == "exhale":
            self.completed_cycles += 1
            if self.completed_cycles >= self.total_cycles:
                self.phase = "complete"
                self.is_playing = False
                self.score += self.level * 10
                self.display_status()
                print("\n🎉 Level Complete! You earned", self.level * 10, "points.\n")
            else:
                self.phase = "inhale"
                self.time_remaining = params["inhaleTime"]

    def next_level(self):
        self.level += 1
        self.phase = "ready"
        self.completed_cycles = 0
        print(f"\n➡️ Moving to Level {self.level}!\n")

    def display_status(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("🌬️  Breathe & Grow")
        print(f"Level: {self.level} | Score: {self.score} | Cycles: {self.completed_cycles}/{self.total_cycles}")
        print(f"Phase: {self.phase.upper()} | Time Remaining: {self.time_remaining}s")


if __name__ == "__main__":
    game = BreathingGame()
    while True:
        print("\n--- Breathing Game ---")
        choice = input("Enter (s) Start | (n) Next Level | (q) Quit: ").lower()
        
        if choice == "s":
            game.start_exercise()
        elif choice == "n":
            game.next_level()
        elif choice == "q":
            print("Goodbye 👋 Keep practicing your breathing!")
            break
