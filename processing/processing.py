from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import processing.utils as utils


class PreProcessing:
    """
        Essa classe é utilizada na etapa de limpeza de dados, é onde tem todas as funções para limpar dados string
    """

    def __init__(self):
        self.stop_words = set(stopwords.words("english"))
        self.more_stopwords = utils.MORE_STOPWORDS
        self.more_stopwords_cloud_minimum_qualifications = utils.MORE_STOPWORDS_CLOUD_MINIMUM_QUALIFICATIONS
        self.punctuations = utils.PUNCTUATIONS

    def remove_punctuation(self, text):
        """
            Método responsável por remover pontuação do texto
        :param text: texto que terá pontuação removidas
        :return: retorna o texto sem pontuação
        """

        for punct in self.punctuations:
            text = text.replace(punct, ' ')

        return text

    def remove_number(self, text):
        """
            Método responsável por remover números do texto
        :param text: texto que terá números removidos
        :return: texto sem números
        """

        text = ''.join(word for word in text if not word.isdigit())

        return text

    def remove_detail(self, text):
        """
            Método responsável por remover alguns detalhes adicionais no texto
        :param text: texto que terá detalhes do texto removido
        :return: texto sem os detalhes
        """

        text = text.replace(' e g ', ' ')
        text = text.replace('etc', ' ')
        text = text.replace('; ;', ' ; ')
        text = text.replace('  ', ' ')

        return text

    def remove_stop_words(self, text):
        """
            Método responsável por remover as stopwords já existentes no nltk e as que foram adicionadas no arquivo
            utils.py.

        :param text: review que terá stopwords removidas.
        :return: texto sem stopwords.
        """

        text = self.remove_punctuation(text)
        text = ' '.join([word for word in word_tokenize(text) if word not in self.stop_words])
        text = ' '.join([word for word in word_tokenize(text) if word not in self.more_stopwords])

        text = self.remove_number(text)

        return text

    def remove_stop_words_cloud_minimum_qualifications(self, text):
        """
            Essa função remove as stopwords já existentes no nltk e as que foram adicionadas no arquivo utils.py.

        :param text: review que terá stopwords removidas.
        :return: retorna o texto sem stopwords.
        """
        text = ' '.join(
            [word for word in word_tokenize(text) if word not in self.more_stopwords_cloud_minimum_qualifications])

        return text