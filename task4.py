class Cat:
    species: str = "Felis catus"
    average_lifespan: int = 15
    def __init__(self, name: str, breed: str, age: int, weight: float, color: str) -> None:
        self.name: str = name
        self.breed: str = breed
        self.age: int = age
        self.weight: float = weight
        self.color: str = color
        self.energy: int = 100
    def __str__(self) -> str:
        return f"{self.breed} {self.name}, {self.age} лет"
    def meow(self) -> str:
        return f"{self.name} говорит: Мяу!"
    def feed(self, food_grams: int) -> None:
        self.weight += food_grams / 1000
        print(f"{self.name} поел. Вес составляет: {self.weight:.2f} кг")
    def sleep(self, hours: int) -> None:
        self.energy = min(100, self.energy + hours * 10)
        print(f"{self.name} поспал {hours} ч. Энергия: {self.energy}%")
    def is_kitten(self) -> bool:
        return self.age < 1
cat1: Cat = Cat("Маркиз", "Сиамская", 3, 4.5, "белый")
cat2: Cat = Cat("Мурка", "Британская", 0.5, 2.1, "серый")
cat3: Cat = Cat("Персик", "Мейн-кун", 5, 8.2, "рыжий")
print(cat1)
print(cat1.meow())
print(f"{cat2.name} - котёнок? {cat2.is_kitten()}")
cat3.feed(500)
cat1.sleep(2)
print(f"Вид: {Cat.species}, живут до {Cat.average_lifespan} лет")