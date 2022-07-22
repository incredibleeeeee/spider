import requests
import json
import time
from random import randint


# 根据自己情况填写self.get_info_headers、self.score_headers

class Score:
    def __init__(self):
        self.USER_AGENTS = [
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        ]

        self.get_info_headers = {
        }

        self.score_headers = {
        }

    def get_info(self):
        url = 'https://jwxt.nwpu.edu.cn/evaluation-student-backend/api/v1/student/summative-evaluation/task/semester/178'

        response = requests.get(url=url, headers=self.get_info_headers)

        response.encoding = 'utf-8'

        response = json.loads(response.text)
        response = response['data']

        taskIds = []
        surveyIds = []
        for i in response:
            taskId = i['id']
            lesson_name = i['lesson']['course']['nameZh']
            surveyId = i['survey']['id']
            print(taskId, end='\t')
            print(lesson_name, end='\t')
            print(surveyId)
            taskIds.append(taskId)
            surveyIds.append(surveyId)

        return (taskIds, surveyIds)
        # print(taskIds, end='\t')
        # print(surveyIds)

    def score(self, list):
        url = 'https://jwxt.nwpu.edu.cn/evaluation-student-backend/api/v1/student/summative-evaluation/result'

        data = {
            'score': '100',
            'answers[0].questionId': '3b528bf7-921c-44f5-b7ea-e5af8535abef',
            'answers[0].questionTitle': '我了解这门课程的教学目标',
            'answers[0].result': '非常同意',
            'answers[0].score': '5',
            'answers[0].checkedArr': '',
            'answers[0].radioName': '非常同意',
            'answers[1].questionId': '6e115e36-498f-461d-b44e-f54c651dc3ef',
            'answers[1].questionTitle': '我认为这门课程教学内容丰富，对我的价值观体系给予有效引导',
            'answers[1].result': '非常同意',
            'answers[1].score': '5',
            'answers[1].checkedArr': '',
            'answers[1].radioName': '非常同意',
            'answers[2].questionId': '03fafa86-f175-422b-86ae-8cdf25c3def8',
            'answers[2].questionTitle': '我认为本课程的课程资源内容鲜活，具有针对性、可读性、时效性',
            'answers[2].result': '非常同意',
            'answers[2].score': '5',
            'answers[2].checkedArr': '',
            'answers[2].radioName': '非常同意',
            'answers[3].questionId': 'ed98b6d9-e8f5-4275-a828-feacea0736d1',
            'answers[3].questionTitle': '我认为教师授课过程中能够引导和启发我们如何做人做事',
            'answers[3].result': '非常同意',
            'answers[3].score': '10',
            'answers[3].checkedArr': '',
            'answers[3].radioName': '非常同意',
            'answers[4].questionId': 'b26fc101-e1ef-459c-b936-e8a206919511',
            'answers[4].questionTitle': '我认为老师如实做好课堂考勤记录，善于管理课堂纪律',
            'answers[4].result': '非常同意',
            'answers[4].score': '10',
            'answers[4].checkedArr': '',
            'answers[4].radioName': '非常同意',
            'answers[5].questionId': '369a8ae9-e355-4d5e-9fc3-9c9fce529512',
            'answers[5].questionTitle': '我认为老师备课认真充分，授课时精神饱满，讲课清晰流畅',
            'answers[5].result': '非常同意',
            'answers[5].score': '10',
            'answers[5].checkedArr': '',
            'answers[5].radioName': '非常同意',
            'answers[6].questionId': '9db9a3d3-18c5-4044-be95-fecd324eb3b0',
            'answers[6].questionTitle': '我认为教师能够结合课程特点灵活选用教学方法',
            'answers[6].result': '非常同意',
            'answers[6].score': '10',
            'answers[6].checkedArr': '',
            'answers[6].radioName': '非常同意',
            'answers[7].questionId': '8c549190-5e5d-4c4b-9fe6-7fbe9afa4b72',
            'answers[7].questionTitle': '我认为教师能有效运用各种方式激发我的学习兴趣',
            'answers[7].result': '非常同意',
            'answers[7].score': '5',
            'answers[7].checkedArr': '',
            'answers[7].radioName': '非常同意',
            'answers[8].questionId': '1fd23ff0-8353-4e45-ab93-2eeec48b1544',
            'answers[8].questionTitle': '我认为教师能积极回应我的问题，课程研讨、答疑辅导等及时有效',
            'answers[8].result': '非常同意',
            'answers[8].score': '10',
            'answers[8].checkedArr': '',
            'answers[8].radioName': '非常同意',
            'answers[9].questionId': '74950b0c-8ebd-400f-8ff6-ad2c2d3f755d',
            'answers[9].questionTitle': '我被鼓励积极参与到课堂活动中，有机会与同学互动交流',
            'answers[9].result': '非常同意',
            'answers[9].score': '5',
            'answers[9].checkedArr': '',
            'answers[9].radioName': '非常同意',
            'answers[10].questionId': 'e03607c1-7a4e-4f91-b4f7-1f6b166be5f1',
            'answers[10].questionTitle': '通过这门课程学习，我的理论知识水平得到提升',
            'answers[10].result': '非常同意',
            'answers[10].score': '5',
            'answers[10].checkedArr': '',
            'answers[10].radioName': '非常同意',
            'answers[11].questionId': '6f2f27ea-50c3-467a-b301-3f2e9079e4cf',
            'answers[11].questionTitle': '通过这门课程学习，我的整体能力水平得到提升',
            'answers[11].result': '非常同意',
            'answers[11].score': '5',
            'answers[11].checkedArr': '',
            'answers[11].radioName': '非常同意',
            'answers[12].questionId': 'd70d3a2b-b010-47bd-bf26-fc4f68f99f22',
            'answers[12].questionTitle': '通过这门课程学习，我的整体水平得到提升(1至10, 1代表不满意,，依次递增，10代表非常满意)',
            'answers[12].result': '非常同意',
            'answers[12].score': '5',
            'answers[12].checkedArr': '',
            'answers[12].radioName': '非常同意',
            'answers[13].questionId': 'f910ce41-5d0f-4e99-a9e2-408a77a6d114',
            'answers[13].questionTitle': '我对这门课程的总体满意度',
            'answers[13].result': '非常同意',
            'answers[13].score': '10',
            'answers[13].checkedArr': '',
            'answers[13].radioName': '非常同意',
            'answers[14].questionId': '133c775c-157e-4dcf-ba43-118a2247a467',
            'answers[14].questionTitle': '我对这门课程的整体评价以及建议',
            'answers[14].result': '无',
            'answers[14].checkedArr': '',
            'taskId': '',
            'surveyId': '',
        }

        taskIds = list[0]
        surveyId = list[1]

        for i, j in zip(taskIds, surveyId):
            random_agent = self.USER_AGENTS[randint(0, len(self.USER_AGENTS) - 1)]
            self.score_headers['User-Agent'] = random_agent
            # print(self.score_headers['User-Agent'])
            data['taskId'] = i
            data['surveyId'] = j
            response = requests.post(url=url, headers=self.score_headers, data=data)
            response.encoding = 'utf-8'
            print(data['taskId'], end='\t')
            print(data['surveyId'], end='提交结果：')
            print(response.text)
            time.sleep(8)


if __name__ == '__main__':
    test = Score()
    list = test.get_info()
    time.sleep(5)
    test.score(list)
