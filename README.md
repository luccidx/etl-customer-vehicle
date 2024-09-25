# ETL Customer-Vehicle Project

## Table of Contents
- [Project Overview](#project-overview)
- [Folder Structure](#folder-structure)
- [ETL Pipelines](#etl-pipelines)
  - [Customer Demography](#customer-demography)
  - [Vehicle Makes](#vehicle-makes)
- [How to Run the Project](#how-to-run-the-project)
- [Logging](#logging)
- [License](#license)

## Project Overview

This project aims to extract, transform, and load (ETL) data related to customers and vehicle makes. It consists of two main ETL pipelines:
1. **Customer Demography Pipeline**: Processes and transforms customer demographic data.
2. **Vehicle Makes Pipeline**: Processes and transforms vehicle make data.

The project is designed to read data from raw sources, apply necessary transformations, and load the transformed data into a CSV format.

## Folder Structure

The project structure is as follows:

```bash
etl-customer-vehicle-main/
│
├── ETL_Customer_Demography/
│   ├── Data/                    # Raw customer demographic data files
│   ├── ETL_CustomerDemography.py # Script for ETL on customer data
│   ├── log_file.txt              # Log file for customer demography ETL process
│   └── transformed_data.csv      # Transformed customer data output
│
├── ETL_Vehicle_Makes/
│   ├── Data/                    # Raw vehicle make data files
│   ├── ETL_Vehicle_Makes.py      # Script for ETL on vehicle makes data
│   ├── log_file.txt              # Log file for vehicle makes ETL process
│   └── transformed_data.csv      # Transformed vehicle make data output
│
├── CODE_OF_CONDUCT.md            # Contributor guidelines
├── LICENSE                       # License information
├── README.md                     # Project documentation (this file)
```

## ETL Pipelines

### Customer Demography

The **Customer Demography Pipeline** is responsible for processing customer demographic data. The `ETL_CustomerDemography.py` script:
- Reads raw demographic data from the `Data/` directory.
- Applies necessary transformations such as data cleansing, normalization, and filtering.
- Saves the transformed data into `transformed_data.csv`.

### Vehicle Makes

The **Vehicle Makes Pipeline** processes vehicle make data. The `ETL_Vehicle_Makes.py` script:
- Reads raw vehicle make data from the `Data/` directory.
- Applies necessary transformations like data enrichment, formatting, and deduplication.
- Outputs the processed data into `transformed_data.csv`.

## How to Run the Project

To execute the ETL pipelines, follow the steps below:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/luccidx/etl-customer-vehicle.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd etl-customer-vehicle-main
    ```

3. **Run the Customer Demography ETL pipeline**:
    ```bash
    python ETL_Customer_Demography/ETL_CustomerDemography.py
    ```

4. **Run the Vehicle Makes ETL pipeline**:
    ```bash
    python ETL_Vehicle_Makes/ETL_Vehicle_Makes.py
    ```

The transformed data will be available as `transformed_data.csv` in their respective directories.

## Logging

Each ETL pipeline logs its activities to a `log_file.txt` located in their respective directories. This log file captures key activities such as data reading, transformation, and any issues encountered during the process.

## License

This project is licensed under the terms of the [MIT License](LICENSE).
