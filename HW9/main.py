from scraper1 import quotes_scraper, db_loader, models

def main():

    quotes_scraper.scrape_quotes()
    db_loader.load_data()
    models.setup_models()

if __name__ == "__main__":
    main()