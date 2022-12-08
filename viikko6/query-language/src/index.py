from statistics import Statistics
from player_reader import PlayerReader
from query_builder import QueryBuilder


def print_players(stats, matcher):
    for player in stats.matches(matcher):
        print(player)
    print("\n")


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)
    query = QueryBuilder()

    matcher = (
        query
        .playsIn("NYR")
        .hasAtLeast(10, "goals")
        .hasFewerThan(20, "goals")
        .build()
    )

    for player in stats.matches(matcher):
        print(player)

    matcher = (
        query
        .oneOf(
            query.playsIn("PHI")
            .hasAtLeast(10, "assists")
            .hasFewerThan(5, "goals")
            .build(),
            query.playsIn("EDM")
            .hasAtLeast(50, "points")
            .build()
        )
        .build()
    )
    print(30*"*")
    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
