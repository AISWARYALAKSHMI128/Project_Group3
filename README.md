# Project_Group3
<b><font size=8>TITLE</font> </b><br>
<b><font size=6>Airline Dataset</font><b>

<b>DESCRIPTION</b>
This is a simple Flask Application designed to visualize data in a tabular form from an SQLite database containing airline passengers information.The application serves webpages to display a various aspects of the data, including a Homepage, an About page and a page displaying a table of passenger data.

<b>INSTALLATION</b>
    STEP 1: Clone the project repository to your Local machine.
             https://github.com/AISWARYALAKSHMI128/Project_Group3
    
    STEP 2: Navigate to Project Directory

    STEP 3: Install dependencies/Libraries using pip.
            pip install -r requirements.txt

<b>USAGE</b>
    STEP 1: Once installed, navigate to project directory in your terminal.
    STEP 2: Run the Flask application be executing the following command:
            python app_template_detail_2.py
    STEP 3: Open your web browser and go to 
            http://127.0.0.1:5000  to view the Home page of the application.
            or follow the link in the terminal after running the python file.
    STEP 4: Navigate through the different pages using navigation links provided.

<b>PROJECT STRUCTURE</b>
        1. app_template_detail_2.py : The is the main Flask application file containing the routes and logics for serving webpages.
        2. templates/ :This directory contains HTML templates used to render the webpages.
                    <ul>
                    <li>index_links.html : Home page template with links to other pages</li>
                    <li>about.html: The about pages gives a brief description about the dataset and variables.</li>
                    <li>data_table.html: Template for displaying the passenger data table.<li>
                    </ul>
        3. create_db.ipynb: This jupyter notebook creates the SQLite database for storing the passenger data.
        4. Airlines.db: SQLite database file containing the Airline passenger data.
        5. README.md : THis file provides the information about the project.
        6. AirlineDataset.csv: The csv file of Airline Dataset.
        7. requirements.txt: The text file containing all the dependencies and libraries needed to run the project.

<b>CONTRIBUTING</b>
Contributions are welcome! Feel free to open issues or pull requests for any improvements or new features you would like to see.
    