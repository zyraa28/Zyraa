def fix_messages_file():
    input_file = "messages.txt"
    output_file = "messages_fixed.txt"

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print("❌ messages.txt not found!")
        return

    fixed_messages = []
    temp = {"Name": "", "Email": "", "Message": ""}

    for line in lines:
        if line.lower().startswith("name:"):
            temp["Name"] = line
        elif line.lower().startswith("email:"):
            temp["Email"] = line
        elif line.lower().startswith("message:"):
            temp["Message"] = line
            msg_line = f"{temp['Name']} | {temp['Email']} | {temp['Message']}"
            fixed_messages.append(msg_line)
            temp = {"Name": "", "Email": "", "Message": ""}
        else:
            temp["Message"] += " " + line

    with open(output_file, "w", encoding="utf-8") as f:
        for msg in fixed_messages:
            f.write(msg.strip() + "\n")

    print(f"✅ Fixed messages written to {output_file}")
    print(f"📝 Total messages fixed: {len(fixed_messages)}")


if __name__ == "__main__":
    fix_messages_file()