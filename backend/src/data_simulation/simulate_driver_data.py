import random
from django.utils import timezone
from models import Driver  # Adjust to your actual app name
from faker import Faker

fake = Faker()

STATUS_CHOICES = ['available', 'on_trip', 'inactive']

def create_fake_driver():
    """
    Generate a fake driver with random details.
    """
    name = fake.name()
    phone_number = fake.phone_number()
    license_number = fake.unique.license_plate()
    status = random.choice(STATUS_CHOICES)

    driver = Driver(
        name=name,
        phone_number=phone_number,
        license_number=license_number,
        status=status
    )
    driver.save()
    print(f"Created Driver: {driver}")

def simulate_driver_data(num_drivers=10):
    """
    Create a specified number of fake driver records.
    """
    for _ in range(num_drivers):
        create_fake_driver()

if __name__ == "__main__":
    simulate_driver_data(10)  # Generate 10 driver records
