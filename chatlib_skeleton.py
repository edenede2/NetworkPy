# Protocol Constants

CMD_FIELD_LENGTH = 16	# Exact length of cmd field (in bytes)
LENGTH_FIELD_LENGTH = 4   # Exact length of length field (in bytes)
MAX_DATA_LENGTH = 10**LENGTH_FIELD_LENGTH-1  # Max size of data field according to protocol
MSG_HEADER_LENGTH = CMD_FIELD_LENGTH + 1 + LENGTH_FIELD_LENGTH + 1  # Exact size of header (CMD+LENGTH fields)
MAX_MSG_LENGTH = MSG_HEADER_LENGTH + MAX_DATA_LENGTH  # Max size of total message
DELIMITER = "|"  # Delimiter character in protocol
DATA_DELIMITER = "#"  # Delimiter in the data part of the message

# Protocol Messages 
# In this dictionary we will have all the client and server command names

PROTOCOL_CLIENT = {
"login_msg" : "LOGIN",
"logout_msg" : "LOGOUT"
} # .. Add more commands if needed


PROTOCOL_SERVER = {
"login_ok_msg" : "LOGIN_OK",
"login_failed_msg" : "ERROR"
} # ..  Add more commands if needed


# Other constants

ERROR_RETURN = None  # What is returned in case of an error


def build_message(cmd, data):
	"""
	Gets command name (str) and data field (str) and creates a valid protocol message
	Returns: str, or None if error occured
	"""
    # Implement code ...


	try:
		if len(data) == 0:
			return ERROR_RETURN
		elif len(cmd) > CMD_FIELD_LENGTH:
			print("Error: command is too long")
			return ERROR_RETURN
		elif len(data) > MAX_DATA_LENGTH:
			print("Error: data is too long")
			return ERROR_RETURN
		

		
		commend_field = f"{cmd:<{CMD_FIELD_LENGTH}}"
		data_field = f"{len(data):04d}"
		return commend_field + DELIMITER + data_field + DELIMITER + data
	
	except Exception as e:
		try:
			if len(data) == 0:
				return ERROR_RETURN
			elif len(cmd) > CMD_FIELD_LENGTH:
				print("Error: command is too long")
				return ERROR_RETURN
			elif len(data) > MAX_DATA_LENGTH:
				print("Error: data is too long")
				return ERROR_RETURN
			cmd_length = len(cmd)

			if cmd_length > CMD_FIELD_LENGTH:
				print("Error: command is too long")
				return ERROR_RETURN
			
			space_padding_length = CMD_FIELD_LENGTH - cmd_length

			cmd_str = cmd + " " * space_padding_length

			data_length = len(data)

			data_str_length = str(data_length)

			if data_length > MAX_DATA_LENGTH:
				print("Error: data is too long")
				return ERROR_RETURN
			
			data_length_str_length = len(data_str_length)

			zero_padding_length = LENGTH_FIELD_LENGTH - data_length_str_length

			data_str = zero_padding_length * "0" + data_str_length

			full_msg = cmd_str + DELIMITER + data_str + DELIMITER + data

			return full_msg

		except Exception as e:
			print(e)
			return ERROR_RETURN


def parse_message(data):
	"""
	Parses protocol message and returns command name and data field
	Returns: cmd (str), data (str). If some error occured, returns None, None
	"""
    # Implement code ...
	data_list = data.split(DELIMITER)

	if len(data_list) != 3:
		print("Error: wrong number of fields in message")
		return ERROR_RETURN, ERROR_RETURN
	
	cmd = data_list[0]
	msg = data_list[2]

	msg_length = int(data_list[1])

	if len(msg) != msg_length:
		print("Error: wrong data length")
		return ERROR_RETURN, ERROR_RETURN
	
	return cmd, msg

    # The function should return 2 values
    # return cmd, msg

	
def split_data(msg, expected_fields):
	"""
	Helper method. gets a string and number of expected fields in it. Splits the string 
	using protocol's data field delimiter (|#) and validates that there are correct number of fields.
	Returns: list of fields if all ok. If some error occured, returns None
	"""
	# Implement code ...
	try:
		msg_list = msg.split(DATA_DELIMITER)

		if len(msg_list) != expected_fields:
			print("Error: wrong number of fields in message")
			return list([None])

		return msg_list
	
	except Exception as e:
		print(e)
		return list([None])

def join_data(msg_fields):
	"""
	Helper method. Gets a list, joins all of it's fields to one string divided by the data delimiter. 
	Returns: string that looks like cell1#cell2#cell3
	"""

	msg_str_list = [str(cell) for cell in msg_fields]

	msg = DATA_DELIMITER.join(msg_str_list)

	return msg