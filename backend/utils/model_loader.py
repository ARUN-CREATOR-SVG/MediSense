import os
import pickle
import logging
from backend.utils.pneumonia_arch import build_pneumonia_model

logger = logging.getLogger(__name__)

MODEL_DIR = os.path.join(os.path.dirname(__file__), '..', 'models')
MODEL_DIR = os.path.abspath(MODEL_DIR)


models = {}

def get_model(name):
    global models
    if name in models:
        return models[name]

    try:
        if name == 'pneumonia':
            model = build_pneumonia_model()
            weights_path = os.path.join(MODEL_DIR, 'xray_model.weights.h5')
            model.load_weights(weights_path)
        else:
            filename = {
                'heart': 'Heart_Disease_model.pkl',
                'liver': 'LiverDiseaseModel.pkl',
                'diabetes': 'diabetes_model.pkl',
            }.get(name)

            if filename is None:
                raise ValueError(f"Unknown model name: {name}")

            with open(os.path.join(MODEL_DIR, filename), 'rb') as f:
                model = pickle.load(f)

        models[name] = model
        logger.info(f"{name.capitalize()} model loaded")
        return model

    except Exception as e:
        logger.error(f"Failed to load {name} model: {e}")
        raise