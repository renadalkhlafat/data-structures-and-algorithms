from stack_and_queue.stack_queue_animal_shelter import AnimalShelter

def test_enqueue_cat():
    expected = "cat"
    animal_shelter=AnimalShelter()
    animal_shelter.enqueue_animal("cat")
    actual = animal_shelter.cat.rear.data

    assert expected == actual

