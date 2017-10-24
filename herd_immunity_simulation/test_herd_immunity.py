from person import Person
from virus import Virus
from logger import Logger
from simulation import Simulation

import pytest


# TODO: Create a function that initializes virus and person to use
# on all testing funtions
ebola = Virus('ebola', 0.7, 2.5)
person = Person(1, True, ebola)
person2 = Person(2, True)

# -----Person file-----
def test_init_Person():
    # ebola = Virus('ebola', 0.7)
    # person = Person(1, True, ebola)
    # person2 = Person(2, True)
    assert person._id == 1
    assert person.is_vaccinated == True
    assert person.infected == ebola
    assert person2.infected == None

def test_did_survive_infection():
    person = Person(3, False, ebola)
    assert person.did_survive_infection() == False

# -----Logger file-----
def test_write_metadata():
    # log = '{}\t{}\t{}\t{}\t{}\n'.format(population_size, vacc_percentage,
    # virus.name, virus.mortality_rate, virus.basic_repro_num)
    population_size = 10
    vacc_percentage = 0.2
    logger = Logger('hello')
    ebola = Virus('ebola', 0.7, 2.5)
    assert logger.write_metadata(10, 0.2, ebola) == '10\t0.2\tebola\t0.7\t2.5\n'

# -----Simulation file-----
def test_init_simulation():
    # TODO: Fix create population function, to be able to test in init func
    population_size = 20
    vacc_percentage = 0.2
    logger = Logger('result_log.txt')
    simulation = Simulation(population_size, vacc_percentage, ebola)
    assert simulation.population_size == 20
    assert simulation.vacc_percentage == 0.2
    assert len(simulation.population) == 20
    assert simulation.total_infected == 0
    assert simulation.current_infected == 0
    assert simulation.next_person_id == 20
    assert simulation.initial_infected == 1
    assert simulation.virus == ebola
    assert simulation.virus_name == ebola.name
    assert simulation.virus_mortality_rate == ebola.mortality_rate
    assert simulation.virus_basic_repro_num == ebola.basic_repro_num
    assert simulation.file_name == 'ebola_simulation_pop_20_vp_0.2_infected_1.txt'
    assert simulation.logger.file_name == logger.file_name
    assert len(simulation.newly_infected) == 1


def test_create_population():
    population_size = 20
    vacc_percentage = 0.2
    logger = Logger('result_log.txt')
    simulation = Simulation(population_size, vacc_percentage, ebola)
    assert simulation._create_population(simulation.initial_infected) == population_size
