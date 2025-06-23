import os
import pickle
import logging

logger = logging.getLogger(__name__)

MODEL_DIR = os.path.join(os.getcwd(), 'models')

def load_models():
    models = {}
    model_files={
        'heart':'Heart_Disease_model.pkl',
        'liver':'LiverDiseaseModel.pkl'
    }
    try:
       for key,filename in model_files.items():
           path=os.path.join(MODEL_DIR,filename)
           with open(path,'rb') as f:
               models[key]=pickle.load(f)
               logger.info(f"{key.capitalize()} model loaded")
    except Exception as e:
        logger.error(f"Model Load error: {e}")
    
    return models