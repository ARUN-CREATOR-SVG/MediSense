import os
import pickle
import logging
from utils.pneumonia_arch import build_pneumonia_model

logger = logging.getLogger(__name__)

MODEL_DIR = os.path.join(os.getcwd(), 'models')

def load_models():
    models = {}
    model_files={
        'heart':'Heart_Disease_model.pkl',
        'liver':'LiverDiseaseModel.pkl',
        'diabetes':'diabetes_model.pkl'
    }
    try:
        for key, filename in model_files.items():
            path = os.path.join(MODEL_DIR, filename)
            with open(path, 'rb') as f:
                models[key] = pickle.load(f)
                logger.info(f"{key.capitalize()} model loaded")

        
        pneumonia_model = build_pneumonia_model()
        pneumonia_weights_path = os.path.join(MODEL_DIR, 'xray_model.weights.h5')
        pneumonia_model.load_weights(pneumonia_weights_path)
        models['pneumonia'] = pneumonia_model
        logger.info("Pneumonia model loaded")

    except Exception as e:
        logger.error(f"Model Load error: {e}")

    return models