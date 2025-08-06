from timeit import timeit
from json import load as json_load
from inbreeding_calculator import InbreedingCalculator
from pathlib import Path

pedigrees = json_load(open(Path(__file__) / "../test_data.json"))

def test_all():
    for pedigree in pedigrees:
        calculator = InbreedingCalculator(
            pedigree[0], sire_key="s", dam_key="d", id_key="name"
        )
        calculator.get_coefficient()

if __name__ == "__main__":
    ITERATIONS = 10_000
    print(f"Speed Test:\t{ITERATIONS} iterations")
    time = timeit(test_all, number=ITERATIONS)
    print(f"Time:\t{time}s")
