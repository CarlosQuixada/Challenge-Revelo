from minimum_qualifications.util_minimum_qualifications import UtilMinimumQualification


class MinimunQualification:
    def __init__(self, data_job):
        self.data_job = data_job
        self.__util_minimum_qualification = UtilMinimumQualification()

    def minimum_qualifications_identifier(self):
        list_minimum_qualifications = self.data_job['Minimum Qualifications'].values

        top_qualifications = []
        for minimum_qualification in list_minimum_qualifications:
            top_qualifications.extend(self.__util_minimum_qualification.process_quali(minimum_qualification))

        return top_qualifications
