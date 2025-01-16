# Quickstart

    python3 main.py --help

    Usage: main.py [OPTIONS]

    Options:
      -a, --ai TEXT             Specify an AI player by name (with optional =xyz
                                buyin amount, default $1000). Can be repeated for
                                multiple AIs
      -h, --player TEXT         Specify a human player by name (with optional =xyz
                                buyin amount, default $1000). Can be repeated for
                                multiple players
      -r, --num-rounds INTEGER  Automatically play this number of rounds
      -R, --autoplay            Automatically play until all players are bankrupt
      -i, --interactive         Continue playing interactively after -r or -R
      --help                    Show this message and exit.


## Dependencies

    pip3 install -r requirements.txt


## Testing

    export PYTHONPATH=$PYTHONPATH:$PWD/planet
    py.test -vvvsx
