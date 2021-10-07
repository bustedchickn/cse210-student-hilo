class PLAYER:

    def choose_hilo(self):
        """This function asks the 
        player to choose hi or lo"""

        # Use a loop to repromt if user input is invalid.
        loop_sentinel = True
        while loop_sentinel:

            # Prompt.
            hi_or_lo = input("Higher or Lower? [h/l] ")

            # Validate input
            if hi_or_lo.lower() == "h" or hi_or_lo.lower() == "l":

                # Return
                return hi_or_lo

            # Display error message.
            else:
                print("That input is not vaild. Try again.")

    def play_again(self):
        """This function asks if 
        the player wants to play again."""

        loop_sentinel = True
        while loop_sentinel:

            # Prompt.
            answer = input("Keep playing? [y/n] ")

            if answer.lower() == "y":
                return True
            elif answer.lower() == "n":
                return False
            else:
                print("That input is not vaild. Try again.")
