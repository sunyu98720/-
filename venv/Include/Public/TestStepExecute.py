from Common.ReadSQL import Read_sql
from Public.Action_Method import Action_Method
from tqdm import tqdm


class TestStepExecute:
    last_func_data = ''

    def __init__(self):
        self.Func_object = Action_Method()  # 初始化函数库

    def function_execute(self, func, handle_value=None, send_value=None, expect_result=None,actual_result=None,error_des=None):  # 利用反射执行函数
        u"""
        :param func:执行函数
        :param handle_value:操作
        :param send_value:函数所需值
        :param expect_result:预期结果
        :param actual_result:实际结果
        :param error_des:错误描述
        :return:
        """
        if func is not None:
            if hasattr(self.Func_object, func):  # 判断函数库中有没有此函数
                # 利用反射读取函数并执行
                function_data = getattr(self.Func_object, func)
                if send_value is None or send_value == '':
                    if handle_value is None or handle_value == '':
                        self.last_func_data = function_data()
                        return
                    else:
                        self.last_func_data = function_data(handle_value,expect_result,actual_result,error_des) if all([expect_result,actual_result,error_des]) else function_data(handle_value)
                        return
                else:
                    self.last_func_data = function_data(handle_value, self.last_func_data if send_value[0] == '#' else send_value)
                    return
            else:  # 没有函数则报错
                raise Exception("当前对象库中没有此函数:%s" % func)
        print("函数不能为空")

    def step_execute(self, case_number):  # 执行测试步骤,动作级别
        sql = "select * from test_step_execute where case_number = '%s' order by step " % case_number
        cases = Read_sql(sql).sqlExecute()
        print("开始执行用例:{%s}" % case_number)
        for case in tqdm(cases):
            if case['execute'] == 1:  # 为1执行当前步骤,不为1跳过执行
                if case['method']:
                    self.function_execute(case['method'], case['handle'], case['send_value'],case['expect_result'],case['actual_result'],case['error_des'])
                    # print("当前执行步骤:%s" % case['describe'],",当前执行函数:%s" % case['method'])
            else:
                continue

    def step_module_execute(self,to_project,case_number): # 执行测试步骤,模块级
        # sql_module = "select * from test_step_module_execute where belong_to_project = '%s',"
        # "test_suit = '%s'," order by step"
        sql_module = (
            " select * from test_step_module_execute"
            " where belong_to_project = '%s'"# 那个项目
            " and test_suit = '%s'"# 那个模块(套件)
            " order by step" % (to_project,case_number)
        )
        cases = Read_sql(sql_module).sqlExecute()
        for case in cases:
            if case['whether_execute'] == 1:
                self.step_execute(case['case_name'])
            else:
                continue



if __name__ == '__main__':
    test = TestStepExecute()
    test.step_module_execute("noah","test")
