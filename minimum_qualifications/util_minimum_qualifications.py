from processing.processing import PreProcessing


class UtilMinimumQualification:
    def __init__(self):
        self.process = PreProcessing()

    def maker_data_graph(self, data_top):
        text_min_top = ' '.join(data_top)
        text_min_top_clear = self.process.remove_stop_words_cloud_minimum_qualifications(text_min_top)

        return text_min_top_clear

    def process_quali(self, qualification):
        qualification = qualification.replace('\n', ' ; ').replace(', ', ' ; ').replace(
            'and/or', ' ; ')

        qualification = self.process.remove_number(qualification)
        qualification = self.process.remove_stop_words(qualification.lower())

        list_quali = qualification.split(' ; ')
        list_quali = [s.replace(' ;', '') for s in list_quali]

        return list_quali
