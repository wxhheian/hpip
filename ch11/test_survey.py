import unittest
from survey import AnonymousSurvey

# class TestAnonymousSurvey(unittest.TestCase):
#     """针对AnonymousSurvey类的测试"""
#
#     def test_store_single_response(self):
#         """测试单个答案会被妥善存储"""
#         question = "What language did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#         my_survey.store_response('English')
#
#         self.assertIn('English',my_survey.responses)
#
#     def test_store_three_responses(self):
#         """测试三个答案被妥善存储"""
#         question = "What language did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#         responses = ['English','French','Chinese']
#         for response  in responses:
#             my_survey.store_response(response)
#
#         for response in responses:
#             self.assertIn(response,my_survey.responses)

#利用unittest.TestCase类中的setUp方法
class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""


    def setUp(self):
        """创建一个调査对象和一组答案，供使用的测试方法使用"""
        question1 = "What language did you first learn to speak?"
        question2 = "What is your favorite food?"
        self.my_survey = AnonymousSurvey(question1)               #创建实例self, my_survey作为实例的属性
        self.responses = ['English','Chinese','French']             #response作为self的属性


    def test_store_single_response(self):
        """测试单个答案会被妥善存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)



    def test_store_three_responses(self):
        """测试三个答案被妥善存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

unittest.main()
