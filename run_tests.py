import unittest

from conditionals_challenges import can_climb, red_light_camera, can_ride_rollercoaster, login

class TestCase(unittest.TestCase):
    def test_can_climb(self):        
        for case, message in {
            (False, False, False): "Inputs: \n - has_helmet: False\n - has_rope: False \nYour program would have let the climber climb without a helmet or rope!",
            (True, False, False): "Inputs: \n - has_helmet: True\n - has_rope: False \nYour program would have let the climber climb without a helmet!",
            (False, True, False): "Inputs: \n - has_helmet: False\n - True: False \nYour program would have let the climber climb without a rope!",
            (True, True, True): "Inputs: \n - has_helmet: False\n - has_rope: False \nYour program won't let the climber climb, but they have everything they need!",
        }.items():
            result = can_climb(case[0], case[1])
            
            if type(result) != bool:
                self.fail(msg=f"Inputs: \n - has_helmet: {case[0]}\n - has_rope: {case[1]} \nYour function returned {type(result)} instead of a boolean!")

            self.assertEqual(can_climb(case[0], case[1]), case[2], msg=message)
    
    def test_red_light_camera(self):
        for case in [
            ("Red", True, True),
            ("Amber", True, False),
            ("Green", True, False),
            ("Red", False, False),
            ("Amber", False, False),
            ("Green", False, False),
        ]:
            result = red_light_camera(case[0], case[1])
            
            if type(result) != bool:
                self.fail(msg=f"Inputs: \n - light_colour: {case[0]}\n - car_detected: {case[1]} \nYour function returned {type(result)} instead of a boolean!")

            self.assertEqual(red_light_camera(case[0], case[1]), case[2], msg=f"Inputs: \n - light_colour: {case[0]}\n - car_detected: {case[1]} \nYour function should have returned {case[2]} but instead returned {result}!")

    def test_can_ride_rollercoaster(self):
        for case in [
            (100.0, False, "the rider is too short"),
            (200.0, True, "the rider is tall enough"),
            (120.0, False, "the rider is exactly 120cm tall (they need to be TALLER than 120cm)"),
        ]:
            result = can_ride_rollercoaster(case[0])

            if type(result) != bool:
                self.fail(msg=f"Input: {case[0]} \nYour function returned {type(result)} instead of a boolean!")

            self.assertEqual(result, case[1], msg=f"At {case[0]}cm, {case[2]}. But your function returned {result}!")

    def test_login(self):
        for case in [
            ("PASSWORD123", False),
            ("quartzgleam?1", True)
        ]:
            result = login(case[0])

            if type(result) != bool:
                self.fail(msg=f"Input: {case[0]} \nYour function returned {type(result)} instead of a boolean!")

            self.assertEqual(result, case[1], msg=f"With input {case[0]} your function returned {result}. The password is 'quartzgleam?1!', so the correct result was {case[1]}!")


runner = unittest.TextTestRunner(verbosity=2)

runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(TestCase))))