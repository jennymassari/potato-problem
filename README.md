# potato-problem
Problem to be completed during Industry Prep - Interview Prep activity time

## Problem Statement

A potato is a plant that has multiple parts, such as leaves, berries, and tubers (the tubers are the actual starchy root vegetables that grow underground).

Our goal will be to create classes that model a potato plant and its tubers.

### Wave 1

Provided for you is a `Plant` class. This `Plant` class should NOT be modified. Instead, you should make a new class, `Potato` that is a subclass of `Plant`.

Each potato should have two instance variables, `energy` and `tubers`. `energy` should be a number that represents how much energy the potato plant itself currently has. `tubers` should be a list containing the tubers the potato plant has.

The `Potato`'s constructor should take a starting energy and set its own energy to that starting energy. The potato should start off with no tubers.

### Wave 2

You should create a class, `Tuber`. It should have an instance variable `energy` which is a number that represents how much energy the tuber has. A `Tuber` begins with 30 energy.

You should add an instance method to `Potato`, `sprout_tuber`. It should create a new tuber and add it to that potato's list of tubers. It should also decrease the potato plant's energy by 30.

If the potato has less than 30 energy, no action should be taken when this function is called.

### Wave 3

In the `Potato` class you should override the `absorb_sunlight` method. It should accept the same arguments as before. However, if the potato plant has tubers, it should distribute the new sunlight_energy as follows:

  - The potato plant itself receives half of the sunlight_energy.
  - The remaining sunlight_energy is split evenly between the potato's tubers.

If the potato plant has no tubers, the plant receives all the energy.

## Notes for the Interviewer

### Delivery Notes

#### THIS QUESTION IS MEANT TO BE DONE ONE WAVE AT A TIME!

- Please only explain the first wave to your interviewee first. Do not discuss the second wave or have them begin implementation on it until they have the first wave fully working. Progress in this fashion for each wave.

#### THE TESTS ARE HELPFUL!

- Encourage your interviewee to closely look at the tests before they begin implementation.

### Clarifying Questions

#### Q: How should I handle invalid input? 
A: You can assume the input will be valid.

#### Q: Can I modify the Plant class?
A: No.

#### Q: Should the energies be ints or floats?
A: Either should work for the given test cases.

#### Q: Where can I learn more about potatoes?
A: "The History and Social Influence of the Potato" by Dr. Redcliffe N. Salaman.

### Hints

- Make sure your candidate's classes aren't accidentally indented and inside the Plant class! If you see your candidate do this, you can immediately let them know.

- If your candidate is struggling to form an algorithm, encourage them to explain how they would do it by hand. Afterwards help them to see what data structures might be useful.
