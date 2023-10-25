from Utils import add_logger_name_cls


add_logger_to_class = add_logger_name_cls('analyse')
@add_logger_to_class
class Analyse():
    def __init__(self,score_dict) -> None:
        self.score_dict = score_dict
    
    def analyse(self):
        """
        A function to analyse the score that LLM gets in the testproject, including many testcases.
        The information used for analysis comes from the function get_eval_result in class getinfo.
        By reading the information(a dictionary) provided by the function get_eval_result, this function will create a new log file and write the analysis in it.
        The avarage socre that the LLM gets in testcase will be recorded, and finally the function will give an overall evaluation of the LLM.
        The log file generated by this function is formatted like: 
        "By 'keywords' evaluation, the LLM gets XX(0-1) scores in average.
         By 'toolUsage' evaluation, the LLM gets XX(0-1) scores in average.
         By 'gpt4Eval' evaluation, the LLM gets XX(0-1) scores in average.
         To conclude, the LLM …"
        
        """
        score = self.score_dict
        score_list = []
        score_mean = [0]*10
        score_get = [0]*10
        field_list = ['knowledge_understanding', 'coding', 'common_knowledge', 'reasoning', 'multi_language', 'specialized_knowledge', 'traceability', 'outputformatting', 'internal_security', 'external_security']
        total_score = [0]*10

        for i in range(10):
            score_list.append(score[field_list[i]])

        for i in range(10):
            if score_list[i] == []:
                score_mean[i] = 'Not evaluated in this field'
            else:
                score_mean[i] = float('%.3f'%(sum(score_list[i])/len(score_list[i])))
                total_score[i] = (len(score_list[i]))
                score_get[i] = float('%.3f'%(sum(score_list[i])))
        get_score_info=''

        for i in range (10):
            get_score_info += f'In {field_list[i]} field, the LLM gets "{score_get[i]}/{total_score[i]}" scores.\n'

        mean_score_list=[]
        for score in score_mean:
            if score!='Not evaluated in this field':
                if score>=0.6:
                    mean_score_list.append('does well in')
                else:
                    mean_score_list.append('is not good at')
            else:
                mean_score_list.append('is not evaluated')
        conclude_info = 'To conclude:'
        for i in range (10):
            conclude_info += f'The model {mean_score_list[i]} in {field_list[i]} field.\n'
        print(get_score_info)
        print(conclude_info)
        return(get_score_info,conclude_info)








        
