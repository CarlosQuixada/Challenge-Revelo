from processing.processing import PreProcessing


class UtilSkill:
    def __init__(self):
        self.process = PreProcessing()

    def maker_data_graph_bar(self, data_top):
        skills = [skill for skill in data_top]
        valores = [valor for valor in data_top.values()]

        return skills, valores

    def process_skill(self, skills):
        list_skills = []

        for skill in skills:
            skill = skill.replace('\n', ' ; ').replace(', ', ' ; ')
            skill = self.process.remove_number(skill)
            skill = self.process.remove_stop_words(skill.lower())
            list_skills.extend(skill.split(' ; '))
            list_skills = [s.replace(' ;', '').replace('; ', '') for s in list_skills]

        return list_skills
