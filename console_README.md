# Code Readme

This code is a Python script that retrieves tick-by-tick market data for a specific futures contract using the Interactive Brokers API (IB API) through
the `ib_insync` library. It connects to the local IB Gateway on the specified port, 
qualifies the contract, and then requests tick-by-tick data for the contract.


## Prerequisites

Before running this code, ensure that you have met the following requirements:

- Python 3.x is installed on your system.
- The `ib_insync` library is installed. You can install it using `pip install ib_insync`.

## Usage

1. Modify the `contract` object to specify the contract details you want to retrieve tick data for. The example code is set up to retrieve data for the FDAX futures contract on the EUREX exchange.
2. Run the Python script using the command `python script_name.py`, where `script_name.py` is the name of the Python file containing the code.
3. The script will establish a connection to the IB Gateway on `localhost` using port `4002` with a client ID of `1`.
4. The script will qualify the contract by requesting contract details from the IB API.
5. Tick-by-tick data for the contract will be requested and printed every 2 seconds.
6. To stop the script, press `Ctrl + C`.

## Disclaimer

This code is provided as a sample and is not intended for use in production environments. It demonstrates how to retrieve tick-by-tick data using the IB API and `ib_insync` library. Make sure to review and modify the code as necessary to fit your specific requirements and trading strategies.

Please note that using the IB API  requires a valid Interactive Brokers account and proper authentication credentials. Make sure to configure your IB Gateway or TWS (Trader Workstation) appropriately before running this code.

## License

This code is released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and distribute it as needed.
