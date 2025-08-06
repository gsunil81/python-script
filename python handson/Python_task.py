import os
if not os.path.exists('data_input'):
    os.makedirs('data_input')
    print("📁 'data_input' folder created. Please add .txt files and run the script again.")
    exit()
if not os.path.exists('data_output'):
    os.makedirs('data_output')
summary = []

for file in os.listdir('data_input'):
    if file.endswith('.txt'):
        input_path = os.path.join('data_input', file)
        output_path = os.path.join('data_output', file)

        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        new_lines = []
        line_count = 0
        word_count = 0

        for line in lines:
            if line.strip().startswith('#'):
                continue  
            line_count += 1
            word_count += len(line.split())
            new_line = line.replace('temp', 'permanent')
            new_lines.append(new_line)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        summary.append(f"{file}: {line_count} lines, {word_count} words")
with open('data_output/summary.txt', 'w', encoding='utf-8') as f:
    f.write("Summary Report\n")
    f.write("=================\n")
    for item in summary:
        f.write(item + '\n')

print(" Done! Check the 'data_output' folder for results.")