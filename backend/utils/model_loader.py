import os
import pickle
import logging

logger = logging.getLogger(__name__)

MODEL_DIR = os.path.join(os.getcwd(), 'models')

def load_models():
    models = {}
    try:
        with open(os.path.join(MODEL_DIR, "Heart_Disease_model.pkl"), 'rb') as f:
            models['heart'] = pickle.load(f)
        logger.info("Heart model loaded")
    except Exception as e:
        logger.error(f"Model load error: {e}")
    return models