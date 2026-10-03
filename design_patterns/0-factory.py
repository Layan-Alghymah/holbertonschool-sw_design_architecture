#!/usr/bin/env python3
"""Demonstrate the Factory design pattern using a vehicle registry."""


class Bus:
    """Represent a bus."""

    def mode(self):
        """Return the mode used by the bus."""
        return "road"


class Train:
    """Represent a train."""

    def mode(self):
        """Return the mode used by the train."""
        return "rails"


class Bike:
    """Represent a bike."""

    def mode(self):
        """Return the mode used by the bike."""
        return "lane"


class Scooter:
    """Represent a scooter."""

    def mode(self):
        """Return the mode used by the scooter."""
        return "scooter_lane"


class VehicleFactory:
    """Create vehicle objects using a registry."""

    def __init__(self):
        """Initialize the vehicle registry."""
        self._registry = {
            "bus": Bus,
            "train": Train,
            "bike": Bike,
        }

    def register_kind(self, name, cls):
        """Register a new vehicle type."""
        self._registry[name] = cls

    def create(self, kind):
        """Create and return a vehicle of the requested type."""
        cls = self._registry[kind]
        return cls()


def main():
    """Demonstrate creating vehicles through the factory."""
    factory = VehicleFactory()

    factory.register_kind("scooter", Scooter)

    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
