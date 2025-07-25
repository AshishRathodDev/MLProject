import logging
import os
from datetime import datetime

from networkx import has_path


LOG_FILE =f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_folder=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_folder,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_folder,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    
    
) 

if __name__=="__main__":
    logging.info("Logging has started")