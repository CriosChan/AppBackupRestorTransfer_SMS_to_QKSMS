import json

def convert_data(input_str):

    messages = []
    temp_line = ""
    for line in input_str.split('\n'):
        if line.strip() == "":
            continue
        parts = line.split("*,*")
        if len(parts) != 6:
            if(len(temp_line.split("*,*")) != 6):
                temp_line += line + "\n"
                if(len(temp_line.split("*,*")) == 6):
                    parts = temp_line.split("*,*")
                else:
                    continue
            else:
                temp_line = ""
                temp_line += line
                continue
        print(parts)
        address, body, protocol, date, status, message_type = parts
        current_message = {
            "type": message_type,
            "address": address,
            "date": int(date),
            "dateSent": int(date),
            "read": True,
            "status": status,
            "body": body,
            "protocol": 0,
            "locked": False,
            "subId": 1
        }
        messages.append(current_message)
    output_dict = {"messageCount": len(messages), "messages": messages}
    output_json = json.dumps(output_dict, indent=4)
    return output_json

with open("input.txt", "r", encoding="utf-8") as f:
    input_str = f.read()

output_json = convert_data(input_str)

with open("output.json", "w", encoding="utf-8") as f:
    f.write(output_json)