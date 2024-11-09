# Importing necessary modules
import os  # Provides functions for interacting with the operating system, such as file paths
import sys  # Provides access to system-specific parameters and functions, including exception details

# Function to capture detailed information about an error (e.g., filename, line number, error message)
def error_message_detail(error, error_detail: sys):
    # Extracting exception traceback information
    _, _, exc_tb = error_detail.exc_info()  # Extract the exception type, value, and traceback

    # Getting the filename from the traceback frame where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Formatting the error message with the filename, line number, and the error description
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)  # Getting the line number and error message
    )

    return error_message  # Returning the formatted error message


# Custom exception class that inherits from the built-in Exception class
class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        """
        Initializes a new CustomException instance.
        
        :param error_message: The error message in string format that describes the error.
        :param error_detail: The details of the error, typically the sys module's exception traceback.
        """
        super().__init__(error_message)  # Calling the base class (Exception) constructor with the error message
        
        # Capturing and storing detailed information about the error using the error_message_detail function
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail  # Passing the error message and error detail (sys) to the function
        )

    def __str__(self):
        # This method returns the string representation of the exception, which is the detailed error message
        return self.error_message  # Returning the detailed error message to be used when the exception is printed
