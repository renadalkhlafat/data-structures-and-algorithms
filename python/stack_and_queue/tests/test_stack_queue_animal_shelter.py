from stack_and_queue.stack_queue_animal_shelter import AnimalShelter

def test_enqueue_cat():
    expected = "cat"
    animal_shelter=AnimalShelter()
    animal_shelter.enqueue_animal("cat")
    actual = animal_shelter.cat.rear.data

    assert expected == actual

def test_enqueues_dog():
    expected = "dog"
    animal_shelter=AnimalShelter()
    animal_shelter.enqueue_animal("dog")
    actual = animal_shelter.dog.rear.data

    assert expected == actual

def test_dequeues_dog():
    expected = "dog"
    animal_shelter=AnimalShelter()
    animal_shelter.enqueue_animal("dog")
    animal_shelter.enqueue_animal("dog")
    animal_shelter.dequeue_animal("dog")
    actual = animal_shelter.dog.rear.data

    assert expected == actual
