from factories import USVehicleFactory, EUVehicleFactory
import logger_config


def main():

    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    car_us = us_factory.create_car("Ford", "Mustang")
    motorcycle_us = us_factory.create_motorcycle("Harley-Davidson", "Sportster")

    car_eu = eu_factory.create_car("Audi", "RS6")
    motorcycle_eu = eu_factory.create_motorcycle("Ducati", "Diavel")

    car_us.start_engine()
    motorcycle_us.start_engine()

    car_eu.start_engine()
    motorcycle_eu.start_engine()


if __name__ == "__main__":
    main()
