# Predictive-Student-Dropout-Prevention-System

## Project Description

This project is part of a university database course, integrating SQL and Recurrent Neural Network (RNN) skills to develop a system that automatically analyzes student data from Excel or CSV files. The system identifies students at risk of dropping out and provides insights to help educators and administrators take preventive measures.

## How It Works

1. **Data Upload**: Users upload their Excel or CSV files containing student data.
2. **Data Analysis**: The system processes the data, leveraging SQL for database management and RNN for predictive analysis.
3. **Results**: The system outputs a list of students at risk of dropping out, along with relevant insights and recommendations.

## Requirements

- Python 3.7+
- SQL Database (e.g., MySQL, PostgreSQL)
- Required Python libraries (listed in `requirements.txt`)

## Setup

1. Clone the repository:
    ```bash
    git clone /u:/DS PROJECTS/predictive student dropout prevention
    ```
2. Navigate to the project directory:
    ```bash
    cd predictive student dropout prevention
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up the SQL database and configure the connection settings in `config.py`.

## Running the Project

1. Upload the dataset (Excel or CSV) to the `uploads` directory.
2. Run the data analysis script:
    ```bash
    python analyze.py
    ```
3. View the results:
    ```bash
    python view_results.py
    ```

## Technologies Used

- Python
- SQL (MySQL, PostgreSQL)
- Recurrent Neural Networks (RNN)
- Pandas
- Streamlit (for dashboard)

## Contact

For any questions or support, please contact Huzaifa Rashid at huzaifaras10@gmail.com.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.