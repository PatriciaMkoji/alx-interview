#!/usr/bin/python3
"""
A method that determines if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """_summary_

    """
    expected_continuation_bytes = 0

    # Define bit patterns
    UTF8_BIT_1 = 1 << 7  # 10000000
    UTF8_BIT_2 = 1 << 6  # 01000000

    # loop over each byte
    for byte in data:
        # Initialize a mask to check for leading
        # 1's in the current byte
        leading_one_mask = 1 << 7

        # we are not currently expecting any
        # continuation bytes
        if expected_continuation_bytes == 0:
            # Count the no of leading 1's in the
            # current byte to determine the no of
            # continuation bytes
            while leading_one_mask & byte:
                expected_continuation_bytes += 1
                leading_one_mask = leading_one_mask >> 1

            # If the byte is not a multi-byte sequence,
            if expected_continuation_bytes == 0:
                continue

            # If the no of continuation bytes is not
            # between 2 and 4, the sequence is invalid
            if expected_continuation_bytes == 1 or\
                    expected_continuation_bytes > 4:
                return False

        #we are expecting continuation bytes
        else:
            # Check that the byte starts with a "10"
            if not (byte & UTF8_BIT_1 and not (byte & UTF8_BIT_2)):
                return False

        # Decrement the expected number of continuation bytes
        expected_continuation_bytes -= 1

    # processed all bytes and are not expecting
    if expected_continuation_bytes == 0:
        return True
    else:
        return False