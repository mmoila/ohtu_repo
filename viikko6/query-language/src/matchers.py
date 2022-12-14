from player import Player


class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class All:
    def test(self, player):
        if isinstance(player, Player):
            return True
        return False


class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def test(self, player):
        return not self._matcher.test(player)


class Or:
    def __init__(self, *matchers):
        self.matchers = matchers

    def test(self, player):
        for matcher in self.matchers:
            if matcher.test(player):
                return True
        return False


class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        result = HasAtLeast(self._value, self._attr).test(player)
        return not result


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value
