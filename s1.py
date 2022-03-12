from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
class txtSim:
    def cs(teacher_res,student_res):
        sentence=teacher_res+student_res
        model_name = 'bert-base-nli-mean-tokens'
        model = SentenceTransformer(model_name)
        sentences_vect= model.encode(sentence)
        return cosine_similarity([sentences_vect[0]], sentences_vect[1:])
        
    

    




'''
class ab:
    def sqr(var1,var2):
        return math.sqrt(var1*var2)
#dusre python file me library import kara kedirect function acess krk
'''

