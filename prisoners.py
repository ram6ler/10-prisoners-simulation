import random
from sys import argv

PRISONERS = 10
GUESSES = 5

def simulate(verbose=True, method="random"):
    """
    Simulates [PRISONERS] prisoners searching for their cards given [GUESSES] guesses;
    returns the number of prisoners who successfully find their cards.

    If [verbose] is set to True, a description of the simulation will be printed out.

    If [method] is set to ["random"], prisoners will randomly pick a drawer they haven't already
    searched for their next guess. If [method] is set to ["sequential"], prisoners will search the
    drawer that matches the card they have just found in the previously guessed drawer.
    """

    def shuffled():
        indices = [x + 1 for x in range(PRISONERS)]
        random.shuffle(indices)
        return indices

    cards = shuffled()

    if verbose:
        print("Card placement:\n")
        print("Drawer\tCard")
        print("\n".join(["{:<6}\t{}".format(i + 1, cards[i]) for i in range(PRISONERS)]))

    successes = 0

    for prisoner in range(PRISONERS):
        if verbose:
            print("\n  Prisoner {}'s turn...".format(prisoner + 1))

        choices = shuffled()
        instrument_found = -1

        for guess in range(GUESSES):
            box = choices[guess]
            if method == "sequential":
                if instrument_found == -1:
                    box = prisoner + 1
                else:
                    box = instrument_found

            instrument = cards[box - 1]
            success = instrument == prisoner + 1

            if verbose:
                print("    Guess {}: Peeks in drawer {}...".format(guess + 1, box))
                print("      Finds card {}.".format(instrument))

            instrument_found = instrument
            if success:
                successes += 1
                if verbose:
                    print("        Success!")
                break
        else:
            if verbose:
                print("        Too bad!")

    return successes

def perform_simulations(simulations, method):
    print("\n{} simulations, {} searching:".format(simulations, method))
    data = [simulate(verbose=False, method=method) for x in range(simulations)]
    print("  Average number of prisoners finding their cards: {}".format(
        sum(data) / simulations))
    print("  Number of simulations in which all {} prisoners found their cards: {}".format(
        PRISONERS, sum([data[i] == PRISONERS for i in range(simulations)])))
    print("\nData:\n")
    per_row = 20
    for row in range(len(data) // per_row + 1):
        print("\t".join(
            ["{:<2}".format(data[e]) for e in range(
                row * per_row, min([len(data), (row + 1) * per_row]))]))
    print("\n")

def example_simulation(method):
    """
    Produces a verbose description of a single simulation using method [method].
    """
    
    print("Method: {}\n".format(method))
    successes = simulate(method=method)
    print("\nTotal successes: {}".format(successes))

def show_help():
    """
    Displays script instructions.
    """
    print("\nUse:")
    print("  {0} --help        or {0} -h  \tDisplay help".format(argv[0]))
    print("  {0} --random      or {0} -r  \tShow example simulation using random searching".format(argv[0]))
    print("  {0} --random N    or {0} -r N\t(N some integer) Perform N simulations using random searching".format(argv[0]))
    print("  {0} --sequence    or {0} -s  \tShow example simulation using sequential searching".format(argv[0]))
    print("  {0} --sequence N  or {0} -s N\t(N some integer) Perform N simulations using sequential searching".format(argv[0]))
    print("\n")

def main():
    print("Call: {}\n".format(" ".join(argv)))
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

main()
