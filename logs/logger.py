# logs/logger.py

import logging
import os
# Create logs directory if it does not exist
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Log file path
log_file = os.path.join(log_dir, "mylogs.log")

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
# Optional: create logger object
logger = logging.getLogger(__name__)

# Test log
logger.info("Logger initialized successfully")