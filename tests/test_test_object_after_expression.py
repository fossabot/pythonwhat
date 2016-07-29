import unittest
import helper

class TestExercise1(unittest.TestCase):

    def setUp(self):
        self.data = {
            "DC_PEC": '''''',
            "DC_CODE": '''
def shout():
    shout_word = 'congratulation' + '!!!'
    return(shout_word)
            ''',
            "DC_SOLUTION": '''
def shout():
    shout_word = 'congratulations' + '!!!'
    return(shout_word)
'''
        }

    def test_Pass(self):
        self.data["DC_SCT"] = '''
# Test the value of shout_word
test_function_definition("shout", arg_names = False,body = lambda: test_object_after_expression("shout_word",undefined_msg = "have you defined `shout_word`?", incorrect_msg = "test"))
success_msg("Nice work!")
        '''
        sct_payload = helper.run(self.data)
        self.assertFalse(sct_payload['correct'])
        self.assertEqual(sct_payload['message'], 'In your definition of <code>shout()</code>, test')
        helper.test_lines(self, sct_payload, 3, 3, 5, 41)

    def test_Pass2(self):
        self.data["DC_SCT"] = '''
# Test the value of shout_word
test_function_definition("shout", arg_names = False, body = lambda: test_object_after_expression("shout_word", undefined_msg = "have you defined `shout_word`?"))
success_msg("Nice work!")
        '''
        sct_payload = helper.run(self.data)
        self.assertFalse(sct_payload['correct'])
        self.assertEqual(sct_payload['message'], 'In your definition of <code>shout()</code>, are you sure you assigned the correct value to <code>shout_word</code>?')
        helper.test_lines(self, sct_payload, 3, 3, 5, 41)

if __name__ == "__main__":
    unittest.main()