from survey import AnonymousSurvey

#定义一个问题，并创建这个问题的实例
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

#显示问题，并存储答案
my_survey.show_question()
print("Enter 'q' an any time to quit.\n")
while True:
    response = input("Language:")
    if response == 'q':
        break
    my_survey.store_response(response)

#显示调査结果
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
