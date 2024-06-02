This Python project is a web scraper that collects job statistics and saves the data into a MongoDB database. It uses Selenium for browser automation and requests for HTTP requests. The locators for web elements are stored in a separate `locators.py` file. You will need to insert your login and password for the job portal at line 56 in `main.py`.

## Features

- Uses Selenium for browser automation.
- Uses requests for making HTTP requests.
- Saves scraped data into a MongoDB database.
- Stores web element locators in a separate `locators.py` file.
- Includes a requirements file for easy setup of dependencies.

## Requirements

- Python 3.7 or higher
- `selenium` library
- `requests` library
- `pymongo` library
- `beautifulsoup4` library
- A MongoDB database

## Installation

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/MOrgacki/selenium-jobstatistics-webscraper.git
   ```

2. Navigate to the project directory.

   ```bash
   cd selenium-jobstatistics-webscraper
   ```

3. Create a virtual environment.

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment.

   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   On macOS and Linux:
   ```bash
   source venv/bin/activate
   ```

5. Install the required dependencies.

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Open `main.py` in a text editor.

2. Insert your login and password for the job portal at line 56.

   ```python
   login = 'your_login'
   password = 'your_password'
   ```

3. Ensure your MongoDB database is running and accessible. You may need to configure the MongoDB connection settings in `main.py`.

## Usage

1. Run the script.

   ```bash
   python main.py
   ```

2. The script will automate the browser, log into the job portal, scrape job statistics, and save the data into your MongoDB database.

## File Structure

- `main.py`: The main script to run the web scraper.
- `locators.py`: Contains the locators for web elements used by Selenium.
- `requirements.txt`: Lists the required dependencies for the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project uses the [Selenium](https://www.selenium.dev/) library for browser automation.
- The [requests](https://docs.python-requests.org/en/master/) library is used for making HTTP requests.
- The [pymongo](https://pymongo.readthedocs.io/en/stable/) library is used for interacting with MongoDB.
- The [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library is used for parsing HTML content.

---

Feel free to contribute to this project by opening issues and submitting pull requests. For major changes, please open an issue first to discuss what you would like to change.

Happy scraping!
