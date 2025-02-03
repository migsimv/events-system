import uvicorn
from .config import ConsumerConfig
from .database import Database
from .api import init_api, app

def main():
    config = ConsumerConfig.from_yaml("config/consumer_config.yaml")
    database = Database(config.database_url)
    init_api(database)
    
    uvicorn.run(app, host="0.0.0.0", port=config.port)

if __name__ == "__main__":
    main()