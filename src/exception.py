import sys


def error_message_details(error, error_detail: sys):
    # Extract the traceback object
    _, _, exc_tb = error_detail.exc_info()
    
    # Get the filename where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Properly pass the variables into the .format() method
    error_message = (
        "Error occurred in python script name [{0}] "
        "line number [{1}] error message [{2}]"
    ).format(file_name, exc_tb.tb_lineno, str(error))
    
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Call the parent Exception class constructor properly
        super().__init__(error_message)
        
        # Generate and store the detailed error message
        self.error_message = error_message_details(
            error_message, error_detail=error_detail
        )
        
    def __str__(self):
        # Ensure the detailed message prints when the exception is raised
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        custom_exception = CustomException(e, sys)
        print(custom_exception)
        