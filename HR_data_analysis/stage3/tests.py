import ast
from hstest.stage_test import List
from hstest import *

answer_1 = ['support', 'marketing', 'technical', 'hr', 'support', 'sales',
       'hr', 'support', 'technical', 'technical']
answer_2 = 847
answer_3 = [[0.87, 0.72],
            [0.56, 0.36],
            [0.94, 0.93]]

class QuestionTest(StageTest):

    def generate(self) -> List[TestCase]:
        return [TestCase(time_limit=15000)]

    def check(self, reply: str, attach):

        reply = reply.strip()

        if len(reply) == 0:
            return CheckResult.wrong("No output was printed")

        if reply.count('[') < 2 or reply.count(']') < 2:
            return CheckResult.wrong('Print the first and the third answers as a list')
        if len(reply.split('\n')) != 3:
            return CheckResult.wrong('The number of answers supplied does not equal 3')

        reply_1 = reply.split('\n')[0]
        reply_2 = reply.split('\n')[1]
        reply_3 = reply.split('\n')[2]

        index_reply_1_from = reply_1.find('[')
        index_reply_1_to = reply_1.find(']')
        list_str_reply_1 = reply_1[index_reply_1_from: index_reply_1_to + 1]

        index_reply_3_from = reply_3.find('[')
        index_reply_3_to = reply_3.rfind(']')
        list_str_reply_3 = reply_3[index_reply_3_from: index_reply_3_to + 1]

        try:
            list_str_reply_1 = ast.literal_eval(list_str_reply_1)
            reply_2 = ast.literal_eval(reply_2)
            list_str_reply_3 = ast.literal_eval(list_str_reply_3)
        except Exception as e:
            return CheckResult.wrong(f"Seems that output is in wrong format.\n"
                                     f"Make sure you use only the following Python structures in the output: string, int, float, list, dictionary")

        if not isinstance(list_str_reply_1, list):
            return CheckResult.wrong(f'Print 1 answer as a list')

        if not isinstance(reply_2, int):
            return CheckResult.wrong(f'Print 2 answer as an integer')

        if not isinstance(list_str_reply_3, list):
            return CheckResult.wrong(f'Print 3 answer as a list')

        if len(list_str_reply_1) != len(answer_1):
            return CheckResult.wrong(f'Output 1 should contain {len(answer_1)} values, found {len(list_str_reply_1)}')

        if len(list_str_reply_3) != len(answer_3):
            return CheckResult.wrong(f'Output 3 should contain {len(answer_3)} values, found {len(list_str_reply_3)}')

        for j in range(len(list_str_reply_3)):
            if len(list_str_reply_3[j]) != 2:
                return CheckResult.wrong(f'Each of answer 3 list elements are supposed to be a list with 2 values, '
                                         f'got {len(list_str_reply_3[j])} value(s)')


        if int(reply_2) != answer_2:
            return CheckResult.wrong(f'Answer 2 is not correct, got {reply_2}, check if you use summation')

        for i in range(len(list_str_reply_1)):
            if answer_1[i] != list_str_reply_1[i]:
                return CheckResult.wrong(f"Seems like answer is not correct\n"
                                         f"Check element {i} of your 1 answer")

        for i in range(len(list_str_reply_3)):
            for j in range(len(list_str_reply_3[i])):
                if answer_3[i][j] != list_str_reply_3[i][j]:
                    return CheckResult.wrong(f"Seems like answer is not correct\n"
                                             f"Check element {j} in nested list {i} of your 3 answer")


        return CheckResult.correct()


if __name__ == '__main__':
    QuestionTest().run_tests()