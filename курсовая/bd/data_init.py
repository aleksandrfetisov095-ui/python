import os

DB_FILE = "car.xlsx"

INITIAL_CARS = [
    ["Lada Granta", "Lada", 98, 100, 3, 160, 1150000],
    ["Lada Vesta NG", "Lada", 122, 100, 5, 178, 1450000],
    ["Lada Niva Travel", "Lada", 80, 100, 3, 220, 1250000],
    ["Renault Logan Stepway", "Renault", 113, 100, 3, 195, 1350000],
    ["Haval Jolion", "Haval", 143, 150, 5, 180, 2100000],
    ["Chery Tiggo 4 Pro", "Chery", 122, 150, 5, 190, 1950000],
    ["Geely Coolray", "Geely", 150, 150, 5, 190, 2300000],

    ["Kia Rio X", "Kia", 123, 150, 5, 195, 1850000],
    ["Hyundai Solaris", "Hyundai", 123, 150, 5, 160, 1750000],
    ["Volkswagen Polo", "Volkswagen", 110, 100, 2, 170, 1900000],
    ["Skoda Rapid", "Skoda", 110, 100, 2, 170, 1850000],
    ["Kia K5", "Kia", 180, 150, 5, 160, 2800000],
    ["Hyundai Sonata", "Hyundai", 180, 150, 5, 155, 2750000],
    ["Mazda 6", "Mazda", 194, 100, 3, 165, 2900000],

    ["Toyota RAV4", "Toyota", 171, 100, 3, 195, 3800000],
    ["Honda CR-V", "Honda", 190, 100, 3, 200, 4100000],
    ["VW Tiguan", "Volkswagen", 180, 100, 2, 200, 3600000],
    ["Skoda Octavia A8", "Skoda", 150, 100, 2, 155, 2900000],
    ["Mazda CX-5", "Mazda", 194, 100, 3, 200, 3500000],
    ["Nissan Qashqai", "Nissan", 144, 100, 3, 200, 2600000],
    ["Mitsubishi Outlander", "Mitsubishi", 149, 100, 5, 215, 3200000],

    ["BMW 3 Series", "BMW", 184, 100, 2, 140, 4800000],
    ["BMW X3", "BMW", 249, 100, 2, 210, 6200000],
    ["BMW X5", "BMW", 340, 100, 2, 210, 8500000],
    ["Toyota Camry", "Toyota", 200, 100, 3, 155, 3600000],
    ["Toyota Land Cruiser 300", "Toyota", 299, 100, 3, 230, 9500000],
    ["Geely Monjaro", "Geely", 238, 150, 5, 210, 4200000],
    ["Li L7", "Li Auto", 449, 150, 5, 215, 5500000],
    ["Zeekr 001", "Zeekr", 544, 150, 5, 175, 5800000],
    ["Avatr 11", "Avatr", 578, 150, 5, 200, 6100000]
]
