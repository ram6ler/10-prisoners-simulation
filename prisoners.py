import random
from sys import argv

prisoners = 10
guesses = 5


def simulate(verbose: bool = True, method: str = "random") -> int:
    """
    Simulates `prisoners` prisoners searching for their cards given `guesses` guesses;
    returns the number of prisoners who successfully find their cards.

    If `verbose` is set to True, a description of the simulation will be printed out.

    If `method` is set to `"random"`, prisoners will randomly pick a drawer they haven't already
    searched for their next guess. If `method` is set to `"sequential"`, prisoners will search the
    drawer that matches the card they have just found in the previously guessed drawer.
    """

    def shuffled() -> list[int]:
        """Returns shuffled prisoner indices."""
        indices = [x + 1 for x in range(prisoners)]
        random.shuffle(indices)
        return indices

    cards = shuffled()

    def show_cards() -> None:
        print("Drawer:", " ".join([str(i + 1).rjust(3) for i in range(prisoners)]))
        print("  Card:", " ".join([str(card).rjust(3) for card in cards]))

    if verbose:
        print("Card placement:\n")
        show_cards()

    successes = 0

    for prisoner in range(prisoners):
        if verbose:
            print(f"\n  Prisoner {prisoner + 1}'s turn...")

        choices = shuffled()
        card_found = -1

        for guess in range(guesses):
            drawer = choices[guess]
            if method == "sequential":
                if card_found == -1:
                    drawer = prisoner + 1
                else:
                    drawer = card_found

            card = cards[drawer - 1]
            success = card == prisoner + 1

            if verbose:
                print(f"    Guess {guess + 1}: Peeks in drawer {drawer}...")
                print(f"      Finds card {card}.")

            card_found = card
            if success:
                successes += 1
                if verbose:
                    print("        Success!")
                break
        else:
            if verbose:
                print("        Too bad!")

    if method == "sequential" and verbose:
        print()
        show_cards()
        cycles: list[list[int]] = []
        for card in cards:
            if any([card in ring for ring in cycles]):
                continue
            ring: list[int] = []
            copy = card
            while copy not in ring:
                ring.append(copy)
                copy = cards[copy - 1]
            cycles.append(ring)
        print(f"Cycles: {cycles}")

    return successes


def perform_simulations(simulations: int, method: str) -> None:
    """
    Performs `simulations` simulations with prisoners choosing the next door randomly
    (`method="random"`) or sequentially (`method="sequential"`).
    """
    print(f"\n{simulations} simulations, {method} searching:")
    data = [simulate(verbose=False, method=method) for x in range(simulations)]
    print(
        f"  Average number of prisoners finding their cards: {sum(data) / simulations}"
    )
    print(
        f"  Number of simulations in which all {prisoners} prisoners found their cards: {sum([data[i] == prisoners for i in range(simulations)])}"
    )
    print("\nData:\n")
    per_row = 20
    for row in range(len(data) // per_row + 1):
        print(
            " ".join(
                [
                    f"{str(data[e]).rjust(4)}"
                    for e in range(row * per_row, min([len(data), (row + 1) * per_row]))
                ]
            )
        )
    print("\n")


def example_simulation(method: str) -> None:
    """
    Produces a verbose description of a single simulation using method `method`.
    """

    print(f"Method: {method}\n")
    successes = simulate(method=method)
    print(f"\nTotal successes: {successes}")


def show_help() -> None:
    """
    Displays script instructions.
    """
    print("\nUse:")
    p = argv[0]
    print(
        f"""
  {p} --help        or {p} -h  \tDisplay help
  {p} --random      or {p} -r  \tShow example simulation using random searching
  {p} --random N    or {p} -r N\t(N some integer) Perform N simulations using random searching
  {p} --sequence    or {p} -s  \tShow example simulation using sequential searching
  {p} --sequence N  or {p} -s N\t(N some integer) Perform N simulations using sequential searching
"""
    )


if __name__ == "__main__":
    print(f"Call: {' '.join(argv)}\n")
    if len(argv) > 1:
        if argv[1] == "--help" or argv[1] == "-h":
            show_help()
        elif argv[1] == "--random" or argv[1] == "-r":
            if len(argv) > 2:
                try:
                    simulations = int(argv[2])
                    perform_simulations(simulations, method="random")
                except:
                    show_help()
            else:
                example_simulation(method="random")
        elif argv[1] == "--sequence" or argv[1] == "-s":
            if len(argv) > 2:
                try:
                    simulations = int(argv[2])
                    perform_simulations(simulations, method="sequential")
                except:
                    show_help()
            else:
                example_simulation(method="sequential")
        else:
            show_help()
    else:
        show_help()
