import yara
import os

def compile_yara_rules(rules_directory):
    rules = {}
    for rule_file in os.listdir(rules_directory):
        if rule_file.endswith('.yar') or rule_file.endswith('.yara'):
            rule_path = os.path.join(rules_directory, rule_file)
            try:
                rules[rule_file] = yara.compile(filepath=rule_path)
                print(f"Compiled {rule_file} successfully!")
            except yara.SyntaxError as e:
                print(f"Failed to compile {rule_file}: {str(e)}")
    return rules

def scan_files(rules, target_directory):
    for root, _, files in os.walk(target_directory):
        for file in files:
            file_path = os.path.join(root, file)
            for rule_name, rule in rules.items():
                try:
                    matches = rule.match(file_path)
                    if matches:
                        print(f"Match found in {file_path} using {rule_name}: {matches}")
                except Exception as e:
                    print(f"Error scanning {file_path} with {rule_name}: {str(e)}")

# Example usage
rules_dir = "./signatures/yara-rules"
target_dir = "./target_files"
compiled_rules = compile_yara_rules(rules_dir)
scan_files(compiled_rules, target_dir)
