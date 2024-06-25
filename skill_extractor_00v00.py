#importing libraries.
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

#function to extract in demand skills form job description.
def extract_skills_nltk(job_description):
    #tokenize the job description.
    tokens = nltk.word_tokenize(job_description)
    #tag parts of speech.
    tagged = nltk.pos_tag(tokens)
    #extract nouns and potential skills.
    skills = [word for word, pos in tagged if pos in ['NN', 'NNS']]
    return skills