from collections import Counter
from skills.util_skill import UtilSkill
from minimum_qualifications.util_minimum_qualifications import UtilMinimumQualification


class Skill:
    def __init__(self, data_job):
        self.__category_ti = ['Data Center & Network', 'Developer Relations', 'Hardware Engineering',
                            'IT & Data Management',
                            'Network Engineering', 'Software Engineering', 'Technical Infrastructure',
                            'User Experience & Design']

        self.__data_job = data_job
        self.__util_skill = UtilSkill()
        self.__util_minimum_qualification = UtilMinimumQualification()

    def __pre_process_minimum_qualifications(self, qualifications):
        minimum_qualifications = []

        for qualification in qualifications:
            result = self.__util_minimum_qualification.process_quali(qualification)
            minimum_qualifications.extend(result)

        return minimum_qualifications

    def skill_identifier(self):
        skill_ti = []

        for category in self.__category_ti:
            data = self.__data_job[self.__data_job['Category'] == category]

            skill_ti.extend(self.__util_skill.process_skill(data['Preferred Qualifications'].values))
            skill_ti.extend(self.__pre_process_minimum_qualifications(data['Minimum Qualifications'].values))

        counts = Counter(skill_ti)
        list_top_skills = dict(counts.most_common(20))

        return list_top_skills
